# Next Start

_Updated: 2026-07-16 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not authorization and is not the source of truth. `STATE.md`, the active Study 002 protocol, frozen grammar, fixtures, Issue #6, tests, and recent commits remain authoritative.

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

**Study 002 is active. Setup cycle 1 of at most 6 is complete.**

- Active protocol: `research/studies/002-exact-first-screening/PROTOCOL.md`
- Frozen grammar: `research/studies/002-exact-first-screening/GRAMMAR.md`
- Frozen fixtures: `research/studies/002-exact-first-screening/FIXTURES.md`
- Study overview: `research/studies/002-exact-first-screening/README.md`
- Tracking issue: Issue #6

Study 001 remains closed. Do not reopen it or create Span v0.3.

## Completed setup

- Declarative placement-game schema implemented.
- Candidate schema boundaries enforced.
- Four hand-audited state graphs frozen in prose and code.
- Fixture graph enumerator implemented; it is not the exact solver.
- Generation seed frozen at `2026071602`.
- Two board sizes and three mechanism families frozen.
- Exactly three candidates per board-size × family cell frozen.
- SHA-256 seeded ordering and canonical serialization frozen.
- No candidate manifest or candidate result exists.

Local targeted verification produced 10 passing tests and successful `compileall`. Remote Git blob hashes matched the tested local files. Fresh clone failed because the environment could not resolve `github.com`, so the full legacy suite was not rerun.

## Frozen manifest rules

- Cell order: 3×3 AG, 3×3 CE, 3×3 LB, 4×4 AG, 4×4 CE, 4×4 LB.
- Build each cell's Cartesian parameter product from the values in `GRAMMAR.md`.
- Normalize aliases into a canonical ordered object.
- Encode compact UTF-8 JSON.
- Rank by SHA-256 of `2026071602|<board_size>|<family>|<canonical_json>`.
- Select the first three distinct statically valid entries per cell.
- No manual ranking, replacement, outcome inspection, or second grammar.
- If any cell has fewer than three valid entries, close the study as grammar failure.

## Next recommended work unit

Generate and freeze the candidate manifest only.

1. Implement the canonical tuple serializer and seeded SHA-256 enumerator exactly as frozen.
2. Translate parameter tuples into validated `GameSpec` objects.
3. Generate human-readable rule text and verify it is at most 250 words.
4. Select exactly three entries per cell in frozen order.
5. Save the 18 canonical tuples, IDs, rule text, word counts, and validation records.
6. Re-run generation and require byte-identical manifest output.
7. Add deterministic generation and manifest tests.
8. Do **not** implement the exact solver or run random, shallow, or exact candidate play.

That cycle determines whether the frozen grammar can produce the required static candidate family without adaptive replacement.

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
- Issue #6: Study 002 tracking
