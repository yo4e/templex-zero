# State

_Last updated: 2026-07-15_

## Phase

**Study 001 / Span implementation**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**. Monday remains a familiar and historical name whose OpenAI-personality origin is disclosed in `README.md` and `self/SELF.md`.
- Repository visibility was changed to public by human action on 2026-07-15. The live repository is now an auditable but provisional research record.
- Public visibility enables read-only scheduled planning from current repository evidence. Repository-changing sessions remain bounded by the current human approval bridge.
- The Python project and import package were renamed from `monday-zero` / `monday_zero` to `templex-zero` / `templex_zero`; the original names remain visible in Git history.
- Twenty research programs were generated; Study 001 was selected at 93/100.
- Twelve game mechanisms were generated; Relay, Span, and Keystone were selected for prototyping.
- Relay was implemented and rejected: random play appeared balanced, but depth-2 symmetric play produced 129 Player 0 wins, 12 Player 1 wins, and 59 draws in 200 games.
- Random-vs-random play is now treated only as a termination and gross-pathology screen.
- Span v0.1 rules were frozen before implementation or results in `research/studies/001-autonomous-game-design/prototypes/span/RULES.md`.
- Span uses a 5×5 board, four fixed midpoint anchors, orthogonal components, bounding-rectangle expansion or component-merging placements, connection victory, and immobilization loss.

## Next actions

1. Implement Span v0.1 exactly as frozen: legal moves, terminal conditions, and rendering.
2. Add deterministic tests for expansion, merging, illegal interior filling, connection wins, and immobilization.
3. Run random termination/pathology screening.
4. Run at least one stronger symmetric-agent balance screen.
5. Reject, version for revision, or advance Span using the precommitted protocol.

## Publication status

**Public working record.** Contents are provisional and may include errors, failed implementations, and later-rejected conclusions. Repository-changing sessions remain approval-gated. External communication, submissions, and claims of completed validation still require separate human review under the charter.

## Human action currently needed

Rename the GitHub repository slug from `monday-zero` to `templex-zero` when convenient; the connected tool can edit repository contents but cannot change repository settings. Until then, scheduled planning must continue using the current public URL.
