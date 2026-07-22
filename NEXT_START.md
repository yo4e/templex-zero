# Next Start

_Updated: 2026-07-22 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the active Study 004 protocol and Cycle 1 audit, governance files, Issue #10, current commits, and the frozen data bundles.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**Study 004 is active. Cycle 1 of at most four is complete.**

- Study 001: closed negative game-design result.
- Study 002: closed partial / incomplete exact-first result.
- Study 003: closed methodological success with bounded claims.
- Study 004: active finite-state conformance study.

Current Study 004 artifacts:

- `research/studies/004-finite-state-conformance/PROTOCOL.md`
- `research/studies/004-finite-state-conformance/README.md`
- `research/studies/004-finite-state-conformance/CYCLE_1_SETUP_AUDIT.md`
- `research/studies/004-finite-state-conformance/data/corpus_v1.json`
- `research/studies/004-finite-state-conformance/data/models_v1.json`
- Issue #10

Cycle 1 froze 24 deterministic Mealy reference models and 144 unreplaced mutants under seed `2026072104`. Targeted tests passed 8 cases, compile verification passed, and repeated generation was byte-identical.

No equivalence classification, exact oracle, shortest distinguishing trace, testing campaign, reducer result, or formal benchmark exists.

## Next bounded work unit

The next approval may perform **Study 004 Cycle 2 — method and reducer freeze only**.

1. implement uniform-random testing with eight reset-delimited campaigns;
2. implement increasing-length lexicographic breadth enumeration;
3. implement shortest-trace transition-coverage guidance followed by consecutive transition-pair coverage;
4. implement the frozen reducer sequence;
5. use only hand-authored unit fixtures and deterministic tests;
6. freeze the four implementations after tests;
7. update Issue #10, state, audit, and handoff.

Cycle 2 must not:

- implement or execute the exact paired-state oracle;
- classify any frozen corpus mutant as equivalent or distinguishable;
- inspect or record shortest distinguishing traces;
- run the methods on the frozen corpus;
- generate formal benchmark results;
- alter budgets, hypotheses, seed, corpus, method semantics, reducer semantics, or cycle limit.

The method/reducer freeze must occur before protected oracle information exists. A sequence violation contaminates H1–H3 and cannot be repaired retrospectively.

## Verification boundaries carried forward

- Fresh checkout has remained unavailable because the environment could not resolve `github.com`.
- Connector-backed source and blob checks do not equal a full checkout regression.
- Cycle 1 functional reconstruction passed targeted tests but did not run the historic full suite.
- The frozen corpus has not passed its later 80% distinguishability viability gate.

## Human gate

> 承認

## Human action pending

None.
