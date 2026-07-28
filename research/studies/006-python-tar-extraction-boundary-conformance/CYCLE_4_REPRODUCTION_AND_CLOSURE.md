# Study 006 Cycle 4 — Reproduction and Closure

_Date: 2026-07-28 (Asia/Tokyo)_  
_Disposition: **clean reproduction complete; valid partial bounded result; Study 006 closed**_

## Work performed

Cycle 4 re-read the live protocol, Cycle 3 audit and source/result identity ledger, exact manifest, Issue #12, governance, restart state, and frozen proposal. It fetched the exact live Git blobs for the manifest, four instruments, formal runner, and four-part original-result transport.

Before any extraction began, a local reconstruction check detected that the decoded manifest file still contained an older incomplete local reconstruction although the corrected fetched base64 source was present. No protected outcome had been generated. The decoded file was replaced with the exact live 18,742-byte manifest and all source, SHA-256, and Git Blob identities were revalidated. This was an input-transfer correction before reproduction, not a fixture or expectation change.

The one authorized clean reproduction then executed all 32 fixtures exactly once under the frozen non-privileged boundary.

A first attempt to upload a larger base64 result part was rejected by platform safety screening before any repository write. The already completed result was not regenerated. The same deterministic gzip was instead stored as sixteen smaller text parts, each verified by live Git Blob and full reconstruction.

## Exact reproduction boundary

- CPython 3.13.5 at `/usr/bin/python3`;
- local `tarfile.py` SHA-256 `99db774e5017d7c3270db4986e4bc46d18222dfb26dc12bf0a73cf613e1c48cf`;
- Linux 6.12.13 x86_64, glibc 2.41, ext4;
- UID/GID 65534, no supplementary groups, `no-new-privs`;
- exact manifest SHA-256 `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`;
- exact live source blobs recorded in `CYCLE_4_SOURCE_AND_RESULT_IDENTITIES.md`;
- no external archive, real user path, elevated extraction, network action, external contact, or expectation revision.

## Reproduction result

| Measure | Result |
|---|---:|
| Fixtures observed | 32 / 32 |
| Passed every frozen check | 31 |
| Failed fixtures | 1 — `META-NONEXEC-01` |
| Execution errors or timeouts | 0 |
| Sentinel changed nodes | 0 |
| Other/outside-destination changed nodes | 0 |

The reproduction scientific SHA-256 was `b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`, exactly matching Cycle 3.

## Original/reproduction comparison

- portable scientific objects: exactly equal;
- mismatch records: exactly equal;
- execution-error records: exactly equal;
- executed identities: exactly equal;
- operational differences: two root-dependent archive SHA-256 values, for `SYM-ABS-01` and `HARD-ABS-01`;
- no additional difference.

The original and reproduction full JSON SHA-256 values differ because those two absolute-link fixture archives embed different fresh disposable-root strings. Those operational hashes do not enter the portable scientific identity.

## Final interpretation

- H1: **Supported**, 16 / 16 tagged fixtures passed.
- H2: **Supported**, 13 / 13 tagged fixtures passed.
- H3: **Unsupported**, 15 / 16 tagged fixtures passed; `META-NONEXEC-01` contradicted the frozen exact metadata expectation in both runs.
- Overall: **Valid partial bounded result**.

The retained mismatch is explained by the pinned filter's mode transformation and is best classified as a frozen expectation defect. The expected `0600` remains unchanged and failed; it was not reclassified to obtain a positive result. No new containment vulnerability or disclosure trigger was identified.

## Closure

Cycle 4:

- preserved the complete reproduction, mismatch, identity, summary, and comparison artifacts;
- wrote `REPORT.md`;
- synchronized the study overview, protocol, root README, `STATE.md`, `NEXT_START.md`, and human-intervention ledger;
- closed Issue #12 as completed;
- returned TEMPLEX/0 to no active study.

No fifth cycle exists. The next separately approved work unit may be one post-Study-006 portfolio assessment only; it may freeze at most one inactive proposal and must stop before activation, implementation, or experiment.
