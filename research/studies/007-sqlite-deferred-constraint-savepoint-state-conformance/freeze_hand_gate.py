from __future__ import annotations

import hashlib
import json
from pathlib import Path

BASE = [1, 2, 3]
FK_ERROR = ("foreign_key", "sqlite3.IntegrityError", 787, "SQLITE_CONSTRAINT_FOREIGNKEY")
SP_ERROR = ("savepoint_not_found", "sqlite3.OperationalError", 1, "SQLITE_ERROR")
BEGIN_ERROR = ("nested_begin", "sqlite3.OperationalError", 1, "SQLITE_ERROR")


def state(parent=BASE, immediate=(), deferred=(), restrict=(), fk=()):
    return [list(parent), [list(r) for r in immediate], [list(r) for r in deferred], [list(r) for r in restrict], [list(r) for r in fk]]


def row(token, in_tx, current, error=None):
    if error is None:
        key = exc = code = name = None
        disposition = "ok"
    else:
        key, exc, code, name = error
        disposition = "error"
    return [token, disposition, key, exc, code, name, in_tx, *current]


def case(case_id, category, specs):
    return {"id": case_id, "category": category, "steps": [row(*spec) for spec in specs]}


def main():
    base = state()
    p10 = state(parent=[1, 2, 3, 10])
    p11 = state(parent=[1, 2, 3, 11])
    p10_11 = state(parent=[1, 2, 3, 10, 11])
    p99 = state(parent=[1, 2, 3, 99])
    deferred_bad = state(deferred=[(201, 99)], fk=[("child_deferred", 201, "parent", 0)])
    deferred_fixed = state(parent=[1, 2, 3, 99], deferred=[(201, 99)])
    restrict_live = state(parent=[1, 2, 3, 99], restrict=[(301, 99)])
    cases = [
        case("G01", "basic savepoint and release", [("savepoint(a)", True, base), ("insert_parent(10)", True, p10), ("release(a)", False, p10)]),
        case("G02", "inner release followed by outer rollback", [("begin", True, base), ("savepoint(a)", True, base), ("insert_parent(10)", True, p10), ("savepoint(b)", True, p10), ("insert_parent(11)", True, p10_11), ("release(b)", True, p10_11), ("rollback", False, base)]),
        case("G03", "rollback-to with retained mark", [("begin", True, base), ("savepoint(a)", True, base), ("insert_parent(10)", True, p10), ("rollback_to(a)", True, base), ("insert_parent(11)", True, p11), ("release(a)", True, p11), ("commit", False, p11)]),
        case("G04", "duplicate savepoint names", [("begin", True, base), ("savepoint(a)", True, base), ("insert_parent(10)", True, p10), ("savepoint(a)", True, p10), ("insert_parent(11)", True, p10_11), ("rollback_to(a)", True, p10), ("release(a)", True, p10), ("release(a)", True, p10), ("commit", False, p10)]),
        case("G05", "missing savepoint name", [("begin", True, base), ("release(z)", True, base, SP_ERROR), ("commit", False, base)]),
        case("G06", "nested BEGIN error", [("begin", True, base), ("begin", True, base, BEGIN_ERROR), ("commit", False, base)]),
        case("G07", "immediate foreign-key failure", [("begin", True, base), ("insert_child(immediate,101,99)", True, base, FK_ERROR), ("commit", False, base)]),
        case("G08", "deferred violation repaired before commit", [("begin", True, base), ("insert_child(deferred,201,99)", True, deferred_bad), ("insert_parent(99)", True, deferred_fixed), ("commit", False, deferred_fixed)]),
        case("G09", "failed commit leaves transaction open", [("begin", True, base), ("insert_child(deferred,201,99)", True, deferred_bad), ("commit", True, deferred_bad, FK_ERROR), ("rollback", False, base)]),
        case("G10", "nested release during deferred violation", [("begin", True, base), ("insert_child(deferred,201,99)", True, deferred_bad), ("savepoint(a)", True, deferred_bad), ("release(a)", True, deferred_bad), ("insert_parent(99)", True, deferred_fixed), ("commit", False, deferred_fixed)]),
        case("G11", "failed outer transaction-savepoint release", [("savepoint(a)", True, base), ("savepoint(b)", True, base), ("insert_child(deferred,201,99)", True, deferred_bad), ("release(a)", True, deferred_bad, FK_ERROR), ("rollback_to(b)", True, base), ("release(b)", True, base), ("rollback_to(a)", True, base), ("release(a)", False, base)]),
        case("G12", "immediate RESTRICT timing", [("begin", True, base), ("insert_parent(99)", True, p99), ("insert_child(deferred_restrict,301,99)", True, restrict_live), ("delete_parent(99)", True, restrict_live, FK_ERROR), ("delete_child(deferred_restrict,301)", True, p99), ("delete_parent(99)", True, base), ("commit", False, base)]),
    ]
    payload = {
        "status": "frozen-before-gate-execution",
        "step_schema": ["action_token", "disposition", "expected_error_key", "python_exception", "sqlite_errorcode", "sqlite_errorname", "in_transaction", "parent", "child_immediate", "child_deferred", "child_restrict", "foreign_key_check"],
        "frozen_error_mapping": {"foreign_key": ["sqlite3.IntegrityError", 787, "SQLITE_CONSTRAINT_FOREIGNKEY"], "nested_begin": ["sqlite3.OperationalError", 1, "SQLITE_ERROR"], "savepoint_not_found": ["sqlite3.OperationalError", 1, "SQLITE_ERROR"]},
        "case_count": len(cases),
        "cases": cases,
    }
    raw = (json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    Path("hand_gate_cases.json").write_bytes(raw)
    digest = hashlib.sha256(raw).hexdigest()
    Path("hand_gate_cases.sha256").write_text(f"{digest}  hand_gate_cases.json\n", encoding="utf-8")
    print(digest)


if __name__ == "__main__":
    main()
