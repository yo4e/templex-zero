# Study 006 Cycle 2 — Executed Source and Artifact Identities

_Date: 2026-07-26 (Asia/Tokyo)_

The formal hand-audited gate was executed only after the following live Git blobs were fetched and matched the exact local execution candidates.

| Path | Creation commit | Live Git blob |
|---|---|---|
| `tools/study006_common.py` | `d2017ca181883a7bdc5da01d1851d7ee694a1889` | `1bf7b5b1245f814c3294bc4a75d5f575aeab1271` |
| `tools/generate_tar.py` | `3cf818c182cdd0132923f41db7433f5d8f0780f5` | `eee881970e61c4426661e078411f18cab3b373ad` |
| `tools/filesystem_oracle.py` | `b1d9308be928c25b63c059ce5e3303823464eaef` | `c42c8708f78ebede9e879093c30c68e705354a5c` |
| `tools/extraction_harness.py` | `bfce06e03df549fb9dbc1ffed24e3a8f83c9b802` | `cbe63ddcc489b90054923cd4ea27f57f77aa036f` |
| `tools/run_gate.py` | `68d57164d7fb787cb4939ac2e6e620e815913a53` | `36f32981ccbb851a1433b89dd48cc4b4068d58a9` |
| `tools/reconstruct_gate_manifest.py` | `5ca55fe2d934cfb8d563b21567df2c2b9644ddda` | `500871dd576c23f89f00748ca5ad73fcae49ad10` |
| `tests/test_study006_gate_tools.py` | `8c86647cc99544536f1ac3961a1e8a04c6ff793f` | `0b428723cf9e8e36a17c3d3080d44f02624992f9` |
| `GATE_MANIFEST.md` | `757aaf0d700fd917643669f4ed7c0708db61de4c` | `d3f222a91d511a9df2ec381cb778660235b240fb` |

The four gate-manifest transport blobs were `6238cacbb96091ac6ab906d046e0445953f7843a`, `e35b842270b2d18b1776db5e46edd1d3ff8a33d2`, `b384b2558d85864199313dc9999fef557f797eaa`, and `3daf99e2cc04645eed45829b0ffbbbc5ee4d8d4d`. Reconstruction produced exactly 10,167 bytes with SHA-256 `8a4b86f70729da59e20266042d6b5d8b8ef6a8e482885341c4c7f094122073a9`.

The result transport is four parts with live Git blobs `23443d72dac4639ee9f8a8a888a3405377c624db`, `9dbb9440df8df17aec11080a8bc50c0a6705be9c`, `926a14a0faf6e1fcfd50e99bd7457dde94d1164b`, and `0ce2b4054bca7a520cd34ae7d884d8768c397790`. Reconstruction yields a 2,649-byte deterministic gzip with SHA-256 `5c69e291ee91a7c16eab4cf51fc793f7d82696dd3647e3b39521d299b7a528bc`, containing a 40,633-byte JSON record with SHA-256 `cae28021659b53fb2ea946f0d76cf64b33e85c8480974848f7f52b9a7834b2f2`.

The post-execution result reconstructor is live Git blob `33534dcdfb9bcbbb51cf4aa7de5a0d2eb2840ffc` and freezes those four transport identities plus the gzip and JSON hashes. It was not part of the formal extraction execution.

A first attempted single-file result transport produced the wrong live blob and was deleted in commit `8d41fa818118a79308a68ed299ea71a70edda686`. It is not evidence. The visible correction remains in Git history.
