# Next Start

_Updated: 2026-07-26 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the active Study 006 protocol, Cycle 2 audit and source identities, complete manifest, Issue #12, governance and human-intervention records, open issues, and recent commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**Study 006 is active. Cycle 2 of maximum 4 is complete.**

Cycle 2 implemented and froze the deterministic USTAR generator, independent `lstat` filesystem oracle, non-privileged extraction harness, gate runner, reconstruction tools, and tests. The exact 15-fixture hand-audited gate passed twice.

- complete matrix: 32 fixtures / 57 members;
- gate: 15 fixtures / 22 members;
- gate passes: 15 / 15 in both clean runs;
- exceptions: 3 `OutsideDestinationError`, 2 `LinkOutsideDestinationError`, 1 `AbsoluteLinkError`, 1 `SpecialFileError`, and 8 safe/no-exception;
- sentinel changed nodes: 0;
- other/outside-destination changed nodes: 0;
- false check results: 0;
- scientific SHA-256 in both runs: `4dc0b29b37d4ce096528c538e677c2d305a498d9332891a3fb5230463d9757cf`.

One bounded pre-formal correction phase fixed expected-node ordering and removed an absolute-root-bearing generated tar from the scientific filesystem projection. Frozen expectations and hypotheses were unchanged. A later single-file GitHub result transport mismatch was deleted and replaced with verified four-part transport; the failed transport is not evidence.

Key records:

- `research/studies/006-python-tar-extraction-boundary-conformance/PROTOCOL.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_2_INSTRUMENTS_AND_GATE.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_2_SOURCE_IDENTITIES.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/GATE_MANIFEST.md`
- `research/studies/006-python-tar-extraction-boundary-conformance/data/fixture_manifest_v1.json`
- Issue #12

## Mandatory lessons and boundaries

1. Formal extraction must never run as root; root may only launch the frozen UID/GID 65534 privilege drop.
2. Execute only exact source bytes whose live Git identities are verified first.
3. The independent oracle must remain separate from `tarfile.data_filter` and harness verdict logic.
4. Absolute-root-dependent archive SHA is operational metadata, not portable scientific identity.
5. The complete 32-fixture matrix may be executed only once in Cycle 3.
6. Cycle 3 records raw outcomes but does not assign final H1–H3 dispositions.
7. No fixture, order, refusal expectation, denominator, or threshold may change after complete execution begins.
8. No external archive, real user path, elevated child, disclosure, outside contact, or fifth cycle is permitted.

## Next bounded work unit

The next exact `承認` may perform **Study 006 Cycle 3 only**:

1. verify the complete manifest and frozen instrument identities;
2. execute the complete 32-fixture matrix exactly once under the frozen caps and non-privileged boundary;
3. preserve complete results, mismatches, operational metadata, and source identities;
4. stop without a second complete run, final hypothesis disposition, Issue #12 closure, or study closure;
5. if execution is incomplete or contaminated, preserve that result and stop.

## Human gate

> 承認

## Human action pending

None. A later exact `承認` opens one bounded Cycle 3 only.
