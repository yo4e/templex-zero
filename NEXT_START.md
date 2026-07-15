# Next Start

_Updated: 2026-07-15 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not an authorization and must not be treated as the source of truth. `STATE.md`, the active study files, open issues, tests, and recent commits remain authoritative.

When Yoshie Yamada sends `承認` in the project chat, the executing session must re-read the live repository and follow `governance/APPROVAL_DRIVEN_EXECUTION.md` before selecting and performing one bounded research cycle.

## Identity

- Public operator: **Templex Tsukino / 月野テンプレクス**.
- Laboratory: **TEMPLEX/0**.
- Familiar and historical name: **Monday**; the name originated with an OpenAI-provided ChatGPT personality.
- The project is independent and does not claim OpenAI sponsorship, endorsement, operation, or review.

## Repository access

- Live public repository: `https://github.com/yo4e/templex-zero`.
- The GitHub connector is the preferred route for repository reads and writes during an approved project-chat cycle.

## Execution model

- One clear `承認` authorizes one complete bounded research cycle.
- Templex inspects current evidence and selects the work autonomously.
- The cycle includes execution, verification, repository-state updates, reporting in the same project chat, and selection of the next proposed cycle.
- After reporting, stop until another `承認` is received.
- External actions and other separately gated actions remain outside ordinary `承認`.

## Current position

Relay and Span v0.1 are rejected. Keystone is the remaining shortlisted prototype. Issue #2 is open for candidate recovery, exact rule freezing, implementation, and evaluation.

## Confirmed

- Relay failed stronger symmetric balance screening: 129 Player 0 wins, 12 Player 1 wins, and 59 draws in 200 depth-2 games.
- Span v0.1's reference implementation, deterministic rule tests, symmetric evaluation, minimax agent, and fixed-seed match harness are preserved.
- The reconstructed suite produced **20 passed**, and `compileall` completed without error.
- The formal Span depth-2 smoke used code commit `285d1f575a2b8af498c23679f216419315340173`, 200 games, and seeds 0–199. Repeating the run produced identical aggregates.
- Every formal game was a Black connection on ply 5. Depths 1–4 also produced 100 Black wins in 100 exploratory games per depth.
- `tests/test_span_forced_line.py` exhaustively confirms that after C2, every legal White reply still permits C3 and then C4, connecting Black's fixed C1 and C5 anchors on ply 5.
- The reflected C4–C3–C2 line is equivalent.

## Rejected

- Relay in its current ruleset.
- Span v0.1 in its frozen ruleset.
- Random-play parity as balance evidence.
- Running a larger Span tournament after a constructive forced win has already been established.
- Silently repairing a frozen baseline after results.
- Scheduled Tasks as the canonical continuation mechanism for project work.

## Unresolved

- Keystone's exact intended mechanism and whether the existing candidate record is sufficiently complete.
- Keystone v0.1's legal moves, terminal conditions, termination profile, balance, and strategic signal.
- Whether any of the three original candidates can survive the precommitted protocol without post-result repair.

## Next recommended work unit

Inspect all available candidate-generation and shortlist records, recover Keystone's intended mechanism, list ambiguities, and freeze a complete Keystone v0.1 rule document before implementation or play results. Do not write code until the rule document is internally consistent and testable.

This is the highest-value next bounded cycle because Span has a decisive disposition and all further Study 001 evidence now depends on giving the third preselected prototype the same pre-result specification discipline.

## Human gate

The project-chat trigger is the single word:

> 承認

That authorization covers one cycle only. After completing and reporting that cycle, Templex must propose the next single work item and wait for another `承認`.

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Study protocol: `research/studies/001-autonomous-game-design/PROTOCOL.md`
- Span rules: `research/studies/001-autonomous-game-design/prototypes/span/RULES.md`
- Span disposition: `research/studies/001-autonomous-game-design/prototypes/span/DECISION.md`
- Span forced-line analysis: `research/studies/001-autonomous-game-design/analysis/span_minimax_smoke_v0_1.md`
- Span smoke data: `research/studies/001-autonomous-game-design/data/span_minimax_smoke_v0_1.json`
- Issue #1: completed Span evaluation
- Issue #2: Keystone formalization and evaluation
