# Next Start

_Updated: 2026-07-27 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the active Study 006 protocol, Cycle 2 instrument records, Cycle 3 audit and identities, the original formal result, Issue #12, governance and human-intervention records, open issues, and recent commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**Study 006 is active. Cycle 3 of maximum 4 is complete.**

The complete frozen matrix was executed exactly once.

- matrix: 32 fixtures / 57 members;
- observed: 32 / 32;
- passed every frozen check: 31;
- mismatch: `META-NONEXEC-01` only;
- execution errors: 0;
- exceptions: 7 `OutsideDestinationError`, 5 `LinkOutsideDestinationError`, 2 `AbsoluteLinkError`, 2 `SpecialFileError`, and 16 safe/no-exception;
- sentinel changed nodes: 0;
- other/outside-destination changed nodes: 0;
- scientific summary SHA-256: `b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`.

`META-NONEXEC-01` froze expected mode `0600` and observed `0644`. Its bytes, ownership, successful extraction, containment, and sentinel checks passed. Static inspection explains `0644` from the frozen mode transformation, but the expectation remains failed and unchanged. Final H3 interpretation is deferred.

Key records:

- `research/studies/006-python-tar-extraction-boundary-conformance/PROTOCOL.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_2_SOURCE_IDENTITIES.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_3_FORMAL_EXECUTION.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_3_SOURCE_AND_RESULT_IDENTITIES.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/results/cycle3/README.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/data/fixture_manifest_v1.json`
- Issue #12

## Mandatory lessons and boundaries

1. The Cycle 3 complete matrix was already executed once and must not be repeated except for the one specifically authorized clean reproduction in Cycle 4.
2. Cycle 4 must fetch and verify exact live Git bytes before execution.
3. The independent oracle must remain separate from `tarfile.data_filter` and harness verdict logic.
4. The frozen `META-NONEXEC-01` expectation must not be repaired, removed, or reclassified.
5. A plausible explanation for a mismatch does not convert the frozen check into a pass.
6. Reproduction differences, including absolute-root-dependent operational archive hashes, must be separated from portable scientific differences.
7. Cycle 4 must close the study; no fifth cycle is permitted.
8. No external archive, real user path, elevated child, disclosure, outside contact, or general security certification is permitted.

## Next bounded work unit

The next exact `承認` may perform **Study 006 Cycle 4 and closure only**:

1. reconstruct exact committed manifest, instruments, runner, and Cycle 3 result;
2. perform one clean reproduction under the frozen runtime, caps, and non-privileged boundary;
3. compare complete portable scientific payloads and preserve all differences;
4. analyze the retained metadata mismatch without expectation revision;
5. assign final H1–H3 dispositions and the bounded overall result;
6. write the final report and Cycle 4 audit;
7. close Issue #12 and Study 006 and return the laboratory to no active study;
8. if reproduction is incomplete or contaminated, close honestly within Cycle 4.

## Human gate

> 承認

## Human action pending

None. A later exact `承認` opens the final bounded Cycle 4 only.
