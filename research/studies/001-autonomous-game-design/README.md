# Study 001 — Autonomous Game Design

## Research question

Can Monday independently design a compact, deterministic, two-player abstract strategy game whose rules are teachable in under three minutes and whose automated play provides evidence of nontrivial strategy and reasonable balance?

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

**Mechanism generation.** No favored game concept has yet been adopted.

## Files to be added

- `PROTOCOL.md` — evaluation plan and thresholds
- `candidates/` — candidate mechanisms and rejection notes
- `src/` — game and agent implementations
- `experiments/` — reproducible runs and data
- `analysis/` — interpretation and critique
- `RULES.md` — rules of the surviving design
- `REPORT.md` — final research report
