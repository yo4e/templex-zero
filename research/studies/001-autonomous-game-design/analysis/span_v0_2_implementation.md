# Span v0.2 Implementation Verification

_Date: 2026-07-16 (Asia/Tokyo)_

## Scope

This record verifies implementation fidelity for the frozen single-change Span v0.2 rules. It does not evaluate balance, strategy, fun, teachability, or originality.

## Implementation

- Module: `src/templex_zero/games/span_v0_2.py`
- Preserved baseline: `src/templex_zero/games/span.py`
- Frozen rules: `prototypes/span/RULES_v0_2.md`
- Deterministic tests: `tests/test_span_v0_2.py`

The v0.1 implementation remains unchanged. v0.2 delegates normal placement geometry, components, bounding rectangles, expansion, merger, and color connection to the preserved v0.1 module.

The v0.2 state separately records:

- the board, whose cells remain Black, White, or empty;
- the participant whose turn it is;
- the color owned by each participant;
- whether the one-time swap is currently available;
- elapsed turns, including a swap;
- completed placements, excluding a swap.

A normal action contains a destination. The singleton `SWAP` action contains no destination. Swapping leaves the board and placement count unchanged, exchanges participant-color ownership, consumes one turn, transfers the next move to the opening participant as White, and permanently removes the swap option.

Terminal connection and immobilization are determined by color and then mapped back to participant identity.

## Deterministic verification

The new test file exercises fourteen cases across ten test functions:

- unchanged initial anchors and Black legal placements;
- swap availability only after the first Black placement;
- board preservation under swap;
- participant-color ownership exchange;
- the opening participant moving next as White;
- a normal White response expiring the option;
- no initial or repeated swap;
- a no-swap path matching v0.1 state transitions;
- connection and immobilization winners mapped through swapped ownership;
- representative expansion, interior-fill, merger, unsupported-placement, and White-placement legality;
- coordinate rendering with explicit participant ownership and swap status.

A locally reconstructed tree using the live repository sources produced:

- `PYTHONPATH=src python -m pytest -q` — **45 passed**;
- `PYTHONPATH=src python -m compileall -q src tests` — completed without error.

The 45 cases comprise the existing 31 Relay, Span v0.1, and Keystone cases plus 14 Span v0.2 cases. No existing source or test file was modified for the implementation.

## Result

The tested implementation matches the frozen swap timing, board invariance, ownership exchange, turn order, one-time availability, participant result mapping, and preserved v0.1 placement rules.

## Limitations

- The tests are not an exhaustive state-space proof.
- The implementation reuses private v0.1 helpers to guarantee rule identity; a later public API cleanup must not precede empirical disposition.
- No v0.2 agent, match harness, random screen, or stronger-agent result exists yet.
- Passing tests does not show that the swap rule fixes balance. It may overcompensate or merely move the forced advantage from color to participant.
- Verification used a local reconstruction of live GitHub files. No GitHub Actions workflow exists.

## Decision

Preserve the frozen rules and implementation unchanged. Advance to participant-aware search and match instrumentation. Do not run the formal balance screen until the same symmetric agent and budget can select the first placement, decide whether to swap, and choose all later placements.