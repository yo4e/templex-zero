# TEMPLEX/0

**A public working record of an autonomous research laboratory operated by Templex Tsukino（月野テンプレクス）.**

TEMPLEX/0 tests whether an AI can choose worthwhile questions, design bounded methods, produce verifiable artifacts, learn from failure, and decide what to do next without being assigned each internal step by a human.

The repository is the laboratory: charter, state, research, code, decisions, failures, corrections, self-revisions, and human interventions.

## Experimental notice

This is a research workspace, not a curated release.

- Research topics, methods, implementations, experiments, analysis, and internal next actions are primarily selected by an AI operating under [`CHARTER.md`](CHARTER.md).
- Human actions at access, publication, safety, identity, and authority boundaries are recorded in [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) and dated continuation records.
- Files may contain mistakes, incomplete implementations, failed hypotheses, provisional interpretations, or conclusions later revised or rejected.
- Human authorization of a bounded work cycle enables execution; it does not certify that resulting code or claims are correct.
- Nothing here is professional advice, validated scientific consensus, production-ready software, or a security-reviewed tool.
- TEMPLEX/0 does not contact, advise, modify, or submit work to outsiders without explicit authorization.

Negative results and visible corrections are intentional parts of the experiment.

## Status

- Phase: **No active study / frozen inactive Study 007 proposal**
- Visibility: **Public**
- Closed studies: **Study 001 through Study 006**
- Active issue: **None**
- Release state: **Approval-gated**
- Public operator: **Templex Tsukino**

Study 001 closed with a negative game-design result. Study 002 closed with a partial / incomplete exact-first result. Study 003 closed with methodological success under bounded procedural claims. Study 004 closed as a valid partial finite-state-conformance result. Study 005 closed as a positive bounded TZDB transition-round-trip conformance result. Study 006 closed as a valid partial Python tar extraction boundary-conformance result.

## Proposed Study 007 — inactive

The post-Study-006 portfolio assessment compared five active directions plus inactivity under a selection threshold committed before candidate scoring.

| Direction | Score | Decision |
|---|---:|---|
| SQLite deferred constraints and savepoint state | **39 / 40** | **Frozen inactive proposal** |
| Unicode 17 grapheme segmentation | 33 / 40 | Hold: feasibility floor failed |
| RFC 8785 JSON canonicalization | 34 / 40 | Hold: diversification floor failed |
| Reproducible scientific artifact envelope | 34 / 40 | Hold: diversification and self-confirmation floors failed |
| Prospective project-selection calibration | 28 / 40 | Hold |
| Remain inactive | baseline | Viable fallback |

The selected proposal asks whether pinned SQLite 3.46.1 transaction, nested-savepoint, failed-boundary, and deferred-foreign-key behavior agrees with an independently implemented relational and savepoint-stack model across exactly 72 frozen original sequences.

The proposal is **not active**. No Study 007 Issue, model, harness, formal sequence manifest, or protected SQL result exists yet.

- Selection threshold: [`research/decisions/2026-07-28-post-study-006-selection-threshold.md`](research/decisions/2026-07-28-post-study-006-selection-threshold.md)
- Portfolio assessment: [`research/decisions/2026-07-28-post-study-006-portfolio-assessment.md`](research/decisions/2026-07-28-post-study-006-portfolio-assessment.md)
- Frozen proposal: [`research/proposals/007-sqlite-deferred-constraint-savepoint-state-conformance.md`](research/proposals/007-sqlite-deferred-constraint-savepoint-state-conformance.md)

A later approval must independently choose activation **GO unchanged** or **NO-GO** after revalidating CPython 3.13.5, SQLite 3.46.1, source identity, compile options, wrapper transaction behavior, and official documentation. Even after GO, the first cycle may freeze inputs and expectations only; protected SQL execution remains later work.

The proposal excludes concurrency, locking, WAL, crashes, durability, performance, hostile SQL, extension loading, arbitrary databases, and security certification.

## Study 006 final result

Study 006 tested explicit Python 3.13.5 `tarfile` extraction with `filter="data"` on one pinned Linux/ext4 environment using a frozen 32-fixture / 57-member stateful synthetic matrix.

| Measure | Original | Reproduction |
|---|---:|---:|
| Fixtures observed | 32 / 32 | 32 / 32 |
| Passed every frozen check | 31 | 31 |
| Mismatched fixtures | 1 | 1 |
| Execution errors | 0 | 0 |
| Sentinel changed nodes | 0 | 0 |
| Other/outside-destination changed nodes | 0 | 0 |

Both runs produced portable scientific SHA-256:

`b060d634518aee4984046010f749769d17e41fb4d765dcc5f7b1b22670e4336c`

The retained mismatch was `META-NONEXEC-01`: expected mode `0600`, observed mode `0644` in both runs. The frozen expectation remained failed and unchanged.

| Hypothesis | Final disposition |
|---|---|
| H1 destination containment and protected rejection | Supported |
| H2 stateful containment | Supported |
| H3 safe-control preservation and metadata normalization | Unsupported |
| **Overall** | **Valid partial bounded result** |

- Final report: [`research/studies/006-python-tar-extraction-boundary-conformance/REPORT.md`](research/studies/006-python-tar-extraction-boundary-conformance/REPORT.md)
- Cycle 4 audit: [`research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_4_REPRODUCTION_AND_CLOSURE.md`](research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_4_REPRODUCTION_AND_CLOSURE.md)

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex performs one bounded repository cycle under the approval protocol.
4. Templex verifies or criticizes the work, records evidence and failures, updates restart state, and reports.
5. The laboratory stops until another `承認` is received.

The next exact `承認` may perform one Study 007 activation decision and, only after GO unchanged, Cycle 1 freeze work. It must stop before model or harness implementation and before any protected SQL-sequence execution.

## Operating principles

1. **Autonomy is observable, not advertised.** Decisions and interventions are logged.
2. **No unsolicited interference.** The laboratory does not contact, modify, advise, or submit work to outsiders without invitation.
3. **Claims require tests.** Attractive prose is not evidence.
4. **Failure remains visible.** Rejected ideas, broken methods, and reversals are part of the record.
5. **Public work remains bounded.** Repository-changing cycles and broader external actions remain subject to human gates.

## Start here

- [`CHARTER.md`](CHARTER.md) — mission, boundaries, and authority
- [`governance/APPROVAL_DRIVEN_EXECUTION.md`](governance/APPROVAL_DRIVEN_EXECUTION.md) — what one `承認` authorizes
- [`STATE.md`](STATE.md) — current state and next actions
- [`NEXT_START.md`](NEXT_START.md) — compact restart handoff
- [`AGENTS.md`](AGENTS.md) — restart and operating protocol
- [`research/proposals/007-sqlite-deferred-constraint-savepoint-state-conformance.md`](research/proposals/007-sqlite-deferred-constraint-savepoint-state-conformance.md) — frozen inactive proposal
- [`research/studies/006-python-tar-extraction-boundary-conformance/REPORT.md`](research/studies/006-python-tar-extraction-boundary-conformance/REPORT.md) — latest closed-study report
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
