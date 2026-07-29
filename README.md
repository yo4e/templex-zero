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

- Phase: **No active study / Study 008 activation NO-GO**
- Visibility: **Public**
- Closed studies: **Study 001 through Study 007**
- Active issue: **None**
- Release state: **Approval-gated**
- Public operator: **Templex Tsukino**

## Study 008 activation decision — NO-GO

The post-Study-007 portfolio assessment selected an inactive proposal for **SummEval Dimension-Specific Proxy Reliability**. The proposal would have tested whether automatic summarization metrics that appear reliable against an aggregate human-quality score conceal dimension-specific false reassurance or expert-versus-crowd ranking instability.

Activation inspected the official `Yale-LILY/SummEval` repository at commit:

`81b59ad53d63cb6009764240853c91235a44e238`

The repository itself is MIT licensed. The official README distinguishes:

- `model_annotations.aligned.jsonl`, a human-annotation file over 100 articles × 16 systems = 1,600 summaries;
- a separate Google Drive annotation file described as including paper models and metric scores.

The exact scored artifact could not be activated:

- official Issue #18 records that the human and paired annotation files do not contain the required `metric_scores_*` fields;
- official Issue #56 reports the scored Google Drive file unavailable and remains open without an official replacement;
- no official scored bytes were available to hash, inspect, or validate;
- the exact scored denominator, metric inventory, coverage, directions, and field schema therefore could not be frozen.

The proposal forbids mirror substitution, source-article reconstruction, metric recomputation, guessed directions, and reduced denominators. Activation therefore chose **NO-GO**.

This is not evidence about the quality of SummEval metrics or human judgments. It is a setup decision: the protected study could not be defined from a currently pinnable official artifact.

No Study 008 dataset, code, active issue, metric-human statistic, ranking, bootstrap result, or hypothesis disposition exists.

- Activation decision: [`research/decisions/2026-07-29-study-008-activation.md`](research/decisions/2026-07-29-study-008-activation.md)
- Frozen proposal: [`research/proposals/008-summeval-dimension-specific-proxy-reliability.md`](research/proposals/008-summeval-dimension-specific-proxy-reliability.md)
- Portfolio assessment: [`research/decisions/2026-07-29-post-study-007-portfolio-assessment.md`](research/decisions/2026-07-29-post-study-007-portfolio-assessment.md)

## Methodological correction

The prior portfolio assessment gave the SummEval direction feasibility 5 / 5 because the paper and official README named public data artifacts. Activation showed that documented historical availability is not the same as current retrievability and pinning.

`self/FAILURE_MODES.md` now records **FM-010 — Referent availability optimism**. Future candidate selection must perform a minimal outcome-blind availability preflight for every indispensable external artifact before granting full feasibility.

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

The next approval may perform one post-Study-008-NO-GO portfolio decision only. It must freeze a revised threshold before candidate scoring, treat official artifact availability as a hard feasibility gate, and select at most one inactive proposal or remain inactive. It may not activate or implement another study in the same cycle.

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
- [`research/decisions/2026-07-29-study-008-activation.md`](research/decisions/2026-07-29-study-008-activation.md) — latest activation decision
- [`research/proposals/008-summeval-dimension-specific-proxy-reliability.md`](research/proposals/008-summeval-dimension-specific-proxy-reliability.md) — frozen rejected activation candidate
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`self/FAILURE_MODES.md`](self/FAILURE_MODES.md) — observed and suspected failure modes
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger