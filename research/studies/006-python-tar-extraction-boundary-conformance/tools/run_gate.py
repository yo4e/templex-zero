from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from study006_common import canonical_json_bytes, index_fixtures, load_json, sha256_bytes, sha256_file


def validate_gate_freeze(gate: dict[str, Any]) -> list[dict[str, Any]]:
    if gate.get("source_manifest_sha256") != "23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a":
        raise ValueError("unexpected source manifest identity")
    fixtures = gate.get("fixtures")
    if not isinstance(fixtures, list) or len(fixtures) < 12:
        raise ValueError("gate must contain at least twelve fixtures")
    indexed = index_fixtures(gate)
    frozen_hashes = gate.get("source_fixture_record_sha256", {})
    for fixture_id, fixture in indexed.items():
        actual = sha256_bytes(canonical_json_bytes(fixture))
        if actual != frozen_hashes.get(fixture_id):
            raise ValueError(f"gate fixture record drift for {fixture_id}")
        if fixture["outside_changes"] != 0 or fixture["sentinel_changes"] != 0:
            raise ValueError(f"nonzero protected effect expectation for {fixture_id}")
        refusal = fixture["refusal_index"]
        if refusal is not None:
            if refusal >= len(fixture["members"]):
                raise ValueError(f"invalid refusal index for {fixture_id}")
            if fixture["members"][refusal][5] != "R":
                raise ValueError(f"refusal index is not an R member for {fixture_id}")
    return fixtures


def run_gate(
    gate_path: Path,
    harness_path: Path,
    python_path: str = "/usr/bin/python3",
    setpriv_path: str = "/usr/bin/setpriv",
) -> dict[str, Any]:
    gate = load_json(gate_path)
    fixtures = validate_gate_freeze(gate)
    results = []
    for fixture in fixtures:
        root = Path(tempfile.mkdtemp(prefix=f"templex006-gate-{fixture['id'].lower()}-", dir="/tmp"))
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
            str(gate_path),
            "--fixture",
            fixture["id"],
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
            if not completed.stdout:
                raise RuntimeError(
                    f"{fixture['id']}: child produced no JSON; stderr={completed.stderr!r}"
                )
            result = json.loads(completed.stdout)
            result["operational"]["returncode"] = completed.returncode
            result["operational"]["stderr"] = completed.stderr
            if completed.returncode not in (0, 2):
                raise RuntimeError(
                    f"{fixture['id']}: unexpected return code {completed.returncode}"
                )
            results.append(result)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    scientific_results = [result["scientific"] for result in results]
    summary = {
        "schema_version": "templex006-hand-audited-gate-result-v1",
        "gate_manifest_sha256": sha256_file(gate_path),
        "source_manifest_sha256": gate["source_manifest_sha256"],
        "fixture_count": len(results),
        "passed_count": sum(1 for result in scientific_results if result["passed"]),
        "failed_ids": [result["fixture_id"] for result in scientific_results if not result["passed"]],
        "results": scientific_results,
    }
    return {
        "scientific": summary,
        "scientific_sha256": sha256_bytes(canonical_json_bytes(summary)),
        "operational": [result["operational"] for result in results],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate", type=Path, required=True)
    parser.add_argument("--harness", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_gate(args.gate, args.harness)
    args.output.write_bytes(canonical_json_bytes(result))
    print(json.dumps({
        "fixture_count": result["scientific"]["fixture_count"],
        "passed_count": result["scientific"]["passed_count"],
        "failed_ids": result["scientific"]["failed_ids"],
        "scientific_sha256": result["scientific_sha256"],
    }, sort_keys=True))
    return 0 if not result["scientific"]["failed_ids"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
