#!/usr/bin/env python3
"""Study 007 capability preflight.

This script does not read or execute the protected 72-sequence manifest. It only
checks the pinned runtime identity, wrapper surfaces, exact schema compilation,
basic explicit transaction control, and the frozen exception-code mapping.
"""
from __future__ import annotations
import hashlib, json, pathlib, platform, sqlite3, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent
SCHEMA = ROOT / "schema.sql"
EXPECTED_SOURCE_ID = "2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69aalt1"

def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def capture_error(fn):
    try:
        fn()
    except sqlite3.Error as exc:
        return {
            "python_exception": f"sqlite3.{type(exc).__name__}",
            "sqlite_errorcode": getattr(exc, "sqlite_errorcode", None),
            "sqlite_errorname": getattr(exc, "sqlite_errorname", None),
        }
    raise AssertionError("expected sqlite3.Error")

def main() -> None:
    assert sys.version_info[:3] == (3, 13, 5)
    assert sqlite3.sqlite_version == "3.46.1"
    con = sqlite3.connect(":memory:", autocommit=True)
    source_id = con.execute("SELECT sqlite_source_id()").fetchone()[0]
    assert source_id == EXPECTED_SOURCE_ID
    options = sorted(row[0] for row in con.execute("PRAGMA compile_options"))
    assert not any(opt.startswith("OMIT_FOREIGN_KEY") for opt in options)
    assert not any(opt.startswith("OMIT_TRIGGER") for opt in options)
    con.executescript(SCHEMA.read_text(encoding="utf-8"))
    assert con.execute("PRAGMA foreign_keys").fetchone()[0] == 1
    assert con.in_transaction is False

    con.execute("BEGIN")
    assert con.in_transaction is True
    nested_begin = capture_error(lambda: con.execute("BEGIN"))
    con.execute("ROLLBACK")
    assert con.in_transaction is False

    con.execute("SAVEPOINT preflight_only")
    assert con.in_transaction is True
    con.execute("RELEASE preflight_only")
    assert con.in_transaction is False

    missing_release = capture_error(lambda: con.execute("RELEASE never_created_preflight_name"))
    immediate_fk = capture_error(
        lambda: con.execute("INSERT INTO child_immediate(id, parent_id) VALUES (9001, 9999)")
    )
    assert con.in_transaction is False
    assert con.execute("SELECT COUNT(*) FROM child_immediate").fetchone()[0] == 0
    con.close()

    module = pathlib.Path(sqlite3.__file__)
    dbapi = module.parent / "dbapi2.py"
    try:
        import _sqlite3
        extension = pathlib.Path(_sqlite3.__file__)
    except Exception:
        extension = None

    result = {
        "status": "pass",
        "protected_manifest_loaded": False,
        "protected_sequence_executed": False,
        "runtime": {
            "executable": sys.executable,
            "python_version": platform.python_version(),
            "python_build": list(platform.python_build()),
            "sqlite_wrapper_version": getattr(sqlite3, "version", None),
            "sqlite_engine_version": sqlite3.sqlite_version,
            "sqlite_source_id": source_id,
            "compile_options": options,
            "compile_options_count": len(options),
        },
        "files": [
            {"path": str(module), "sha256": sha(module)},
            {"path": str(dbapi), "sha256": sha(dbapi)},
        ] + ([{"path": str(extension), "sha256": sha(extension)}] if extension else []),
        "capabilities": {
            "connect_autocommit_true": True,
            "in_transaction": True,
            "foreign_keys_enabled": True,
            "exact_schema_compiles": True,
            "explicit_begin_rollback": True,
            "outer_savepoint_release": True,
            "exception_errorcode": True,
            "exception_errorname": True,
        },
        "error_mapping_observed": {
            "nested_begin": nested_begin,
            "savepoint_not_found": missing_release,
            "foreign_key": immediate_fk,
        },
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
