# Study 001 — Autonomous Game Design

## Research question

Can Templex Tsukino independently design a compact, deterministic, two-player abstract strategy game whose rules are teachable in under three minutes and whose automated play provides evidence of nontrivial strategy and reasonable balance?

This is the same study selected under the earlier internal name Monday. The public identity change does not alter the protocol, thresholds, or prior results.

## Intended artifact

A complete game package containing concise rules, a reference implementation, command-line play, reproducible evaluation tools, agents of differing strength, experiment data and analysis, and a record of rejected prototypes and revisions.

## Constraints

- Two players, deterministic, perfect information.
- No proprietary assets or external services.
- Core rules at or below 400 words.
- Small generic physical equipment or pencil-and-paper play.
- No originality claim before deliberate prior-art review.

## Current phase

**Span v0.2 empirical screening.** Relay, Span v0.1, and Keystone v0.1 are rejected in their tested forms. Span v0.2 is the only selected revision. Its participant-aware implementation, search agent, match recorder, and deterministic tests now pass; no formal v0.2 play screen has been run.

## Prototype outcomes

### Relay — rejected

Stronger symmetric play produced 129 first-player wins, 12 second-player wins, and 59 unresolved 200-ply games. One rule would not honestly repair both initiative and cycling symptoms.

### Span v0.1 — rejected

- [`prototypes/span/RULES.md`](prototypes/span/RULES.md) — frozen baseline
- [`prototypes/span/DECISION.md`](prototypes/span/DECISION.md) — disposition
- [`analysis/span_minimax_smoke_v0_1.md`](analysis/span_minimax_smoke_v0_1.md) — diagnosis

Exhaustive reply enumeration proves that Black can force C2–C3–C4, or the reflection, and connect on ply 5.

### Keystone v0.1 — rejected

- [`prototypes/keystone/RULES.md`](prototypes/keystone/RULES.md) — frozen baseline
- [`prototypes/keystone/DECISION.md`](prototypes/keystone/DECISION.md) — disposition
- [`analysis/keystone_random_v0_1.md`](analysis/keystone_random_v0_1.md) — diagnosis

Only 50.9% of 2,000 fixed-seed random games completed by 200 plies. The long population exhausted reserves and entered extended shifting play.

## Selected revision

### Span v0.2 — instrumented, not yet empirically evaluated

- [`analysis/prototype_revision_selection.md`](analysis/prototype_revision_selection.md) — revision selection
- [`prototypes/span/RULES_v0_2.md`](prototypes/span/RULES_v0_2.md) — frozen rules
- [`../../../src/templex_zero/games/span_v0_2.py`](../../../src/templex_zero/games/span_v0_2.py) — participant-aware game
- [`../../../tests/test_span_v0_2.py`](../../../tests/test_span_v0_2.py) — swap and rule regressions
- [`../../../src/templex_zero/span_v0_2_agents.py`](../../../src/templex_zero/span_v0_2_agents.py) — participant-aware agents
- [`../../../src/templex_zero/span_v0_2_match.py`](../../../src/templex_zero/span_v0_2_match.py) — match records
- [`../../../tests/test_span_v0_2_agents.py`](../../../tests/test_span_v0_2_agents.py) — agent and match tests
- [`analysis/span_v0_2_agent_instrumentation.md`](analysis/span_v0_2_agent_instrumentation.md) — verification and limits

v0.2 changes exactly one rule: after the first Black placement, the second participant may place White normally or swap sides. Swap exchanges participant ownership of colors and goals without changing the board.

The evaluation maps each participant to their currently owned color and uses the same color-symmetric geometry before and after swap. The same minimax depth and procedure choose the opening, swap response, and later placements. Match records retain participant and color results separately.

The locally reconstructed full suite produced **52 passed**: 45 previous cases plus 7 new instrumentation cases. `compileall` completed without error. This verifies the measurement tools only; balance, strategic signal, viable openings, and swap frequency remain unresolved.

## Next work

Commit a reproducible experiment script before execution, then run and repeat a fixed-seed random pathology screen and an equal-budget symmetric minimax screen. Report participant and color results, swap frequency, openings, termination, win modes, duration, and branching. Reject or advance the frozen version under the unchanged protocol.

If v0.2 survives basic empirical evaluation, perform a deliberate prior-art and similarity review before making an originality claim.

## Planned study files

- `PROTOCOL.md` — evaluation plan and thresholds
- `candidates/` — candidate mechanisms and rejection notes
- `prototypes/` — versioned rules and dispositions
- `src/templex_zero/` — implementations and agents
- `experiments/` — reproducible runs
- `data/` — machine-readable results
- `analysis/` — interpretation and critique
- `RULES.md` — rules of a surviving design, if any
- `REPORT.md` — final report
