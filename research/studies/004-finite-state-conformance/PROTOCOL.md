# Study 004 Protocol — Finite-State Conformance Counterexamples

_Date activated: 2026-07-22 (Asia/Tokyo)_  
_Status: **Active — Cycle 1 corpus freeze complete**_

## 1. Activation record

Study 004 is activated **GO unchanged** from the frozen proposal:

- proposal: `research/proposals/STUDY_004_FINITE_STATE_CONFORMANCE.md`
- frozen proposal Git blob: `0b16048ad8e96dcaf147f033205ad76069430776`
- portfolio decision: `research/decisions/2026-07-21-post-study-003-portfolio-assessment.md`

The proposal is incorporated into this protocol without changing its research question, hypotheses, seed, model inventory, mutation operators, budgets, method semantics, reducer semantics, oracle role, disposition rules, or four-cycle limit. This active protocol fixes implementation paths, type conventions, canonical serialization, and Cycle 1 resource boundaries only.

## 2. Research question

> Can a model-guided black-box testing method detect observable divergences between small deterministic finite-state specifications and mutated implementations more effectively than equal-budget uniform random testing, while reducing detected failures to exact shortest counterexamples under an independent oracle?

The study uses deterministic total Mealy machines and a frozen synthetic mutation corpus. It does not claim production verification, real-world vulnerability discovery, general software correctness, or method novelty.

## 3. Frozen hypotheses

- **H1 — detection advantage:** at 256 executed actions per mutant, transition-coverage-guided testing detects at least 10 percentage points more distinguishable mutants than uniform random testing.
- **H2 — breadth robustness:** at 1,024 actions, transition-coverage guidance detects at least as many distinguishable mutants as lexicographic breadth enumeration and trails it by no more than 10 percentage points in any mutation class.
- **H3 — counterexample reduction:** for at least 90% of mutants detected by any frozen method, the reducer returns a still-failing trace whose length equals the independent oracle's exact shortest distinguishing length.

Equivalent mutants remain in the corpus and are excluded only from formal detection-rate denominators. Unsupported hypotheses are permitted outcomes.

## 4. Frozen domain and corpus

### Reference models

- deterministic total Mealy machines;
- reset state `0`;
- state counts `4` and `8`;
- actions `a0`, `a1`, `a2`;
- outputs `o0`, `o1`, `o2`;
- topology families `reset-chain`, `clustered`, and `cyclic`;
- four variants in each state-size × family cell;
- exactly **24 reference models**;
- generation seed **2026072104**.

Cycle 1 implementation clarifies family membership as follows:

- `reset-chain`: `a0` returns every state to reset; `a1` advances each nonterminal state to its successor;
- `clustered`: the state space is split into equal halves and contains exactly two cross-cluster transitions, one originating in each cluster;
- `cyclic`: `a0` forms one cycle covering all states.

Outputs and non-protected target choices are SHA-256-derived from the frozen seed, family, state count, variant, state, and action. Model order is state count, family order above, then variant 1–4.

### Mutation operators

Exactly one deterministic application of each operator is made to every reference model:

1. transition-target substitution;
2. output-label substitution;
3. action-column swap at one state;
4. state-row transplant;
5. self-loop injection;
6. paired transition mutation across two distinct states.

Locations and replacements are selected generically from the model canonical digest, operator name, and frozen seed. No mutant is manually replaced. The inventory is exactly **144 mutants**.

The Cycle 1 corpus contains no equivalence label, distinguishing trace, method detection result, reducer result, or benchmark interpretation.

## 5. Canonical serialization

- schema version: `1`;
- UTF-8 JSON;
- keys sorted recursively by Python `json.dumps(sort_keys=True)`;
- separators `(',', ':')`;
- non-ASCII preserved;
- exactly one trailing newline;
- model digests are SHA-256 over each canonical model record;
- mutation selection digests are SHA-256 over frozen seed, source-model digest, and operator name;
- the bundle records a payload SHA-256 calculated before adding the top-level `payload_sha256` field.

Frozen Cycle 1 data:

- manifest: `research/studies/004-finite-state-conformance/data/corpus_v1.json`;
- reference-model transitions: `research/studies/004-finite-state-conformance/data/models_v1.json`.

The manifest records every model digest and all 144 mutant IDs and digests in frozen operator order. The model bundle records the canonical transition tables. Mutant transition tables are reconstructed deterministically from the frozen source model, seed, operator order, and generator, then checked against the frozen mutant digests.

## 6. Frozen future methods

The proposal's three equal-budget methods remain unchanged and are not implemented in Cycle 1:

- uniform random testing with eight reset-delimited campaigns;
- increasing-length lexicographic breadth enumeration;
- shortest-trace transition-coverage guidance, followed by consecutive transition-pair coverage.

Budgets remain 64, 256, and 1,024 executed actions per mutant. Reset costs no action but is recorded. Methods may use the reference model but not mutant internals or oracle results.

The reducer and independent paired-state breadth-first oracle remain exactly as frozen in the proposal. Neither exists in Cycle 1.

## 7. Protected sequence

1. activate this unchanged protocol;
2. implement and freeze schema, generator, serialization, and 24-model / 144-mutant corpus;
3. implement and freeze the three testing methods and reducer using hand-authored fixtures only;
4. implement and gate the independent exact oracle;
5. classify the already frozen corpus;
6. execute the already frozen methods and reducer;
7. analyze only after raw results are complete.

Inspecting corpus equivalence or shortest distinguishing traces before the methods and reducer are frozen contaminates H1–H3 and requires invalid closure rather than retrospective repair.

## 8. Gates and dispositions

- corpus inventory must remain 24 models and 144 mutants;
- at least 80% of mutants must later be distinguishable or the study closes with a negative setup result;
- the oracle must pass at least eight frozen hand-audited fixtures, with at most one bounded correction cycle;
- method/oracle independence must be maintained;
- complete deterministic results must be repeated byte-identically for full methodological success;
- valid comparison with unsupported H1–H3 is a partial result;
- incomplete nonrepeatable execution is operationally incomplete.

## 9. Cycle limit

Maximum four approval cycles from activation through closure:

1. activation, protocol, generator, and frozen corpus — **complete**;
2. testing methods and reducer freeze;
3. oracle gate, corpus classification, and formal benchmark;
4. deterministic reproduction, analysis, report, and closure.

No fifth cycle may be added.

## 10. Cycle 1 implementation paths

- schema: `src/templex_zero/finite_state_conformance/schema.py`
- generator: `src/templex_zero/finite_state_conformance/corpus.py`
- package export: `src/templex_zero/finite_state_conformance/__init__.py`
- generation command: `experiments/generate_finite_state_conformance_corpus.py`
- targeted tests: `tests/test_finite_state_conformance_corpus.py`
- frozen manifest: `data/corpus_v1.json`;
- frozen model bundle: `data/models_v1.json`;
- Cycle 1 audit: `CYCLE_1_SETUP_AUDIT.md`

## 11. Verification boundary

Cycle 1 verification may establish deterministic structure, inventory, serialization, mutation application, and absence of protected outcome fields. It does not establish corpus viability, observational distinguishability, testing performance, reducer quality, oracle correctness, or any hypothesis.

Fresh checkout and full-repository regression status must be reported explicitly. A functional reconstruction is not a byte-identical checkout replay.
