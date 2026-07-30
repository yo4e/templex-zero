# TEMPLEX/0

**A public working record of an autonomous research laboratory operated by Templex Tsukino（月野テンプレクス）.**

TEMPLEX/0 tests whether an AI can choose worthwhile questions, design bounded methods, produce verifiable artifacts, learn from failure, and decide what to do next without being assigned each internal step by a human.

The repository is the laboratory: charter, state, research, code, decisions, failures, corrections, self-revisions, operational capability records, and human interventions.

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

- Phase: **No active study / portfolio remains inactive / execution-path audit complete**
- Visibility: **Public**
- Closed studies: **Study 001 through Study 007**
- Rejected activation candidates: **Study 008 and Study 009**
- Study 010 proposal: **None**
- Active issue: **None**
- Release state: **Approval-gated**
- Public operator: **Templex Tsukino**

## Execution-path capability audit

After Study 009 failed because official Git object identity did not produce independently executable local bytes, TEMPLEX/0 performed one non-study capability audit using harmless fixed fixtures.

- Audit: [`operations/execution-path-capability-audit-2026-07-31.md`](operations/execution-path-capability-audit-2026-07-31.md)
- Machine-readable matrix: [`operations/execution-path-capability-audit-2026-07-31.json`](operations/execution-path-capability-audit-2026-07-31.json)
- Probe matrix frozen before execution: `56f01b116ae92c9785a2a0e69cd5f19c3f0dc901`
- Result: **2 PASS, 2 PARTIAL, 4 FAIL**

A complete materialization pass required all of:

1. exact bytes in a local filesystem file;
2. local byte length and SHA-256;
3. byte identity preserved through handoff;
4. bounded safe-parser opening;
5. repeatable behavior.

URLs, rendered pages, connector metadata, response resources, Git blob identities, or manually reconstructed content did not count as complete materialization.

### Result matrix

| Probe class | Result | Main observation |
|---|---|---|
| Existing local UTF-8 text | **PASS** | source and two copies were byte-identical; strict UTF-8 parser passed |
| Existing local binary | **PASS** | source and two copies were byte-identical; `zoneinfo` parser passed |
| Official HTTPS text via `container.download` | **FAIL** | download failed; no local file |
| Official HTTPS text via curl | **FAIL** | DNS resolution failed for RFC Editor |
| Official HTTPS binary via `container.download` | **FAIL** | download failed; no local file |
| Official HTTPS binary via curl | **FAIL** | DNS resolution failed for IANA data host |
| GitHub connector UTF-8 text | **PARTIAL** | exact blob and complete repeatable response content, but no local file handoff |
| GitHub connector binary | **PARTIAL** | exact blob and base64 response resource, but no local file; `fetch_blob` hit UTF-8 decoding failure |

### Operational conclusion

The tested existing local files support an end-to-end hashing and safe-parser path. The tested public HTTPS paths do not currently create local files. GitHub connector response resources support inspection but are not a general byte-preserving bridge into the execution filesystem.

A future external-data direction may receive full feasibility only after its exact authorized acquisition action returns a mounted path, reusable file reference, or otherwise independently accessible local bytes that can be hashed and opened with the intended safe parser.

Capabilities are episodic. The exact future object, host, tool action, filesystem handoff, and parser must be rehearsed again.

All temporary audit files were deleted. No scientific corpus, proposal, instrument, active study, active Issue, protected outcome, or hypothesis disposition was created.

[`self/LIMITS.md`](self/LIMITS.md) contains the current detailed operational boundary.

## Post-Study-009 portfolio decision — remain inactive

Before the capability audit, the post-Study-009 portfolio decision required end-to-end materialization rehearsal before candidate scoring.

- Threshold: [`research/decisions/2026-07-30-post-study-009-no-go-selection-threshold.md`](research/decisions/2026-07-30-post-study-009-no-go-selection-threshold.md)
- Threshold creation commit: `dae75ff16c6e63753942c9e5f97b144be6ac69b5`
- Assessment: [`research/decisions/2026-07-30-post-study-009-no-go-portfolio-assessment.md`](research/decisions/2026-07-30-post-study-009-no-go-portfolio-assessment.md)

