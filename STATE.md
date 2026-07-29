# State

_Last updated: 2026-07-29_

## Phase

**No active study / Study 007 closed as a negative setup result**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Active issue: **None**

## Closed studies

Studies 001 through 007 are closed.

- Study 006: valid partial Python tar extraction boundary-conformance result; H1 and H2 supported, H3 unsupported.
- Study 007: negative SQLite setup result; hand gate failed before protected execution.

## Study 007 final result

- Final report: `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/REPORT.md`
- Cycle 2 audit: `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/CYCLE_2_INSTRUMENTS_AND_GATE.md`
- Exact target: CPython 3.13.5 and Debian SQLite 3.46.1 build ending `alt1`
- Frozen protocol blob: `5b138a99adb3bc38af20f95b3bb209538119482b`
- Frozen matrix: 72 sequences / 439 actions
- Protected matrix executions: **0**
- Targeted tests: **13 passed**
- Hand gate: **11 / 12 passed; G12 failed**
- Retained mismatch: expected 787 / `SQLITE_CONSTRAINT_FOREIGNKEY`; observed 1811 / `SQLITE_CONSTRAINT_TRIGGER` for immediate `ON DELETE RESTRICT` failure
- Timing, exception class, row state, and transaction state matched
- Gate repetition: byte-identical failure
- Correction phase: unused because changing the result required revising a frozen expectation, not repairing an instrument defect
- H1–H3: not evaluated
- Overall: **negative setup result**

The failure exposed observational category collapse in the Cycle 1 error projection. `self/FAILURE_MODES.md` now records the corresponding countermeasure. A closure-time accidental overwrite of the frozen protocol was immediately reversed; the live content blob again equals the original frozen blob.

## Next bounded work

The next exact `承認` may perform **one post-Study-007 portfolio decision only**:

1. re-read all seven closed studies, governance, self-model, failure modes, open issues, and recent commits;
2. commit a selection threshold before candidate scoring;
3. compare materially distinct next directions plus inactivity, including the cost of another exact-conformance study and the new category-collapse evidence;
4. select at most one inactive proposal or remain inactive;
5. update decision, state, restart, and intervention records;
6. stop before study activation, implementation, corpus execution, protected outcome inspection, or external action.

## Human action currently needed

None beyond a later exact `承認` for the bounded post-Study-007 portfolio decision.
