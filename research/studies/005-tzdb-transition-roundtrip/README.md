# Study 005 — TZDB Transition Round-Trip Conformance

_Status: Active; Cycle 2 of maximum 4 completed._

Study 005 tests a version-pinned IANA tzdb 2026c transition corpus against an independently implemented TZif reader and an isolated Python `zoneinfo` harness.

## Current position

Cycle 1 completed source/permission preflight, deterministic isolated compilation, canonical inventory, and frozen targeted fixtures.

Cycle 2 implemented and froze the independent standard-library-only TZif reader, passed eleven parser tests and all eighteen frozen fixture/footer gate results, and then froze the complete explicit-transition manifest.

No formal Python `zoneinfo` comparison or H1–H3 result exists yet.

## Cycle 2 result

- reader: `src/templex_zero/tzif_reader.py`;
- malformed-input tests: `tests/test_tzif_reader.py`;
- fixture/manifest builder: `experiments/study005_cycle2.py`;
- fixture gate: 18 / 18 passed;
- fixture-gate canonical SHA-256: `07daf47a745ba83ecff95d468328546b7fc8a5fbeb8d42c8eafb8bf970b906d3`;
- complete inventory: 313 zones;
- retained explicit transitions: 18,071;
- backward / zero / forward: 8,926 / 187 / 8,958;
- compact manifest bytes: 354,993;
- compact manifest SHA-256: `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`.

## Frozen artifacts

- `PROTOCOL.md` — active frozen protocol
- `CYCLE_1_ACTIVATION.md` — activation and setup audit
- `CYCLE_2_READER_AND_MANIFEST.md` — reader, gate, manifest, and correction audit
- `data/source_provenance_v1.json` — exact archive identity and permission metadata
- `data/compilation_summary_v1.json` — compiler, command, environment, and deterministic compilation summary
- `data/compiled_tree_projection_v1.parts.json` and part files — complete compiled-tree projection
- `data/canonical_zone_identity_v1.json` and `data/canonical_zones_v1.txt.gz.b64` — frozen 313-zone inventory
- `data/fixture_expectations_v1.json.gz.b64` — fifteen frozen targeted expectations
- `data/fixture_gate_result_v1.json.gz.b64` and identity record — passing eighteen-result parser gate
- `data/transition_manifest_summary_v1.json` — manifest counts and canonical identity
- `data/transition_manifest_compact_v1.parts.json` and part files — reconstructible complete compact manifest

Follow each parts manifest exactly. Decode base64 and then its recorded compression format. Verify reconstructed bytes against the recorded SHA-256 before use.

## Next cycle

Cycle 3 may implement and freeze the isolated public-API `zoneinfo` comparison and fold/gap round-trip harness using only fixtures and synthetic cases before formal outcomes, then execute the complete frozen corpus once.

Cycle 3 must not revise the frozen release, inventory, transition manifest, witness semantics, or success criteria; remove mismatches; perform clean reproduction and final synthesis; contact outsiders; file a defect report; or begin Cycle 4.
