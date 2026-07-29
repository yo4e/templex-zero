# Study 007 Final Report — SQLite Deferred-Constraint and Savepoint State Conformance

_Date: 2026-07-29 (Asia/Tokyo)_  
_Final status: **Closed — negative setup result**_  
_Completed cycles: 2 of maximum 4_  
_Protected matrix executions: 0_

## Summary

Study 007 proposed comparing one exact CPython 3.13.5 / SQLite 3.46.1 Debian distribution build with an independently implemented relational and savepoint-stack model across 72 frozen declarative sequences.

The study closed before the protected matrix. Its twelve-case hand-audited correctness gate produced eleven complete matches and one retained mismatch. Under a deferred foreign-key declaration with `ON DELETE RESTRICT`, the frozen expectation required extended error code 787 / `SQLITE_CONSTRAINT_FOREIGNKEY`; the exact local engine returned 1811 / `SQLITE_CONSTRAINT_TRIGGER` while matching the expected immediate timing, relational preservation, and open transaction state.

Because the error map and inspected gate expectations were frozen, this difference could not be repaired without retrospective expectation revision. The gate therefore failed and the study closed as required.

## Research question

The proposed research question asked whether transaction boundaries, nested and duplicate savepoints, deferred and immediate constraints, failed boundaries, and recovery operations matched the independent model over exactly 72 sequences.

**The research question was not evaluated over that matrix.** Setup validity failed before protected execution.

## Exact target

- CPython 3.13.5 at `/usr/bin/python3.13`;
- Debian `python3.13 3.13.5-2`;
- SQLite API 3.46.1;
- Debian `libsqlite3-0 3.46.1-7+deb13u1`;
- source ID ending `f69aalt1`;
- exact paths, compile options, and digests recorded in `environment.json`.

The target is not the vanilla SQLite 3.46.1 artifact.

## Frozen protected design

Cycle 1 froze:

- one exact schema and seed state;
- a bounded declarative action grammar;
- an observation projection including extended error code/name;
- exactly 72 sequences and 439 actions;
- manifest SHA-256 `16a01c109b196a1127d7783f110e492e4609713f8f527e50e95d7ef254678b4c`;
- resource caps and a four-cycle maximum.

None of the 72 sequences was executed.

## Instrument and gate evidence

Cycle 2 created source-separated model, harness, and comparator layers. Thirteen targeted tests passed. Twelve miniature traces and every expected step were committed before the formal gate under expectation SHA-256 `cde3e40e9c43a9771123c4bc9a48750e6aa4ea1a1a0eac5747b6d0882f5b162e`.

Formal gate result:

| Measure | Result |
|---|---:|
| cases | 12 |
| complete matches | 11 |
| failed cases | 1 |
| mismatched steps | 1 |
| mismatched fields | 2 |
| protected matrix loaded | no |
| protected matrix executed | no |

The gate result was reproduced once with byte-identical output. Result SHA-256: `e40f3da0658418678b4b7e7343c5f9484d64965ef2306bacb06038d7f79fd4e6`.

## Retained mismatch

Case G12 tested immediate `RESTRICT` timing inside an explicit transaction.

At the failing delete:

- expected and observed exception class: `sqlite3.IntegrityError`;
- expected and observed timing: immediate statement failure;
- expected and observed relational effect: no parent or child deletion;
- expected and observed transaction state: transaction remains open;
- expected extended code/name: 787 / `SQLITE_CONSTRAINT_FOREIGNKEY`;
- observed extended code/name: 1811 / `SQLITE_CONSTRAINT_TRIGGER`.

The frozen expectation was not revised.

## Why no correction was applied

The model faithfully emitted the frozen error projection. The harness faithfully emitted runtime metadata. The comparator correctly reported the mismatch. No instrument implementation correction could remove the difference without falsifying one side or changing the frozen expectation.

The permitted correction phase was therefore unused.

## Hypothesis dispositions

| Hypothesis | Disposition |
|---|---|
| H1 savepoint-stack and rollback semantics | Not evaluated over the protected matrix |
| H2 immediate/deferred constraint timing | Not evaluated over the protected matrix |
| H3 failed-boundary recovery and reproducibility | Not evaluated over the protected matrix |
| Overall | **Negative setup result** |

The eleven passing miniature cases are setup evidence only. They do not support H1–H3.

## Methodological result

The negative result identifies a concrete design error: Cycle 1 treated semantically related foreign-key failures as one exact extended-error equivalence class without checking every distinct action family. The `RESTRICT` branch was behaviorally immediate as expected but observably distinct at the extended-code layer.

The hand gate served its intended function. It stopped a formally neat but invalid oracle before the protected denominator could produce misleading pass/fail counts.

## Reusable artifacts and limits

Retained artifacts include the 72-sequence declarative corpus, exact environment ledger, independent state model, fixed-template harness, immutable comparator, targeted tests, and twelve-case gate corpus. They are audit artifacts from a failed setup, not validated conformance instruments.

No claim is made about SQLite generally, the vanilla 3.46.1 release, security, durability, concurrency, performance, or another environment.

## Closure

Issue #13 is closed. Cycle 3 and Cycle 4 are cancelled. No protected outcome, reproduction, or hypothesis assignment will be manufactured after the gate failure.
