# Next Start

_Updated: 2026-07-15 (Asia/Tokyo)_

## Purpose

This is a compact bridge from a GitHub-aware execution session to a GitHub-blind planning session. It is **not** the source of truth. After human approval, the executing session must re-read the repository and prefer current evidence over this snapshot.

## Current position

Study 001 is comparing three candidate abstract-game mechanisms. Relay has been implemented and rejected in its current form. Span is the next prototype. Issue #1 is open.

## Confirmed

- The repository is private; publication remains blocked pending human review.
- Relay appeared balanced under random play but showed a severe first-player advantage under depth-2 symmetric play: 129–12 with 59 draws in 200 games.
- Random-vs-random play is useful only for termination and gross-pathology screening, not as evidence of strategic balance.
- The next prototype must be evaluated with at least one stronger symmetric-agent screen.

## Rejected

- Relay in its current ruleset.
- Random-play parity as sufficient balance evidence.

## Unresolved

- Span's exact rules have not yet been frozen.
- Span's termination behavior, first-player advantage, and response to stronger play are unknown.
- Keystone remains unimplemented and should not be started before Span receives a documented disposition.

## Next recommended work unit

Formalize and freeze Span's exact rules before seeing results; implement legal moves, terminal conditions, and rendering in the shared Python framework; add deterministic tests; run random pathology screening and at least one stronger symmetric-agent screen; record the evidence; then reject, revise, or advance Span and update `STATE.md`.

This is an internal A0 work unit. It does not authorize publication, external communication, third-party repository changes, spending, contracts, permission changes, credential exposure, unlawful action, or harmful action.

## Human gate

The planning report may ask for the single-word approval token: `承認`.

That approval authorizes only the bounded internal work unit described in the report. The executing session must inspect the live repository before acting and may narrow or revise the plan if the repository has changed.

## Anchors

- `STATE.md` verified on 2026-07-15; content SHA `9c94cd23e7cf56287279f06bc4a2595ebcfc06ad`
- Issue #1: `Study 001: Implement and evaluate Span`
