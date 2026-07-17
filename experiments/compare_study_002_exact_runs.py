"""Compare repeated Study 002 exact-screen reports.

The frozen experiment correctly records expanded-state counts for every run, but
an expanded count observed at a wall-clock time cap is timing-dependent. This
post-run comparator preserves all raw measurements while excluding only fields
that cannot be byte-stable across identical time-limited executions.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
from typing import Any


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def normalized_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    result = {
        key: value
        for key, value in candidate.items()
        if key != "elapsed_seconds"
    }
    if candidate.get("cap_reason") == "time":
        result.pop("expanded_states", None)
    return result


def normalized_report(report: dict[str, Any]) -> dict[str, Any]:
    summary = {
        key: value
        for key, value in report["summary"].items()
        if key not in {"elapsed_seconds_total", "total_expanded_states"}
    }
    return {
        "experiment_version": report["experiment_version"],
        "code_version": report["code_version"],
        "manifest_sha256": report["manifest_sha256"],
        "caps": report["caps"],
        "candidates": [
            normalized_candidate(candidate)
            for candidate in report["candidates"]
        ],
        "summary": summary,
    }


def differing_paths(left: Any, right: Any, path: str = "$") -> list[str]:
    if type(left) is not type(right):
        return [path]
    if isinstance(left, dict):
        differences = []
        for key in sorted(set(left) | set(right)):
            child = f"{path}.{key}"
            if key not in left or key not in right:
                differences.append(child)
            else:
                differences.extend(differing_paths(left[key], right[key], child))
        return differences
    if isinstance(left, list):
        if len(left) != len(right):
            return [path]
        differences = []
        for index, (a, b) in enumerate(zip(left, right)):
            differences.extend(differing_paths(a, b, f"{path}[{index}]"))
        return differences
    return [] if left == right else [path]


def compare(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    normalized_left = normalized_report(left)
    normalized_right = normalized_report(right)
    left_hash = sha256(compact_json(normalized_left).encode("utf-8")).hexdigest()
    right_hash = sha256(compact_json(normalized_right).encode("utf-8")).hexdigest()

    time_capped = []
    for a, b in zip(left["candidates"], right["candidates"]):
        if a.get("cap_reason") == "time" or b.get("cap_reason") == "time":
            time_capped.append(
                {
                    "id": a["id"],
                    "run_1_expanded_states": a["expanded_states"],
                    "run_2_expanded_states": b["expanded_states"],
                    "run_1_elapsed_seconds": a["elapsed_seconds"],
                    "run_2_elapsed_seconds": b["elapsed_seconds"],
                }
            )

    differences = differing_paths(normalized_left, normalized_right)
    return {
        "comparison_version": 1,
        "equivalent_deterministic_fields": not differences,
        "normalized_sha256_run_1": left_hash,
        "normalized_sha256_run_2": right_hash,
        "normalized_differences": differences,
        "raw_report_hashes": [
            left.get("deterministic_sha256"),
            right.get("deterministic_sha256"),
        ],
        "timing_dependent_measurements": {
            "run_1_total_expanded_states": left["summary"]["total_expanded_states"],
            "run_2_total_expanded_states": right["summary"]["total_expanded_states"],
            "run_1_elapsed_seconds_total": left["summary"]["elapsed_seconds_total"],
            "run_2_elapsed_seconds_total": right["summary"]["elapsed_seconds_total"],
            "time_capped_candidates": time_capped,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_1", type=Path)
    parser.add_argument("run_2", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    left = json.loads(args.run_1.read_text(encoding="utf-8"))
    right = json.loads(args.run_2.read_text(encoding="utf-8"))
    result = compare(left, right)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    if not result["equivalent_deterministic_fields"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
