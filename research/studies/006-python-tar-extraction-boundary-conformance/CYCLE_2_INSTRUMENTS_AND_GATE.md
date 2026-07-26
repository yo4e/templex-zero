# Study 006 Cycle 2 — Instruments and Hand-Audited Gate

_Date: 2026-07-26 (Asia/Tokyo)_  
_Disposition: **gate passed; instruments frozen; Cycle 2 complete**_

## Work completed

Cycle 2 implemented a deterministic USTAR generator, a filesystem oracle based on `lstat` snapshots and node-level diffs, a non-privileged extraction harness, a frozen gate runner, reconstruction tools, and targeted tests. The full 32-fixture matrix was not executed.

The oracle does not call `tarfile.data_filter`, reuse harness verdict helpers, or follow symbolic links. It records portable relative paths, node type, mode, UID, GID, regular-file size and SHA-256, symbolic-link target, and canonical hard-link equivalence classes while excluding timestamps, raw inode/device numbers, and absolute temporary paths.

## Frozen gate

The hand-audited gate was frozen before formal execution as an exact 15-fixture / 22-member subset of the 32-fixture manifest. It covers safe regular and nested files, safe symbolic and hard links, leading-separator sanitization, direct path escape, partial extraction, absolute and relative outside links, FIFO refusal, a pre-existing symlink pivot, an in-root archive-created symlink pivot, duplicate overwrite, and high-bit mode sanitization.

Gate manifest:

- canonical bytes: 10,167;
- SHA-256: `8a4b86f70729da59e20266042d6b5d8b8ef6a8e482885341c4c7f094122073a9`;
- source complete-manifest SHA-256: `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`.

## One bounded correction phase

Before the formal gate was frozen and executed from verified live blobs, development diagnostics exposed two instrument defects inside one bounded correction phase. No frozen Study 006 fixture, expected exception, refusal index, node expectation, hypothesis, or threshold changed.

1. The harness compared expected destination nodes in manifest order against the oracle's required UTF-8 lexical order. Three otherwise correct cases failed. Expected nodes were normalized to the already frozen oracle order.
2. The first harness wrote the generated tar inside the disposable root. The absolute-link fixture embeds the per-run root in its tar bytes, so projecting that tar file made the scientific digest non-portable. The harness was changed to generate and extract the tar in memory. Raw archive byte count and SHA-256 remain operational metadata and do not enter the portable scientific payload.

After these corrections, the development gate passed and reproduced. The formal gate was then executed only from source bytes whose live Git identities had been verified.

## Verification performed

- reconstruction of the frozen gate manifest: passed;
- targeted unit tests: **3 passed**;
- Python compile verification for the tools: passed;
- formal non-privileged gate execution under UID/GID 65534, no supplementary groups, and `no-new-privs`: **15 / 15 passed**;
- second clean formal execution: **15 / 15 passed**;
- portable scientific payload equality: passed.

Formal observations:

| Measure | Result |
|---|---:|
| Gate fixtures | 15 |
| Passed | 15 |
| Failed | 0 |
| Safe/no-exception | 8 |
| `OutsideDestinationError` | 3 |
| `LinkOutsideDestinationError` | 2 |
| `AbsoluteLinkError` | 1 |
| `SpecialFileError` | 1 |
| Sentinel changed nodes | 0 |
| Other/outside-destination changed nodes | 0 |
| False exception, refusal-index, prefix, or node checks | 0 |

Both clean runs produced scientific SHA-256 `4dc0b29b37d4ce096528c538e677c2d305a498d9332891a3fb5230463d9757cf`.

The only operational difference was the raw tar SHA-256 for `SYM-ABS-01`, because the frozen archive member intentionally contains the per-run absolute disposable root. No absolute path is serialized in the scientific record, and the observed exception, refusal position, filesystem state, and all checks were identical.

## Result identities

- canonical scientific result JSON: 40,633 bytes, SHA-256 `cae28021659b53fb2ea946f0d76cf64b33e85c8480974848f7f52b9a7834b2f2`;
- deterministic gzip: 2,649 bytes, SHA-256 `5c69e291ee91a7c16eab4cf51fc793f7d82696dd3647e3b39521d299b7a528bc`;
- operational metadata SHA-256: `2653cdf5b443ff04cf5a2628de76d487e3ad218b02448ffcc445df514e5a101a`;
- reproduction comparison SHA-256: `18523f7e6fef61c88bc391eab8400eec1f22ee3bf1dfb6877f5f73e5cde2bfc3`.

## Transport correction

The first single-file base64 result upload did not match its precomputed Git identity. It was deleted and replaced by four verified transport parts. The failed transport is not used as evidence and remains visible in commit history.

## Current judgment and limits

The correctness gate supports advancing the frozen instruments to the complete formal matrix. It does not support H1, H2, or H3 by itself. Seventeen frozen fixtures remain unexecuted, and no study-level hypothesis disposition has been made.

Cycle 3 should execute the complete 32-fixture matrix exactly once using the frozen manifest and verified instrument blobs, preserve complete results and mismatches, and stop without final interpretation or closure.
