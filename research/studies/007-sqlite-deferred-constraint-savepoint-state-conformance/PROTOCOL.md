# Study 007 Active Protocol

_Status: **Frozen active protocol — Cycle 1 complete**_  
_Activated: 2026-07-29 (Asia/Tokyo)_  
_Issue: #13_  
_Proposal: `research/proposals/007-sqlite-deferred-constraint-savepoint-state-conformance.md`_

## 1. Activation disposition

**GO unchanged.**

The exact runtime and wrapper capabilities required by the frozen proposal are available. Activation discovered that the local SQLite source ID ends in `alt1`, while SQLite's vanilla 3.46.1 release record ends in `1e33`. The earlier portfolio feasibility sentence saying that the local source ID was the published release source ID was incorrect.

This does not change the frozen proposal because the proposal explicitly requires activation to pin the exact local library, source ID, compile options, paths, and digests. It does narrow all later claims to the exact Debian distribution build. No result may be presented as a test of the vanilla release artifact or of SQLite generally.

## 2. Research question and hypotheses

The research question and H1–H3 are unchanged from the frozen proposal:

- **H1:** savepoint stack, duplicate-name, rollback, release, invalid-operation, and transaction-boundary behavior matches an independent state model with zero protected mismatch.
- **H2:** immediate, deferred, outer-boundary, repair, and `RESTRICT` timing matches the model with zero protected mismatch.
- **H3:** failed-boundary recovery, surviving nested marks, follow-up operations, and clean reproducibility match the frozen model and observation projection.

A plausible explanation does not convert a frozen mismatch into a pass.

## 3. Exact environment

The selected executable is `/usr/bin/python3.13`.

- CPython: `3.13.5`, Debian package `3.13.5-2`
- Python `sqlite3` wrapper version: `2.6.0`
- SQLite API version: `3.46.1`
- Debian SQLite package: `3.46.1-7+deb13u1`
- local source ID: `2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69aalt1`
- vanilla release source ID: `2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69a1e33`
- linked library: `/usr/lib/x86_64-linux-gnu/libsqlite3.so.0.8.6`
- linked-library SHA-256: `14c4418a06c5c2e30f5fb57bc8add93762236ae17898c6708984cf15e680ca71`
- `_sqlite3` extension SHA-256: `ad902edee2ed8dbbaec17309130436ffef1b69b1547a204e41e01e0d807a0c3d`
- `sqlite3/__init__.py` SHA-256: `6e956d2166e24ccf36fef21ad63d06a5dd8f7b674aca6c81ea91eacca6b85b01`
- `sqlite3/dbapi2.py` SHA-256: `7c5c8d98df1f2c50c4062a3be2c0f0499190c179fa4fc281507a1ef763a98f28`

The complete 60-option compile list is frozen in `environment.json`. Neither `OMIT_FOREIGN_KEY` nor `OMIT_TRIGGER` is present. `PRAGMA foreign_keys = ON`, `autocommit=True`, `Connection.in_transaction`, `sqlite_errorcode`, and `sqlite_errorname` passed preflight.

A later runtime, package, source ID, compile-option, module-path, or digest change invalidates protected execution. There is no silent migration.

## 4. Documentation identities

Retrieved 2026-07-29:

- `https://www.sqlite.org/lang_savepoint.html`
- `https://www.sqlite.org/foreignkeys.html`
- `https://sqlite.org/releaselog/3_46_1.html`
- `https://docs.python.org/3.13/library/sqlite3.html`

The Python URL is the maintained 3.13 documentation branch and displayed Python 3.13.14 documentation at retrieval. Runtime identity remains CPython 3.13.5; documentation drift must be recorded rather than treated as runtime migration.

## 5. Connection and setup

Each protected sequence uses one fresh `:memory:` database, one connection, one thread, and `sqlite3.connect(":memory:", autocommit=True)`.

The harness must:

1. enable foreign keys before schema creation;
2. execute the exact statements in `schema.sql` individually or by a setup-only script before the protected trace begins;
3. verify `PRAGMA foreign_keys` returns `1`;
4. begin the protected trace with `Connection.in_transaction == False`;
5. use no adapters, converters, row factory, user function, collation, extension, callback, authorizer, attached database, external file, network, subprocess, or arbitrary SQL.

## 6. Exact schema

`schema.sql` is authoritative. It contains:

- `parent(id INTEGER PRIMARY KEY)` seeded with IDs 1, 2, and 3;
- `child_immediate` with `ON DELETE NO ACTION NOT DEFERRABLE INITIALLY IMMEDIATE`;
- `child_deferred` with `ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED`;
- `child_restrict` with `ON DELETE RESTRICT DEFERRABLE INITIALLY DEFERRED`.

No schema mutation is permitted during a protected sequence.

## 7. Declarative action grammar

The manifest contains no SQL strings. The harness must translate only these actions through fixed templates:

