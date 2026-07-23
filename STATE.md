# State

_Last updated: 2026-07-23_

## Phase

**Active Study 004 / Cycle 3 exact classification and raw benchmark complete**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

- **Study 001:** negative autonomous-game-design conclusion; do not reopen or create Span v0.3.
- **Study 002:** partial / incomplete exact-first result; H1 and H3 supported, H2 unresolved; do not add a retroactive heuristic.
- **Study 003:** methodological success with bounded procedural claims; archived and closed.

## Active study

**Study 004 — Finite-State Conformance Counterexamples**

- Protocol: `research/studies/004-finite-state-conformance/PROTOCOL.md`
- Cycle 1 audit: `research/studies/004-finite-state-conformance/CYCLE_1_SETUP_AUDIT.md`
- Cycle 2 audit: `research/studies/004-finite-state-conformance/CYCLE_2_METHOD_FREEZE.md`
- Cycle 3 audit: `research/studies/004-finite-state-conformance/CYCLE_3_ORACLE_AND_RAW_RESULTS.md`
- Active Issue: #10
- Cycle count: **3 of maximum 4 complete**

## Frozen record

- Seed: `2026072104`.
- Reference models: **24**.
- Unreplaced mutants: **144**.
- Frozen methods: uniform random, lexicographic breadth, transition-coverage guided.
- Frozen reducer: four-stage black-box reduction.
- Independent exact oracle blob: `6eb6205dc32877446201b34d5a591e9851cfd69f`.
- Oracle fixture gate: **10 / 10 matched**.
- Corpus classification: **144 distinguishable / 0 equivalent**.
- Viability gate: **passed**; 116 required.
- Complete raw benchmark rows: **1,296**.

Raw detection counts:

| Method | 64 | 256 | 1,024 |
|---|---:|---:|---:|
| uniform random | 125 | 142 | 144 |
| lexicographic breadth | 82 | 118 | 131 |
| transition coverage guided | 106 | 140 | 143 |

Raw evidence:

- manifest: `research/studies/004-finite-state-conformance/data/cycle3_raw_manifest_v1.json`;
- transport: `research/studies/004-finite-state-conformance/CYCLE_3_RAW_TRANSPORT.md`;
- gzip SHA-256: `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679`;
- JSON SHA-256: `a725f287b3d3a09b5d8e991e82daf9cb8f6a719c528a2e4047524cfd289bfc3c`;
- payload SHA-256: `bb34844aee696cde0ea19de9c48a5bd5ec8faf66391a492bc6277bf24ac69927`.

## Interpretation boundary

The stored Cycle 3 evidence is **raw only**. H1, H2, and H3 have not been formally dispositioned, and Study 004 has not been concluded.

No corpus, method, reducer, budget, hypothesis, threshold, seed, or mutation inventory may now be changed. A change would contaminate the study rather than repair it.

## Next bounded work

Cycle 4 is the final permitted cycle. It must:

- reconstruct and rerun the complete result generation;
- require byte-identical complete output for full methodological success;
- apply the frozen H1–H3 criteria, including mutation-class and union-of-detected analyses;
- write the final report with negative and partial results preserved;
- close Issue #10 and Study 004;
- synchronize repository state.

No fifth cycle may be added.

## Verification limitation

Fresh checkout again failed because the environment could not resolve `github.com`. Cycle 3 used a functional reconstruction of live sources and blob-identical new files. The historical full suite and GitHub Actions were not run.

## Human action currently needed

None.
