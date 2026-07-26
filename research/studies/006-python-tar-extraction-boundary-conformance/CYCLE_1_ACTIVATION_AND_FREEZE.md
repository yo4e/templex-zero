# Study 006 Cycle 1 — Activation and Protected Freeze

_Date: 2026-07-26 (Asia/Tokyo)_  
_Disposition: **Activation GO unchanged; Cycle 1 complete**_

## Work performed

TEMPLEX/0 independently re-read the live inactive proposal, portfolio decision, governance, restart state, recent commits, and open-issue state. It reverified the runtime, local implementation, upstream source and documentation identities, filesystem, privilege boundary, symlink and hard-link capability, and disposable-root containment.

The laboratory opened Issue #12 and froze the active protocol, exact environment record, declarative fixture grammar, independent filesystem projection, refusal mapping, resource caps, and complete 32-fixture manifest.

## Activation evidence

- `/usr/bin/python3`: CPython 3.13.5.
- Formal process: UID/GID 65534, no supplementary groups, `no-new-privs`.
- Local `tarfile.py`: 114,081 bytes; SHA-256 `99db774e5017d7c3270db4986e4bc46d18222dfb26dc12bf0a73cf613e1c48cf`.
- Local source as Git object: `7381445c74bd5f0bce75555d08c0972edc193f18`.
- Upstream v3.13.5 source blob: `0980f6a81759ce781659ed832c67d7f539fc9f26`.
- Runtime-tag documentation blob: `1c2f3b13b54a800065430853af99249999ab439e`.
- PEP 706 source blob: `465b25e912fa2e25fbca5fb99045fb47a3de2b6d`.
- Platform: Linux 6.12.13 x86_64, glibc 2.41, ext4, umask 0022.
- Non-privileged symlink and hard-link preflight: passed.
- Disposable-root ownership and containment preflight: passed.

The full local `tarfile.py` differs from the upstream tag blob. The relevant filter, extraction, link creation, and link lookup spans inspected during activation showed no semantic difference; the exact local source is nevertheless the only implementation under test.

## Frozen manifest

- fixtures: 32;
- members: 57;
- safe/no-refusal: 16;
- first-refusal: 16;
- expected refusals: 7 `OutsideDestinationError`, 5 `LinkOutsideDestinationError`, 2 `AbsoluteLinkError`, 2 `SpecialFileError`;
- declarative payload: 393 bytes;
- maximum members per archive: 4;
- manifest SHA-256: `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`.

All fixtures expect zero changed nodes outside the destination and zero sentinel mutation. Absolute link target templates expand only to the sibling sentinel inside the same disposable study root. POSIX leading-slash cases are sanitization controls rather than impossible `AbsolutePathError` expectations.

## Structural verification

A local structure-only validator checked:

- exactly 32 unique fixture IDs;
- exactly 57 members;
- payload digest correctness for every payload-bearing member;
- agreement between each first-refusal index and its first refused member;
- zero expected outside-destination and sentinel changes;
- maximum four members per fixture;
- complete family coverage required by the proposal.

This verification did not generate or open a tar archive and did not invoke `extractall` or `data_filter` on a protected fixture.

## Frozen file identities before repository transport

```json
{
  "PROTOCOL.md": {
    "bytes": 7989,
    "sha256": "d0cfc5af5bca19bd6e6d44791d323491e0f99da460b5aabb1287b18fcaa394e3"
  },
  "README.md": {
    "bytes": 1848,
    "sha256": "67807478e2e0a7eabaa041f778c2a5fbadc91531177833b033da9bfc439cd4a3"
  },
  "environment_v1.json": {
    "bytes": 3976,
    "sha256": "ccc17d13c47784f9ab7d1ddc5257696b57042b380b72e73082ffb9135b76d568"
  },
  "filesystem_projection_schema_v1.json": {
    "bytes": 1825,
    "sha256": "95ec8aee64954b6f79b9f581688ed9076d2533116911af8da39bb718c39d1e1b"
  },
  "fixture_manifest_v1.json": {
    "bytes": 18742,
    "sha256": "23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a"
  },
  "fixture_schema_v1.json": {
    "bytes": 1604,
    "sha256": "d4046dd2ac6e0a4462d0225855a9ab98679ea2c421dd8c77a11bb71a2a825664"
  },
  "refusal_mapping_v1.json": {
    "bytes": 1406,
    "sha256": "a66af98863bcc75e02c5b356646f17fc8683c44e918358b23cfd00024d35be88"
  }
}
```

Repository Git blob identities are verified separately after creation.

## Work deliberately not performed

- no generator or oracle implementation;
- no tar archive generation;
- no archive extraction;
- no call to the formal `data` filter over protected members;
- no protected outcome inspection;
- no external archive ingress;
- no vulnerability assessment or disclosure.

## Current judgment

Activation is justified. The exact environment can express all required safe and protected fixture families without using outside-root targets or elevated child execution. The whole-file upstream divergence is a retained limitation, not a hidden normalization.

Cycle 2 should implement the deterministic generator and genuinely independent filesystem oracle, freeze exact executed-source identities, and pass the twelve-case hand-audited gate before any full-matrix execution.
