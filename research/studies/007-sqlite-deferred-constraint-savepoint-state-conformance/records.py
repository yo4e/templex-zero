from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from actions import Action


@dataclass(frozen=True, slots=True)
class StepRecord:
    sequence_id: str
    step_index: int
    action: Action
    disposition: str
    python_exception: str | None
    sqlite_errorcode: int | None
    sqlite_errorname: str | None
    in_transaction: bool
    parent: tuple[int, ...]
    child_immediate: tuple[tuple[int, int], ...]
    child_deferred: tuple[tuple[int, int], ...]
    child_restrict: tuple[tuple[int, int], ...]
    foreign_key_check: tuple[tuple[str, int, str, int], ...]
    expected_error_key: str | None = None

    def portable_dict(self, *, include_expected_error_key: bool = True) -> dict[str, Any]:
        result: dict[str, Any] = {
            "sequence_id": self.sequence_id,
            "step_index": self.step_index,
            "action": self.action.to_dict(),
            "disposition": self.disposition,
            "python_exception": self.python_exception,
            "sqlite_errorcode": self.sqlite_errorcode,
            "sqlite_errorname": self.sqlite_errorname,
            "in_transaction": self.in_transaction,
            "parent": list(self.parent),
            "child_immediate": [list(row) for row in self.child_immediate],
            "child_deferred": [list(row) for row in self.child_deferred],
            "child_restrict": [list(row) for row in self.child_restrict],
            "foreign_key_check": [list(row) for row in self.foreign_key_check],
        }
        if include_expected_error_key:
            result["expected_error_key"] = self.expected_error_key
        return result


@dataclass(frozen=True, slots=True)
class Mismatch:
    sequence_id: str
    step_index: int
    field: str
    expected: object
    observed: object


@dataclass(frozen=True, slots=True)
class ComparisonResult:
    matched: bool
    mismatches: tuple[Mismatch, ...]


def step_record_from_dict(data: dict[str, Any]) -> StepRecord:
    action_data = data["action"]
    action = Action(
        kind=action_data["kind"],
        name=action_data.get("name"),
        relation=action_data.get("relation"),
        row_id=action_data.get("row_id"),
        parent_id=action_data.get("parent_id"),
    )
    return StepRecord(
        sequence_id=data["sequence_id"],
        step_index=data["step_index"],
        action=action,
        disposition=data["disposition"],
        python_exception=data.get("python_exception"),
        sqlite_errorcode=data.get("sqlite_errorcode"),
        sqlite_errorname=data.get("sqlite_errorname"),
        in_transaction=data["in_transaction"],
        parent=tuple(data["parent"]),
        child_immediate=tuple(tuple(row) for row in data["child_immediate"]),
        child_deferred=tuple(tuple(row) for row in data["child_deferred"]),
        child_restrict=tuple(tuple(row) for row in data["child_restrict"]),
        foreign_key_check=tuple(tuple(row) for row in data["foreign_key_check"]),
        expected_error_key=data.get("expected_error_key"),
    )
