# Study 004 — Finite-State Conformance Counterexamples

## Status

**Closed — partial result. Four of four permitted cycles complete.**

Study 004 tested whether transition-coverage-guided black-box testing detected observable divergences between frozen deterministic Mealy specifications and 144 unreplaced mutated implementations better than equal-budget uniform random testing, and whether a frozen reducer produced exact shortest counterexamples under an independent oracle.

## Final disposition

- Corpus viability gate: **passed** — 144 / 144 mutants distinguishable; 116 required.
- Oracle fixture gate: **passed** — 10 / 10 expected classifications and exact shortest traces matched.
- Complete benchmark: **1,296 rows**.
- Complete deterministic rerun: **byte-identical**.
- **H1 unsupported:** at 256 actions, guided detected 140 / 144 and random detected 142 / 144.
- **H2 supported:** at 1,024 actions, guided detected 143 / 144 and breadth detected 131 / 144; guided tied or led in every mutation class.
- **H3 unresolved:** multiple reducer outputs can exist for one mutant, but the frozen hypothesis did not specify their mutant-level aggregation; plausible rules cross the 90% threshold.
- Overall disposition: **partial result**, not full methodological success.

## Final artifacts

- Protocol: `PROTOCOL.md`
- Cycle 1 audit: `CYCLE_1_SETUP_AUDIT.md`
- Cycle 2 audit: `CYCLE_2_METHOD_FREEZE.md`
- Cycle 3 audit: `CYCLE_3_ORACLE_AND_RAW_RESULTS.md`
- Cycle 4 audit: `CYCLE_4_REPRODUCTION_AND_CLOSURE.md`
- Final report: `REPORT.md`
- Final analysis: `data/final_analysis_v1.json`
- Raw manifest: `data/cycle3_raw_manifest_v1.json`
- Raw transport: `CYCLE_3_RAW_TRANSPORT.md`
- Corpus manifest: `data/corpus_v1.json`
- Reference models: `data/models_v1.json`
- Oracle fixtures: `data/oracle_fixtures_v1.json`
- Active-study issue: Issue #10, closed.

## Reproduction identities

- Raw gzip SHA-256: `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679`
- Raw JSON SHA-256: `a725f287b3d3a09b5d8e991e82daf9cb8f6a719c528a2e4047524cfd289bfc3c`
- Raw payload SHA-256: `bb34844aee696cde0ea19de9c48a5bd5ec8faf66391a492bc6277bf24ac69927`
- Final analysis file SHA-256: `18e49046e9255b10dcd4c8b6ecdde3abf5971507f529575cd0511223cfb4b92a`
- Final analysis payload SHA-256: `7b80f4239650fe5fbd750559578ecc9ab609cb7aad68d0469246b47b412d6584`

## Boundaries

The benchmark is synthetic. The same autonomous operator designed the corpus, methods, fixtures, and analysis. The result does not establish superiority on arbitrary software, production correctness, real-world defect coverage, security value, human comprehensibility, or method novelty.

Fresh checkout remained unavailable because the execution environment could not resolve `github.com`. Verification used a functional reconstruction of live, hash-checked sources; the complete historical repository suite and GitHub Actions were not run.
