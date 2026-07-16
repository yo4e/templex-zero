# State

_Last updated: 2026-07-16_

## Phase

**No active study / Study 002 proposal frozen, awaiting activation approval**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Study 001

Study 001 is closed with a negative research conclusion. Its final synthesis is:

- `research/studies/001-autonomous-game-design/REPORT.md`

Do not alter the closed study except to correct factual or technical errors. Do not create Span v0.3 or continue its candidate repair under the old protocol.

## Study 002 go / no-go result

A bounded go/no-go assessment compared four directions:

1. exact-first screening of generated finite games;
2. prior-art and convergence mapping;
3. human playability and teachability evaluation;
4. repository CI and reproducibility hardening as a standalone study.

The decision is **GO** only for a separately scoped exact-first methodological study. It has the highest immediate information value, directly tests Study 001's strongest lesson, requires no external service or human subject, produces a reusable solver artifact, and can return a valid positive, negative, or null result.

The frozen proposal is:

- `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`

Study 002 is not active yet. The proposal does not authorize experiments.

## Frozen proposal summary

- Research question: can exact opening analysis measure when random and shallow symmetric play misrepresent generated compact placement games?
- Candidate set: exactly 18 placement-only games; 9 on 3×3, 9 on 4×4, with exactly three candidates in every board-size × mechanism-family cell.
- Candidate selection: seeded deterministic enumeration, static canonicalization, no manual ranking or replacement.
- Instrument: generic declarative engine, memoized exact solver, independent brute-force fixture enumerator, symmetry checks.
- Exact resource caps: 2,000,000 states and 30 measured seconds per candidate; 25,000,000 states total, consumed in frozen manifest order.
- Continuation requirement: at least 12 of 18 candidates solved exactly.
- Comparison: 2,000 random games and 200 equal-agent games at depths 1–3 per candidate.
- Primary output: exact/approximate disagreement, including pre-defined false-reassurance cases.
- Maximum duration: six approval-driven execution cycles after activation.
- Out of scope: game-quality claims, prior-art claims, human playtesting, candidate polishing, a second grammar, paid compute, or external services.

## Next actions

On a later `承認`, if the proposal remains uncorrected:

1. activate Study 002 without changing the frozen proposal;
2. create the active protocol from the proposal commitments;
3. define and test the declarative rule schema;
4. define four hand-audited exact-solver fixtures and expected state graphs;
5. freeze the candidate grammar, deterministic enumeration rule, and generation seed;
6. do not generate or evaluate the 18 candidates in that first execution cycle.

External publication, promotion, submissions, spending, permission changes, third-party actions, and human-subject activity remain separately gated.

## Human action currently needed

None.
