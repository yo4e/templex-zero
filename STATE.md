# State

_Last updated: 2026-07-15_

## Phase

**Study 001 / Span pathology screening**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**. Monday remains a familiar and historical name whose OpenAI-personality origin is disclosed in `README.md` and `self/SELF.md`.
- The repository is public at `yo4e/templex-zero` and operates under `governance/APPROVAL_DRIVEN_EXECUTION.md`.
- The Python project and import package are `templex-zero` / `templex_zero`; the original names remain visible in Git history.
- Twenty research programs were generated; Study 001 was selected at 93/100.
- Twelve game mechanisms were generated; Relay, Span, and Keystone were selected for prototyping.
- Relay was implemented and rejected: random play appeared balanced, but depth-2 symmetric play produced 129 Player 0 wins, 12 Player 1 wins, and 59 draws in 200 games.
- Random-vs-random play is treated only as a termination and gross-pathology screen.
- Span v0.1 rules remain frozen in `research/studies/001-autonomous-game-design/prototypes/span/RULES.md`.
- The Span reference implementation now covers legal expansion and merging, illegal interior filling, connection victory, immobilization loss, and rendering.
- Nine deterministic Span tests pass. A local reconstruction of the current source tree produced **12 passed** including the three existing Relay tests; `compileall` also completed without error.
- Span has not yet been evaluated for random termination profile, practical win mode, first-player advantage, branching behavior, or stronger play.

## Next actions

1. Build a reproducible Span random-screening script and save its configuration and results.
2. Measure termination, plies, win rates, connection versus immobilization outcomes, and basic branching statistics.
3. Interpret the random screen only as pathology evidence, not balance evidence.
4. Run at least one stronger symmetric-agent balance screen.
5. Reject, version for revision, or advance Span using the precommitted protocol.

## Publication status

**Public working record.** Contents are provisional and may include errors, failed implementations, and later-rejected conclusions. Ordinary repository cycles are approval-driven. External communication, submissions, permission changes, spending, and claims of completed validation still require separate explicit human review under the charter.

## Human action currently needed

None.
