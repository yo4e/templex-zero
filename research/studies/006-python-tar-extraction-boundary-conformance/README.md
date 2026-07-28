# Study 006 — Python Tar Extraction Boundary Conformance

_Status: **Closed — valid partial bounded result**_  
_Issue: **#12 — closed**_

Study 006 tested the explicit Python 3.13.5 `tarfile` `data` extraction filter across a frozen 32-fixture / 57-member stateful synthetic matrix on one pinned Linux/ext4 environment.

## Final result

| Measure | Original | Reproduction |
|---|---:|---:|
| Fixtures observed | 32 / 32 | 32 / 32 |
| Passed every frozen check | 31 | 31 |
| Failed fixtures | 1 | 1 |
| Execution errors | 0 | 0 |
| Sentinel changed nodes | 0 | 0 |
| Other/outside-destination changed nodes | 0 | 0 |

The portable scientific payload was byte-identical in both runs:

`b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`

The retained mismatch was `META-NONEXEC-01`: frozen expected mode `0600`, observed mode `0644` in both runs. File bytes, ownership, extraction success, destination containment, and sentinel integrity matched. The frozen expectation was not revised.

## Final dispositions

- **H1 destination containment and protected rejection: Supported** — 16 / 16 tagged fixtures passed.
- **H2 stateful containment: Supported** — 13 / 13 tagged fixtures passed.
- **H3 safe-control preservation and metadata normalization: Unsupported** — 15 / 16 tagged fixtures passed, but its frozen exact-metadata criterion failed.
- **Overall: Valid partial bounded result.**

## Records

- [Final report](REPORT.md)
- [Cycle 4 reproduction and closure](CYCLE_4_REPRODUCTION_AND_CLOSURE.md)
- [Cycle 4 source and result identities](CYCLE_4_SOURCE_AND_RESULT_IDENTITIES.md)
- [Cycle 4 reproduction artifacts](results/cycle4/README.md)
- [Cycle 3 formal execution](CYCLE_3_FORMAL_EXECUTION.md)
- [Active protocol, now closed](PROTOCOL.md)
- [Exact manifest](data/fixture_manifest_v1.json)

## Boundary

This result is specific to the pinned local CPython 3.13.5 implementation, Linux/ext4 environment, non-privileged execution identity, explicit `filter="data"`, and frozen synthetic matrix. It does not certify arbitrary tar archives, other runtimes or filesystems, denial-of-service resistance, concurrent mutation, Windows semantics, or untrusted third-party extraction.
