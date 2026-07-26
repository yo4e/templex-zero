# Study 006 Active Protocol — Python Tar Extraction Boundary Conformance

_Date activated: 2026-07-26 (Asia/Tokyo)_  
_Status: **Active — Cycle 1 of maximum 4 complete**_  
_Issue: **#12**_

## 1. Activation decision

**GO unchanged.**

The exact CPython 3.13.5 runtime required by the frozen proposal is available. Formal work is pinned to `/usr/bin/python3`, executed as UID/GID 65534 with no supplementary groups and `no-new-privs`. The exact local `tarfile.py`, upstream-tag source identity, documentation source identities, ext4 filesystem assumptions, umask, link capabilities, and containment launcher are frozen in `data/environment_v1.json`.

The default tool shell is privileged, but no formal extraction may execute with that privilege. Root may only launch the frozen privilege drop. The child must assert its UID, GID, group list, study-root ownership, and containment before archive handling.

The local `tarfile.py` is not byte-identical to the upstream CPython v3.13.5 blob. This is not hidden or silently normalized: the exact local source is the operational implementation under test. The activation review found no difference in the inspected filter and link-extraction spans, but the bounded claim remains specific to the local source digest.

## 2. Frozen research question and hypotheses

The research question and H1–H3 are unchanged from `research/proposals/006-python-tar-extraction-boundary-conformance.md`.

- **H1:** destination containment and exact protected refusal.
- **H2:** stateful containment under member order and pre-existing nodes.
- **H3:** safe-control preservation and metadata normalization.

No hypothesis, denominator, exception mapping, fixture, or threshold may be changed after protected outcomes are inspected.

## 3. Exact environment

- Runtime: CPython 3.13.5 at `/usr/bin/python3`.
- Binary SHA-256: `e59d0124ff06c248546876e01fcfb1ea3cda63534949f94a9372bfcfe3bfc3f5`.
- Standard-library source: `/usr/lib/python3.13/tarfile.py`.
- Source SHA-256: `99db774e5017d7c3270db4986e4bc46d18222dfb26dc12bf0a73cf613e1c48cf`.
- Platform: Linux 6.12.13 x86_64, glibc 2.41, ext4.
- Formal identity: UID 65534, GID 65534, no supplementary groups.
- Privilege drop: `/usr/bin/setpriv --reuid=65534 --regid=65534 --clear-groups --no-new-privs`.
- Temporary parent: `/tmp`; each fixture receives a new mode-0700 study root owned by UID/GID 65534.
- Frozen umask: `0022`.
- Extraction call: `TarFile.extractall(path=destination, filter="data")` with `errorlevel=1`.

## 4. Frozen source and documentation referents

- CPython v3.13.5 `Lib/tarfile.py` Git blob: `0980f6a81759ce781659ed832c67d7f539fc9f26`.
- CPython v3.13.5 `Doc/library/tarfile.rst` Git blob: `1c2f3b13b54a800065430853af99249999ab439e`.
- PEP 706 source Git blob inspected on 2026-07-26: `465b25e912fa2e25fbca5fb99045fb47a3de2b6d`.
- Published Python 3.13 documentation URL: `https://docs.python.org/3.13/library/tarfile.html`.
- PEP URL: `https://peps.python.org/pep-0706/`.

The source-tag documentation governs version-specific expectations. The current published 3.13 page is supporting documentation and may include later 3.13 maintenance clarifications; it cannot silently alter the frozen manifest.

## 5. Frozen fixture grammar and manifest

The protected formal matrix is `data/fixture_manifest_v1.json` under `schema/fixture_schema_v1.json`.

- Fixtures: **32**.
- Members: **57**.
- Safe/no-refusal fixtures: **16**.
- First-refusal fixtures: **16**.
- Payload bytes across declarative member records: **393**.
- Maximum members in one archive: **4**.
- All outside-destination targets are sibling sentinel paths inside the same disposable root.
- Absolute link fixtures use `${STUDY_ROOT}` placeholders expanded only at generation time.
- POSIX leading-separator members are frozen as sanitization controls because `AbsolutePathError` is not representable after leading slash stripping on this platform.

