# Study 007 — SQLite Deferred-Constraint and Savepoint State Conformance

_Status: **Closed — negative setup result**_  
_Activated and closed: 2026-07-29 (Asia/Tokyo)_  
_Tracking issue: #13 (closed)_

Study 007 proposed testing one exact local CPython/SQLite build against an independently implemented finite relational and savepoint-state model across exactly 72 frozen original declarative sequences.

The study closed in Cycle 2 before the protected matrix. The twelve-case hand-audited gate produced eleven complete matches and one retained mismatch: the frozen `foreign_key` projection expected extended code 787 / `SQLITE_CONSTRAINT_FOREIGNKEY` for `ON DELETE RESTRICT`, while the exact local build returned 1811 / `SQLITE_CONSTRAINT_TRIGGER`. Timing, exception class, relational preservation, and transaction state matched.

The mismatch could not be repaired without changing a frozen expectation. No protected sequence was executed and H1–H3 were not evaluated.

## Exact target

- CPython: 3.13.5 at `/usr/bin/python3.13`
- Python package: `python3.13 3.13.5-2` on Debian 13
- SQLite API version: 3.46.1
- SQLite package: `libsqlite3-0 3.46.1-7+deb13u1`
- SQLite source ID ending `f69aalt1`

The target is a distribution-modified build, not the vanilla 3.46.1 artifact.

## Final evidence

- protected matrix: **0 / 72 executed**;
- targeted tests: **13 passed**;
- hand gate: **11 / 12 passed**;
- failed case: G12 immediate `RESTRICT` timing error projection;
- expectation SHA-256: `cde3e40e9c43a9771123c4bc9a48750e6aa4ea1a1a0eac5747b6d0882f5b162e`;
- result SHA-256: `e40f3da0658418678b4b7e7343c5f9484d64965ef2306bacb06038d7f79fd4e6`;
- repeated gate result: byte-identical.

## Main artifacts

- `PROTOCOL.md` — frozen active protocol retained as historical authority
- `schema.sql`, `manifest.tsv`, `manifest.sha256` — unexecuted protected design
- `actions.py`, `records.py`, `model.py`, `harness.py`, `comparator.py` — failed-gate instruments
- `tests/test_instruments.py` — targeted tests
- `HAND_GATE_EXPECTATIONS.md`, `hand_gate_cases.json`, `hand_gate_cases.sha256` — pre-execution gate freeze
- `hand_gate_result.json`, `hand_gate_result.sha256` — retained failure
- `CYCLE_1_ACTIVATION_AND_FREEZE.md` — Cycle 1 audit
- `CYCLE_2_INSTRUMENTS_AND_GATE.md` — Cycle 2 and closure audit
- `REPORT.md` — final report

These are auditable artifacts from a failed setup, not validated SQLite conformance instruments.