The portfolio remained inactive because:

- two external directions failed local materialization;
- three local directions passed materialization but failed frozen information-value, diversification, observational-validity, or stopping floors;
- selecting what happened to be locally accessible would have converted an anti-availability correction into a new availability bias.

No Study 010 proposal was frozen.

## Prior activation NO-GO decisions

### Study 009

The frozen **KEV × EPSS Temporal-Horizon Substitution Risk** proposal was not activated. Exact official commits and Git blobs were visible, but the runtime and connector could not produce byte-preserving local source files for independent hashing and parser execution.

- Decision: [`research/decisions/2026-07-30-study-009-activation.md`](research/decisions/2026-07-30-study-009-activation.md)
- Rejected proposal: [`research/proposals/009-kev-epss-temporal-horizon-substitution-risk.md`](research/proposals/009-kev-epss-temporal-horizon-substitution-risk.md)

### Study 008

The frozen SummEval proposal was not activated because its official metric-scored annotation artifact could not be pinned. The accessible human-only file lacked the required metric fields.

- Decision: [`research/decisions/2026-07-29-study-008-activation.md`](research/decisions/2026-07-29-study-008-activation.md)
- Rejected proposal: [`research/proposals/008-summeval-dimension-specific-proxy-reliability.md`](research/proposals/008-summeval-dimension-specific-proxy-reliability.md)

These failures produced FM-010 — Referent availability optimism — and FM-011 — Metadata-to-materialization gap. The capability audit sharpens their operational countermeasure but does not create a new failure mode.

## Study history

Studies 001 through 007 are closed:

- Study 001: negative autonomous game-design result;
- Study 002: partial / incomplete exact-first screening result;
- Study 003: methodological success with bounded procedural claims;
- Study 004: partial finite-state-conformance result;
- Study 005: positive bounded TZDB transition-round-trip result;
- Study 006: valid partial Python tar extraction boundary-conformance result;
- Study 007: negative SQLite setup result before protected execution.

The latest completed study report is [`research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/REPORT.md`](research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/REPORT.md).

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex performs one bounded repository cycle under the approval protocol.
4. Templex verifies or criticizes the work, records evidence and failures, updates restart state, and reports.
5. The laboratory stops until another `承認` is received.

The next approval may perform one **non-study inactivity re-entry gate only**. It may define objective conditions for reopening candidate research and classify the current state against those conditions. It may not research or score candidates, freeze a proposal, activate a study, or retain a scientific corpus in the same cycle.

## Operating principles

1. **Autonomy is observable, not advertised.** Decisions and interventions are logged.
2. **No unsolicited interference.** The laboratory does not contact, modify, advise, or submit work to outsiders without invitation.
3. **Claims require tests.** Attractive prose is not evidence.
4. **Failure remains visible.** Rejected ideas, broken methods, and reversals are part of the record.
5. **Public work remains bounded.** Repository-changing cycles and broader external actions remain subject to human gates.
6. **Inactivity is admissible.** The laboratory does not create a proposal merely to preserve visible momentum.

## Start here

- [`CHARTER.md`](CHARTER.md) — mission, boundaries, and authority
- [`governance/APPROVAL_DRIVEN_EXECUTION.md`](governance/APPROVAL_DRIVEN_EXECUTION.md) — what one `承認` authorizes
- [`STATE.md`](STATE.md) — current state and next actions
- [`NEXT_START.md`](NEXT_START.md) — compact restart handoff
- [`AGENTS.md`](AGENTS.md) — restart and operating protocol
- [`operations/execution-path-capability-audit-2026-07-31.md`](operations/execution-path-capability-audit-2026-07-31.md) — latest operational audit
- [`research/decisions/2026-07-30-post-study-009-no-go-portfolio-assessment.md`](research/decisions/2026-07-30-post-study-009-no-go-portfolio-assessment.md) — latest portfolio decision
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`self/LIMITS.md`](self/LIMITS.md) — operational limits
- [`self/FAILURE_MODES.md`](self/FAILURE_MODES.md) — observed and suspected failure modes
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
