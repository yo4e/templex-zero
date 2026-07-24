# Study 005 Cycle 3 — Formal Runner Source-Identity Correction

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **Post-execution correction; formal result not rerun**_

## Authority of this correction

This record supersedes any statement in `CYCLE_3_HARNESS_FREEZE.md`, `CYCLE_3_FORMAL_EXECUTION.md`, or the first version of `data/harness_freeze_identity_v1.json` that implies the formal execution used a runner byte-identical to the pre-outcome repository file `experiments/study005_cycle3.py`.

The harness module and targeted-test file were byte-identical to their pre-outcome repository blobs. The formal runner was not.

## Evidence

Pre-outcome repository runner:

- path: `experiments/study005_cycle3.py`;
- Git blob: `f1fcb1166580d874112c09ff8fe438ae8837a81a`.

Execution-local runner:

- bytes: 8,810;
- SHA-256: `cbbd781f478c0d54c59f1b1bea66f515698adccdb17111bd14fa1e87b1b0c381`;
- Git blob: `06280fe92a279a3ef847dd07448a041c379af9b0`;
- preserved unchanged at `data/study005_cycle3_executed_runner_v1.py`.

Frozen support files that did match:

- `src/templex_zero/zoneinfo_harness.py`: Git blob `09692057aae2575c6760e07a41d378a79571c3a0`;
- `tests/test_zoneinfo_harness.py`: Git blob `0ce9da76c736b1d4585014da9250bfd49b520d1c`.

The first identity file incorrectly associated the execution-local runner SHA-256 with the repository path. It has been replaced by schema v2, which records both distinct identities.

## Difference assessment

Direct source inspection found formatting differences and two imports (`hashlib` and `importlib.util`) that were unused in the execution-local form. No intended comparison, isolation, serialization, record-generation, or output-path difference was identified.

However, this cycle does **not** treat semantic equivalence as proven. The protected sequence required the executed runner to be frozen before outcomes, and literal byte identity did not hold. This is a procedural deviation even though the mechanical result may still reproduce exactly.

## Effect on Cycle 3 result

The formal corpus was not rerun. The preserved mechanical artifacts remain:

- H1 records: 90,079;
- H2 records: 26,778;
- H3 records: 44,790;
- nonzero mismatch records: 0;
- canonical result SHA-256: `7115ba2b6a11ce0c6eb0230c2918f47e4f7721e314e97c438b97b3157795cfd6`.

These values are not promoted to final hypothesis conclusions in Cycle 3.

## Required Cycle 4 resolution

Cycle 4 must use a clean repository state and the exact committed source. It must run the pre-outcome repository runner without adapting it to the Cycle 3 outcome and compare all generated identities with the preserved Cycle 3 artifacts.

- Exact identity reproduction would show that the runner byte difference was mechanically irrelevant for this corpus, while the procedural deviation remains reportable.
- Any identity difference must be preserved, analyzed, and reflected in H1–H3 and study disposition.
- No fifth cycle and no adaptive repair are permitted.
