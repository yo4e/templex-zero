# Study 005 — TZDB Transition Round-Trip Conformance

_Status: Active; Cycle 3 of maximum 4 completed._

Study 005 tests a version-pinned IANA tzdb 2026c transition corpus against an independently implemented TZif reader and an isolated Python `zoneinfo` harness.

## Current position

Cycle 1 completed source/permission preflight, deterministic isolated compilation, canonical inventory, and frozen targeted fixtures.

Cycle 2 implemented and froze the independent TZif reader, passed eleven parser tests and all eighteen frozen transition/control/footer checks, and froze a 313-zone manifest containing 18,071 explicit transitions.

Cycle 3 froze a public-API `zoneinfo` harness before complete outcomes, executed the full frozen corpus exactly once under an isolated 2026c data path, and preserved **161,647** comparison records:

- H1 UTC projection: 90,079 records;
- H2 repeated-time fold and round trip: 26,778 records;
- H3 gap and adjacent-valid classification: 44,790 records;
- nonzero mismatch masks: 0.

These are mechanical Cycle 3 results, not yet the final H1–H3 dispositions. Cycle 4 must cleanly reproduce them from the exact repository source, analyze limitations, write the final report, and close the study.

## Material limitations discovered in Cycle 3

The compact Cycle 2 manifest is not independently self-contained for the pre-transition type of the first retained transition because it omits pre-1970 transition records. The frozen reader and exact TZif source bytes supply that context. The manifest bytes and digest remain unchanged, but the earlier independent-self-containment claim is withdrawn.

The formal local execution also used a compatibility bridge to an independently implemented local TZif parser rather than importing the literal frozen repository reader blob. Every manifest row's source identity, type table, and retained transition list was verified, but Cycle 4 must reproduce the exact result using the exact repository source.

## Frozen artifacts

- `PROTOCOL.md` — active frozen protocol
- `CYCLE_1_ACTIVATION.md` — activation and setup audit
- `CYCLE_2_READER_AND_MANIFEST.md` — independent-reader and manifest audit
- `CYCLE_3_HARNESS_FREEZE.md` — pre-outcome harness semantics
- `CYCLE_3_FORMAL_EXECUTION.md` — isolated formal-execution audit
- `data/source_provenance_v1.json` — exact archive identity and permission metadata
- `data/compilation_summary_v1.json` — compiler, command, environment, and deterministic compilation summary
- `data/compiled_tree_projection_v1.parts.json` and part files — complete compiled-tree projection
- `data/canonical_zone_identity_v1.json` and `data/canonical_zones_v1.txt.gz.b64` — ordered 313-zone inventory
- `data/fixture_expectations_v1.json.gz.b64` and fixture-gate artifacts — frozen reader expectations and results
- `data/transition_manifest_compact_v1.parts.json` and part files — complete transition-manifest reconstruction
- `data/harness_freeze_identity_v1.json` — pre-outcome harness identities
- `data/zoneinfo_formal_summary_v1.json` — mechanical Cycle 3 summary
- `data/zoneinfo_mismatches_v1.json.xz.b64` — complete mismatch artifact
- `data/zoneinfo_formal_artifacts_v1.json` — exact full-result and reconstruction identities and part order
- `data/zoneinfo_result_reconstruction_v1.json.xz.b64.part*` — reconstructible formal-result package

Follow each parts manifest exactly and verify reconstructed byte counts and SHA-256 identities before use.

## Next and final cycle

Cycle 4 is the last permitted cycle. It must:

1. obtain a clean repository state and use the exact committed reader, harness, tests, and runner;
2. reconstruct the source, compiled tree, inventory, fixtures, manifest, and Cycle 3 result artifacts;
3. reproduce the frozen manifest, summary, mismatch artifact, full canonical result, and deterministic XZ identities;
4. investigate any reproduction difference without changing the frozen experiment or rerunning adaptively;
5. analyze H1, H2, and H3 under the precommitted criteria;
6. write the final report and closure audit;
7. close Issue #11 and mark Study 005 closed.

No fifth cycle is permitted.
