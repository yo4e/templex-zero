# Study 006 Cycle 1 — Repository Identity Verification

_Date: 2026-07-26 (Asia/Tokyo)_

This record verifies that the Cycle 1 scientific and operational files were materialized as live Git blobs after connector transport. The pre-transport byte counts and SHA-256 identities remain in `CYCLE_1_ACTIVATION_AND_FREEZE.md`.

| Path | Creation commit | Live Git blob |
|---|---|---|
| `README.md` | `2cce8739d4ac487f890f06735e13de5056f58516` | `a297494bf0d42f2547c8fba5ab4f856507425980` |
| `PROTOCOL.md` | `8732e435dd988928816ef5a392e2f75c944662a9` | `7541064cce435de6cf91c5cae7a69f530d458878` |
| `data/environment_v1.json` | `a343364d4d009f9f9659a03d67cb1e8c2ba15784` | `57251ddb6c6ab4c01aef20d5ab98e4d5fdf1329c` |
| `schema/fixture_schema_v1.json` | `4c73ddbd0e344d6d7fee6fd46ef9895103123e14` | `4b858e0e436717e7d22b75adb50211cfbfeffd0b` |
| `schema/filesystem_projection_schema_v1.json` | `56ce54c4c2d574dafade4033891f5a2fb312f67b` | `46cbf14591b145ea0e18c9bbff83279dd4f50b4c` |
| `schema/refusal_mapping_v1.json` | `501f2b154f0c64f90e1b22a2230a92d624ea9e3c` | `70ed252e0c68c4b3af1db88d8719a1562a6015a7` |
| `data/fixture_manifest_v1.json` | `127759543f179ea3bf18b7e761c731cfcee2c24d` | `6578551c58a40a1ca86e8ede5289f2b9b73ec803` |
| `CYCLE_1_ACTIVATION_AND_FREEZE.md` | `b6ea3b8566b25774a306f0ca3290822bc096788e` | `db6fdfe1e01c53c61e193b019115ca40188fa30e` |

The compact manifest's pre-transport SHA-256 is `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`; its live Git blob is `6578551c58a40a1ca86e8ede5289f2b9b73ec803`.

No committed file is treated as executed evidence. Cycle 2 must compute the exact live blob and byte identity of every generator, oracle, harness, gate fixture, and runner before use.
