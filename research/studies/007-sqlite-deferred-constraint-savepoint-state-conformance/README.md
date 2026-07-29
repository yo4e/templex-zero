# Study 007 — SQLite Deferred-Constraint and Savepoint State Conformance

_Status: **Active — Cycle 1 complete; instruments not implemented**_  
_Activated: 2026-07-29 (Asia/Tokyo)_  
_Tracking issue: #13_

Study 007 tests whether one exact local CPython/SQLite build follows the documented transaction-stack, savepoint, deferred-foreign-key, failed-boundary, and recovery semantics across exactly 72 frozen original declarative sequences when compared with an independently implemented finite relational and savepoint-state model.

## Frozen target

- CPython: 3.13.5 at `/usr/bin/python3.13`
- Python package: `python3.13 3.13.5-2` on Debian 13
- SQLite API version: 3.46.1
- SQLite package: `libsqlite3-0 3.46.1-7+deb13u1`
- SQLite source ID: `2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69aalt1`

The local source ID is not the vanilla 3.46.1 release source ID ending in `1e33`. This is a distribution-modified build. The study is therefore scoped to the exact local binary and does not claim byte-identical coverage of SQLite's vanilla release artifact.

## Frozen artifacts

- `PROTOCOL.md` — active protocol, hypotheses, grammar, observations, errors, caps, and cycle rules
- `schema.sql` — exact schema and seed rows
- `manifest.tsv` — exactly 72 protected sequences
- `manifest.sha256` — frozen manifest identity
- `validate_manifest.py` — structure-only validator; imports no SQLite and executes no SQL
- `preflight.py` and `cycle1_preflight.json` — setup capability preflight, not protected evidence
- `environment.json` — runtime, package, source, compile, path, digest, and documentation identities
- `CYCLE_1_ACTIVATION_AND_FREEZE.md` — activation and freeze audit

## Current boundary

No independent model, SQLite harness, comparator, hand-audited gate, or protected matrix result exists. No protected sequence has been executed.

The next cycle is Cycle 2 only: implement independent instruments, freeze twelve hand-audited traces, pass the correctness gate with at most one bounded implementation-correction phase, and stop before the complete 72-sequence matrix.
