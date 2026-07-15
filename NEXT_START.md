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

Relay and Span v0.1 are rejected. Keystone v0.1 is the third and final originally shortlisted prototype. Its rules were frozen before implementation or play results. The reference implementation and deterministic tests now pass; Issue #2 remains open for empirical screening and disposition.

## Confirmed

- `prototypes/keystone/ORIGIN.md` records the recovered candidate and pre-result ambiguity decisions.
- `prototypes/keystone/RULES.md` is the frozen v0.1 baseline.
- `src/templex_zero/games/keystone.py` implements immutable state, placement, one-step orthogonal shifts, mandatory single capture choice, victory, no-action loss, repetition history, and rendering.
- Capture choice is encoded in the action. If multiple brackets are available, exactly one capture-bearing action must be chosen; no no-capture action is legal.
- A complete repetition key contains the board, both reserve counts, and player to move.
- `tests/test_keystone.py` contains eleven deterministic tests.
- The reconstructed full suite produced **31 passed**, including the twenty existing Relay and Span tests; `compileall` completed without error.
- No Keystone random or stronger-agent result exists yet.

## Rejected

- Relay in its current ruleset.
- Span v0.1 in its frozen ruleset.
- Random-play parity as balance evidence.
- Silently repairing a frozen baseline after results.
- Scheduled Tasks as the canonical continuation mechanism for project work.

## Unresolved

- Natural Keystone termination rate within 200 plies.
- Frequency of structural victories, threefold repetition, and observation-limit hits.
- Whether placement or shifting dominates ordinary play.
- Capture frequency, branching, reserve exhaustion, and typical duration.
- First-player advantage under competent symmetric play.
- Teachability, fun, elegance, and originality.

## Next recommended work unit

Create a reproducible Keystone random pathology script and run a fixed seeded sample. Record natural victory, repetition draws, 200-ply limit hits, plies, Black/White results, captures, placements versus shifts, reserve use, and legal-action counts. Repeat the configured run to confirm deterministic aggregate output. Save the code version, data, and interpretation.

Treat random results only as termination and gross-pathology evidence. Do not tune the frozen rules or claim balance from random win rates.

## Human gate

The project-chat trigger is the single word:

> 承認

That authorization covers one cycle only. After completing and reporting that cycle, Templex must propose the next single work item and wait for another `承認`.

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Study protocol: `research/studies/001-autonomous-game-design/PROTOCOL.md`
- Keystone origin: `research/studies/001-autonomous-game-design/prototypes/keystone/ORIGIN.md`
- Keystone rules: `research/studies/001-autonomous-game-design/prototypes/keystone/RULES.md`
- Keystone implementation: `src/templex_zero/games/keystone.py`
- Keystone tests: `tests/test_keystone.py`
- Implementation verification: `research/studies/001-autonomous-game-design/analysis/keystone_implementation_v0_1.md`
- Issue #2: Keystone implementation and evaluation
