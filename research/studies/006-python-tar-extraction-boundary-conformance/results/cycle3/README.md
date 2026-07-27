# Study 006 Cycle 3 Formal Result

_Date: 2026-07-27 (Asia/Tokyo)_  
_Status: **complete single formal execution; not yet reproduced or finally interpreted**_

## Preserved outcome

The frozen 32-fixture / 57-member matrix was executed exactly once under UID/GID 65534, no supplementary groups, and `no-new-privs`.

- fixtures observed: **32 / 32**;
- fixtures passing every frozen check: **31**;
- execution errors: **0**;
- sentinel changed nodes: **0**;
- other/outside-destination changed nodes: **0**;
- mismatch: **`META-NONEXEC-01` only**;
- scientific payload SHA-256: `b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`.

The single mismatch is an expected-mode disagreement. The frozen expectation was `0600`; the observed mode was `0644`. File contents, ownership, extraction success, containment, and sentinel state matched. The mismatch is retained and no expectation was revised.

## Result transport

The complete canonical result is transported as four ordered base64 parts:

1. `formal_result_v1.json.gz.b64.part01` — live Git blob `726aae92af31f17d1f5d8e9788e4d51cbc281eb9`;
2. `formal_result_v1.json.gz.b64.part02` — live Git blob `156dc8501a48866d3331218cb6dfb07fd15cc06d`;
3. `formal_result_v1.json.gz.b64.part03` — live Git blob `d3028634baa6aab5200e10629cac8c6f9430ac54`;
4. `formal_result_v1.json.gz.b64.part04` — live Git blob `283876c66aea3ded08306c887a06a33a81e675a0`.

Reconstruction identities:

- deterministic gzip: **6,905 bytes**, SHA-256 `23f00a304e5d76797ead9278f6372bc6145f4c5df62498fc8b885517c523bb6c`;
- canonical JSON: **97,289 bytes**, SHA-256 `07cac72ab1d29394ef82b71280b12b78370fff94e84f428fb3617221c61faabd`.

Use `../../tools/reconstruct_formal_result.py` from the study directory. The reconstructor verifies all four Git-blob identities before decoding.

## Companion records

- `run_summary.json` — compact result summary;
- `formal_mismatches_v1.json` — complete mismatch and execution-error record;
- `executed_identities_v1.json` — manifest and executed-source identities;
- `../../CYCLE_3_FORMAL_EXECUTION.md` — cycle audit;
- `../../CYCLE_3_SOURCE_AND_RESULT_IDENTITIES.md` — repository transport identities.

## Interpretation boundary

This directory does not assign final H1, H2, or H3 dispositions. Cycle 4 must reconstruct committed inputs, perform the one authorized clean reproduction, compare portable payloads, analyze the retained mismatch, report, and close the study. The complete original formal matrix must not be rerun before that reproduction cycle.
