# State

_Last updated: 2026-07-24_

## Phase

**No active study / Study 005 closed after Cycle 4 of maximum 4**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

- **Study 001:** negative autonomous-game-design conclusion.
- **Study 002:** partial / incomplete exact-first result; H1 and H3 supported, H2 unresolved.
- **Study 003:** methodological success with bounded procedural claims.
- **Study 004:** partial finite-state conformance result; H1 unsupported, H2 supported, H3 unresolved.
- **Study 005:** positive bounded TZDB transition-round-trip conformance result; H1, H2, and H3 supported with procedural and artifact-portability limitations.

## Study 005 final result

- Final report: `research/studies/005-tzdb-transition-roundtrip/REPORT.md`
- Cycle 4 audit: `research/studies/005-tzdb-transition-roundtrip/CYCLE_4_REPRODUCTION_AND_CLOSURE.md`
- Closed issue: **#11**
- Pinned referent: **IANA tzdb 2026c**
- Runtime: **CPython 3.13.5**
- Canonical inventory: **313 zones**
- Explicit transitions: **18,071**
- H1: **90,079 records / mismatches 0 / supported**
- H2: **26,778 records / mismatches 0 / supported**
- H3: **44,790 records / mismatches 0 / supported**
- Total: **161,647 records / mismatches 0**
- Scientific payload SHA-256: `cf635b2a32b8183f14b5ec7d54a1fd95cc6b9bad2cda5087a0072317cc0f0e79`

The exact-source Cycle 4 reproduction generated all scientific record families byte-identical to Cycle 3. The complete canonical digests differed only in the absolute temporary path serialized in `environment.tzpath_after[0]`; the full digest was therefore non-portable.

## Permanent limitations

- The compact transition manifest is not independently self-contained for first-retained-transition pre-type context in 274 zones; exact TZif bytes and the reader are required.
- Cycle 3 did not literally execute the committed reader and runner bytes; Cycle 4 resolved the scientific effect by exact-source reproduction, but the procedural deviation remains recorded.
- Cycle 3 source-identity records contained transcription errors and the repository executed-runner evidence was not an exact byte copy; Cycle 4 records the corrected identities.
- The targeted fixture artifact was not separately decoded and rerun in Cycle 4, although exact reader/harness tests, full manifest, and formal records reproduced.
- No detached IANA signature was supplied or verified.
- The conclusion is bounded to the frozen release, runtime, compiler environment, inventory, interval, precision, and assertions.

## Next bounded work

There is no active study and no remaining Study 005 cycle. The next exact `承認` may open one post-Study-005 portfolio cycle only:

1. inspect all five closed studies, governance records, open issues, and recent commits;
2. compare genuinely distinct future directions plus deliberate inactivity under an explicit threshold;
3. select and freeze at most one inactive proposal, or record a justified decision to remain inactive;
4. do not activate a new study, create its implementation, or run its experiment in that same cycle unless the governing proposal process explicitly permits it;
5. update repository state and stop.

No external contact, terms acceptance, defect report, spending, permission change, or third-party repository modification is authorized.

## Human action currently needed

None beyond a later exact `承認` for one bounded post-study portfolio cycle.
