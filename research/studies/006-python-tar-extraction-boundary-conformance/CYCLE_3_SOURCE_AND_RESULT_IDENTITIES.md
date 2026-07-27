# Study 006 Cycle 3 — Source and Result Identities

_Date: 2026-07-27 (Asia/Tokyo)_

The complete formal matrix was executed only after the following live Git identities matched the local execution candidates.

## Executed inputs and instruments

| Path | Commit | Live Git blob |
|---|---|---|
| `data/fixture_manifest_v1.json` | `127759543f179ea3bf18b7e761c731cfcee2c24d` | `6578551c58a40a1ca86e8ede5289f2b9b73ec803` |
| `tools/study006_common.py` | `d2017ca181883a7bdc5da01d1851d7ee694a1889` | `1bf7b5b1245f814c3294bc4a75d5f575aeab1271` |
| `tools/generate_tar.py` | `3cf818c182cdd0132923f41db7433f5d8f0780f5` | `eee881970e61c4426661e078411f18cab3b373ad` |
| `tools/filesystem_oracle.py` | `b1d9308be928c25b63c059ce5e3303823464eaef` | `c42c8708f78ebede9e879093c30c68e705354a5c` |
| `tools/extraction_harness.py` | `bfce06e03df549fb9dbc1ffed24e3a8f83c9b802` | `cbe63ddcc489b90054923cd4ea27f57f77aa036f` |
| `tools/run_formal_matrix.py` | `0fbd61d235a1e5ce785faf19507f604e08ca1bba` | `9ba6608b0e0e52fd94bfd23faf93a8174845fed8` |

The manifest reconstructed to 18,742 bytes with SHA-256 `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a` before execution.

## Preserved result transport

| Path | Commit | Live Git blob |
|---|---|---|
| `results/cycle3/formal_result_v1.json.gz.b64.part01` | `993543b102c166f97ecbbc4744497915a24215a4` | `726aae92af31f17d1f5d8e9788e4d51cbc281eb9` |
| `results/cycle3/formal_result_v1.json.gz.b64.part02` | `81632c19b687c46778f686aae3e0aabee7a5bbb3` | `156dc8501a48866d3331218cb6dfb07fd15cc06d` |
| `results/cycle3/formal_result_v1.json.gz.b64.part03` | `b55e64f13346fda55724b47cb844b84c84ef0817` | `d3028634baa6aab5200e10629cac8c6f9430ac54` |
| `results/cycle3/formal_result_v1.json.gz.b64.part04` | `d529d7f0c20eb121951cd2dbbf8400b851b89110` | `283876c66aea3ded08306c887a06a33a81e675a0` |
| `results/cycle3/formal_mismatches_v1.json` | `6d3dd65bc75fc894460b1a15ae54eab3ebc1a46b` | `951f1599abcaa8a65ffec3c945e00702be8af2e6` |
| `results/cycle3/executed_identities_v1.json` | `f787c7445f8f6c57c1c46c808977ddda20e8a805` | `23cba081753cea247e9d5e54291cf92aeaea76b9` |
| `results/cycle3/run_summary.json` | `341b1013c612832091600a2fd6340af291a8fc8c` | `73d0624c736796763cd346776439fde5d05fd7f2` |
| `tools/reconstruct_formal_result.py` | `44f11b6f64d62f831a4429d17acebc4c5209e6c7` | `356e4f7134e4a277f8fe4efb685cb50a2d1b2380` |

The four-part transport reconstructs to:

- gzip: 6,905 bytes, SHA-256 `23f00a304e5d76797ead9278f6372bc6145f4c5df62498fc8b885517c523bb6c`;
- JSON: 97,289 bytes, SHA-256 `07cac72ab1d29394ef82b71280b12b78370fff94e84f428fb3617221c61faabd`.

The scientific summary inside the result has SHA-256 `b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`.

No committed source or result filename is treated as sufficient evidence by itself. Cycle 4 must fetch these live blobs, reconstruct the exact bytes, and record what was actually executed in the clean reproduction.
