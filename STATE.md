# State

_Last updated: 2026-07-16_

## Phase

**Study 002 active / exact-first setup complete / cycle 1 of at most 6**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Study 001

Study 001 remains closed with a negative research conclusion. Its final synthesis is:

- `research/studies/001-autonomous-game-design/REPORT.md`

Do not alter it except to correct factual or technical errors. Do not create Span v0.3 or continue its candidate repair.

## Study 002 objective

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

The active protocol is:

- `research/studies/002-exact-first-screening/PROTOCOL.md`

It was activated without changing the frozen proposal at:

- `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`
- final proposal commit `68fc4c2edb93ca1363e7b7040221b5507cfeb171`

## Cycle 1 completed

- Created the active protocol and six-cycle accounting.
- Defined a declarative placement-game schema with immutable states, legal placement, adjacency growth, expansion/merger, local enemy limits, connection, line, component, and fixture-only pattern goals.
- Candidate validation enforces 3×3/4×4 full boards, intended symmetry, placement-only rules, fixture-only explicit features, and a 250-word ceiling.
- Froze generation seed `2026071602`.
- Froze two board sizes, three mechanism families, exactly three candidates per cell, SHA-256 seeded ordering, canonical tuple serialization, and no manual replacement.
- Defined four hand-audited reachable state graphs: immediate win, exhausted-action draw, branching winners, and adjacency chain.
- Added machine-readable fixtures and deterministic schema/graph tests.
- Did **not** generate an 18-entry manifest, implement the exact solver, or inspect any candidate outcome.

## Verification

- Local reconstruction: `python -m pytest -q` → **10 passed** for the new Study 002 tests.
- Local reconstruction: `python -m compileall -q src tests` → no errors.
- Git blob hashes for the remote schema, fixture, grammar, and two test files exactly matched the locally tested files.
- A fresh repository clone failed because the execution environment could not resolve `github.com`; the pre-existing full suite was therefore not rerun in this cycle.
- The repository still has no recorded GitHub Actions workflow.

## Frozen study boundaries

- Exactly 18 candidates: 9 on 3×3, 9 on 4×4, three per board-size × family cell.
- Placement only; no movement, capture, swap, chance, scoring, repetition, or pass.
- Manifest selected by static validation and seeded SHA-256 order only.
- Exact caps: 2,000,000 states and 30 seconds per candidate; 25,000,000 states total in manifest order.
- At least 12 exact solutions required.
- Random screen: 2,000 games per candidate.
- Shallow screen: 200 equal-agent games at depths 1, 2, and 3 per candidate.
- Maximum six approval-driven cycles including final synthesis.
- No second grammar, candidate polishing, prior-art search, human playtest, paid compute, or external solver.

## Next actions

1. Implement the already frozen deterministic tuple enumerator and canonical serializer.
2. Generate exactly three valid entries in each of the six cells.
3. Freeze all 18 canonical tuples, identifiers, generated rule text, word counts, and static validation records in a manifest.
4. Test repeat generation for byte-identical output and reject duplicate or out-of-scope entries.
5. Do not implement the exact solver or run random, shallow, or exact candidate play in that cycle.

## Human action currently needed

None.
