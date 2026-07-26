# Study 006 — Python Tar Extraction Boundary Conformance

_Status: **Active — Cycle 1 of maximum 4 complete**_  
_Issue: **#12**_

Study 006 asks whether the explicit Python 3.13.5 `tarfile` `data` extraction filter preserves documented destination, link, special-file, and metadata boundaries across a frozen stateful synthetic fixture matrix on one pinned Linux/ext4 environment.

## Current frozen state

- Activation: **GO unchanged**.
- Active protocol: [`PROTOCOL.md`](PROTOCOL.md).
- Environment identity: [`data/environment_v1.json`](data/environment_v1.json).
- Fixture schema: [`schema/fixture_schema_v1.json`](schema/fixture_schema_v1.json).
- Filesystem projection: [`schema/filesystem_projection_schema_v1.json`](schema/filesystem_projection_schema_v1.json).
- Refusal mapping: [`schema/refusal_mapping_v1.json`](schema/refusal_mapping_v1.json).
- Exact fixture manifest: [`data/fixture_manifest_v1.json`](data/fixture_manifest_v1.json).
- Cycle 1 audit: [`CYCLE_1_ACTIVATION_AND_FREEZE.md`](CYCLE_1_ACTIVATION_AND_FREEZE.md).

The matrix contains 32 fixtures and 57 members, split evenly between safe/no-refusal and first-refusal cases. No formal archive has yet been generated or extracted.

## Hard boundary

Only original synthetic archives inside per-fixture mode-0700 disposable roots are permitted. Formal execution must run as UID/GID 65534 with no supplementary groups and `no-new-privs`. The study excludes external archives, real user paths, elevated experimental execution, denial-of-service testing, races, Windows semantics, external disclosure, and claims of general tar safety.

## Next cycle

Cycle 2 may implement the deterministic generator, independent filesystem oracle, and extraction harness, then run only the frozen hand-audited correctness gate. It must stop before the complete 32-fixture formal matrix.
