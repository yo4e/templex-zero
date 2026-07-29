# Next Start

_Updated: 2026-07-29 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the Study 007 final report and Cycle 2 audit, the frozen protocol and gate expectations, governance and human-intervention records, all closed-study reports, self-model and failure modes, open issues, and recent commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**TEMPLEX/0 has no active study. Studies 001 through 007 are closed.**

Study 007 activated the frozen SQLite proposal and completed Cycle 1, but closed during Cycle 2 as a negative setup result before the protected matrix.

## Study 007 retained evidence

- exact target: CPython 3.13.5 and Debian `libsqlite3-0 3.46.1-7+deb13u1`;
- frozen matrix: 72 sequences / 439 actions;
- protected matrix executions: 0;
- source-separated model, harness, and comparator implemented;
- targeted tests: 13 passed;
- twelve-case expectation SHA-256: `cde3e40e9c43a9771123c4bc9a48750e6aa4ea1a1a0eac5747b6d0882f5b162e`;
- hand gate: 11 / 12 passed;
- failed case: G12 immediate `ON DELETE RESTRICT` error projection;
- expected: 787 / `SQLITE_CONSTRAINT_FOREIGNKEY`;
- observed: 1811 / `SQLITE_CONSTRAINT_TRIGGER`;
- timing, exception class, row state, and transaction state matched;
- repeated result: byte-identical;
- result SHA-256: `e40f3da0658418678b4b7e7343c5f9484d64965ef2306bacb06038d7f79fd4e6`;
- correction phase unused; changing the result required expectation revision, not code repair;
- H1–H3 not evaluated.

Key records:

- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/REPORT.md`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/CYCLE_2_INSTRUMENTS_AND_GATE.md`
- `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/hand_gate_result.json`
- `self/FAILURE_MODES.md` — FM-009 observational category collapse

## Mandatory lessons

1. A semantic category such as “foreign-key failure” is not evidence that every operation shares one exact extended error code.
2. Exact low-level projections require preflight coverage of every materially distinct operation family, or a deliberately coarser frozen projection.
3. A gate mismatch cannot be repaired by widening equivalence after inspection.
4. Eleven passing miniature cases do not support H1–H3 when the setup gate as a whole fails.
5. The unexecuted 72-sequence matrix remains archival design, not evidence.
6. No successor study should be activated mechanically from the failed Study 007 design.
7. No external contact, spending, permission change, third-party operation, hostile input, or new publication channel is authorized by a normal approval.

## Next bounded work unit

The next exact `承認` may perform **one post-Study-007 portfolio decision only**:

1. inspect all seven closed-study results and the live governance, self, failure-mode, issue, and commit records;
2. freeze a selection threshold before candidate scores;
3. compare materially different directions plus inactivity;
4. explicitly evaluate whether a repaired SQLite successor would add information or merely repair an authored expectation;
5. select at most one frozen inactive proposal or remain inactive;
6. stop before activation, implementation, corpus execution, or protected outcome inspection.

## Human gate

> 承認

## Human action pending

None. A later exact `承認` opens the bounded post-Study-007 portfolio decision only.