| Action | Frozen SQL template |
|---|---|
| `begin` | `BEGIN` |
| `savepoint(name)` | one of `SAVEPOINT a`, `SAVEPOINT b`, `SAVEPOINT c`, `SAVEPOINT d` |
| `release(name)` | one of `RELEASE a`, `RELEASE b`, `RELEASE c`, `RELEASE d`, plus reserved missing name `z` |
| `rollback` | `ROLLBACK` |
| `rollback_to(name)` | one of `ROLLBACK TO a`, `ROLLBACK TO b`, `ROLLBACK TO c`, `ROLLBACK TO d`, plus reserved missing name `z` |
| `commit` | `COMMIT` |
| `insert_parent(id)` | `INSERT INTO parent(id) VALUES (?)` |
| `delete_parent(id)` | `DELETE FROM parent WHERE id = ?` |
| `insert_child(relation,id,parent_id)` | fixed table selected from `child_immediate`, `child_deferred`, `child_restrict`; `INSERT ... VALUES (?, ?)` |
| `delete_child(relation,id)` | fixed table selected from the same three-table enum; `DELETE ... WHERE id = ?` |

Names, relation selectors, and integer values must be validated against the frozen manifest before translation. They may never be interpolated from external input.

## 8. Observation schema

After every protected action, whether successful or failed, the SQLite harness emits exactly one portable step record:

- sequence ID and one-based step index;
- declarative action object;
- disposition: `ok` or `error`;
- Python exception class, or null;
- `sqlite_errorcode`, or null;
- `sqlite_errorname`, or null;
- `Connection.in_transaction`;
- ordered `parent` rows;
- ordered `child_immediate` rows;
- ordered `child_deferred` rows;
- ordered `child_restrict` rows;
- ordered `PRAGMA foreign_key_check` rows.

Exception prose, absolute paths, wall-clock timestamps, timing, memory addresses, raw pages, undeclared rowids, and platform-dependent tracebacks are excluded from the portable scientific payload. They may appear only in a separate operational log.

The independent model must emit the same logical fields except Python-specific exception metadata, for which it emits the frozen expected error key and mapped class/code/name.

## 9. Frozen error mapping

| Expectation key | Python class | Code | Name |
|---|---|---:|---|
| `savepoint_not_found` | `sqlite3.OperationalError` | 1 | `SQLITE_ERROR` |
| `nested_begin` | `sqlite3.OperationalError` | 1 | `SQLITE_ERROR` |
| `foreign_key` | `sqlite3.IntegrityError` | 787 | `SQLITE_CONSTRAINT_FOREIGNKEY` |

Cycle 1 preflight observed these mappings without reading or executing the protected manifest. Exception prose is not a verdict field.

## 10. Exact protected matrix

`manifest.tsv` is frozen with SHA-256:

`16a01c109b196a1127d7783f110e492e4609713f8f527e50e95d7ef254678b4c`

It contains exactly 72 sequences and 439 actions:

- A: 12 basic savepoint-stack and rollback sequences;
- B: 12 duplicate-name, missing-name, and nested-`BEGIN` sequences;
- C: 12 immediate/deferred/`RESTRICT` timing sequences;
- D: 12 failed-commit or failed-outer-release repair/rollback sequences;
- E: 12 nested versus transaction-savepoint sequences under violation;
- F: 12 failed-boundary survival and `RESTRICT` control sequences.

No sequence, order, action, expected error key, hypothesis tag, or denominator may change after this freeze. Full model-generated step expectations will be produced and committed in Cycle 2 before any protected matrix execution; they must be derivations from this protocol and manifest, not revisions based on SQLite outcomes.

## 11. Resource caps

- exact sequences: 72;
- maximum actions per sequence: 24;
- observed frozen maximum actions: 12;
- maximum active savepoint depth: 6;
- observed frozen structural maximum: 3;
- maximum distinct created names: 4;
- maximum rows per table: 16;
- maximum total inserted logical rows per sequence: 32;
- maximum portable step records per sequence: 24;
- maximum wall time per sequence: 2 seconds;
- maximum complete-matrix wall time: 120 seconds;
- no runner subprocess, network, extension loading, filesystem database, attached database, or external input.

Caps may not be raised after protected execution begins.

## 12. Instrument independence and correctness gate

Cycle 2 must keep three layers source-separated:

1. independent finite state model: no SQLite import or call, no harness helpers;
2. SQLite harness: no model transition functions or expected-verdict helpers;
3. comparator: reads immutable records from both, mutates neither.

Before the complete matrix, Cycle 2 must freeze twelve hand-audited miniature traces covering every gate category in the proposal. Every model state and expected SQLite observation must be written before running the gate. At most one bounded implementation-correction phase is allowed. It may repair code but may not change the proposal, protocol, manifest, error mapping, denominator, or inspected gate expectations to obtain a pass.

## 13. Cycle plan and stopping rule

- **Cycle 1 complete:** activation, environment and referent identities, protocol/schema/manifest/error/cap freeze, structure validation, setup preflight.
- **Cycle 2 next:** model, harness, comparator, targeted tests, twelve-case hand gate, instrument freeze. Stop before the 72-sequence matrix.
- **Cycle 3:** execute the complete protected matrix exactly once. Preserve results; do not assign final H1–H3 dispositions.
- **Cycle 4:** reconstruct committed inputs, perform one clean reproduction, compare portable payloads, analyze, assign dispositions, report, close.

No fifth cycle is permitted.

## 14. Exclusions

The study makes no claim about concurrency, locks, WAL, shared cache, durability, crash recovery, corruption, performance, hostile SQL, arbitrary databases, extension loading, security certification, other engines, other SQLite versions, or the vanilla SQLite 3.46.1 source artifact.
