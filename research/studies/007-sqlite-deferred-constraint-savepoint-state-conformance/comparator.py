from __future__ import annotations

from records import ComparisonResult, Mismatch, StepRecord

_FIELDS = (
    "sequence_id",
    "step_index",
    "action",
    "disposition",
    "python_exception",
    "sqlite_errorcode",
    "sqlite_errorname",
    "in_transaction",
    "parent",
    "child_immediate",
    "child_deferred",
    "child_restrict",
    "foreign_key_check",
)


def compare_records(expected: tuple[StepRecord, ...], observed: tuple[StepRecord, ...]) -> ComparisonResult:
    mismatches: list[Mismatch] = []
    if len(expected) != len(observed):
        mismatches.append(Mismatch("<sequence>", 0, "length", len(expected), len(observed)))
    for left, right in zip(expected, observed):
        for field in _FIELDS:
            expected_value = getattr(left, field)
            observed_value = getattr(right, field)
            if expected_value != observed_value:
                mismatches.append(Mismatch(left.sequence_id, left.step_index, field, expected_value, observed_value))
    return ComparisonResult(matched=not mismatches, mismatches=tuple(mismatches))
