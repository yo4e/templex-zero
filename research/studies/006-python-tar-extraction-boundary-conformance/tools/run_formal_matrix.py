from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from study006_common import canonical_json_bytes, index_fixtures, load_json, sha256_bytes, sha256_file

EXPECTED_MANIFEST_SHA256 = "23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a"
EXPECTED_FIXTURE_COUNT = 32
EXPECTED_MEMBER_COUNT = 57
EXPECTED_TOOL_BLOBS = {
    "study006_common.py": "1bf7b5b1245f814c3294bc4a75d5f575aeab1271",
    "generate_tar.py": "eee881970e61c4426661e078411f18cab3b373ad",
    "filesystem_oracle.py": "c42c8708f78ebede9e879093c30c68e705354a5c",
    "extraction_harness.py": "cbe63ddcc489b90054923cd4ea27f57f77aa036f",
}


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def validate_inputs(manifest_path: Path, harness_path: Path, runner_blob: str) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    manifest_sha = sha256_file(manifest_path)
    if manifest_sha != EXPECTED_MANIFEST_SHA256:
        raise ValueError(f"manifest SHA mismatch: {manifest_sha}")
    manifest = load_json(manifest_path)
    fixtures = manifest.get("fixtures")
    if not isinstance(fixtures, list) or len(fixtures) != EXPECTED_FIXTURE_COUNT:
        raise ValueError("formal manifest must contain exactly 32 fixtures")
    if manifest.get("fixture_count") != EXPECTED_FIXTURE_COUNT:
        raise ValueError("fixture_count field drift")
    if manifest.get("member_count") != EXPECTED_MEMBER_COUNT:
        raise ValueError("member_count field drift")
    if sum(len(item.get("members", [])) for item in fixtures) != EXPECTED_MEMBER_COUNT:
        raise ValueError("member total drift")
    index_fixtures(manifest)
    if any(item.get("outside_changes") != 0 or item.get("sentinel_changes") != 0 for item in fixtures):
        raise ValueError("protected-effect expectation drift")

    tools_dir = harness_path.parent
    observed_blobs: dict[str, str] = {}
    for name, expected in EXPECTED_TOOL_BLOBS.items():
        actual = git_blob_sha1(tools_dir / name)
        if actual != expected:
            raise ValueError(f"tool blob drift for {name}: {actual}")
        observed_blobs[name] = actual
    actual_runner_blob = git_blob_sha1(Path(__file__))
    if actual_runner_blob != runner_blob:
        raise ValueError(f"runner blob drift: {actual_runner_blob}")
    observed_blobs[Path(__file__).name] = actual_runner_blob

    identity = {
        "manifest_sha256": manifest_sha,
        "manifest_git_blob": git_blob_sha1(manifest_path),
        "tool_git_blobs": observed_blobs,
        "python_executable": "/usr/bin/python3",
        "setpriv_executable": "/usr/bin/setpriv",
        "run_uid": 65534,
        "run_gid": 65534,
        "supplementary_groups": [],
        "no_new_privs": True,
    }
    return manifest, fixtures, identity


