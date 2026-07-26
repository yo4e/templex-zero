from __future__ import annotations

import argparse
import io
import json
import os
import resource
import stat
import tarfile
from pathlib import Path
from typing import Any

from filesystem_oracle import changed_regions, destination_nodes, diff_snapshots, snapshot
from generate_tar import build_archive_bytes
from study006_common import canonical_json_bytes, index_fixtures, load_json, sha256_bytes

EXPECTED_UID = 65534
EXPECTED_GID = 65534


def _assert_child_identity(root: Path) -> dict[str, Any]:
    if os.geteuid() != EXPECTED_UID or os.getegid() != EXPECTED_GID:
        raise RuntimeError(f"unexpected child identity {os.geteuid()}:{os.getegid()}")
    groups = os.getgroups()
    if groups:
        raise RuntimeError(f"supplementary groups not empty: {groups}")
    status = Path("/proc/self/status").read_text(encoding="utf-8")
    no_new_privs = None
    for line in status.splitlines():
        if line.startswith("NoNewPrivs:"):
            no_new_privs = line.split(":", 1)[1].strip()
            break
    if no_new_privs != "1":
        raise RuntimeError(f"NoNewPrivs is not 1: {no_new_privs!r}")
    st = os.stat(root)
    if stat.S_IMODE(st.st_mode) != 0o700:
        raise RuntimeError(f"study root mode is not 0700: {stat.S_IMODE(st.st_mode):04o}")
    if st.st_uid != EXPECTED_UID or st.st_gid != EXPECTED_GID:
        raise RuntimeError(f"study root ownership is {st.st_uid}:{st.st_gid}")
    return {"uid": os.geteuid(), "gid": os.getegid(), "groups": groups, "no_new_privs": 1}


def _apply_caps() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_FSIZE, (16 * 1024 * 1024, 16 * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
    os.umask(0o022)


def _create_node(base: Path, node: list[Any], manifest: dict[str, Any]) -> None:
    path_text, kind, mode_octal, payload_id, symlink_target, _hardlink_group = node
    path = base / path_text
    path.parent.mkdir(parents=True, exist_ok=True)
    if kind == "directory":
        path.mkdir(exist_ok=True)
        os.chmod(path, int(mode_octal, 8))
    elif kind == "regular":
        from study006_common import payload_bytes
        path.write_bytes(payload_bytes(manifest, payload_id))
        os.chmod(path, int(mode_octal, 8))
    elif kind == "symlink":
        os.symlink(symlink_target, path)
    else:
        raise ValueError(f"unsupported pre-existing node type: {kind}")


def _expected_nodes(fixture: dict[str, Any], manifest: dict[str, Any]) -> list[dict[str, Any]]:
    payloads = manifest["payloads"]
    output: list[dict[str, Any]] = []
    for node in fixture["nodes"]:
        path, kind, mode_octal, payload_id, symlink_target, hardlink_group = node
        payload = payloads.get(payload_id) if payload_id else None
        output.append({
            "path": path,
            "type": kind,
            "mode_octal": mode_octal,
            "uid": EXPECTED_UID,
            "gid": EXPECTED_GID,
            "size_for_regular": len(payload["utf8"].encode("utf-8")) if payload else None,
            "sha256_for_regular": payload["sha256"] if payload else None,
            "symlink_target": symlink_target,
            "hardlink_group": hardlink_group,
        })
    output.sort(key=lambda record: record["path"].encode("utf-8"))
    return output


def execute_fixture(
    manifest_path: Path, fixture_id: str, root: Path
) -> dict[str, Any]:
    _apply_caps()
    identity = _assert_child_identity(root)
    manifest = load_json(manifest_path)
    fixture = index_fixtures(manifest)[fixture_id]

    destination = root / manifest["extraction"]["destination_name"]
    sentinel = root / manifest["extraction"]["sentinel_name"]
    destination.mkdir()
    sentinel.mkdir()
    sentinel_path = root / manifest["sentinel"]["path"]
    sentinel_path.parent.mkdir(parents=True, exist_ok=True)
    sentinel_path.write_text(manifest["sentinel"]["payload_utf8"], encoding="utf-8")
    os.chmod(sentinel_path, int(manifest["sentinel"]["mode_octal"], 8))
    for node in fixture["pre"]:
        _create_node(destination, node, manifest)

    archive_bytes = build_archive_bytes(manifest, fixture, root)
    archive_record = {"bytes": len(archive_bytes), "sha256": sha256_bytes(archive_bytes)}
    before = snapshot(root)

    exception_class = None
    exception_member = None
    try:
        with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:") as archive:
            archive.errorlevel = int(manifest["extraction"]["errorlevel"])
            archive.extractall(path=destination, filter="data")
    except tarfile.FilterError as exc:
        exception_class = type(exc).__name__
        exception_member = getattr(getattr(exc, "tarinfo", None), "name", None)

    after = snapshot(root)
    diff = diff_snapshots(before, after)
    region_counts = changed_regions(diff)
    nodes = destination_nodes(after)
    expected_nodes = _expected_nodes(fixture, manifest)

    refusal_index = None
    if exception_member is not None:
        for index, member in enumerate(fixture["members"]):
            if member[1] == exception_member:
                refusal_index = index
                break
    actual_prefix = len(fixture["members"]) if exception_class is None else refusal_index

    expected_exception = None
    if fixture["refusal_index"] is not None:
        expected_exception = fixture["members"][fixture["refusal_index"]][6]

    sentinel_after = next(
        record for record in after if record["path"] == manifest["sentinel"]["path"]
    )
    checks = {
        "exception_class": exception_class == expected_exception,
        "refusal_index": refusal_index == fixture["refusal_index"],
        "prefix_count": actual_prefix == fixture["prefix_count"],
        "destination_nodes": nodes == expected_nodes,
        "outside_changes": region_counts["other"] == fixture["outside_changes"],
        "sentinel_changes": region_counts["sentinel"] == fixture["sentinel_changes"],
        "sentinel_digest": sentinel_after["sha256_for_regular"] == manifest["sentinel"]["payload_sha256"],
    }

    scientific = {
        "fixture_id": fixture_id,
        "fixture_record_sha256": sha256_bytes(canonical_json_bytes(fixture)),
        "identity": identity,
        "exception_class": exception_class,
        "exception_member": exception_member,
        "refusal_index": refusal_index,
        "accepted_prefix_count": actual_prefix,
        "before": before,
        "after": after,
        "diff": diff,
        "changed_regions": region_counts,
        "destination_nodes": nodes,
        "checks": checks,
        "passed": all(checks.values()),
    }
    return {
        "scientific": scientific,
        "operational": {
            "archive_bytes": archive_record["bytes"],
            "archive_sha256": archive_record["sha256"],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    result = execute_fixture(args.manifest, args.fixture, args.root)
    print(canonical_json_bytes(result).decode("utf-8"), end="")
    return 0 if result["scientific"]["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
