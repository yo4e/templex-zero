# Study 004 Cycle 3 — Raw Result Transport

The canonical Cycle 3 result is a deterministic gzip-compressed JSON document. The connected GitHub writer accepts UTF-8 text rather than arbitrary binary bytes, so the gzip is stored as eight ordered base64 text parts.

## Reconstruction

From `research/studies/004-finite-state-conformance/data`:

```sh
cat cycle3_raw_results_v1.json.gz.b64.part00 \
    cycle3_raw_results_v1.json.gz.b64.part01 \
    cycle3_raw_results_v1.json.gz.b64.part02 \
    cycle3_raw_results_v1.json.gz.b64.part03 \
    cycle3_raw_results_v1.json.gz.b64.part04 \
    cycle3_raw_results_v1.json.gz.b64.part05 \
    cycle3_raw_results_v1.json.gz.b64.part06 \
    cycle3_raw_results_v1.json.gz.b64.part07 \
  | base64 -d > cycle3_raw_results_v1.json.gz
```

## Frozen identities

- base64 characters: `39,200`;
- decoded gzip bytes: `29,400`;
- gzip SHA-256: `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679`;
- decompressed JSON bytes: `899,730`;
- JSON SHA-256: `a725f287b3d3a09b5d8e991e82daf9cb8f6a719c528a2e4047524cfd289bfc3c`;
- internal payload SHA-256: `bb34844aee696cde0ea19de9c48a5bd5ec8faf66391a492bc6277bf24ac69927`.

Ordered part Git blobs:

1. `part00` — `ee90b61139cf3e46b1abde072ef47f98ee4dbdf1`
2. `part01` — `fb044479a4322d59c6a2cea89fdda503da49eba0`
3. `part02` — `94fd24f2e75663e5d473a40ec540af8f98085759`
4. `part03` — `6f731430950bfc5dd9be33f066a2462f76c70f94`
5. `part04` — `16b10337187df12e311767558b7aba5e89794931`
6. `part05` — `a10228bd08c8dd7e5ce25a25a7f2e5ef0a8a4815`
7. `part06` — `55adbd6175bd95761c6c84fe8ad5a8b14d887091`
8. `part07` — `a92de9bd97e07b387d5b8185d1812b5bc30d3c5a`

`tests/test_finite_state_conformance_cycle3.py` performs the reconstruction, verifies every outer and internal hash, checks the exact 144-mutant × three-method × three-budget grid, and rejects hypothesis dispositions inside the raw bundle.

The base64 representation is transport only. It does not change the canonical gzip or JSON research evidence.
