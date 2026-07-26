# Next Start

_Updated: 2026-07-26 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the active Study 006 protocol and Cycle 1 records, Issue #12, governance and human-intervention records, open issues, recent commits, and the frozen proposal.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**Study 006 is active. Cycle 1 of maximum 4 is complete.**

Activation was **GO unchanged** after re-verifying the exact runtime, implementation and documentation identities, ext4 filesystem, privilege boundary, and non-privileged link capabilities.

- Runtime: CPython 3.13.5 at `/usr/bin/python3`.
- Formal child: UID/GID 65534, no supplementary groups, `no-new-privs`.
- Local `tarfile.py` SHA-256: `99db774e5017d7c3270db4986e4bc46d18222dfb26dc12bf0a73cf613e1c48cf`.
- Whole local source differs from the upstream v3.13.5 blob; the exact local implementation is the only operational referent.
- Exact matrix: 32 fixtures, 57 members, 16 safe/no-refusal, 16 first-refusal.
- Manifest SHA-256: `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`.
- No archive has been generated or extracted and no protected outcome has been inspected.

Key records:

- `research/studies/006-python-tar-extraction-boundary-conformance/PROTOCOL.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/data/environment_v1.json`
- `research/studies/006-python-tar-extraction-boundary-conformance/data/fixture_manifest_v1.json`
- `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_1_ACTIVATION_AND_FREEZE.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_1_REPOSITORY_IDENTITIES.md`
- Issue #12

## Mandatory lessons and boundaries

1. Formal extraction must never run as root; root may only perform the frozen privilege drop.
2. The exact local `tarfile.py` source, not an assumed upstream source, defines the operational runtime.
3. The generator, oracle, and harness must have directly verified live source identities before execution.
4. The independent oracle may not call `tarfile.data_filter` or reuse harness verdict helpers.
5. POSIX leading-slash members are frozen sanitization controls, not `AbsolutePathError` cases.
6. Partial extraction before a first fatal `FilterError` is evidence, not rollback failure.
7. Absolute temporary paths, raw inode numbers, and timestamps must not enter the portable scientific payload.
8. No path outside a per-fixture disposable study root may be intentionally targeted or walked.
9. Cycle 2 may execute only the hand-audited gate, not the complete 32-fixture matrix.

## Next bounded work unit

The next exact `承認` may perform **Study 006 Cycle 2 only**:

1. implement the deterministic tar generator from the frozen manifest;
2. implement the independent filesystem projection and diff oracle;
3. implement the extraction harness and frozen privilege launcher assertions;
4. write targeted structural and source-identity tests;
5. freeze at least twelve manually expected miniature gate cases drawn from the existing manifest;
6. run the hand-audited gate only;
7. if it passes, freeze the instruments and stop;
8. if it fails, use at most the one permitted bounded correction or close negatively.

Do not execute the complete formal matrix, migrate runtime, use external archives, test real paths, raise child privileges, contact outsiders, disclose a possible vulnerability, or add a fifth cycle.

## Human gate

> 承認

## Human action pending

None. A later exact `承認` opens one bounded Cycle 2 only.
