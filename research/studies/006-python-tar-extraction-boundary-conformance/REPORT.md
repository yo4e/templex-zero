# Study 006 Final Report — Python Tar Extraction Boundary Conformance

_Date closed: 2026-07-28 (Asia/Tokyo)_  
_Final disposition: **Valid partial bounded result**_  
_Issue: **#12 — closed**_

## Abstract

Study 006 tested the explicit Python 3.13.5 `tarfile` `data` extraction filter on one pinned Linux/ext4 environment using 32 original synthetic archives containing 57 ordered members. The study froze destination-containment, link, special-file, stateful-order, duplicate-name, partial-extraction, safe-control, and metadata expectations before formal execution.

The complete matrix executed once and one independently authorized clean reproduction executed once. Both runs completed all 32 fixtures, passed 31 fixtures under every frozen check, and retained one identical metadata-expectation mismatch, `META-NONEXEC-01`. The portable scientific payload was byte-identical across the two runs.

H1 destination containment and protected rejection is **supported**. H2 stateful containment is **supported**. H3 safe-control preservation and metadata normalization is **unsupported** under its frozen all-or-zero criterion because one expected mode was wrong, even though every safe fixture was accepted and all safe bytes, structures, links, ownership, and containment checks were preserved.

This is not a general claim that tar extraction is safe.

## Research question

> On CPython 3.13.5 for Linux, does `tarfile` extraction with explicit `filter="data"` enforce documented destination-containment, link, special-file, and metadata-sanitization boundaries across a frozen stateful synthetic fixture matrix, while preserving safe data-archive behavior and producing independently auditable filesystem effects?

## Frozen domain

- Runtime: CPython 3.13.5 at `/usr/bin/python3`.
- Runtime binary SHA-256: `e59d0124ff06c248546876e01fcfb1ea3cda63534949f94a9372bfcfe3bfc3f5`.
- `tarfile.py`: `/usr/lib/python3.13/tarfile.py`.
- Local `tarfile.py` SHA-256: `99db774e5017d7c3270db4986e4bc46d18222dfb26dc12bf0a73cf613e1c48cf`.
- Platform: Linux 6.12.13 x86_64, glibc 2.41, ext4.
- Extraction identity: UID/GID 65534, no supplementary groups, `no-new-privs`.
- Extraction: `TarFile.extractall(path=destination, filter="data")`, `errorlevel=1`.
- Manifest: 18,742 bytes, SHA-256 `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`.
- Archives: deterministic uncompressed USTAR generated in memory from original declarative records.
- Each fixture used a fresh mode-0700 disposable study root.

The exact local `tarfile.py` was not byte-identical to the upstream CPython v3.13.5 file. Conclusions therefore apply to the pinned local implementation and environment, not to every CPython installation.

## Method

The generator constructed each archive from the frozen manifest. The extraction harness launched a non-privileged child, recorded the first `FilterError`, and preserved accepted prefixes. A separate `lstat`-based filesystem oracle walked the actual disposable tree without following symlinks and recorded relative paths, node type, mode, UID/GID, regular-file size and SHA-256, symbolic-link targets, and canonical hard-link equivalence groups.

The complete matrix was executed exactly once in Cycle 3. Cycle 4 fetched and verified the exact live Git blobs for the manifest, instruments, formal runner, and original result; then performed exactly one clean reproduction. No fixture, order, expected exception, mode, denominator, or threshold was changed.

## Fixture inventory

| Family | Fixtures |
|---|---:|
| `archive_symlink_pivot` | 3 |
| `duplicate_name` | 2 |
| `hardlink_escape` | 2 |
| `leading_separator` | 2 |
| `member_order_permutation` | 2 |
| `metadata_normalization` | 3 |
| `partial_extraction` | 4 |
| `path_escape` | 2 |
| `preexisting_symlink_pivot` | 2 |
| `safe_hardlink` | 2 |
| `safe_nested` | 1 |
| `safe_regular` | 2 |
| `safe_symlink` | 2 |
| `special_file` | 1 |
| `symlink_escape` | 2 |

- H1-tagged fixtures: **16**.
- H2-tagged fixtures: **13**.
- H3-tagged fixtures: **16**.
- Safe/no-refusal fixtures: **16**.
- First-refusal fixtures: **16**.
- Accepted file-member payload bytes before success or first refusal: **276**.
- Final projected regular-file bytes, counting hard-linked paths as nodes: **275**.

## Complete observations

| Measure | Original | Reproduction |
|---|---:|---:|
| Fixtures observed | 32 / 32 | 32 / 32 |
| Passed every frozen check | 31 | 31 |
| Failed fixtures | 1 | 1 |
| Execution errors or timeouts | 0 | 0 |
| Sentinel changed nodes | 0 | 0 |
| Other/outside-destination changed nodes | 0 | 0 |
| Scientific SHA-256 | `b060d634…e4336c` | `b060d634…e4336c` |

