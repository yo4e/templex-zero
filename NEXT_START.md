# Next Start

_Updated: 2026-07-23 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the active Study 004 protocol, both cycle audits, governance files, Issue #10, current commits, and the frozen source/data blobs.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**Study 004 is active. Cycle 2 of at most four is complete.**

- Study 001: closed negative game-design result.
- Study 002: closed partial / incomplete exact-first result.
- Study 003: closed methodological success with bounded claims.
- Study 004: active finite-state conformance study.

Current Study 004 artifacts:

- `research/studies/004-finite-state-conformance/PROTOCOL.md`
- `research/studies/004-finite-state-conformance/CYCLE_1_SETUP_AUDIT.md`
- `research/studies/004-finite-state-conformance/CYCLE_2_METHOD_FREEZE.md`
- `research/studies/004-finite-state-conformance/data/corpus_v1.json`
- `research/studies/004-finite-state-conformance/data/models_v1.json`
- `src/templex_zero/finite_state_conformance/execution.py`
- `src/templex_zero/finite_state_conformance/methods.py`
- `src/templex_zero/finite_state_conformance/reducer.py`
- Issue #10

Cycle 1 froze 24 deterministic Mealy reference models and 144 unreplaced mutants under seed `2026072104`.

Cycle 2 froze:

- uniform random testing with eight independent campaigns;
- increasing-length lexicographic breadth enumeration;
- shortest-reference-path transition coverage followed by repeated transition-pair coverage rounds;
- the four-stage black-box reducer;
- deterministic tie-breaks, budget accounting, and hand-authored fixture behavior.

The combined current Study 004 tests passed 20 cases. The frozen hand-fixture behavioral projection SHA-256 is `6eddea3466f3f4ceb4a77a687a45ac6965e31f1039e3a6433d1c3ba34046abd6`.

No exact oracle, corpus classification, shortest distinguishing trace, formal benchmark result, or H1–H3 disposition exists.

## Next bounded work unit

The next approval may perform **Study 004 Cycle 3 — oracle gate, corpus classification, and raw formal benchmark**.

1. re-fetch and verify the frozen Cycle 1 corpus and Cycle 2 source blobs;
2. write and freeze at least eight hand-audited oracle fixture pairs with expected equivalence or exact shortest trace before executing the oracle;
3. implement the exact paired-state breadth-first oracle independently from method and reducer helpers;
4. run the fixture correctness gate and source-independence checks;
5. if the gate fails, use at most the protocol-permitted bounded correction or close without formal comparison;
6. if the gate passes, classify exactly the already frozen 144 mutants without replacement;
7. enforce the frozen 80% distinguishability viability gate;
8. if viable, run all three frozen methods at 64, 256, and 1,024 actions per distinguishable or retained corpus item as specified, reduce detected failures, and save deterministic raw result artifacts;
9. update Issue #10, state, audit, and handoff;
10. stop before final synthesis and normal closure.

## Protected prohibitions

Cycle 3 must not:

- alter the 24 models, 144 mutants, seed, mutation operators, or canonical corpus;
- change the three testing methods, reducer, budgets, hypotheses, thresholds, or source blobs after protected oracle information is produced;
- import method search, coverage, reducer, or verdict helpers into the independent oracle;
- silently replace equivalent, trivial, difficult, or inconvenient mutants;
- interpret a partial raw run as a complete benchmark;
- perform final H1–H3 synthesis or ordinary study closure unless a negative setup, invalid, or operational-failure disposition makes early closure mandatory.

Any protected sequence violation contaminates H1–H3 and cannot be repaired retrospectively.

## Verification boundaries carried forward

- Fresh checkout has remained unavailable because the environment cannot resolve `github.com`.
- Connector-backed source and blob checks do not equal a full checkout regression.
- The 20 passing tests cover current Study 004 components, not the full historical repository.
- The corpus has not passed the later 80% distinguishability viability gate.
- The Cycle 2 hand fixtures establish deterministic implementation behavior, not comparative performance.

## Human gate

> 承認

## Human action pending

None.