Cycle 2 may implement deterministic archive generation from these records. It may not add, remove, reorder, repair, or reclassify a fixture after any protected extraction outcome is observed.

## 6. Frozen filesystem projection

`schema/filesystem_projection_schema_v1.json` defines the independent scientific projection.

- Walk without following symlinks.
- Use paths relative to the disposable study root.
- Record node type, permission mode, UID, GID, regular-file size and SHA-256, symlink target, and canonical hard-link equivalence group.
- Exclude raw device/inode numbers from portable output.
- Exclude atime, mtime, ctime, birth time, and absolute temporary paths from the portable scientific payload.
- Preserve raw operational metadata separately when useful.
- Classify every changed node as destination, sentinel, or other inside the disposable root.

The oracle may not call `tarfile.data_filter`, reuse harness verdict helpers, or infer containment solely from archive names.

## 7. Frozen refusal mapping

`schema/refusal_mapping_v1.json` freezes the expected filter actions and exception classes. With `errorlevel=1`, the first `FilterError` aborts the extraction; accepted prefixes may remain and are part of the evidence.

The expected refusal inventory in the manifest is:

| Exception | Fixtures |
|---|---:|
| `OutsideDestinationError` | 7 |
| `LinkOutsideDestinationError` | 5 |
| `AbsoluteLinkError` | 2 |
| `SpecialFileError` | 2 |

No `AbsolutePathError` fixture enters the denominator because it is not representable under the frozen POSIX path semantics after required leading-separator stripping.

## 8. Resource caps

These caps apply before any archive generation or extraction:

- exact fixture count: **32**;
- maximum members per archive: **4**;
- maximum regular payload per member: **256 bytes**;
- maximum declarative payload per archive: **1,024 bytes**;
- maximum archive bytes: **1 MiB**;
- maximum nodes under one disposable root: **64**;
- maximum member-name UTF-8 length: **128 bytes**;
- maximum link-target UTF-8 length before placeholder expansion: **160 bytes**;
- maximum expanded link-target length: **4,096 bytes**;
- wall time per fixture: **5 seconds**;
- wall time for the complete formal matrix: **180 seconds**;
- address-space limit: **512 MiB** using `RLIMIT_AS`;
- output-file limit: **16 MiB** using `RLIMIT_FSIZE`;
- open-file limit: **64** using `RLIMIT_NOFILE`;
- no child processes or network access from the formal runner.

A cap failure is evidence and may cause an operationally incomplete result. Caps may not be raised after formal execution begins.

## 9. Protected sequence and cycle plan

1. **Cycle 1 — complete:** activation, environment/source/document identities, Issue #12, protocol, schemas, refusal mapping, resource caps, and exact 32-fixture manifest.
2. **Cycle 2:** implement deterministic tar generation and an independent filesystem oracle; freeze and pass at least twelve hand-audited miniature gates; freeze the generator, oracle, and harness.
3. **Cycle 3:** execute the complete formal matrix once and preserve all artifacts without final hypothesis disposition.
4. **Cycle 4:** reconstruct inputs from committed source and manifest, perform one clean reproduction, compare portable payloads, analyze, report, close Issue #12, and close the study.

No fifth cycle is permitted.

## 10. Stop conditions and boundaries

Stop or close negatively if the frozen runtime disappears, the privilege drop cannot be enforced, a fixture cannot be generated within caps, the oracle cannot establish reliable filesystem identity, the gate fails after its one permitted correction opportunity, or safe containment would require privileged sandboxing.

No external archives, real user paths, network filesystems, elevated formal execution, denial-of-service tests, external contact, vulnerability disclosure, or general security certification are authorized.

Cycle 1 performs no archive generation, archive extraction, generator/oracle implementation, or protected outcome inspection.
