# Study 007 Cycle 2 — Instruments and Correctness-Gate Audit

_Date: 2026-07-29 (Asia/Tokyo)_  
_Disposition: **hand gate failed; Study 007 closes as a negative setup result**_  
_Issue: #13_

## Work selected

Implement the SQLite-independent relational/savepoint-stack model, separate SQLite harness, immutable-record comparator, and targeted tests; freeze twelve hand-audited traces and every expected step before gate execution; run the gate with at most one bounded implementation-correction phase; stop before the protected 72-sequence matrix.

## Instruments implemented

- `actions.py`: bounded declarative action representation and parser;
- `records.py`: frozen portable step, mismatch, and comparison records;
- `model.py`: SQLite-independent relation and savepoint-snapshot model;
- `harness.py`: fixed-template SQLite observation harness;
- `comparator.py`: immutable field comparator;
- `tests/test_instruments.py`: thirteen targeted tests;
- `freeze_hand_gate.py`, `run_hand_gate.py`: expectation freezer and gate runner.

Source-separation tests confirm that the model imports no SQLite or harness code, the harness imports no model code, and the comparator imports neither instrument.

## Pre-gate development evidence

Thirteen targeted tests passed after one test-only repair. The first discovery run accidentally named a test helper `run`, overriding `unittest.TestCase.run`; it stopped the test framework before gate execution. The helper was renamed. This was not the post-gate instrument-correction phase and changed no model, harness, protocol, or expectation.

A targeted harness test observed that the exact local SQLite build reports an `ON DELETE RESTRICT` failure as extended code 1811 / `SQLITE_CONSTRAINT_TRIGGER`. This was seen before the formal hand gate, but the Cycle 1 frozen `foreign_key` expectation remained unchanged at 787 / `SQLITE_CONSTRAINT_FOREIGNKEY`.

## Expectations frozen before gate execution

The twelve required miniature traces were committed before gate execution:

- expectation SHA-256: `cde3e40e9c43a9771123c4bc9a48750e6aa4ea1a1a0eac5747b6d0882f5b162e`;
- categories: basic release, outer rollback, retained rollback-to mark, duplicate names, missing name, nested `BEGIN`, immediate failure, deferred repair, failed commit, nested release under violation, failed outer release, and immediate `RESTRICT`;
- every step records disposition, exception projection, `in_transaction`, all relation rows, and `foreign_key_check`;
- the protected manifest is not loaded by the gate runner.

The expectations deliberately preserve the Cycle 1 mapping. No expectation was changed after the targeted observation or formal gate result.

## Formal gate result

Result: **11 / 12 cases passed; G12 failed**.

For G12 step 4, `delete_parent(99)` under a deferred `ON DELETE RESTRICT` declaration:

| Field | Frozen expectation | Observed |
|---|---:|---:|
| Python exception | `sqlite3.IntegrityError` | `sqlite3.IntegrityError` |
| SQLite extended code | `787` | `1811` |
| SQLite extended name | `SQLITE_CONSTRAINT_FOREIGNKEY` | `SQLITE_CONSTRAINT_TRIGGER` |
| failure timing | immediate | immediate |
| relational state | parent and child preserved | parent and child preserved |
| transaction state | open | open |

There were no other mismatches. Model state, row projections, foreign-key-check output, savepoint behavior, and transaction state matched in all twelve cases.

The result file SHA-256 is `e40f3da0658418678b4b7e7343c5f9484d64965ef2306bacb06038d7f79fd4e6`.

The gate was executed a second time without changing inputs. It failed identically and produced a byte-identical result file.

## Correction decision

The one permitted post-gate correction opportunity was not used. The model implements the frozen mapping, the harness reports the exact runtime metadata, and the comparator correctly exposes the difference. Changing any of them to make 787 equal 1811 would either falsify the observation or revise the frozen expectation.

The mismatch is therefore an expectation/protocol defect, not a correctable instrument implementation defect.

## Protected boundary

- protected manifest loaded by gate: **false**;
- protected 72-sequence matrix executed: **false**;
- protected outcome inspected: **none**;
- full matrix expectations generated: **no**, because the setup gate failed and no protected execution may follow;
- H1–H3 dispositions assigned: **none**.

## Methodological diagnosis

Cycle 1 collapsed all foreign-key failures into one low-level extended-code class after observing only a subset of operation families. The schema already distinguished `NO ACTION` from `RESTRICT`, but the error projection did not. The hand gate correctly prevented that untested equivalence assumption from contaminating the 72-sequence experiment.

## Final Cycle 2 judgment

Study 007 cannot advance to Cycle 3 under its frozen protocol. It closes in Cycle 2 as a **negative setup result**. The failed expectation remains visible and unchanged; the 72-sequence matrix is cancelled unexecuted.
