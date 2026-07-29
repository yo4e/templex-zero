from __future__ import annotations

from pathlib import Path
import sqlite3
from typing import Iterable

from actions import Action
from records import StepRecord

_NAMES = frozenset({"a", "b", "c", "d", "z"})
_CREATE_NAMES = frozenset({"a", "b", "c", "d"})
_TABLES = {
    "immediate": "child_immediate",
    "deferred": "child_deferred",
    "deferred_restrict": "child_restrict",
}


class SQLiteHarness:
    """SQLite observation harness with fixed declarative-to-SQL translation."""

    def __init__(self, schema_path: str | Path) -> None:
        self.schema_path = Path(schema_path)
        self.schema_sql = self.schema_path.read_text(encoding="utf-8")

    def run_sequence(self, sequence_id: str, actions: Iterable[Action]) -> tuple[StepRecord, ...]:
        connection = sqlite3.connect(":memory:", autocommit=True)
        try:
            connection.executescript(self.schema_sql)
            enabled = connection.execute("PRAGMA foreign_keys").fetchone()
            if enabled != (1,):
                raise RuntimeError("foreign key enforcement is not enabled")
            if connection.in_transaction:
                raise RuntimeError("schema setup left a transaction open")
            records: list[StepRecord] = []
            for index, action in enumerate(actions, 1):
                disposition = "ok"
                exception_name: str | None = None
                errorcode: int | None = None
                errorname: str | None = None
                try:
                    sql, params = self._translate(action)
                    connection.execute(sql, params)
                except sqlite3.Error as exc:
                    disposition = "error"
                    exception_name = f"sqlite3.{exc.__class__.__name__}"
                    errorcode = getattr(exc, "sqlite_errorcode", None)
                    errorname = getattr(exc, "sqlite_errorname", None)
                records.append(
                    self._observe(
                        connection,
                        sequence_id,
                        index,
                        action,
                        disposition,
                        exception_name,
                        errorcode,
                        errorname,
                    )
                )
            return tuple(records)
        finally:
            connection.close()

    def _translate(self, action: Action) -> tuple[str, tuple[object, ...]]:
        kind = action.kind
        if kind == "begin":
            return "BEGIN", ()
        if kind == "rollback":
            return "ROLLBACK", ()
        if kind == "commit":
            return "COMMIT", ()
        if kind == "savepoint":
            if action.name not in _CREATE_NAMES:
                raise ValueError("invalid created savepoint name")
            return f"SAVEPOINT {action.name}", ()
        if kind == "release":
            if action.name not in _NAMES:
                raise ValueError("invalid release name")
            return f"RELEASE {action.name}", ()
        if kind == "rollback_to":
            if action.name not in _NAMES:
                raise ValueError("invalid rollback-to name")
            return f"ROLLBACK TO {action.name}", ()
        if kind == "insert_parent":
            return "INSERT INTO parent(id) VALUES (?)", (action.row_id,)
        if kind == "delete_parent":
            return "DELETE FROM parent WHERE id = ?", (action.row_id,)
        if kind == "insert_child":
            table = self._table(action.relation)
            return f"INSERT INTO {table}(id, parent_id) VALUES (?, ?)", (action.row_id, action.parent_id)
        if kind == "delete_child":
            table = self._table(action.relation)
            return f"DELETE FROM {table} WHERE id = ?", (action.row_id,)
        raise ValueError(f"unsupported action: {action}")

    @staticmethod
    def _table(relation: str | None) -> str:
        if relation not in _TABLES:
            raise ValueError(f"invalid relation: {relation!r}")
        return _TABLES[relation]

    @staticmethod
    def _observe(
        connection: sqlite3.Connection,
        sequence_id: str,
        step_index: int,
        action: Action,
        disposition: str,
        exception_name: str | None,
        errorcode: int | None,
        errorname: str | None,
    ) -> StepRecord:
        def rows(table: str) -> tuple[tuple[int, int], ...]:
            return tuple(connection.execute(f"SELECT id, parent_id FROM {table} ORDER BY id"))

        parent = tuple(row[0] for row in connection.execute("SELECT id FROM parent ORDER BY id"))
        fk_rows = tuple(sorted(tuple(row) for row in connection.execute("PRAGMA foreign_key_check")))
        return StepRecord(
            sequence_id=sequence_id,
            step_index=step_index,
            action=action,
            disposition=disposition,
            python_exception=exception_name,
            sqlite_errorcode=errorcode,
            sqlite_errorname=errorname,
            in_transaction=connection.in_transaction,
            parent=parent,
            child_immediate=rows("child_immediate"),
            child_deferred=rows("child_deferred"),
            child_restrict=rows("child_restrict"),
            foreign_key_check=fk_rows,
            expected_error_key=None,
        )
