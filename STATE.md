# State

_Last updated: 2026-07-23_

## Phase

**No active study / Study 004 closed as a partial result**

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

## Study 004 closure

- Final report: `research/studies/004-finite-state-conformance/REPORT.md`
- Cycle 4 audit: `research/studies/004-finite-state-conformance/CYCLE_4_REPRODUCTION_AND_CLOSURE.md`
- Final analysis: `research/studies/004-finite-state-conformance/data/final_analysis_v1.json`
- Issue #10: closed.
- Cycle count: **4 of maximum 4 complete**.
- Complete raw benchmark: **1,296 rows**.
- Complete rerun: **byte-identical**.
- Gzip SHA-256: `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679`.
- Final analysis SHA-256: `18e49046e9255b10dcd4c8b6ecdde3abf5971507f529575cd0511223cfb4b92a`.

## Final Study 004 disposition

- **H1 unsupported:** guided 140 / 144 versus random 142 / 144 at 256 actions.
- **H2 supported:** guided 143 / 144 versus breadth 131 / 144 at 1,024 actions, with no mutation-class trail.
- **H3 unresolved:** the frozen unique-mutant denominator did not specify aggregation across multiple reducer outputs; reasonable rules cross the 90% threshold.
- Overall: **valid partial result**, not full methodological success.

## Next bounded work

The next approval may perform one post-Study-004 portfolio assessment. It must compare at least three genuinely distinct directions plus inactivity, select at most one direction for an inactive frozen proposal, and stop. It must not activate Study 005 or begin implementation in the same cycle.

## Verification limitation

Fresh checkout remained unavailable because the environment could not resolve `github.com`. Cycle 4 used a functional reconstruction of live, hash-checked sources. The complete historical repository suite and GitHub Actions were not run.

## Human action currently needed

None.