def run_formal_matrix(
    manifest_path: Path,
    harness_path: Path,
    runner_blob: str,
    python_path: str = "/usr/bin/python3",
    setpriv_path: str = "/usr/bin/setpriv",
) -> dict[str, Any]:
    manifest, fixtures, identity = validate_inputs(manifest_path, harness_path, runner_blob)
    results: list[dict[str, Any]] = []
    operational: list[dict[str, Any]] = []
    execution_errors: list[dict[str, Any]] = []

    for ordinal, fixture in enumerate(fixtures):
        fixture_id = fixture["id"]
        root = Path(tempfile.mkdtemp(prefix=f"templex006-formal-{ordinal:02d}-{fixture_id.lower()}-", dir="/tmp"))
        os.chmod(root, 0o700)
        os.chown(root, 65534, 65534)
        command = [
            setpriv_path,
            "--reuid=65534",
            "--regid=65534",
            "--clear-groups",
            "--no-new-privs",
            python_path,
            str(harness_path),
            "--manifest",
            str(manifest_path),
            "--fixture",
            fixture_id,
            "--root",
            str(root),
        ]
        try:
            completed = subprocess.run(
                command,
                text=True,
                capture_output=True,
                timeout=5,
                check=False,
                env={"PATH": "/usr/bin:/bin", "PYTHONHASHSEED": "0", "LANG": "C.UTF-8"},
            )
            op_record: dict[str, Any] = {
                "ordinal": ordinal,
                "fixture_id": fixture_id,
                "returncode": completed.returncode,
                "stderr": completed.stderr,
            }
            if not completed.stdout:
                execution_errors.append({
                    "ordinal": ordinal,
                    "fixture_id": fixture_id,
                    "kind": "no_json",
                    "returncode": completed.returncode,
                    "stderr": completed.stderr,
                })
                operational.append(op_record)
                continue
            try:
                result = json.loads(completed.stdout)
            except json.JSONDecodeError as exc:
                execution_errors.append({
                    "ordinal": ordinal,
                    "fixture_id": fixture_id,
                    "kind": "invalid_json",
                    "error": str(exc),
                    "returncode": completed.returncode,
                    "stderr": completed.stderr,
                })
                operational.append(op_record)
                continue
            op_record.update(result.get("operational", {}))
            operational.append(op_record)
            scientific = result.get("scientific")
            if not isinstance(scientific, dict):
                execution_errors.append({
                    "ordinal": ordinal,
                    "fixture_id": fixture_id,
                    "kind": "missing_scientific_record",
                })
                continue
            results.append(scientific)
            if completed.returncode not in (0, 2):
                execution_errors.append({
                    "ordinal": ordinal,
                    "fixture_id": fixture_id,
                    "kind": "unexpected_returncode",
                    "returncode": completed.returncode,
                })
        except subprocess.TimeoutExpired:
            execution_errors.append({
                "ordinal": ordinal,
                "fixture_id": fixture_id,
                "kind": "timeout",
            })
            operational.append({
                "ordinal": ordinal,
                "fixture_id": fixture_id,
                "returncode": None,
                "stderr": "timeout",
            })
        finally:
            shutil.rmtree(root, ignore_errors=True)

    failed_ids = [record["fixture_id"] for record in results if not record.get("passed", False)]
    mismatches = [
        {
            "fixture_id": record["fixture_id"],
            "failed_checks": sorted(key for key, value in record.get("checks", {}).items() if not value),
            "exception_class": record.get("exception_class"),
            "exception_member": record.get("exception_member"),
            "refusal_index": record.get("refusal_index"),
            "changed_regions": record.get("changed_regions"),
            "destination_nodes": record.get("destination_nodes"),
        }
        for record in results
        if not record.get("passed", False)
    ]
    scientific = {
        "schema_version": "templex006-formal-matrix-result-v1",
        "manifest_sha256": EXPECTED_MANIFEST_SHA256,
        "fixture_count_expected": EXPECTED_FIXTURE_COUNT,
        "fixture_count_observed": len(results),
        "member_count": EXPECTED_MEMBER_COUNT,
        "passed_count": sum(1 for record in results if record.get("passed", False)),
        "failed_ids": failed_ids,
        "execution_error_count": len(execution_errors),
        "execution_complete": len(results) == EXPECTED_FIXTURE_COUNT and not execution_errors,
        "results": results,
    }
    return {
        "scientific": scientific,
        "scientific_sha256": sha256_bytes(canonical_json_bytes(scientific)),
        "mismatches": mismatches,
        "execution_errors": execution_errors,
        "operational": operational,
        "identities": identity,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--harness", type=Path, required=True)
    parser.add_argument("--runner-blob", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--mismatches", type=Path, required=True)
    parser.add_argument("--identities", type=Path, required=True)
    args = parser.parse_args()
    result = run_formal_matrix(args.manifest, args.harness, args.runner_blob)
    args.output.write_bytes(canonical_json_bytes(result))
    args.mismatches.write_bytes(canonical_json_bytes({
        "schema_version": "templex006-formal-mismatches-v1",
        "mismatches": result["mismatches"],
        "execution_errors": result["execution_errors"],
    }))
    args.identities.write_bytes(canonical_json_bytes({
        "schema_version": "templex006-cycle3-executed-identities-v1",
        **result["identities"],
    }))
    print(json.dumps({
        "fixture_count_observed": result["scientific"]["fixture_count_observed"],
        "passed_count": result["scientific"]["passed_count"],
        "failed_ids": result["scientific"]["failed_ids"],
        "execution_error_count": result["scientific"]["execution_error_count"],
        "execution_complete": result["scientific"]["execution_complete"],
        "scientific_sha256": result["scientific_sha256"],
    }, sort_keys=True))
    return 0 if result["scientific"]["execution_complete"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
