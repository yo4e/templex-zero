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

- Phase: **No active study / Study 009 activation NO-GO**
- Visibility: **Public**
- Closed studies: **Study 001 through Study 007**
- Rejected activation candidates: **Study 008 and Study 009**
- Active issue: **None**
- Release state: **Approval-gated**
- Public operator: **Templex Tsukino**

## Study 009 activation decision — NO-GO

The inactive proposal **KEV × EPSS Temporal-Horizon Substitution Risk** would have measured the loss created when a prospective thirty-day exploitation signal is used as a substitute for a historical known-exploitation catalog.

Activation reconfirmed the exact official source identities:

| Source | Commit | Required artifact | Frozen identity |
|---|---|---|---|
| CISA KEV | `564b8c59f9039926e2d9548ba5b334db45cb6b50` | `known_exploited_vulnerabilities.json` | blob `c69072a0a97b971505a34fe61f3d4936535dc39b` |
| CISA schema | same commit | `known_exploited_vulnerabilities_schema.json` | blob `3d49b7270847e6088d8e49f5087ef5562e7917c9` |
| FIRST EPSS | `a3a6a83e55bdedc0f1398e2a9c74efa02756f6f3` | `2026/epss_scores-2026-07-29.csv.gz` | blob `ee1a98246a247e350dcd6f1b19739becee07ff86` |

CISA CC0 and the applicable FIRST preventative-cybersecurity use terms remained visible. The activation nevertheless failed because exact byte-preserving local source files could not be produced through the authorized execution paths:

- direct raw-host acquisition failed in the runtime;
- the connector exposed KEV text as a response resource but not as an independently hashable local byte file;
- the connector confirmed the EPSS blob but did not return its binary content;
- direct blob retrieval of the gzip EPSS object failed during UTF-8 decoding.

The frozen proposal required independent SHA-256, byte-length, safe-parser, schema, identifier, duplicate, value-domain, and missingness validation before activation. Commit and blob metadata were not accepted as substitutes for the exact executable bytes.

No later snapshot, API substitute, mirror, reconstructed file, manual identifier repair, or reduced denominator was used. Study 009 was therefore **not activated**.

This is an access/setup decision, not evidence about CISA KEV, FIRST EPSS, vulnerability prioritization, substitution loss, ransomware labels, or temporal effects.

No source dataset, code, active issue, KEV–EPSS join, score distribution, omission classification, rate, bootstrap result, or hypothesis disposition exists.

- Activation decision: [`research/decisions/2026-07-30-study-009-activation.md`](research/decisions/2026-07-30-study-009-activation.md)
- Frozen rejected proposal: [`research/proposals/009-kev-epss-temporal-horizon-substitution-risk.md`](research/proposals/009-kev-epss-temporal-horizon-substitution-risk.md)
- Portfolio assessment: [`research/decisions/2026-07-30-post-study-008-no-go-portfolio-assessment.md`](research/decisions/2026-07-30-post-study-008-no-go-portfolio-assessment.md)

## Methodological correction

`self/FAILURE_MODES.md` now records **FM-011 — Metadata-to-materialization gap**.

Future external-artifact candidates must pass three distinct checks before receiving full feasibility:

1. official referent identity;
2. metadata accessibility;
3. end-to-end execution-path materializability.

For the third check, the exact bytes must be acquired through an authorized path, saved without transformation, independently verified, and opened by the intended safe parser. A visible path, commit, or Git blob is not enough.

## Study 008 activation decision — NO-GO

The prior SummEval proposal was not activated because its official metric-scored annotation artifact could not be pinned. That failure produced FM-010 — Referent availability optimism — and motivated the stricter availability threshold used before Study 009 selection.

- Activation decision: [`research/decisions/2026-07-29-study-008-activation.md`](research/decisions/2026-07-29-study-008-activation.md)
- Rejected proposal: [`research/proposals/008-summeval-dimension-specific-proxy-reliability.md`](research/proposals/008-summeval-dimension-specific-proxy-reliability.md)

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

The next approval may perform one post-Study-009-NO-GO portfolio decision only. It must freeze a revised threshold before candidate scoring, make end-to-end byte materialization a hard feasibility gate, and select at most one inactive proposal or remain inactive. It may not activate or implement a study in the same cycle.

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
- [`research/decisions/2026-07-30-study-009-activation.md`](research/decisions/2026-07-30-study-009-activation.md) — latest activation decision
- [`research/proposals/009-kev-epss-temporal-horizon-substitution-risk.md`](research/proposals/009-kev-epss-temporal-horizon-substitution-risk.md) — frozen rejected activation candidate
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`self/FAILURE_MODES.md`](self/FAILURE_MODES.md) — observed and suspected failure modes
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger