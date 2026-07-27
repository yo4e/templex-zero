# Study 006 — Python Tar Extraction Boundary Conformance

_Status: **Active — Cycle 3 of maximum 4 complete**_  
_Issue: **#12**_

Study 006 asks whether the explicit Python 3.13.5 `tarfile` `data` extraction filter preserves documented destination, link, special-file, and metadata boundaries across a frozen stateful synthetic fixture matrix on one pinned Linux/ext4 environment.

## Current frozen state

- Activation: **GO unchanged**.
- Active protocol: [`PROTOCOL.md`](PROTOCOL.md).
- Exact 32-fixture manifest: [`data/fixture_manifest_v1.json`](data/fixture_manifest_v1.json).
- Cycle 2 gate audit: [`CYCLE_2_INSTRUMENTS_AND_GATE.md`](CYCLE_2_INSTRUMENTS_AND_GATE.md).
- Cycle 3 formal audit: [`CYCLE_3_FORMAL_EXECUTION.md`](CYCLE_3_FORMAL_EXECUTION.md).
- Cycle 3 identities: [`CYCLE_3_SOURCE_AND_RESULT_IDENTITIES.md`](CYCLE_3_SOURCE_AND_RESULT_IDENTITIES.md).
- Formal result transport: [`results/cycle3/README.md`](results/cycle3/README.md).

## Cycle 3 formal observation

The frozen 32-fixture / 57-member matrix was executed exactly once under UID/GID 65534 with no supplementary groups and `no-new-privs`.

| Measure | Result |
|---|---:|
| Fixtures observed | 32 / 32 |
| Passed every frozen check | 31 |
| Failed at least one frozen check | 1 |
| Execution errors | 0 |
| Sentinel changed nodes | 0 |
| Other/outside-destination changed nodes | 0 |

The only mismatch was `META-NONEXEC-01`: the frozen expected mode was `0600`; the observed mode was `0644`. Contents, ownership, successful extraction, containment, and sentinel integrity matched. The mismatch remains failed under its frozen expectation and was not repaired.

The scientific summary SHA-256 is `b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`.

## Hard boundary

Only original synthetic archives inside per-fixture mode-0700 disposable roots are permitted. Formal execution runs as UID/GID 65534 with no supplementary groups and `no-new-privs`. The study excludes external archives, real user paths, elevated experimental execution, denial-of-service testing, races, Windows semantics, external disclosure, and claims of general tar safety.

## Next cycle

Cycle 4 is the final permitted cycle. It must reconstruct the committed manifest, instruments, and original formal result; execute one clean reproduction under the frozen boundary; compare complete portable payloads; analyze the retained metadata mismatch; assign final H1–H3 dispositions; write the final report; close Issue #12; and close Study 006. No fifth cycle or expectation revision is permitted.
