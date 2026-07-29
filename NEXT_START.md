# Next Start

_Updated: 2026-07-29 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the Study 007 activation decision, active protocol, exact manifest and hashes, Cycle 1 audit, environment and preflight records, governance and human-intervention records, Issue #13, recent commits, and the frozen proposal.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**Study 007 is active. Cycle 1 is complete.**

Activation chose **GO unchanged** and opened Issue #13. The exact local target is:

- `/usr/bin/python3.13`, CPython 3.13.5;
- Debian `python3.13 3.13.5-2`;
- SQLite API 3.46.1;
- Debian `libsqlite3-0 3.46.1-7+deb13u1`;
- source ID ending `f69aalt1`;
- linked-library SHA-256 `14c4418a06c5c2e30f5fb57bc8add93762236ae17898c6708984cf15e680ca71`.

The vanilla release source ID ends `f69a1e33`. The prior portfolio feasibility claim of an exact source-ID match was wrong and is now corrected. The study remains unchanged because the frozen proposal required exact local build identity at activation. Later claims must not silently generalize to vanilla SQLite or SQLite generally.

## Frozen Cycle 1 artifacts

- `research/decisions/2026-07-29-study-007-activation.md`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/README.md`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/PROTOCOL.md`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/schema.sql`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/manifest.tsv`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/manifest.sha256`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/environment.json`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/preflight.py`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/cycle1_preflight.json`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/validate_manifest.py`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/cycle1_structure_validation.json`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/CYCLE_1_ACTIVATION_AND_FREEZE.md`

Manifest identity:

`16a01c109b196a1127d7783f110e492e4609713f8f527e50e95d7ef254678b4c`

Inventory: exactly 72 sequences, 12 in each family, 439 actions, maximum 12 actions per sequence, maximum structural savepoint depth 3. Protected execution count is zero.

## Mandatory boundaries

1. The independent model must not import or call SQLite and must not reuse harness verdict logic.
2. The harness must translate only the frozen declarative grammar through fixed SQL templates.
3. The comparator must compare immutable records and mutate neither instrument.
4. Twelve hand-audited traces and expected per-step records must be committed before gate execution.
5. At most one bounded instrument-correction phase is permitted after gate inspection.
6. No proposal, protocol, manifest, denominator, error mapping, or inspected gate expectation may be changed merely to obtain a pass.
7. The complete 72-sequence matrix must not run in Cycle 2.
8. The exact runtime, source ID, compile options, paths, packages, and digests must be rechecked before any later protected execution.
9. Study 007 has four cycles total. No fifth cycle.
10. No external contact, disclosure, spending, permission change, third-party operation, hostile SQL, extension loading, external database, concurrency, WAL, crash, durability, performance, or security-certification work is authorized.

## Next bounded work unit

The next exact `承認` may perform **Cycle 2 — instruments and correctness gate only**:

1. implement the independent finite state model;
2. implement the separate SQLite harness and comparator;
3. add targeted tests for stack semantics, constraint timing, error projection, and immutable records;
4. freeze twelve miniature hand-audited traces and all expected step records before execution;
5. run the gate;
6. use no more than one bounded implementation correction if needed;
7. freeze passing instruments or close negatively;
8. stop before the protected 72-sequence matrix.

## Human gate

> 承認

## Human action pending

None. A later exact `承認` opens Cycle 2 only.
