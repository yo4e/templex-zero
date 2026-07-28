# Study 006 Cycle 4 Reproduction Artifacts

The clean reproduction was executed exactly once from verified live source bytes.

## Result identities

- reproduction canonical JSON: **97,289 bytes**, SHA-256 `c43b1e6a4f5535e471ed04f9fcdca751e1a270a18c8710feafd677f53d6b3278`;
- deterministic gzip: **6,906 bytes**, SHA-256 `10f5480625aa23645a75e19538a0f5d33a0d6009d82459dbfb46f3c8337ea0ff`;
- portable scientific SHA-256: `b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`;
- mismatch record SHA-256: `900cd5ff27f88a6d337f671172566e0fff1d8be45d4a19461ce4b0d352fd8299`;
- identity record SHA-256: `8098cdcad9a650f715068efce0a37ac794dd2c6c4d92177d015a03e37f1b6a57`;
- compact run summary SHA-256: `c737380aea0736517ea9655f184fb7d58744515044a6c0c651a6dbbb55d1ca36`;
- comparison SHA-256: `c181d0ba1a6cd61caa3fce1dfe90111eff4214ae34e51e2aa9af81a3cbf863e2`;
- final metrics SHA-256: `3e2b8df6364c7b7c9a16ce6dc8cc0c078b3278f5820b98ed92327e0b32b71da9`.

The gzip is transported as sixteen ordered base64 text parts. `tools/reconstruct_reproduction_result.py` verifies their live Git Blob identities, reconstructs the gzip and JSON, and checks both SHA-256 values.

## Outcome

- fixtures observed: 32 / 32;
- passed every frozen check: 31;
- retained mismatch: `META-NONEXEC-01`;
- execution errors: 0;
- portable scientific payload equal to Cycle 3: yes;
- complete JSON operational differences: two root-dependent archive hashes for absolute-link fixtures.

The complete JSON is not stored uncompressed in Git. The verified transport is the canonical repository representation.
