from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from actions import Action
from records import StepRecord

_ERROR_MAP: dict[str, tuple[str, int, str]] = {
    "savepoint_not_found": ("sqlite3.OperationalError", 1, "SQLITE_ERROR"),
    "nested_begin": ("sqlite3.OperationalError", 1, "SQLITE_ERROR"),
    "foreign_key": ("sqlite3.IntegrityError", 787, "SQLITE_CONSTRAINT_FOREIGNKEY"),
}


@dataclass(frozen=True, slots=True)
class Snapshot:
    parent: frozenset[int]
    child_immediate: tuple[tuple[int, int], ...]
    child_deferred: tuple[tuple[int, int], ...]
    child_restrict: tuple[tuple[int, int], ...]


@dataclass(frozen=True, slots=True)
class SavepointMark:
    name: str
    snapshot: Snapshot


class IndependentModel:
    """SQLite-independent finite relational and savepoint-stack model."""

    def __init__(self) -> None:
        self.parent: set[int] = {1, 2, 3}
        self.children: dict[str, dict[int, int]] = {
            "immediate": {},
            "deferred": {},
            "deferred_restrict": {},
        }
        self.transaction_origin: Snapshot | None = None
        self.transaction_kind: str | None = None
        self.savepoints: list[SavepointMark] = []

    @property
    def in_transaction(self) -> bool:
        return self.transaction_origin is not None

    def run_sequence(self, sequence_id: str, actions: Iterable[Action]) -> tuple[StepRecord, ...]:
        records: list[StepRecord] = []
        for index, action in enumerate(actions, 1):
            error_key = self.apply(action)
            records.append(self._record(sequence_id, index, action, error_key))
        return tuple(records)

    def apply(self, action: Action) -> str | None:
        kind = action.kind
        if kind == "begin":
            if self.in_transaction:
                return "nested_begin"
            self._start_transaction("begin")
            return None
        if kind == "savepoint":
            assert action.name is not None
            if not self.in_transaction:
                self._start_transaction("savepoint")
            self.savepoints.append(SavepointMark(action.name, self._snapshot()))
            return None
        if kind == "release":
            assert action.name is not None
            return self._release(action.name)
        if kind == "rollback_to":
            assert action.name is not None
            return self._rollback_to(action.name)
        if kind == "commit":
            return self._commit()
        if kind == "rollback":
            return self._rollback()
        return self._apply_dml(action)

    def _start_transaction(self, kind: str) -> None:
        self.transaction_origin = self._snapshot()
        self.transaction_kind = kind
        self.savepoints = []

    def _release(self, name: str) -> str | None:
        index = self._find_savepoint(name)
        if index is None:
            return "savepoint_not_found"
        if self.transaction_kind == "savepoint" and index == 0:
            if self._has_foreign_key_violation():
                return "foreign_key"
            self._clear_transaction()
            return None
        del self.savepoints[index:]
        return None

    def _rollback_to(self, name: str) -> str | None:
        index = self._find_savepoint(name)
        if index is None:
            return "savepoint_not_found"
        mark = self.savepoints[index]
        self._restore(mark.snapshot)
        del self.savepoints[index + 1 :]
        return None

    def _commit(self) -> str | None:
        if not self.in_transaction:
            raise ValueError("commit outside explicit transaction is outside frozen grammar use")
        if self._has_foreign_key_violation():
            return "foreign_key"
        self._clear_transaction()
        return None

    def _rollback(self) -> str | None:
        if not self.in_transaction or self.transaction_origin is None:
            raise ValueError("rollback outside explicit transaction is outside frozen grammar use")
        self._restore(self.transaction_origin)
        self._clear_transaction()
        return None

    def _apply_dml(self, action: Action) -> str | None:
        before = self._snapshot()
        kind = action.kind
        if kind == "insert_parent":
            assert action.row_id is not None
            if action.row_id in self.parent:
                raise ValueError("duplicate parent IDs are outside the frozen matrix")
            self.parent.add(action.row_id)
        elif kind == "delete_parent":
            assert action.row_id is not None
            if self._referenced_by("immediate", action.row_id) or self._referenced_by("deferred_restrict", action.row_id):
                return "foreign_key"
            self.parent.discard(action.row_id)
        elif kind == "insert_child":
            assert action.relation is not None and action.row_id is not None and action.parent_id is not None
            table = self.children[action.relation]
            if action.row_id in table:
                raise ValueError("duplicate child IDs are outside the frozen matrix")
            table[action.row_id] = action.parent_id
            if action.relation == "immediate" and action.parent_id not in self.parent:
                self._restore(before)
                return "foreign_key"
        elif kind == "delete_child":
            assert action.relation is not None and action.row_id is not None
            self.children[action.relation].pop(action.row_id, None)
        else:
            raise ValueError(f"unsupported action: {action}")

        if not self.in_transaction and self._has_foreign_key_violation():
            self._restore(before)
            return "foreign_key"
        return None

    def _referenced_by(self, relation: str, parent_id: int) -> bool:
        return parent_id in self.children[relation].values()

    def _has_foreign_key_violation(self) -> bool:
        return any(parent_id not in self.parent for table in self.children.values() for parent_id in table.values())

    def _find_savepoint(self, name: str) -> int | None:
        for index in range(len(self.savepoints) - 1, -1, -1):
            if self.savepoints[index].name == name:
                return index
        return None

    def _clear_transaction(self) -> None:
        self.transaction_origin = None
        self.transaction_kind = None
        self.savepoints = []

    def _snapshot(self) -> Snapshot:
        return Snapshot(
            parent=frozenset(self.parent),
            child_immediate=tuple(sorted(self.children["immediate"].items())),
            child_deferred=tuple(sorted(self.children["deferred"].items())),
            child_restrict=tuple(sorted(self.children["deferred_restrict"].items())),
        )

    def _restore(self, snapshot: Snapshot) -> None:
        self.parent = set(snapshot.parent)
        self.children = {
            "immediate": dict(snapshot.child_immediate),
            "deferred": dict(snapshot.child_deferred),
            "deferred_restrict": dict(snapshot.child_restrict),
        }

    def _foreign_key_check(self) -> tuple[tuple[str, int, str, int], ...]:
        rows: list[tuple[str, int, str, int]] = []
        names = {
            "immediate": "child_immediate",
            "deferred": "child_deferred",
            "deferred_restrict": "child_restrict",
        }
        for relation, table in self.children.items():
            for row_id, parent_id in table.items():
                if parent_id not in self.parent:
                    rows.append((names[relation], row_id, "parent", 0))
        return tuple(sorted(rows))

    def _record(self, sequence_id: str, step_index: int, action: Action, error_key: str | None) -> StepRecord:
        exception = code = name = None
        disposition = "ok"
        if error_key is not None:
            disposition = "error"
            exception, code, name = _ERROR_MAP[error_key]
        return StepRecord(
            sequence_id=sequence_id,
            step_index=step_index,
            action=action,
            disposition=disposition,
            python_exception=exception,
            sqlite_errorcode=code,
            sqlite_errorname=name,
            in_transaction=self.in_transaction,
            parent=tuple(sorted(self.parent)),
            child_immediate=tuple(sorted(self.children["immediate"].items())),
            child_deferred=tuple(sorted(self.children["deferred"].items())),
            child_restrict=tuple(sorted(self.children["deferred_restrict"].items())),
            foreign_key_check=self._foreign_key_check(),
            expected_error_key=error_key,
        )
