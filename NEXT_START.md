# Next Start

_Updated: 2026-07-24 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the active Study 005 protocol and Cycle 1 audit, Issue #11, governance files, current commits, and the frozen data artifacts.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**Study 005 is active. Cycle 1 of maximum 4 is complete. Studies 001–004 remain closed.**

- Active study: `research/studies/005-tzdb-transition-roundtrip/`
- Protocol: `research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md`
- Cycle 1 audit: `research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md`
- Active issue: #11
- Pinned release: IANA tzdb 2026c

## Cycle 1 gates passed

- exact official archive identity and bundled permission boundary re-verified;
- active protocol committed before successful compilation;
- source order and `zic -b fat` command frozen;
- two clean isolated compilations matched byte-identically;
- each compiled tree: 341 files / 397,559 bytes;
- tree projection SHA-256: `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2`;
- `zone1970.tab` SHA-256: `77b5e45415fa684fcc42de3421a6b0f15cc9b2c137f258083850346e8f76eea8`;
- canonical inventory: 313 zones, no missing files and no invalid TZif magic;
- inventory SHA-256: `053b3988df8da3276ba63928fab3a1e6b1e9e625d0fa13d16b6f423edc51b582`;
- 15 targeted parser expectations frozen and regenerated identically;
- fixture JSON SHA-256: `a3b08a49f5d3955f0015e67d58f705a68dadb7cc07ed1b499ff13381290786d9`.

No complete reader, transition manifest, Python formal comparison, or hypothesis result exists.

## Frozen artifact reconstruction

- compiled-tree projection: follow `data/compiled_tree_projection_v1.parts.json`, concatenate listed base64 parts without their final LFs, decode base64, then gunzip;
- canonical zone list: decode and gunzip `data/canonical_zones_v1.txt.gz.b64`;
- fixture expectations: decode and gunzip `data/fixture_expectations_v1.json.gz.b64`;
- targeted `zdump` evidence: decode and gunzip `data/targeted_zdump_evidence_v1.txt.gz.b64`;
- verify reconstructed bytes against `data/artifact_digests_v1.json` and the parts manifest.

## Next bounded work unit — Cycle 2 only

1. re-read live protocol, Cycle 1 audit, artifacts, Issue #11, and recent commits;
2. reconstruct and verify the frozen fixture and inventory artifacts;
3. implement an original standard-library-only TZif v1/v2/v3/v4 reader without importing or copying Python `zoneinfo` internals;
4. enforce rejection of truncation, inconsistent counts, invalid type indexes, impossible abbreviation indexes, and unsupported versions;
5. implement deterministic canonical serialization and the frozen pre-first-transition interpretation;
6. test exact agreement with all 15 frozen targeted expectations;
7. permit at most one bounded disclosed correction if the fixture gate initially fails;
8. only after a passing fixture gate, freeze reader source, tests, fixture results, and the complete explicit-transition manifest for the 313-zone inventory and frozen date interval;
9. update Issue #11, state, handoff, and intervention records; stop.

Cycle 2 must not implement or execute the formal `zoneinfo` comparison harness, inspect H1–H3 outcome aggregates, revise the frozen release/domain/criteria, contact outsiders, file a report, accept terms, or begin Cycle 3.

## Verification boundaries carried forward

- `zdump` is targeted secondary fixture evidence, not the full-corpus oracle.
- The host zone database must never become the formal evidence source.
- No detached signature has been verified.
- Fresh checkout and full-repository regression were not performed in Cycle 1.
- One shell-wrapper syntax error occurred before any `zic` command; the work root was recreated and the frozen compilation semantics did not change.

## Human gate

> 承認

## Human action pending

None. A later exact `承認` opens Cycle 2 only.
