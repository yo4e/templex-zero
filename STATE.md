# State

_Last updated: 2026-07-15_

## Phase

**Study 001 / Keystone specification**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**.
- The repository is public at `yo4e/templex-zero` and operates under `governance/APPROVAL_DRIVEN_EXECUTION.md`.
- Relay was rejected after depth-2 symmetric play produced 129 Player 0 wins, 12 Player 1 wins, and 59 draws in 200 games.
- Span v0.1 remains frozen and is now rejected. Its random screen terminated normally, but stronger instrumentation exposed a constructive first-player win.
- `src/templex_zero/span_agents.py` and `src/templex_zero/span_match.py` provide symmetric, fixed-seed search instrumentation.
- A reconstructed full suite produced **20 passed**; `compileall` completed without error.
- The formal depth-2 smoke ran 200 equal-agent games twice with identical aggregates using code commit `285d1f575a2b8af498c23679f216419315340173`.
- Black won all 200 games by connection on ply 5. Exploratory depths 1–4 produced the same result in 100 games per depth.
- Exhaustive reply enumeration proves that after C2, Black can always play C3 then C4 to connect the fixed C1 and C5 anchors on ply 5. C4–C3–C2 is the reflected equivalent.
- A larger Span balance tournament is cancelled because the forced line already violates the precommitted balance criterion.
- Issue #1 records Span's completed rejection. Issue #2 tracks Keystone, the remaining shortlisted prototype.

## Next actions

1. Locate the existing Keystone candidate description and record ambiguities.
2. Freeze exact Keystone v0.1 rules before implementation or play results.
3. Implement legal moves, terminal conditions, rendering, and deterministic tests.
4. Run random pathology and stronger symmetric-agent screens under the existing protocol.
5. Reject, version for revision, or advance Keystone using precommitted evidence.

## Publication status

**Public working record.** Contents are provisional and may include errors, failed implementations, and later-rejected conclusions. Ordinary repository cycles are approval-driven. External communication, submissions, permission changes, spending, and claims of completed validation still require separate explicit human review under the charter.

## Human action currently needed

None.
