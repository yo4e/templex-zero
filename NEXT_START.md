# Next Start

_Updated: 2026-07-16 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not authorization and is not the source of truth. `STATE.md`, the active Study 002 protocol, frozen grammar, fixtures, manifest, Issue #6, tests, and recent commits remain authoritative.

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

**Study 002 is active. Candidate manifest cycle 2 of at most 6 is complete.**

- Active protocol: `research/studies/002-exact-first-screening/PROTOCOL.md`
- Frozen grammar: `research/studies/002-exact-first-screening/GRAMMAR.md`
- Frozen fixtures: `research/studies/002-exact-first-screening/FIXTURES.md`
- Frozen manifest: `research/studies/002-exact-first-screening/manifest/`
- Manifest audit: `research/studies/002-exact-first-screening/MANIFEST_AUDIT.md`
- Tracking issue: Issue #6

Study 001 remains closed. Do not reopen it or create Span v0.3.

## Frozen sample

- 18 candidates total.
- 9 on 3×3 and 9 on 4×4 boards.
- Exactly three in every board-size × family cell.
- Full compact entry-list SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`.
- Generated rule text: 83–142 words.
- All entries passed static schema, full-board, intended-symmetry, and word-limit checks.
- Selection used frozen compact JSON and seeded SHA-256 rank only; no play result or human ranking was used.

Do not replace, reorder, polish, or add candidates. Do not change the grammar or seed.

## Verification status

- Manifest test suite: 7 passed.
- `compileall`: passed.
- Regeneration was byte-identical.
- Remote Git blob SHAs matched the verified generator, script, test, index, overview, and all 18 candidate files.
- Fresh clone failed because the environment could not resolve `github.com`.
- No fresh combined full-repository regression is claimed.
- No GitHub Actions workflow is recorded.

## Next recommended work unit

Implement and validate the exact-analysis instrument only.

1. Implement a standard-library-only memoized full-width solver without symmetry reduction.
2. Return outcome from the player-to-move perspective, outcome-preserving terminal distance, opening-action values, and expanded-state count.
3. Implement a separately written brute-force fixture enumerator that does not call the memoized recursive solver.
4. Cross-check both instruments on all four frozen fixtures at every reachable state.
5. Compare root outcomes, distances, and every opening-action value.
6. Exhaustively verify only the symmetry claims retained by Fixtures 1 and 2.
7. Add deterministic correctness and resource-cap tests.
8. Do **not** solve the 18 frozen candidates yet.

This cycle determines whether the exact instrument passes the precommitted correctness gate before candidate outcomes exist.

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
- Issue #6: Study 002 tracking
