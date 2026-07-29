from __future__ import annotations

import hashlib
import json
from pathlib import Path

from actions import parse_action
from comparator import compare_records
from harness import SQLiteHarness
from model import IndependentModel
from records import StepRecord


def expected_record(sequence_id, step_index, row, *, model):
    token, disposition, key, exc, code, name, in_tx, parent, ci, cd, cr, fk = row
    return StepRecord(
        sequence_id=sequence_id,
        step_index=step_index,
        action=parse_action(token),
        disposition=disposition,
        python_exception=exc,
        sqlite_errorcode=code,
        sqlite_errorname=name,
        in_transaction=in_tx,
        parent=tuple(parent),
        child_immediate=tuple(tuple(r) for r in ci),
        child_deferred=tuple(tuple(r) for r in cd),
        child_restrict=tuple(tuple(r) for r in cr),
        foreign_key_check=tuple(tuple(r) for r in fk),
        expected_error_key=key if model else None,
    )


def mismatch_dict(item):
    return {"sequence_id": item.sequence_id, "step_index": item.step_index, "field": item.field, "expected": item.expected, "observed": item.observed}


def main() -> int:
    raw = Path("hand_gate_cases.json").read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != Path("hand_gate_cases.sha256").read_text().split()[0]:
        raise SystemExit("hand-gate expectation identity mismatch")
    payload = json.loads(raw)
    harness = SQLiteHarness("schema.sql")
    results = []
    for case in payload["cases"]:
        actions = tuple(parse_action(row[0]) for row in case["steps"])
        expected_model = tuple(expected_record(case["id"], i, row, model=True) for i, row in enumerate(case["steps"], 1))
        expected_sqlite = tuple(expected_record(case["id"], i, row, model=False) for i, row in enumerate(case["steps"], 1))
        model_records = IndependentModel().run_sequence(case["id"], actions)
        sqlite_records = harness.run_sequence(case["id"], actions)
        checks = {
            "model_expected": compare_records(expected_model, model_records),
            "sqlite_expected": compare_records(expected_sqlite, sqlite_records),
            "model_sqlite": compare_records(model_records, sqlite_records),
        }
        passed = all(check.matched for check in checks.values())
        results.append({"id": case["id"], "category": case["category"], "passed": passed, **{name + "_mismatches": [mismatch_dict(m) for m in check.mismatches] for name, check in checks.items()}})
    result = {
        "status": "pass" if all(r["passed"] for r in results) else "fail",
        "expectation_sha256": digest,
        "case_count": len(results),
        "passed_cases": sum(r["passed"] for r in results),
        "failed_cases": sum(not r["passed"] for r in results),
        "protected_manifest_loaded": False,
        "protected_matrix_executed": False,
        "cases": results,
    }
    Path("hand_gate_result.json").write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("status", "case_count", "passed_cases", "failed_cases")}, sort_keys=True))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
