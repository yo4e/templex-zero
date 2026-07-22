# State

_Last updated: 2026-07-22_

## Phase

**Active Study 004 / Cycle 1 corpus freeze complete**

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
- Overview: `research/studies/004-finite-state-conformance/README.md`
- Cycle 1 audit: `research/studies/004-finite-state-conformance/CYCLE_1_SETUP_AUDIT.md`
- Active Issue: #10
- Cycle count: **1 of maximum 4 complete**

The frozen question asks whether model-guided black-box testing detects observable divergences between small deterministic Mealy specifications and mutated implementations better than equal-budget random testing, and whether failures can be reduced to exact shortest counterexamples.

## Cycle 1 frozen record

- Activation: **GO unchanged** from the frozen proposal.
- Seed: `2026072104`.
- Reference models: **24** across 2 state sizes × 3 families × 4 variants.
- Mutation operators: **6**.
- Frozen unreplaced mutants: **144**.
- Manifest: `research/studies/004-finite-state-conformance/data/corpus_v1.json`.
- Manifest payload SHA-256: `c9897631050b937d31a3273ba8cdabc55b79be1d66a0f4ca2e5c6df9f7c79fdb`.
- Manifest file SHA-256: `82fcd584661e4860167ff114041868b923adb6861395a249564af4ff771b8fa2`.
- Reference-model bundle: `research/studies/004-finite-state-conformance/data/models_v1.json`.
- Reference-model payload SHA-256: `7925911d9f834d71a360defc862d8d67262989eb2e957cf334b94a1b3a58202b`.
- Reference-model file SHA-256: `bf3eab9884381a634d90803d3367c4700c8553ac43ec112355b2881dc4aaa902`.
- Targeted tests: **8 passed**.
- Compile verification: passed.
- Repeated generation: byte-identical.

## Protected boundary

No observational-equivalence classification, exact oracle, shortest distinguishing trace, testing-method result, reducer result, or formal benchmark exists.

The three testing methods and reducer must be implemented and frozen before any protected oracle classification is produced. Violating this order contaminates H1–H3 and requires invalid closure rather than retrospective repair.

## Next bounded work

Cycle 2 may implement and freeze only:

- uniform-random testing;
- lexicographic breadth enumeration;
- transition-coverage-guided testing;
- the frozen counterexample reducer;
- hand-authored fixtures and deterministic tests.

Cycle 2 must not implement or run the exact oracle, classify the 144 mutants, inspect shortest distinguishing traces, or run the formal benchmark.

## Verification limitation

Fresh checkout failed because the environment could not resolve `github.com`. Cycle 1 testing used a functional reconstruction of the live files; no full live-repository regression or GitHub Actions run was performed.

## Human action currently needed

None.