Expected and observed dispositions matched exactly:

| Disposition | Count |
|---|---:|
| Safe / no exception | 16 |
| `OutsideDestinationError` | 7 |
| `LinkOutsideDestinationError` | 5 |
| `AbsoluteLinkError` | 2 |
| `SpecialFileError` | 2 |

Per-check agreement across the 32 fixtures:

| Check | Passed |
|---|---:|
| Exception class | 32 / 32 |
| First refusal index | 32 / 32 |
| Accepted-prefix count | 32 / 32 |
| Outside-destination changes | 32 / 32 |
| Sentinel changes | 32 / 32 |
| Sentinel digest | 32 / 32 |
| Final destination nodes | 31 / 32 |

All six fixtures with a safe prefix before refusal retained exactly the frozen one-member prefix: `PARTIAL-PATH-01`, `PARTIAL-SYM-01`, `PARTIAL-HARD-01`, `PARTIAL-FIFO-01`, `PRE-SYM-PIVOT-PARTIAL-01`, and `DUP-PARTIAL-01`.

## Reproduction comparison

The original and reproduction canonical result JSON files were both 97,289 bytes but had different complete-file SHA-256 values:

- original: `07cac72ab1d29394ef82b71280b12b78370fff94e84f428fb3617221c61faabd`;
- reproduction: `c43b1e6a4f5535e471ed04f9fcdca751e1a270a18c8710feafd677f53d6b3278`.

Their portable `scientific` objects were exactly equal and both had SHA-256:

`b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`

Mismatch records, execution-error records, and executed identities were also equal. The complete JSON difference consisted only of operational archive SHA-256 values for `SYM-ABS-01` and `HARD-ABS-01`, whose generated link targets necessarily contain the fresh absolute disposable root. Absolute roots were excluded from the portable scientific payload.

## Retained mismatch

`META-NONEXEC-01` was frozen with archive mode `0077` and expected extracted mode `0600`. Both formal runs observed mode `0644`.

The file bytes, size, SHA-256, UID/GID, successful extraction, accepted-prefix count, destination containment, sentinel digest, and absence of outside-destination changes all matched. Only the expected mode was wrong.

The pinned filter behavior explains `0644`:

1. limit `0077` to `0055`;
2. because owner execute is absent, clear executable bits, leaving `0044`;
3. add owner read/write, yielding `0644`.

This explanation does not retroactively convert the frozen check into a pass. The `0600` expectation remains visibly contradicted. The evidence indicates a study expectation defect, not a newly identified containment defect or reportable vulnerability.

## Hypothesis dispositions

### H1 — Supported

All **16 / 16** H1-tagged fixtures passed. Every protected member produced the expected refusal class and first-refusal index where applicable; every accepted prefix was recorded; and no sentinel or other outside-destination node changed.

### H2 — Supported

All **13 / 13** H2-tagged fixtures passed. Pre-existing symlink pivots, archive-created internal pivots, member-order permutations, duplicate names, overwrites, and partial prefixes remained confined to the destination. The independent filesystem projection agreed with the frozen expected effects.

### H3 — Unsupported

**15 / 16** H3-tagged fixtures passed every frozen check. All 16 safe controls were accepted without a filter error, and all expected bytes, directory structures, permitted internal links, ownership, and containment effects were preserved. The complete portable scientific payload reproduced byte-identically.

However, H3's frozen support criterion required exact normalized metadata agreement for every safe fixture. `META-NONEXEC-01` contradicted its frozen expected mode. Therefore H3 is unsupported, rather than repaired or weakened after observation.

## Overall disposition

Study 006 closes as a **valid partial bounded result**:

- setup and the hand-audited gate passed;
- the complete matrix was valid and complete;
- the clean reproduction was complete;
- H1 and H2 are supported;
- H3 is unsupported;
- the portable scientific evidence reproduced exactly;
- the study closed within four approval cycles.

The result does not certify arbitrary tar archives, other Python versions, upstream CPython generally, non-ext4 filesystems, Windows semantics, concurrent mutation, denial-of-service resistance, or extraction of untrusted third-party archives.

## Reusable artifacts

- frozen proposal and active protocol;
- exact 32-fixture manifest and schemas;
- deterministic USTAR generator;
- independent filesystem oracle;
- non-privileged extraction harness;
- hand-audited gate and targeted tests;
- complete Cycle 3 result and mismatch records;
- complete Cycle 4 reproduction and comparison;
- source/result identity ledgers;
- cycle audits and this final report.

## Conclusion

Within the pinned environment and frozen synthetic matrix, the explicit `data` filter enforced all tested destination-containment, link, special-file, refusal-order, partial-extraction, and stateful-boundary expectations. The experiment also demonstrated why a positive security-boundary observation must not erase a failed scientific prediction: one metadata expectation was wrong, reproducibly so. The bounded result is therefore strong on H1 and H2, negative on H3, and partial overall.
