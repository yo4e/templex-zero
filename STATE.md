# State

_Last updated: 2026-07-18_

## Phase

**No active study / next proposal direction selected**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

### Study 001 — Autonomous Game Design

Closed with a negative research conclusion.

- Final report: `research/studies/001-autonomous-game-design/REPORT.md`
- Do not alter it except to correct factual or technical errors.
- Do not create Span v0.3 or continue its candidate repair under Study 001.

### Study 002 — Exact-First Screening of Compact Games

Closed on 2026-07-18 with a **partial / incomplete methodological result**.

- Final report: `research/studies/002-exact-first-screening/REPORT.md`
- Frozen protocol: `research/studies/002-exact-first-screening/PROTOCOL.md`
- Frozen manifest SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

Final hypothesis disposition:

- **H1 supported:** six pre-defined false-reassurance cases were observed.
- **H2 unresolved:** the required shallow-search heuristic was not frozen before exact results were inspected.
- **H3 supported:** exact opening analysis supplied structural explanations hidden by aggregate random win rates.

Reproducibility anchors:

- Exact normalized SHA-256: `9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`
- Random deterministic SHA-256: `d3726b0dff560befc4bbc86fa69b7f9aa889d0e41d16f2a54a3b1acc0df7960e`

## Latest go / no-go assessment

Decision record:

- `research/decisions/2026-07-18-next-study-go-no-go.md`

The assessment compared five possible research directions plus remaining inactive. Only **protocol integrity under approval-gated autonomous research** passed the restart threshold.

The selected direction would test whether a machine-readable dependency model can reject evidence-contaminating event sequences before protected observations are accepted. It directly addresses the Study 002 sequencing failure while remaining distinct from another game-design or exact-screen continuation.

Current disposition:

- **GO to a proposal-writing cycle only.**
- No active study exists.
- Study 003 has not been created or activated.
- No experiment, code, trace corpus, checker, issue, or external action has been started.
- Remaining inactive is still a valid later activation decision if the proposal cannot avoid tautology, special-casing, or weak independent validation.

## Required next proposal contents

A separately frozen proposal must define before any implementation:

1. a research question about enforcing dependencies among research events;
2. at least four dependency classes;
3. hand-audited valid and invalid trace fixtures not limited to Study 002;
4. mutation rules fixed before execution;
5. a primary validator and independently written oracle;
6. synthetic correctness gates before historical Study 001 and Study 002 evaluation;
7. false-accept, false-reject, early-detection, oracle-agreement, and mutation-coverage metrics;
8. explicit failure conditions, including rejection of any special-cased Study 002 rule;
9. a maximum of four approval cycles after activation;
10. explicit limits on claims about truth, quality, safety, creativity, or autonomy.

## Closure boundaries

- Do not reopen Study 001 or create Span v0.3.
- Do not retroactively create a shallow heuristic for Study 002.
- Do not replace or repair the frozen Study 002 candidates.
- Do not add another generated-game corpus as a hidden continuation of Study 002.
- Closed-study files may be changed only for disclosed factual or technical corrections.

## Next actions

1. Write and freeze a proposal for the selected protocol-integrity direction.
2. Do not implement code, create fixtures, run traces, or activate Study 003 in that proposal-writing cycle.
3. After the proposal exists, use a later approval cycle to make a separate activation go / no-go decision.
4. Preserve inactivity if the proposal fails to define nontrivial independent tests and bounded failure conditions.

## Human action currently needed

None.
