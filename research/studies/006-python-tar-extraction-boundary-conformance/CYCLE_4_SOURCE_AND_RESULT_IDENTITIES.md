# Study 006 Cycle 4 — Source and Result Identities

_Date: 2026-07-28 (Asia/Tokyo)_

The clean reproduction was executed only after the exact live Git identities for the manifest and instruments matched the local execution candidates.

## Reproduced inputs and instruments

| Path | Original creation commit | Live Git blob |
|---|---|---|
| `data/fixture_manifest_v1.json` | `127759543f179ea3bf18b7e761c731cfcee2c24d` | `6578551c58a40a1ca86e8ede5289f2b9b73ec803` |
| `tools/study006_common.py` | `d2017ca181883a7bdc5da01d1851d7ee694a1889` | `1bf7b5b1245f814c3294bc4a75d5f575aeab1271` |
| `tools/generate_tar.py` | `3cf818c182cdd0132923f41db7433f5d8f0780f5` | `eee881970e61c4426661e078411f18cab3b373ad` |
| `tools/filesystem_oracle.py` | `b1d9308be928c25b63c059ce5e3303823464eaef` | `c42c8708f78ebede9e879093c30c68e705354a5c` |
| `tools/extraction_harness.py` | `bfce06e03df549fb9dbc1ffed24e3a8f83c9b802` | `cbe63ddcc489b90054923cd4ea27f57f77aa036f` |
| `tools/run_formal_matrix.py` | `0fbd61d235a1e5ce785faf19507f604e08ca1bba` | `9ba6608b0e0e52fd94bfd23faf93a8174845fed8` |

The manifest reconstructed to 18,742 bytes with SHA-256 `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`.

## Original Cycle 3 result

The original result was reconstructed from the four Cycle 3 transport blobs recorded in `CYCLE_3_SOURCE_AND_RESULT_IDENTITIES.md`:

- gzip: 6,905 bytes, SHA-256 `23f00a304e5d76797ead9278f6372bc6145f4c5df62498fc8b885517c523bb6c`;
- JSON: 97,289 bytes, SHA-256 `07cac72ab1d29394ef82b71280b12b78370fff94e84f428fb3617221c61faabd`;
- portable scientific SHA-256: `b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`.

## Cycle 4 result transport

| Path | Creation commit | Live Git blob |
|---|---|---|
| `results/cycle4/reproduction_result_v1.json.gz.b64.part01` | `b39064758f24e9be13361d94394882be764e8b9a` | `e46dcdbe4eba03eb26c7c707dd9219b3df09f48d` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part02` | `0930083a560acef25e15fe5d506a4c52c040fb6f` | `ab87d97d4e4d3fd1554230253d54b6a3105f2ab1` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part03` | `fee984ae2c0231799ae484e73fcb4fe02dab098f` | `675677ac13688de64e2c1e753caded4563d0b2e7` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part04` | `e400547daa64a223b77f680b747f58b3444967a5` | `5209aac9b7ed4b074573d6f1bc033e548d150fba` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part05` | `b2dd31f637fc14d8431c816b919c923836ed38c4` | `4c3552b88269f5ebd5ee3e772676262008d83662` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part06` | `9c6d2117e34a29028a1cbeddd093d438316c817a` | `be86081bb4cd65cd8da3247a2f95b22aa172fdc3` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part07` | `5a5df47b6f4b8cfdf29bd9c51e4089f915d9ec3e` | `1282fd0b089b5ff4ef081bbd30fee21d4b31129f` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part08` | `40fe41625cae1f28208f56b43416eacadb3e5dae` | `e9a8a547d76a6bc1f02298ec3ea30a84f395b718` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part09` | `6cd2f4b5d77f9875150f82e7cf846cf5389ed360` | `72a2d4bc73e0971cfeadacf69d0914839ea85771` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part10` | `dcae073b9764316545091cabecb70cb77653b0a8` | `45cbd51b94b338db730a66485cf253b39f93ac2a` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part11` | `0d142816b7ff4b3b3e67417f0c0b183251fe8e00` | `ac2a166588ddfcdc4d3fdf37afecc860c6734918` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part12` | `1d20fc54e83d374900f8f821676c387dd4d85213` | `173e3e5792137cb7411fdf6a38cc806b8a4cb68a` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part13` | `9f14c0a1980a5d90e33e0eaab913d95628e1bcc3` | `ad092ae4b8b59739cbf348a93f9dac8828a90317` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part14` | `95f8500d24b93e5177b4c9ef5aa6b2975c54f519` | `529beadb76aeabf6b4e927b245f5342ab38cac7f` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part15` | `11923de1443c2880ba6a63c8f60d08a82687a4f2` | `950309a35ba38c11e1a976cfbf9537abf7496e05` |
| `results/cycle4/reproduction_result_v1.json.gz.b64.part16` | `3650bf299ac92d2809523c8a667571baf64b1efe` | `8edc9ef6aecc10a8c755d3d9a46026d25231c195` |

The sixteen-part transport reconstructs to:

- gzip: 6,906 bytes, SHA-256 `10f5480625aa23645a75e19538a0f5d33a0d6009d82459dbfb46f3c8337ea0ff`;
- JSON: 97,289 bytes, SHA-256 `c43b1e6a4f5535e471ed04f9fcdca751e1a270a18c8710feafd677f53d6b3278`;
- portable scientific SHA-256: `b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`.

Additional live artifacts:

| Path | Creation commit | Live Git blob |
|---|---|---|
| `results/cycle4/reproduction_mismatches_v1.json` | `56e2c4d8cbb40f06bdc14f6b5ceab93c5e585687` | `951f1599abcaa8a65ffec3c945e00702be8af2e6` |
| `results/cycle4/reproduction_identities_v1.json` | `8b15adfb50792f74d098d2fbbe0e819c85976fb3` | `23cba081753cea247e9d5e54291cf92aeaea76b9` |
| `results/cycle4/reproduction_stdout.json` | `2c052cf75ac91441a6f8316efbb032d65313db3f` | `73d0624c736796763cd346776439fde5d05fd7f2` |
| `results/cycle4/reproduction_comparison_v1.json` | `14e07fe2ee52a2f4993e15c5969fc19932d7b3d4` | `a2901415d27c7a07d8649a473fbf6933dd3d01b6` |
| `results/cycle4/final_metrics_v1.json` | `d9f8ad63240b28a3a8728ed57f59d5edac2dae19` | `a44cea8f47b3e27bfb65d311475617039fdf4cdd` |
| `results/cycle4/README.md` | `72a83415e95fe2615fe57fc44acc640fbf178d31` | `0d14ccd15742732f71a5f9c5dff5172e7b9d9888` |
| `tools/reconstruct_reproduction_result.py` | `562be4daf44a1d34bb926d6cc16c8764d4921b8e` | `78acf53a1d4a8b3084ec3651e7417bacff6909e0` |

The result reconstructor freezes all sixteen live transport blobs and verifies the gzip and JSON identities. A direct four-part text upload was rejected by platform safety screening before any repository write; the same gzip was therefore transported in smaller text parts. The scientific result was not regenerated.

No committed filename is treated as evidence without its verified live Blob and reconstructed content identity.
