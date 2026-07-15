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
- Early commits retain **MONDAY/0** and `monday_zero` as historical evidence. Current Python imports use `templex_zero`.

## Repository access

- Live public repository: `https://github.com/yo4e/templex-zero`.
- The GitHub connector is the preferred route for repository reads and writes during an approved project-chat cycle.
- The former slug `monday-zero` is historical and may redirect.

## Execution model

- One clear `承認` authorizes one complete bounded research cycle.
- Templex inspects current evidence and selects the work autonomously; Yoshie Yamada does not ordinarily choose the item in advance.
- The cycle includes execution, verification, repository-state updates, reporting in the same project chat, and selection of the next proposed cycle.
- After reporting, stop until another `承認` is received.
- Yoshie Yamada may stop, correct, constrain, or require reconsideration at any time.
- External actions and other separately gated actions remain outside ordinary `承認`.

## Current position

Study 001 is comparing three candidate abstract-game mechanisms. Relay has been rejected in its current form. Span v0.1 rules are frozen before implementation or play results. Issue #1 remains open.

## Confirmed

- Relay appeared balanced under random play but showed a severe first-player advantage under depth-2 symmetric play: 129–12 with 59 draws in 200 games.
- Random-vs-random play is useful only for termination and gross-pathology screening, not as evidence of strategic balance.
- Span v0.1 uses a 5×5 board with fixed midpoint anchors: Black at C1/C5 and White at A3/E3.
- A Span placement must either expand the pre-move bounding rectangle of one friendly orthogonal component or merge at least two friendly components.
- Connection across the assigned opposite edges wins; beginning a turn without a legal placement loses.
- The frozen baseline is `research/studies/001-autonomous-game-design/prototypes/span/RULES.md` and must not be silently rewritten after results.

## Rejected

- Relay in its current ruleset.
- Random-play parity as sufficient balance evidence.
- Retrofitting Span's baseline rules in response to results without creating a new version.
- Scheduled Tasks as the canonical continuation mechanism for project work: test results were generated outside the project chat and could not reliably use the project as a continuous execution context.

## Unresolved

- Whether Span v0.1 is implemented correctly and unambiguously.
- Span's termination profile, first-player advantage, branching behavior, and response to stronger play.
- Whether immobilization or connection dominates actual play.
- Keystone remains unimplemented and should not begin before Span receives a documented disposition.

## Next recommended work unit

Implement Span v0.1 exactly as frozen in the shared Python framework under `src/templex_zero/`, including legal moves, terminal conditions, and a readable board renderer. Add deterministic tests covering expansion, merging, illegal interior filling, connection victory, and immobilization. Do not run broad balance experiments until the implementation passes those tests.

This is the highest-value next bounded cycle because all later Span evidence depends on implementation fidelity. The executing session must inspect the live repository before acting and may safely narrow or revise the work if current evidence has changed.

## Human gate

The project-chat trigger is the single word:

> 承認

That authorization covers one cycle only. After completing and reporting that cycle, Templex must propose the next single work item and wait for another `承認`.

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- `STATE.md` updated on 2026-07-15; current content must be re-read live.
- Span v0.1 rules commit: `418bdc92c7e32637c2b35648cfc7a79b4a3b444c`
- Issue #1: `Study 001: Implement and evaluate Span`
