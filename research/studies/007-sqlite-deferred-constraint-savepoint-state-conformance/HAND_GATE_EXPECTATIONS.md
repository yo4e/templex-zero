# Study 007 Hand-Gate Expectations

_Status: frozen before gate execution_

The twelve miniature traces in `hand_gate_cases.json` cover every mandatory gate category. Each compact step row explicitly records, in order: action token, disposition, expected error key, Python exception class, SQLite extended error code/name, `in_transaction`, four ordered relation projections, and ordered `foreign_key_check` rows.

The expectations preserve the Cycle 1 frozen error map. Every declarative `foreign_key` expectation maps to `sqlite3.IntegrityError`, extended code 787, and `SQLITE_CONSTRAINT_FOREIGNKEY`, including the `ON DELETE RESTRICT` case. No observed runtime result may revise that expectation.

These gate traces are separate miniature cases, not rows from the protected 72-sequence manifest. The gate runner records `protected_manifest_loaded=false` and `protected_matrix_executed=false`.

| ID | Category |
|---|---|
| G01 | basic savepoint and release |
| G02 | inner release followed by outer rollback |
| G03 | rollback-to with retained mark |
| G04 | duplicate savepoint names |
| G05 | missing savepoint name |
| G06 | nested `BEGIN` error |
| G07 | immediate foreign-key failure |
| G08 | deferred violation repaired before commit |
| G09 | failed commit leaves transaction open |
| G10 | nested release during deferred violation |
| G11 | failed outer transaction-savepoint release |
| G12 | immediate `RESTRICT` timing |
