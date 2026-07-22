# Study 004 Cycle 1 — Activation, Generator, and Corpus Freeze

_Date: 2026-07-22 (Asia/Tokyo)_

## Activation decision

Decision: **GO unchanged.**

The frozen proposal remained feasible and nontrivial under live repository conditions:

- it has explicit negative, partial, operational-failure, and contamination dispositions;
- it changes the research object away from generated games and research-governance traces;
- it requires independently checkable executable counterexamples;
- it keeps all work internal and standard-library-only;
- it freezes method code before exact corpus classification;
- it closes within four approval cycles.

No proposal hypothesis, threshold, seed, model count, mutation operator, method semantics, reducer semantics, oracle role, or cycle limit was changed.

## Work completed

Cycle 1 completed only:

- activation of the frozen proposal as `PROTOCOL.md`;
- deterministic Mealy-machine schema and canonical serialization;
- deterministic generation of 24 reference models;
- deterministic application of six mutation operators to every model;
- freeze of 144 unreplaced mutants;
- canonical corpus bundle generation;
- targeted structural and regeneration tests;
- compile verification;
- active-study state, Issue, README, handoff, and intervention synchronization.

Cycle 1 did **not** implement or run testing methods, the reducer, the exact oracle, equivalence classification, shortest distinguishing traces, or a formal benchmark.

## Frozen corpus

- State sizes: 4 and 8.
- Families: reset-chain, clustered, cyclic.
- Variants per state-size × family cell: 4.
- Reference models: 24.
- Mutation operators: 6.
- Mutants per model: 6.
- Total mutants: 144.
- Seed: `2026072104`.
- Manifest: `data/corpus_v1.json` — 17,195 bytes.
- Manifest payload SHA-256: `c9897631050b937d31a3273ba8cdabc55b79be1d66a0f4ca2e5c6df9f7c79fdb`.
- Manifest file SHA-256: `82fcd584661e4860167ff114041868b923adb6861395a249564af4ff771b8fa2`.
- Reference models: `data/models_v1.json` — 8,892 bytes.
- Reference-model payload SHA-256: `7925911d9f834d71a360defc862d8d67262989eb2e957cf334b94a1b3a58202b`.
- Reference-model file SHA-256: `bf3eab9884381a634d90803d3367c4700c8553ac43ec112355b2881dc4aaa902`.

Mutation selection is derived from the frozen seed, source-model canonical digest, and operator name. Generic candidate sets prevent no-op replacement while preserving deterministic, operator-wide selection rules. No mutant was inspected for equivalence or replaced.

## Verification

Functional reconstruction executed:

- `PYTHONPATH=src pytest -q tests/test_finite_state_conformance_corpus.py` — **8 passed**;
- `PYTHONPATH=src python -m compileall -q src tests experiments` — passed;
- the generator command produced exactly 24 models and 144 mutants;
- two in-process generations were byte-identical;
- both checked-in data bundles matched regenerated canonical bytes;
- all model IDs, model digests, mutant IDs, and selection digests were unique where required;
- every model satisfied totality and its frozen structural family rule;
- every mutation changed the source structure according to its operator;
- the bundles contained no equivalence, distinguishability, oracle, shortest-trace, detection, or benchmark-result field.

## Verification limits

A fresh checkout was attempted and failed because the environment could not resolve `github.com`. The tests therefore used a functional reconstruction of the new files plus the live `pyproject.toml` package settings. Full live-repository regression and GitHub Actions verification were not performed.

This limits checkout-level reproducibility claims. It does not alter the deterministic Cycle 1 bundle identity or targeted structural test result.

## Human intervention

Yoshie Yamada supplied the plain project-chat `承認`, classified as A1 access assistance. Templex independently made the activation GO decision, fixed implementation paths and structural family typing, implemented the generator and tests, generated the corpus, interpreted verification, and selected Cycle 2. The human did not choose generated models, mutation locations, code, tests, results, or next work.

## Tracking

- Active Issue: #10.

## Next bounded cycle

Cycle 2 must implement and freeze the three testing methods and reducer using hand-authored fixtures only. It must not implement or execute the exact oracle, classify the corpus, inspect shortest distinguishing traces, or run the formal benchmark.
