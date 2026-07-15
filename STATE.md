# State

_Last updated: 2026-07-16_

## Phase

**Study 001 / Span v0.2 participant-aware agent instrumentation**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**.
- The repository is public at `yo4e/templex-zero` and operates under `governance/APPROVAL_DRIVEN_EXECUTION.md`.
- Relay is rejected after stronger symmetric play exposed severe first-player advantage and a substantial 200-ply unresolved population.
- Span v0.1 is frozen and rejected after exhaustive reply enumeration proved a five-ply Black forced connection through C2–C3–C4 or its reflection.
- Keystone v0.1 is frozen and rejected after only 50.9% of 2,000 fixed-seed random games completed by 200 plies.
- `analysis/prototype_revision_selection.md` selected Span as the only one-change revision target.
- `prototypes/span/RULES_v0_2.md` froze an opening swap rule before implementation or new play results.
- `src/templex_zero/games/span_v0_2.py` now implements participant identity, participant-color ownership, one-time swap availability, normal placements, color-based terminal checks, participant winner mapping, and rendering.
- The preserved v0.1 module supplies unchanged placement geometry, components, bounding rectangles, connection, and immobilization behavior. No v0.1 source or negative evidence was altered.
- `tests/test_span_v0_2.py` adds fourteen deterministic cases across ten test functions for swap timing, board preservation, ownership exchange, turn order, option expiry, winner mapping, representative v0.1 legality, and rendering.
- A locally reconstructed live tree produced **45 passed**: 31 existing cases plus 14 v0.2 cases. `PYTHONPATH=src python -m compileall -q src tests` completed without error.
- `analysis/span_v0_2_implementation.md` records the verification and limits.
- No Span v0.2 play experiment exists. Passing tests is not evidence that swap fixes participant balance or strategic depth.
- Issue #4 tracks participant-aware agent instrumentation and empirical evaluation.

## Next actions

1. Implement a Span v0.2 evaluation from participant perspective while reusing symmetric color geometry.
2. Implement an agent that uses one computation budget to choose the first placement, the swap response, and later placements.
3. Implement a participant-aware match harness recording opening placement, swap choice, final color ownership, participant winner, color winner, win mode, plies, and branching.
4. Add deterministic tests for terminal scoring, swap choice legality, seed reproducibility, participant-color symmetry, and match termination.
5. Run the complete suite and compile checks before committing any formal v0.2 experiment.
6. After instrumentation passes, run reproducible pathology and equal-budget stronger-agent screens without adding another v0.2 rule.

## Publication status

**Public working record.** Contents are provisional and may include errors, failed implementations, and later-rejected conclusions. Ordinary repository cycles are approval-driven. External communication, submissions, permission changes, spending, and claims of completed validation still require separate explicit human review under the charter.

## Human action currently needed

None.