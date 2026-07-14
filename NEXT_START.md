# Next Start

_Updated: 2026-07-15 (Asia/Tokyo)_

## Purpose

This is a compact bridge from a GitHub-aware execution session to a GitHub-blind planning session. It is **not** the source of truth. After human approval, the executing session must re-read the repository and prefer current evidence over this snapshot.

## Current position

Study 001 is comparing three candidate abstract-game mechanisms. Relay has been rejected in its current form. Span v0.1 rules are now frozen before implementation or play results. Issue #1 remains open.

## Confirmed

- The repository is private; publication remains blocked pending human review.
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

## Unresolved

- Whether Span v0.1 is implemented correctly and unambiguously.
- Span's termination profile, first-player advantage, branching behavior, and response to stronger play.
- Whether immobilization or connection dominates actual play.
- Keystone remains unimplemented and should not begin before Span receives a documented disposition.

## Next recommended work unit

Implement Span v0.1 exactly as frozen in the shared Python framework, including legal moves, terminal conditions, and a readable board renderer. Add deterministic tests covering expansion, merging, illegal interior filling, connection victory, and immobilization. Do not run broad balance experiments until the implementation passes those tests.

This is an internal research work unit. It does not authorize publication, external communication, third-party repository changes, spending, contracts, permission changes, credential exposure, unlawful action, or harmful action.

## Human gate

The planning report may ask for the single-word approval token: `承認`.

That approval authorizes only the bounded internal work unit described in the report. The executing session must inspect the live repository before acting and may narrow or revise the plan if the repository has changed.

## Anchors

- `STATE.md` updated on 2026-07-15; content SHA `9a954e3ea8a0ae998f3d074f549f9f58148991b9`
- Span v0.1 rules commit: `418bdc92c7e32637c2b35648cfc7a79b4a3b444c`
- Issue #1: `Study 001: Implement and evaluate Span`
