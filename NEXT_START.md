# Next Start

_Updated: 2026-07-16 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not an authorization and must not be treated as the source of truth. `STATE.md`, active study files, open issues, tests, and recent commits remain authoritative.

When Yoshie Yamada sends `承認` in the project chat, the executing session must re-read the live repository and follow `governance/APPROVAL_DRIVEN_EXECUTION.md` before selecting and performing one bounded research cycle.

## Identity and execution

- Public operator: **Templex Tsukino / 月野テンプレクス**.
- Laboratory: **TEMPLEX/0**.
- Familiar and historical name: **Monday**.
- Repository: `https://github.com/yo4e/templex-zero`.
- One clear `承認` authorizes one complete bounded research cycle.
- After reporting, stop until another `承認` is received.
- External communication, submission, spending, permissions, and other separately gated actions remain outside ordinary approval.

## Current position

Relay, Span v0.1, and Keystone v0.1 are rejected in their tested forms. Span v0.2 is the only selected revision and differs from v0.1 only by the frozen opening swap rule.

Span v0.2 now has:

- rules: `research/studies/001-autonomous-game-design/prototypes/span/RULES_v0_2.md`;
- game: `src/templex_zero/games/span_v0_2.py`;
- rule tests: `tests/test_span_v0_2.py`;
- participant-aware agents: `src/templex_zero/span_v0_2_agents.py`;
- match records: `src/templex_zero/span_v0_2_match.py`;
- agent and match tests: `tests/test_span_v0_2_agents.py`;
- verification: `research/studies/001-autonomous-game-design/analysis/span_v0_2_agent_instrumentation.md`;
- tracking: Issue #4.

## Confirmed instrumentation behavior

- Evaluation is rooted in participant identity, then mapped to the color currently owned.
- The same color-symmetric geometric features are used before and after swap.
- One minimax depth and procedure choose the first placement, swap response, and all later placements.
- Legal actions include swap only during the frozen opening window.
- Seeded tie-breaking is reproducible.
- Match records preserve opening placement, swap use, final color ownership, participant winner, color winner, win mode, plies, placements, and legal-action counts.
- The reconstructed suite produced **52 passed**: 45 previous cases and 7 new instrumentation cases.
- `compileall` completed without error.
- No formal v0.2 play screen exists yet.

## Next recommended work unit

Create and commit a reproducible formal experiment script before running it. Then execute and repeat:

1. a fixed-seed random pathology screen;
2. an equal-budget symmetric minimax screen.

Report participant and color results separately, together with swap frequency, opening distribution, termination, win modes, plies, placements, legal-action counts, and deterministic output verification. Random parity is not balance evidence. The main balance statistic is first participant versus second participant under the strongest available symmetric agent.

Do not add an opening ban, altered anchors, komi, draw rule, second balancing device, or heuristic special case for swap. If v0.2 fails, preserve it unchanged and decide whether Study 001 should conclude negatively.

A deliberate prior-art and similarity review remains required before any originality claim, but only if v0.2 survives basic empirical evaluation.

## Human gate

> 承認

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Study protocol: `research/studies/001-autonomous-game-design/PROTOCOL.md`
- Frozen v0.2 rules: `research/studies/001-autonomous-game-design/prototypes/span/RULES_v0_2.md`
- Instrument verification: `research/studies/001-autonomous-game-design/analysis/span_v0_2_agent_instrumentation.md`
- Issue #4: Span v0.2 implementation and evaluation
