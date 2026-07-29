# Study 007 Cycle 1 — Activation and Freeze Audit

_Date: 2026-07-29 (Asia/Tokyo)_  
_Disposition: **GO unchanged; Cycle 1 complete**_  
_Issue: #13_

## Work selected

Re-evaluate the frozen proposal against the live repository and exact execution environment; choose GO unchanged or NO-GO; after GO, freeze the active protocol, schema, grammar, observations, errors, caps, and exact 72-sequence manifest; perform structure-only validation and setup capability preflight; stop before instrument implementation or protected execution.

## Activation evidence

- CPython 3.13.5 exists at `/usr/bin/python3.13`.
- `sqlite3.sqlite_version` is 3.46.1.
- `autocommit=True`, `Connection.in_transaction`, `sqlite_errorcode`, and `sqlite_errorname` are available.
- foreign-key support is compiled in and can be enabled.
- the exact schema compiles in one fresh in-memory database.
- explicit `BEGIN`/`ROLLBACK` and an outer setup-only savepoint/`RELEASE` work without wrapper-generated transaction interference.
- setup-only observations confirmed the frozen exception class/code/name mapping.

## Source-identity correction

The local source ID is:

`2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69aalt1`

SQLite's vanilla 3.46.1 release record gives:

`2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69a1e33`

The earlier portfolio assessment's statement that the environment exposed the published release source ID was therefore false. Debian package metadata identifies the local library as `libsqlite3-0 3.46.1-7+deb13u1`, a distribution-modified build.

GO unchanged remains justified because the frozen proposal explicitly requires the activation cycle to identify and pin the exact local library rather than require the vanilla amalgamation. The correction changes no hypothesis or method, but it narrows the object and every later claim to the exact local build.

## Frozen artifacts

- active protocol: `PROTOCOL.md`;
- exact schema: `schema.sql`;
- exact manifest: `manifest.tsv`;
- manifest SHA-256: `16a01c109b196a1127d7783f110e492e4609713f8f527e50e95d7ef254678b4c`;
- structure validator: `validate_manifest.py`;
- preflight instrument and result: `preflight.py`, `cycle1_preflight.json`;
- structure result: `cycle1_structure_validation.json`;
- environment identity: `environment.json`.

## Verification performed

Structure-only validation passed:

- 72 / 72 unique sequences;
- exactly 12 sequences in each of six families;
- 439 actions total;
- maximum 12 actions per sequence under the cap of 24;
- maximum structural savepoint depth 3 under the cap of 6;
- every action belongs to the frozen grammar;
- every expected error belongs to the frozen mapping;
- every declared transaction/savepoint control sequence ends with an empty static stack;
- validator imported no SQLite and executed no SQL.

Capability preflight passed and explicitly recorded `protected_manifest_loaded=false` and `protected_sequence_executed=false`.

## Protected boundary

No protected manifest sequence was loaded by the preflight. No protected sequence was translated into SQL or executed. No model, harness, comparator, hand-gate trace, protected result, mismatch, or hypothesis disposition exists.

## Limitations

- The Python 3.13 documentation URL is maintained and displayed 3.13.14 documentation at retrieval, while the runtime is 3.13.5. Relevant API surfaces exist locally, but the web page is not a patch-level snapshot.
- The local SQLite build includes distribution modifications. This cycle did not audit every Debian patch; binary identity is the binding study referent.
- Cycle 1 freezes declarative sequences and expected error keys. Complete step-by-step model expectations do not yet exist and must be generated and frozen in Cycle 2 before protected execution.
- The setup-only error-map observations are capability evidence, not protected hypothesis evidence.

## Current judgment

Study 007 is active and methodologically viable under the exact local build. Cycle 1 is complete. The highest-value next work is the independent-instrument and twelve-case correctness-gate cycle.
