# State

_Last updated: 2026-07-16_

## Phase

**Study 001 / Span v0.2 implementation**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**.
- The repository is public at `yo4e/templex-zero` and operates under `governance/APPROVAL_DRIVEN_EXECUTION.md`.
- Relay is rejected after stronger symmetric play exposed severe first-player advantage and a substantial 200-ply unresolved population.
- Span v0.1 is frozen and rejected after exhaustive reply enumeration proved a five-ply Black forced connection through C2–C3–C4 or its reflection.
- Keystone v0.1 is frozen and rejected after only 50.9% of 2,000 fixed-seed random games completed by 200 plies.
- `analysis/prototype_revision_selection.md` compares evidence strength, rule failure, repair cost, and mechanism preservation for all three prototypes.
- Span is the only selected revision target. Relay would require separate initiative and cycling repairs; Keystone would require restricting its defining movement phase or adding a new progress system.
- `prototypes/span/RULES_v0_2.md` freezes Span v0.2 before implementation or new play results.
- v0.2 differs from v0.1 only by an opening swap option after the first Black placement.
- The swap exchanges participant ownership of colors, goals, and existing stones without changing the board. It consumes the second participant's turn; the opening participant then moves as White.
- Fixed anchors, expansion and merge legality, connection, immobilization, and finite placement remain unchanged.
- The v0.2 core rules contain 308 words. No v0.2 code or play evidence exists yet.
- Issue #3 records the completed comparison. A new implementation issue tracks Span v0.2.

## Next actions

1. Implement participant identity, color ownership, swap availability, and the swap action while preserving all v0.1 placement rules.
2. Add deterministic tests for swap timing, board preservation, ownership exchange, one-time availability, post-swap turn order, and unchanged normal legality.
3. Run the complete existing test suite and compile checks.
4. After implementation fidelity is established, adapt symmetric search so the same agent decides both opening placement and swap under equal budgets.
5. Evaluate participant balance, color results, swap frequency, opening distribution, termination, and strategic signal without adding another v0.2 rule.

## Publication status

**Public working record.** Contents are provisional and may include errors, failed implementations, and later-rejected conclusions. Ordinary repository cycles are approval-driven. External communication, submissions, permission changes, spending, and claims of completed validation still require separate explicit human review under the charter.

## Human action currently needed

None.
