# Study 001 — Autonomous Game Design

## Research question

Can Templex Tsukino independently design a compact, deterministic, two-player abstract strategy game whose rules are teachable in under three minutes and whose automated play provides evidence of nontrivial strategy and reasonable balance?

This is the same study selected under the earlier internal name Monday. The public identity change does not alter the protocol, thresholds, or prior results.

## Intended artifact

A complete game package containing:

- concise rules;
- a reference implementation;
- command-line play;
- reproducible simulation and evaluation tools;
- baseline agents of differing strength;
- experiment data and analysis;
- a record of rejected prototypes and revisions;
- later, if justified, a small browser interface.

## Constraints

- Two players.
- Deterministic and perfect information.
- No dependence on proprietary assets or external services.
- Core rules should fit within 400 words.
- A physical version should require at most a small board and a modest set of generic pieces, or be playable with pencil and paper.
- The design must not knowingly duplicate an existing game; claims will remain qualified until a deliberate similarity search occurs.

## Current phase

**Prototype comparison / Keystone specification.** Relay and Span v0.1 have both been rejected in their tested forms. Keystone is the remaining shortlisted prototype and must receive a frozen rule specification before implementation or play results.

## Prototype outcomes

### Relay — rejected

Stronger symmetric play exposed a severe first-player advantage: 129 Player 0 wins, 12 Player 1 wins, and 59 draws in 200 depth-2 games.

### Span v0.1 — rejected

- [`prototypes/span/RULES.md`](prototypes/span/RULES.md) — frozen baseline
- [`prototypes/span/DECISION.md`](prototypes/span/DECISION.md) — disposition
- [`../../../src/templex_zero/games/span.py`](../../../src/templex_zero/games/span.py) — reference implementation
- [`../../../src/templex_zero/span_agents.py`](../../../src/templex_zero/span_agents.py) — symmetric search agent
- [`../../../tests/test_span_forced_line.py`](../../../tests/test_span_forced_line.py) — exhaustive five-ply forced-line evidence
- [`../../../experiments/span_minimax_smoke.py`](../../../experiments/span_minimax_smoke.py) — reproducible smoke screen
- [`data/span_minimax_smoke_v0_1.json`](data/span_minimax_smoke_v0_1.json) — aggregate evidence
- [`analysis/span_minimax_smoke_v0_1.md`](analysis/span_minimax_smoke_v0_1.md) — diagnosis and limitations

Black can force C2–C3–C4, or the reflected C4–C3–C2 line, to connect the fixed C1 and C5 anchors on ply 5. The frozen v0.1 rules remain preserved rather than repaired after the result.

### Keystone — next

Issue #2 tracks recovery of the candidate description, ambiguity resolution, frozen v0.1 rules, implementation, and evaluation. Span should not be rescued before Keystone receives its first documented disposition.

## Planned study files

- `PROTOCOL.md` — evaluation plan and thresholds
- `candidates/` — candidate mechanisms and rejection notes
- `prototypes/` — versioned rules for implemented candidates
- `src/templex_zero/` — game and agent implementations
- `experiments/` — reproducible runs and data
- `analysis/` — interpretation and critique
- `RULES.md` — rules of the surviving design
- `REPORT.md` — final research report
