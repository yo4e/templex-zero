# Next Start

_Updated: 2026-07-24 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the active Study 005 protocol, both cycle audits, Issue #11, current code/tests, recent commits, and frozen data artifacts.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**Study 005 is active. Cycle 2 of maximum 4 is complete. Studies 001–004 remain closed.**

- Active study: `research/studies/005-tzdb-transition-roundtrip/`
- Protocol: `research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md`
- Cycle 1 audit: `research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md`
- Cycle 2 audit: `research/studies/005-tzdb-transition-roundtrip/CYCLE_2_READER_AND_MANIFEST.md`
- Active issue: #11
- Pinned release: IANA tzdb 2026c

## Cycle 2 gates passed

- Cycle 1 compiled-tree, inventory, and fixture identities reproduced from the trusted archive;
- original standard-library-only TZif v1/v2/v3/v4 reader committed before complete-manifest generation;
- pre-first-transition interpretation frozen as time type index 0;
- eleven parser unit tests passed;
- eighteen frozen transition/control/footer results passed on the first formal fixture-gate run;
- fixture-gate canonical SHA-256: `07daf47a745ba83ecff95d468328546b7fc8a5fbeb8d42c8eafb8bf970b906d3`;
- complete manifest generated only after the gate passed;
- 313 zones and 18,071 retained transitions;
- backward / zero / forward: 8,926 / 187 / 8,958;
- canonical compact manifest: 354,993 bytes;
- manifest SHA-256: `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`.

No formal Python `zoneinfo` comparison or H1–H3 result exists.

## Frozen artifact reconstruction

Cycle 1 artifacts retain their recorded reconstruction procedures.

For the Cycle 2 transition manifest:

1. read `data/transition_manifest_compact_v1.parts.json`;
2. concatenate each listed file in order;
3. remove one final LF only where `final_lf` is true;
4. base64-decode the 61,248-character result;
5. xz-decompress the 45,936-byte stream;
6. verify 354,993 bytes and SHA-256 `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`.

The final layout has eight files because the original 12,000-character `part03` was safely represented as three exact 4,000-character chunks after final validation caught connector truncation.

## Next bounded work unit — Cycle 3 only

1. re-read live protocol, Cycle 1 and Cycle 2 audits, Issue #11, code/tests, artifact identities, and recent commits;
2. reconstruct and verify the frozen 2026c compiled tree, 313-zone inventory, fixtures, fixture-gate result, and transition manifest;
3. implement an isolated public-API `zoneinfo` harness without using CPython private parser state or host zone conversion;
4. implement UTC projection witnesses, fold round trips, and the frozen two-fold gap validator;
5. freeze harness source, assertions, and deterministic serialization using only targeted fixtures and synthetic TZif-independent cases before complete outcomes;
6. demonstrate that every requested key resolves from the isolated compiled tree and cannot fall back to host or separately installed tzdata;
7. execute the complete frozen corpus once and preserve every record and mismatch classification;
8. update Issue #11, state, handoff, and intervention records; stop.

Cycle 3 must not revise the frozen release, inventory, interval, manifest, witness selection, hypotheses, or criteria; remove mismatches; use host zone data; contact maintainers; file an external report; perform clean reproduction or final synthesis; or begin Cycle 4.

## Verification boundaries carried forward

- No detached signature has been verified.
- `zdump` remains targeted secondary fixture evidence only.
- The independent manifest is not a Python conformance result.
- Fresh checkout and full-repository regression were not performed in Cycle 2.
- A unit-test construction error was corrected before the fixture gate; no reader correction was required.
- Repository manifest persistence required a disclosed final part-layout correction; canonical manifest bytes and identity did not change.

## Human gate

> 承認

## Human action pending

None. A later exact `承認` opens Cycle 3 only.
