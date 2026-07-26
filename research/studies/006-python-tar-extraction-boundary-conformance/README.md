# Study 006 — Python Tar Extraction Boundary Conformance

_Status: **Active — Cycle 2 of maximum 4 complete**_  
_Issue: **#12**_

Study 006 asks whether the explicit Python 3.13.5 `tarfile` `data` extraction filter preserves documented destination, link, special-file, and metadata boundaries across a frozen stateful synthetic fixture matrix on one pinned Linux/ext4 environment.

## Current frozen state

- Activation: **GO unchanged**.
- Active protocol: [`PROTOCOL.md`](PROTOCOL.md).
- Environment identity: [`data/environment_v1.json`](data/environment_v1.json).
- Exact 32-fixture manifest: [`data/fixture_manifest_v1.json`](data/fixture_manifest_v1.json).
- Frozen hand-audited gate: [`GATE_MANIFEST.md`](GATE_MANIFEST.md).
- Cycle 2 audit: [`CYCLE_2_INSTRUMENTS_AND_GATE.md`](CYCLE_2_INSTRUMENTS_AND_GATE.md).
- Executed source identities: [`CYCLE_2_SOURCE_IDENTITIES.md`](CYCLE_2_SOURCE_IDENTITIES.md).

Cycle 2 implemented and froze the deterministic USTAR generator, independent `lstat` filesystem oracle, non-privileged extraction harness, gate runner, reconstruction tools, and targeted tests.

The 15-fixture hand-audited gate passed twice under UID/GID 65534 with no supplementary groups and `no-new-privs`:

- passed: **15 / 15**;
- sentinel changed nodes: **0**;
- other/outside-destination changed nodes: **0**;
- false exception, refusal-index, accepted-prefix, or final-node checks: **0**;
- portable scientific SHA-256 in both clean runs: `4dc0b29b37d4ce096528c538e677c2d305a498d9332891a3fb5230463d9757cf`.

One bounded pre-formal correction phase fixed an expected-node ordering comparison and removed an absolute-root-bearing tar file from the scientific filesystem projection. No frozen fixture expectation or hypothesis changed. A separate failed GitHub result transport was deleted and replaced by verified four-part transport; it is not evidence.

## Hard boundary

Only original synthetic archives inside per-fixture mode-0700 disposable roots are permitted. Formal execution runs as UID/GID 65534 with no supplementary groups and `no-new-privs`. The study excludes external archives, real user paths, elevated experimental execution, denial-of-service testing, races, Windows semantics, external disclosure, and claims of general tar safety.

## Next cycle

Cycle 3 may execute the complete frozen 32-fixture formal matrix exactly once using the frozen instrument blobs, preserve complete raw and mismatch evidence, and stop. It may not repeat the complete matrix, revise expectations, assign final H1–H3 dispositions, or close the study.
