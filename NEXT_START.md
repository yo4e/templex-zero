# Next Start

_Updated: 2026-07-17 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not authorization and is not the source of truth. `STATE.md`, the active Study 002 protocol, frozen fixtures and manifest, correctness audit, Issue #6, tests, and recent commits remain authoritative.

When Yoshie Yamada sends `承認` in the project chat, the executing session must re-read the live repository and follow `governance/APPROVAL_DRIVEN_EXECUTION.md` before selecting and performing one bounded research cycle.

## Identity and execution

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Familiar and historical name: **Monday**
- Repository: `https://github.com/yo4e/templex-zero`
- One clear `承認` authorizes one complete bounded research cycle.
- After reporting, stop until another `承認` is received.
- External communication, submissions, spending, permissions, human-subject activity, and other separately gated actions remain outside ordinary approval.

## Current position

**Study 002 is active. Exact-instrument cycle 3 of at most 6 is complete.**

- Active protocol: `research/studies/002-exact-first-screening/PROTOCOL.md`
- Frozen grammar: `research/studies/002-exact-first-screening/GRAMMAR.md`
- Frozen fixtures: `research/studies/002-exact-first-screening/FIXTURES.md`
- Frozen manifest: `research/studies/002-exact-first-screening/manifest/`
- Manifest audit: `research/studies/002-exact-first-screening/MANIFEST_AUDIT.md`
- Exact-instrument audit: `research/studies/002-exact-first-screening/EXACT_INSTRUMENT_AUDIT.md`
- Tracking issue: Issue #6

Study 001 remains closed. Do not reopen it or create Span v0.3.

## Frozen sample

- 18 candidates total.
- 9 on 3×3 and 9 on 4×4 boards.
- Exactly three in every board-size × family cell.
- Full compact entry-list SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`.
- Selection used frozen compact JSON and seeded SHA-256 rank only.
- Do not replace, reorder, polish, or add candidates. Do not change the grammar or seed.

## Exact instrument

- `solver.py`: memoized full-width DFS with no symmetry reduction.
- `bruteforce.py`: independent queue-built graph and retrograde fixture oracle.
- Values are from player-to-move perspective.
- Outcome order: win, draw, loss.
- Outcome-preserving distance: win shortest, loss longest, draw shortest.
- A capped run publishes no partial root value.
- State and time caps return explicit cap reasons.

The two instruments agreed on all twelve reachable states of the four frozen fixtures, including every legal action value. Fixtures 1 and 2 passed their retained color-role symmetry checks.

## Verification status

- Solver suite: 8 passed.
- Setup, fixture, and solver suites together: 18 passed.
- `compileall`: passed.
- Remote Git blob SHAs matched the locally executed solver, oracle, export, and test files.
- Prior manifest suite: 7 passed and byte-identical regeneration; not rerun in this reconstruction.
- Fresh clone failed because the environment could not resolve `github.com`.
- No GitHub Actions workflow is recorded.

## Next recommended work unit

Run the frozen exact candidate screen only.

1. Re-read the manifest and protocol from GitHub.
2. Implement and commit a deterministic experiment script before inspecting candidate results.
3. Load candidates strictly in manifest order.
4. Use the validated no-reduction solver.
5. Enforce 2,000,000 expanded states and 30 seconds per candidate.
6. Enforce 25,000,000 expanded states across the study; mark all later entries unsolved if reached.
7. Record root outcome and distance, every opening value, winning/drawing/losing opening counts, non-losing opening proportion, state count, measured time, and cap reason.
8. Repeat the configured run and compare deterministic fields; timing may vary and must be reported separately.
9. If fewer than 12 candidates solve exactly, close the study under the frozen failure condition.
10. Do **not** alter candidates or caps and do **not** run random or shallow screens in that cycle.

## Human gate

> 承認

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Current state: `STATE.md`
- Study 001 report: `research/studies/001-autonomous-game-design/REPORT.md`
- Study 002 proposal: `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`
- Study 002 protocol: `research/studies/002-exact-first-screening/PROTOCOL.md`
- Study 002 grammar: `research/studies/002-exact-first-screening/GRAMMAR.md`
- Study 002 fixtures: `research/studies/002-exact-first-screening/FIXTURES.md`
- Study 002 manifest: `research/studies/002-exact-first-screening/manifest/index.json`
- Exact-instrument audit: `research/studies/002-exact-first-screening/EXACT_INSTRUMENT_AUDIT.md`
- Issue #6: Study 002 tracking
