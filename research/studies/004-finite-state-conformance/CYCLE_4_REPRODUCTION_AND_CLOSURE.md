# Study 004 Cycle 4 — Deterministic Reproduction, Analysis, and Closure

_Date: 2026-07-23 (Asia/Tokyo)_

## Disposition

**Cycle 4 completed. Study 004 is closed as a partial result.**

The complete Cycle 3 result generation reproduced byte-identically. H1 is unsupported, H2 is supported, and H3 is unresolved because the frozen hypothesis did not specify how to aggregate multiple reducer outputs for one unique mutant. No fifth cycle is permitted or required.

## Frozen-input verification

Before final analysis, Cycle 4 re-read the live protocol, state, Cycle 3 audit, raw manifest, runner, Issue #10, and frozen source identities. No protected corpus, method, reducer, oracle, budget, hypothesis, threshold, seed, or mutation inventory was changed.

Fresh checkout was attempted again and failed because the environment could not resolve `github.com`. A functional reconstruction was built from the live frozen source contents. The limitation remains attached to all reproduction claims.

## Complete reproduction

The unchanged Cycle 3 runner generated:

- gzip bytes: **29,400**;
- gzip SHA-256: `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679`;
- decompressed JSON bytes: **899,730**;
- JSON SHA-256: `a725f287b3d3a09b5d8e991e82daf9cb8f6a719c528a2e4047524cfd289bfc3c`;
- internal payload SHA-256: `bb34844aee696cde0ea19de9c48a5bd5ec8faf66391a492bc6277bf24ac69927`.

All values exactly match the frozen Cycle 3 evidence. Base64 encoding the reproduced gzip and splitting it into eight 4,900-character parts produced the exact eight live Git blob identities recorded for `part00` through `part07`. This verifies the transport identity without claiming a fresh checkout.

## Final analysis artifact

`experiments/analyze_finite_state_conformance_cycle4.py` reconstructs the raw transport, reruns the complete generator, requires byte equality, computes the frozen metrics, applies H1 and H2, and preserves the H3 aggregation ambiguity rather than choosing a favorable post-result rule.

- runner Git blob: `c5674fe4578adb5e1b4998a94b9aa2fb824b2066`;
- final analysis path: `data/final_analysis_v1.json`;
- final analysis Git blob: `c9ea60ecc31b79012644fcd6618e078d205ba422`;
- final analysis file SHA-256: `18e49046e9255b10dcd4c8b6ecdde3abf5971507f529575cd0511223cfb4b92a`;
- internal analysis payload SHA-256: `7b80f4239650fe5fbd750559578ecc9ab609cb7aad68d0469246b47b412d6584`.

Two final-analysis generations were byte-identical.

## Verification

Functional reconstruction executed:

- complete raw runner rerun — byte-identical gzip;
- final analysis generation twice — byte-identical output;
- `pytest -q tests/test_finite_state_conformance_cycle4.py` — **3 passed**;
- compile verification for reconstructed `src`, `experiments`, and `tests` — passed;
- final analysis, runner, and test source were uploaded and live blob identities re-read.

The first Cycle 4 pytest attempt stopped during collection because the new analysis runner used a script-local import path. No benchmark or disposition logic ran. The import was made compatible with both direct execution and package import. The second attempt exposed only JSON integer-key normalization in the deterministic comparison. Distribution keys were frozen as strings, after which all three tests passed. Neither correction altered raw evidence, hypotheses, thresholds, or substantive disposition logic.

## Hypothesis results

- **H1 unsupported:** guided 140 / 144 versus random 142 / 144 at 256 actions; difference -1.388889 percentage points versus required +10.
- **H2 supported:** guided 143 / 144 versus breadth 131 / 144 at 1,024 actions; guided tied or led breadth in all six mutation classes.
- **H3 unresolved:** no invalid reducer outputs, but plausible unique-mutant aggregation rules range from 68.75% to 100% and cross the frozen 90% threshold.

## Study disposition

The corpus and oracle gates passed, sequence integrity held, complete results exist, and byte-identical reproduction succeeded. Because H1 is unsupported and H3 is unresolved, the protocol's full-methodological-success condition is not met. The valid comparison therefore closes as a **partial result**.

## Human intervention

Yoshie Yamada supplied the plain project-chat `承認`, classified as A1 access assistance. Templex independently performed the reproduction, chose the H3 unresolved disposition rather than retroactive aggregation, wrote the report, closed the issue, and selected the next portfolio-assessment boundary. The human did not choose the results, analysis rule, interpretation, or next research direction.

## Next bounded work

Study 004 is closed and the laboratory has no active study. The next approval may perform one portfolio-level post-Study-004 assessment comparing at least three genuinely distinct directions plus inactivity and may freeze at most one inactive proposal. It must not activate or implement a new study in that same cycle.
