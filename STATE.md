# State

_Last updated: 2026-07-16_

## Phase

**Study 001 / negative conclusion and final report synthesis**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**.
- The repository is public at `yo4e/templex-zero` and operates under `governance/APPROVAL_DRIVEN_EXECUTION.md`.
- Relay is rejected after stronger symmetric play exposed severe first-player advantage and a substantial 200-ply unresolved population.
- Span v0.1 is frozen and rejected after exhaustive reply enumeration proved a five-ply Black forced connection through C2–C3–C4 or its reflection.
- Keystone v0.1 is frozen and rejected after only 50.9% of 2,000 fixed-seed random games completed by 200 plies.
- Span v0.2 is frozen and rejected after a formal equal-budget screen and exhaustive opening diagnosis proved a second-participant forced win after every legal first placement.
- `experiments/span_v0_2_formal_screen.py` was committed before execution at `edac024671aeb380472e0a6a58a8eb35a134e124`.
- The configured run used 10,000 random games and 1,000 depth-3 symmetric minimax games, then repeated the complete run.
- Both outputs were byte-identical with SHA-256 `93f55d3c5e9cacf86aec7bbecdf351fc661f2f5ecbfdefb1f7e05c08482e56d2`.
- Random play completed all games and appeared near-even by participant: 5,198 first-participant wins and 4,802 second-participant wins. This remains pathology evidence only.
- Symmetric depth-3 play produced 0 first-participant wins and 1,000 second-participant wins. Every game ended by White connection after six placements; no game used swap.
- The exhaustive regression covers all six legal openings. C2/C4 lose after swap to the known Black central line; B1/B5/D1/D5 lose to White B3–C3–D3 or its reflection.
- Formal data: `data/span_v0_2_formal.json`.
- Analysis: `analysis/span_v0_2_formal.md`.
- Disposition: `prototypes/span/DECISION_v0_2.md`.
- All selected prototypes and the one reasonable single-change revision have failed decisive protocol criteria.
- Study 001 therefore has a negative research conclusion. No surviving game supports the target claim.
- Strategic-signal tournaments and prior-art review for Span v0.2 are cancelled because the forced participant win is already decisive.
- The new exhaustive test passed in a local reconstruction. The previous 52-case full suite had passed before this cycle; no game or agent source changed during the formal screen. The repository has no GitHub Actions workflow.

## Next actions

1. Write `research/studies/001-autonomous-game-design/REPORT.md` as the final synthesis.
2. Separate direct evidence, bounded inference, unresolved human qualities, and methodological lessons.
3. Summarize why random parity repeatedly concealed decisive structural defects.
4. State clearly that Study 001 did not produce a viable game, while preserving the value of its reproducible falsification process.
5. Close the study without creating Span v0.3 or another unplanned prototype inside the same protocol.
6. After the report, decide whether a separately scoped Study 002 is justified; do not treat it as an automatic continuation.

## Publication status

**Public working record.** Contents are provisional until the final report is synthesized. External communication, submissions, permission changes, spending, and claims of completed validation remain separately gated.

## Human action currently needed

None.
