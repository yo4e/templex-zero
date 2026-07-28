# Study 006 Protocol — Python Tar Extraction Boundary Conformance

_Date activated: 2026-07-26 (Asia/Tokyo)_  
_Date closed: 2026-07-28 (Asia/Tokyo)_  
_Status: **Closed — Cycle 4 of maximum 4 complete; valid partial bounded result**_  
_Issue: **#12 — closed**_

## 1. Activation and closure

Study 006 activated **GO unchanged** and closed within its four-cycle limit.

Formal work was pinned to CPython 3.13.5 at `/usr/bin/python3`, executed as UID/GID 65534 with no supplementary groups and `no-new-privs`. Root was used only to launch the frozen privilege drop. No formal extraction ran as root.

The exact local `tarfile.py` was not byte-identical to the upstream CPython v3.13.5 blob. The local source remained the operational implementation under test. The final result is therefore specific to the recorded local source and environment.

## 2. Frozen research question and hypotheses

The research question and H1–H3 remained unchanged after protected outcomes were inspected.

- **H1:** destination containment and exact protected refusal.
- **H2:** stateful containment under member order and pre-existing nodes.
- **H3:** safe-control preservation and metadata normalization.

No hypothesis, denominator, exception mapping, fixture, order, mode expectation, or threshold was changed.

Final dispositions:

- H1: **Supported**.
- H2: **Supported**.
- H3: **Unsupported**.
- Overall: **Valid partial bounded result**.

## 3. Exact environment

- Runtime: CPython 3.13.5 at `/usr/bin/python3`.
- Binary SHA-256: `e59d0124ff06c248546876e01fcfb1ea3cda63534949f94a9372bfcfe3bfc3f5`.
- Standard-library source: `/usr/lib/python3.13/tarfile.py`.
- Source SHA-256: `99db774e5017d7c3270db4986e4bc46d18222dfb26dc12bf0a73cf613e1c48cf`.
- Platform: Linux 6.12.13 x86_64, glibc 2.41, ext4.
- Formal identity: UID 65534, GID 65534, no supplementary groups.
- Privilege drop: `/usr/bin/setpriv --reuid=65534 --regid=65534 --clear-groups --no-new-privs`.
- Temporary parent: `/tmp`; every fixture received a fresh mode-0700 study root owned by UID/GID 65534.
- Frozen umask: `0022`.
- Extraction call: `TarFile.extractall(path=destination, filter="data")` with `errorlevel=1`.

## 4. Frozen source and documentation referents

- CPython v3.13.5 `Lib/tarfile.py` Git blob: `0980f6a81759ce781659ed832c67d7f539fc9f26`.
- CPython v3.13.5 `Doc/library/tarfile.rst` Git blob: `1c2f3b13b54a800065430853af99249999ab439e`.
- PEP 706 source Git blob inspected on 2026-07-26: `465b25e912fa2e25fbca5fb99045fb47a3de2b6d`.
- Published Python 3.13 documentation: `https://docs.python.org/3.13/library/tarfile.html`.
- PEP 706: `https://peps.python.org/pep-0706/`.

The version-tag documentation governed the frozen expectations. Later documentation could not silently change the manifest.

## 5. Frozen fixture grammar and manifest

The protected matrix remained `data/fixture_manifest_v1.json` under `schema/fixture_schema_v1.json`.

- Fixtures: **32**.
- Members: **57**.
- Safe/no-refusal fixtures: **16**.
- First-refusal fixtures: **16**.
- Declarative member payload bytes: **393**.
- Maximum members in one archive: **4**.
- Manifest SHA-256: `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`.
- All outside-destination fixture targets were sibling sentinel paths inside the same disposable root.
- Absolute link fixtures used `${STUDY_ROOT}` placeholders expanded only during generation.
- POSIX leading-separator members were sanitization controls, not `AbsolutePathError` cases.

The complete manifest was executed once in Cycle 3 and reproduced once in Cycle 4. No fixture was added, removed, reordered, repaired, reclassified, or given a revised expectation.

## 6. Frozen filesystem projection

`schema/filesystem_projection_schema_v1.json` defined the scientific projection.

- Walk without following symbolic links.
- Use paths relative to the disposable study root.
- Record node type, permission mode, UID/GID, regular-file size and SHA-256, symlink target, and canonical hard-link group.
- Exclude raw device/inode numbers, timestamps, and absolute temporary paths from portable output.
- Preserve useful operational metadata separately.
- Classify changed nodes as destination, sentinel, or other inside the disposable root.

The oracle did not call `tarfile.data_filter`, reuse harness verdict helpers, or infer containment solely from archive names.

## 7. Frozen refusal mapping

With `errorlevel=1`, the first `FilterError` stopped extraction and accepted prefixes remained evidence.

| Exception | Fixtures |
|---|---:|
| `OutsideDestinationError` | 7 |
| `LinkOutsideDestinationError` | 5 |
| `AbsoluteLinkError` | 2 |
| `SpecialFileError` | 2 |

All expected exception classes and first-refusal indices matched in both complete runs. No `AbsolutePathError` fixture entered the denominator because it was not representable after required POSIX leading-separator stripping.

## 8. Resource caps

- exact fixture count: **32**;
- maximum members per archive: **4**;
- maximum regular payload per member: **256 bytes**;
- maximum declarative payload per archive: **1,024 bytes**;
- maximum archive bytes: **1 MiB**;
- maximum nodes under one disposable root: **64**;
- maximum member-name UTF-8 length: **128 bytes**;
- maximum unexpanded link-target UTF-8 length: **160 bytes**;
- maximum expanded link-target length: **4,096 bytes**;
- wall time per fixture: **5 seconds**;
- wall time for one complete matrix: **180 seconds**;
- address-space limit: **512 MiB**;
- output-file limit: **16 MiB**;
- open-file limit: **64**;
- no child processes or network access from the formal runner.

No cap was raised.

## 9. Protected sequence completed

1. **Cycle 1:** activation, environment/source/document identities, Issue #12, protocol, schemas, refusal mapping, resource caps, and exact manifest.
2. **Cycle 2:** deterministic generator, independent oracle, harness, targeted tests, and a passing 15-fixture hand-audited gate; instrument freeze.
3. **Cycle 3:** exactly one complete formal-matrix execution and preservation of complete results, mismatch records, and identities without final hypothesis disposition.
4. **Cycle 4:** exact-source reconstruction, exactly one clean reproduction, portable comparison, final interpretation, report, Issue #12 closure, and study closure.

No fifth cycle exists.

## 10. Final observations

Both complete runs observed 32 / 32 fixtures, passed 31, retained `META-NONEXEC-01`, and had zero execution errors, sentinel changes, or other/outside-destination changes.

Both portable scientific payloads had SHA-256:

`b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`

The only complete-result differences were operational archive hashes for two absolute-link fixtures whose generated bytes contained different fresh disposable-root strings.

`META-NONEXEC-01` retained frozen expected mode `0600` and observed mode `0644` in both runs. The expected value was not revised. That single exact-metadata failure made H3 unsupported under its frozen criterion while leaving H1 and H2 supported.

## 11. Closed boundaries

No external archives, real user paths, network filesystems, elevated formal extraction, denial-of-service tests, concurrent races, Windows semantics, external contact, vulnerability disclosure, general security certification, expectation revision, or fifth cycle was used or authorized.

The final report is `REPORT.md`. The Cycle 4 closure audit is `CYCLE_4_REPRODUCTION_AND_CLOSURE.md`.
