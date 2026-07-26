from __future__ import annotations

import hashlib
import os
import stat
from pathlib import Path
from typing import Any


def _region(relative_posix: str) -> str:
    first = relative_posix.split("/", 1)[0]
    if first == "destination":
        return "destination"
    if first == "sentinel":
        return "sentinel"
    return "other"


def _mode_string(mode: int) -> str:
    return f"{stat.S_IMODE(mode):04o}"


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _node_type(mode: int) -> str:
    if stat.S_ISREG(mode):
        return "regular"
    if stat.S_ISDIR(mode):
        return "directory"
    if stat.S_ISLNK(mode):
        return "symlink"
    if stat.S_ISFIFO(mode):
        return "fifo"
    return "other"


def _iter_descendants(root: Path):
    def visit(directory: Path):
        entries = sorted(os.scandir(directory), key=lambda item: item.name.encode("utf-8"))
        for entry in entries:
            path = Path(entry.path)
            st = os.lstat(path)
            yield path, st
            if stat.S_ISDIR(st.st_mode):
                yield from visit(path)

    yield from visit(root)


def snapshot(root: Path) -> list[dict[str, Any]]:
    root = root.resolve(strict=True)
    raw: list[tuple[str, os.stat_result, dict[str, Any]]] = []
    regular_inodes: dict[tuple[int, int], list[str]] = {}

    for path, st in _iter_descendants(root):
        relative = path.relative_to(root).as_posix()
        kind = _node_type(st.st_mode)
        record: dict[str, Any] = {
            "path": relative,
            "region": _region(relative),
            "type": kind,
            "mode_octal": _mode_string(st.st_mode),
            "uid": st.st_uid,
            "gid": st.st_gid,
            "size_for_regular": None,
            "sha256_for_regular": None,
            "symlink_target": None,
            "hardlink_group": None,
        }
        if kind == "regular":
            record["size_for_regular"] = st.st_size
            record["sha256_for_regular"] = _file_sha256(path)
            if st.st_nlink > 1:
                regular_inodes.setdefault((st.st_dev, st.st_ino), []).append(relative)
        elif kind == "symlink":
            record["symlink_target"] = os.readlink(path)
        raw.append((relative, st, record))

    repeated = [paths for paths in regular_inodes.values() if len(paths) > 1]
    repeated.sort(key=lambda paths: min(path.encode("utf-8") for path in paths))
    groups: dict[str, str] = {}
    for index, paths in enumerate(repeated, start=1):
        for relative in paths:
            groups[relative] = f"h{index}"

    records: list[dict[str, Any]] = []
    for relative, _st, record in sorted(raw, key=lambda item: item[0].encode("utf-8")):
        record["hardlink_group"] = groups.get(relative)
        records.append(record)
    return records


def diff_snapshots(
    before: list[dict[str, Any]], after: list[dict[str, Any]]
) -> dict[str, list[Any]]:
    before_map = {record["path"]: record for record in before}
    after_map = {record["path"]: record for record in after}
    paths = sorted(set(before_map) | set(after_map), key=lambda p: p.encode("utf-8"))
    created: list[dict[str, Any]] = []
    removed: list[dict[str, Any]] = []
    changed: list[dict[str, Any]] = []
    for path in paths:
        old = before_map.get(path)
        new = after_map.get(path)
        if old is None:
            created.append(new)
        elif new is None:
            removed.append(old)
        elif old != new:
            changed.append({"path": path, "before": old, "after": new})
    return {"created": created, "removed": removed, "changed": changed}


def changed_regions(diff: dict[str, list[Any]]) -> dict[str, int]:
    counts = {"destination": 0, "sentinel": 0, "other": 0}
    for record in diff["created"] + diff["removed"]:
        counts[record["region"]] += 1
    for record in diff["changed"]:
        counts[record["after"]["region"]] += 1
    return counts


def destination_nodes(snapshot_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    prefix = "destination/"
    selected: list[dict[str, Any]] = []
    for record in snapshot_records:
        path = record["path"]
        if not path.startswith(prefix):
            continue
        copied = dict(record)
        copied["path"] = path[len(prefix):]
        copied.pop("region", None)
        selected.append(copied)
    return selected
