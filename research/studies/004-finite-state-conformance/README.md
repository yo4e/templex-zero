# Study 004 — Finite-State Conformance Counterexamples

## Status

**Active — Cycle 2 testing-method and reducer freeze complete.**

Study 004 tests whether model-guided black-box testing detects observable divergences between small deterministic Mealy-machine specifications and mutated implementations more effectively than equal-budget random testing, and whether detected failures can be reduced to exact shortest counterexamples.

## Cycle 1 frozen corpus

- Activation decision: **GO unchanged**.
- Reference models: **24**.
- Topology cells: 2 state sizes × 3 families × 4 variants.
- Mutation operators: **6**.
- Frozen mutants: **144**.
- Generation seed: `2026072104`.
- Corpus payload SHA-256: `c9897631050b937d31a3273ba8cdabc55b79be1d66a0f4ca2e5c6df9f7c79fdb`.
- Corpus file SHA-256: `82fcd584661e4860167ff114041868b923adb6861395a249564af4ff771b8fa2`.
- Reference-model payload SHA-256: `7925911d9f834d71a360defc862d8d67262989eb2e957cf334b94a1b3a58202b`.
- Reference-model file SHA-256: `bf3eab9884381a634d90803d3367c4700c8553ac43ec112355b2881dc4aaa902`.

## Cycle 2 frozen methods

The following implementations are frozen before any protected exact-oracle or corpus-classification result exists:

- black-box reset/step execution and first-mismatch recording;
- uniform random testing with eight independently seeded campaigns;
- increasing-length lexicographic breadth enumeration;
- shortest-reference-path transition coverage followed by repeated transition-pair coverage rounds;
- the four-stage black-box counterexample reducer.

Cycle 2 used only hand-authored fixtures. Its targeted method/reducer tests passed **12** cases; the combined current Study 004 Cycle 1 and Cycle 2 tests passed **20** cases. Compile verification passed, live source blobs matched the tested bytes, and the frozen hand-fixture behavioral projection SHA-256 is `6eddea3466f3f4ceb4a77a687a45ac6965e31f1039e3a6433d1c3ba34046abd6`.

## Frozen artifacts

- Protocol: `PROTOCOL.md`
- Cycle 1 audit: `CYCLE_1_SETUP_AUDIT.md`
- Cycle 2 audit: `CYCLE_2_METHOD_FREEZE.md`
- Corpus manifest: `data/corpus_v1.json`
- Reference-model bundle: `data/models_v1.json`
- Schema: `../../../src/templex_zero/finite_state_conformance/schema.py`
- Generator: `../../../src/templex_zero/finite_state_conformance/corpus.py`
- Black-box execution: `../../../src/templex_zero/finite_state_conformance/execution.py`
- Testing methods: `../../../src/templex_zero/finite_state_conformance/methods.py`
- Reducer: `../../../src/templex_zero/finite_state_conformance/reducer.py`
- Corpus tests: `../../../tests/test_finite_state_conformance_corpus.py`
- Method/reducer tests: `../../../tests/test_finite_state_conformance_methods.py`
- Active tracking: Issue #10

## Current protected boundary

The frozen corpus has **not** been classified by observational equivalence. No exact paired-state oracle, oracle correctness result, shortest distinguishing trace, frozen-corpus method result, reducer benchmark result, or formal H1–H3 disposition exists.

The method and reducer source blobs recorded in `CYCLE_2_METHOD_FREEZE.md` may not be repaired or tuned after protected corpus classification begins. Such a change would contaminate H1–H3 rather than improve the result.

## Next bounded cycle

Cycle 3 may:

1. freeze at least eight hand-audited exact-oracle fixture pairs and expected results before oracle execution;
2. implement the independent paired-state breadth-first oracle without importing testing-method or reducer helpers;
3. run the correctness and independence gate;
4. if the gate passes, classify the already frozen 144 mutants;
5. enforce the frozen 80% distinguishability viability gate;
6. if viable, execute the frozen methods and reducer at 64, 256, and 1,024 actions per mutant and save deterministic raw results.

Cycle 3 must not change the corpus, methods, reducer, budgets, hypotheses, thresholds, or mutation inventory after protected classification begins. Final synthesis, repeated complete-report reproduction, H1–H3 disposition, and normal closure remain Cycle 4 work unless a negative setup or invalid result requires earlier closure.
