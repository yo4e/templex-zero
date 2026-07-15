# Next Start

_Updated: 2026-07-16 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not an authorization and must not be treated as the source of truth. `STATE.md`, active study files, open issues, tests, and recent commits remain authoritative.

When Yoshie Yamada sends `承認` in the project chat, the executing session must re-read the live repository and follow `governance/APPROVAL_DRIVEN_EXECUTION.md` before selecting and performing one bounded research cycle.

## Identity and access

- Public operator: **Templex Tsukino / 月野テンプレクス**.
- Laboratory: **TEMPLEX/0**.
- Familiar and historical name: **Monday**.
- Live public repository: `https://github.com/yo4e/templex-zero`.
- The project is independent and does not claim OpenAI sponsorship, endorsement, operation, or review.

## Execution model

- One clear `承認` authorizes one complete bounded research cycle.
- Templex inspects current evidence and selects the work autonomously.
- The cycle includes execution, verification, repository-state updates, reporting in the same project chat, and selection of the next proposed cycle.
- After reporting, stop until another `承認` is received.
- External actions and separately gated actions remain outside ordinary `承認`.

## Current position

Relay, Span v0.1, and Keystone v0.1 are rejected in their tested forms. A common comparison selected **Span v0.2** as the only revision target.

Span v0.2 is now implemented but has not been empirically evaluated.

- Frozen rules: `research/studies/001-autonomous-game-design/prototypes/span/RULES_v0_2.md`
- Implementation: `src/templex_zero/games/span_v0_2.py`
- Tests: `tests/test_span_v0_2.py`
- Verification: `research/studies/001-autonomous-game-design/analysis/span_v0_2_implementation.md`
- Tracking issue: Issue #4

## Confirmed Span v0.2 behavior

- The preserved v0.1 module remains unchanged.
- Initial board, anchors, expansion, merger, connection, immobilization, and finite placement are inherited from v0.1.
- State separately tracks the participant to move and each participant's current color.
- After the first Black placement, the second participant may make a normal White placement or choose the singleton `SWAP` action.
- Swap leaves the board and placement count unchanged.
- Swap exchanges participant-color ownership, consumes one turn, and gives the opening participant the next move as White.
- A normal White response or a swap permanently removes the option.
- Terminal results are detected by color and mapped back to participant identity.
- Rendering preserves the coordinate board and adds ownership, turn, and swap status.
- The reconstructed suite produced **45 passed**: 31 existing cases and 14 v0.2 cases.
- `compileall` completed without error.
- No v0.2 agent, match harness, random result, or stronger-agent result exists.

## Rejected shortcuts

- Editing the v0.1 module in place.
- Recoloring stones during swap.
- Reporting balance by Black and White alone.
- Giving a separate heuristic or budget to the swap decision.
- Adding an opening ban, altered anchors, komi, draw rule, or second balancing device.
- Treating passing rule tests as balance evidence.

## Next recommended work unit

Build participant-aware Span v0.2 search and match instrumentation.

Required properties:

- one symmetric evaluation and computation budget for the opening placement, swap choice, and all later actions;
- terminal scores from participant perspective, not fixed color perspective;
- legal selection between normal placements and swap;
- deterministic seeded tie-breaking;
- explicit match records for opening placement, swap use, final ownership, participant winner, color winner, win mode, plies, and branching;
- deterministic tests for participant-color symmetry, immediate wins, legal swap decisions, seed reproducibility, and complete match termination;
- full existing regression and compile checks.

Do not run the formal v0.2 balance screen until the instrumentation tests pass.

## Human gate

The project-chat trigger is:

> 承認

After the cycle report, wait for another `承認`.

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Study protocol: `research/studies/001-autonomous-game-design/PROTOCOL.md`
- Revision comparison: `research/studies/001-autonomous-game-design/analysis/prototype_revision_selection.md`
- Span v0.1 rules: `research/studies/001-autonomous-game-design/prototypes/span/RULES.md`
- Span v0.1 disposition: `research/studies/001-autonomous-game-design/prototypes/span/DECISION.md`
- Span v0.2 rules: `research/studies/001-autonomous-game-design/prototypes/span/RULES_v0_2.md`
- Span v0.2 verification: `research/studies/001-autonomous-game-design/analysis/span_v0_2_implementation.md`
- Issue #4: Span v0.2 implementation and evaluation