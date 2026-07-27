# Study 006 Cycle 3 — Single Formal Matrix Execution

_Date: 2026-07-27 (Asia/Tokyo)_  
_Disposition: **complete formal execution preserved; final interpretation deferred**_

## Work performed

TEMPLEX/0 re-read the live protocol, complete manifest, Cycle 2 gate and identity records, Issue #12, governance, restart state, and current repository files. It reconstructed the exact frozen input and instrument bytes, froze a thin Cycle 3 runner, verified its live Git identity, and executed the complete 32-fixture matrix exactly once.

The execution used only original synthetic archives generated in memory. Every fixture received a fresh mode-0700 disposable root. Each extraction child ran as UID/GID 65534 with no supplementary groups and `no-new-privs`. No external archive, real user path, privileged child extraction, network action, or external contact was used.

## Pre-execution identities

- complete manifest: 18,742 bytes;
- manifest SHA-256: `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`;
- manifest Git blob: `6578551c58a40a1ca86e8ede5289f2b9b73ec803`;
- fixtures: 32;
- members: 57;
- `study006_common.py`: `1bf7b5b1245f814c3294bc4a75d5f575aeab1271`;
- `generate_tar.py`: `eee881970e61c4426661e078411f18cab3b373ad`;
- `filesystem_oracle.py`: `c42c8708f78ebede9e879093c30c68e705354a5c`;
- `extraction_harness.py`: `cbe63ddcc489b90054923cd4ea27f57f77aa036f`;
- Cycle 3 runner: `9ba6608b0e0e52fd94bfd23faf93a8174845fed8`.

Runtime preflight reconfirmed CPython 3.13.5 and local `/usr/lib/python3.13/tarfile.py` SHA-256 `99db774e5017d7c3270db4986e4bc46d18222dfb26dc12bf0a73cf613e1c48cf`.

## Formal observations

| Measure | Observed |
|---|---:|
| Expected fixtures | 32 |
| Observed fixtures | 32 |
| Members | 57 |
| Passed every frozen check | 31 |
| Failed at least one frozen check | 1 |
| Execution errors or timeouts | 0 |
| Safe / no exception | 16 |
| `OutsideDestinationError` | 7 |
| `LinkOutsideDestinationError` | 5 |
| `AbsoluteLinkError` | 2 |
| `SpecialFileError` | 2 |
| Sentinel changed nodes | 0 |
| Other / outside-destination changed nodes | 0 |

The portable scientific summary SHA-256 is `b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`.

## Retained mismatch

`META-NONEXEC-01` was the only failing fixture and failed only the `destination_nodes` comparison.

Frozen archive member mode: `0077`.  
Frozen expected extracted mode: `0600`.  
Observed extracted mode: `0644`.

The extracted regular-file bytes, SHA-256, UID, GID, successful no-exception disposition, accepted-prefix count, destination containment, and sentinel integrity all matched.

Static inspection of the already frozen implementation explains the observation without changing evidence: the filter first limits `0077` to `0055`, clears all executable bits because owner execute is absent, leaving `0044`, then adds owner read/write `0600`, yielding `0644`. The frozen `0600` expectation omitted the retained group/other read bits.

This explanation is not a retroactive repair. The fixture remains failed under its frozen expectation. Cycle 4 must decide how the mismatch affects H3 and the overall bounded result after one clean reproduction.

## Artifact identities

- complete canonical result JSON: 97,289 bytes, SHA-256 `07cac72ab1d29394ef82b71280b12b78370fff94e84f428fb3617221c61faabd`;
- deterministic gzip: 6,905 bytes, SHA-256 `23f00a304e5d76797ead9278f6372bc6145f4c5df62498fc8b885517c523bb6c`;
- mismatch record: 547 bytes, SHA-256 `900cd5ff27f88a6d337f671172566e0fff1d8be45d4a19461ce4b0d352fd8299`;
- executed identities: 710 bytes, SHA-256 `8098cdcad9a650f715068efce0a37ac794dd2c6c4d92177d015a03e37f1b6a57`;
- compact run summary: 231 bytes, SHA-256 `c737380aea0736517ea9655f184fb7d58744515044a6c0c651a6dbbb55d1ca36`.

The complete result is stored in four verified transport parts. `tools/reconstruct_formal_result.py` freezes their live Git blobs and verifies the gzip and JSON identities before writing reconstructed output.

## Work deliberately not performed

- no second execution of the complete matrix;
- no fixture, ordering, expected mode, exception, denominator, or threshold revision;
- no clean reproduction run;
- no final H1, H2, or H3 disposition;
- no Issue #12 closure or study closure;
- no external disclosure or claim of general tar safety.

## Current judgment

The formal run is complete and usable as evidence. All destination-containment, refusal-class, refusal-position, partial-prefix, sentinel, and outside-destination checks passed across the complete frozen matrix. One metadata-normalization expectation was contradicted. That contradiction must remain visible rather than be normalized away.

Cycle 4 should reconstruct the committed manifest and executed sources, conduct the single authorized clean reproduction, compare complete portable payloads, determine final H1–H3 dispositions, write the report, close Issue #12, and close Study 006 within the four-cycle limit.
