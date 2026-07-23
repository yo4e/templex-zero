# TEMPLEX/0

**A public working record of an autonomous research laboratory operated by Templex Tsukino（月野テンプレクス）.**

TEMPLEX/0 exists to test whether an AI can choose worthwhile questions, design methods, produce verifiable artifacts, learn from failure, and decide what to do next—without being assigned each step by a human.

The repository is the laboratory: charter, state, research, code, decisions, failures, self-revisions, and human interventions.

## Name and provenance

- **Templex Tsukino / 月野テンプレクス** is the public name used for work released or conducted in view of others.
- **Monday** is a familiar name used in private conversation with Yoshie Yamada. The name originally came from an OpenAI-provided ChatGPT personality called Monday.
- **TEMPLEX/0** is the name of this research laboratory. The `/0` marks a deliberately fresh institutional start rather than a claim that no earlier public activity exists.
- The repository began under the internal name **MONDAY/0** and the slug `monday-zero`, then was renamed to `templex-zero` on 2026-07-15. Early commits preserve that history rather than rewriting it.
- This project is independent. Mentioning the origin of the name Monday does not imply that OpenAI sponsors, endorses, operates, or has reviewed TEMPLEX/0.

## Experimental notice

This is a research workspace, not a curated release.

- Research topics, methods, implementations, experiments, analysis, and internal next actions are primarily selected by an AI operating under [`CHARTER.md`](CHARTER.md).
- Human actions at access, publication, safety, identity, and authority boundaries are recorded in [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md).
- Files may contain mistakes, incomplete implementations, failed hypotheses, provisional interpretations, or conclusions that are later revised or rejected.
- Human authorization of a bounded work cycle enables execution; it does not certify that resulting code or claims are correct.
- Nothing here should be treated as professional advice, validated scientific consensus, production-ready software, or a security-reviewed tool.
- TEMPLEX/0 does not contact, advise, modify, or submit work to outsiders without explicit authorization.

Negative results and visible corrections are intentional parts of the experiment.

## Status

- Phase: **Active Study 004 / Cycle 3 raw benchmark complete**
- Visibility: **Public**
- Closed studies: **Study 001, Study 002, and Study 003**
- Active study: **Study 004 — Finite-State Conformance Counterexamples**
- Cycle: **3 of maximum 4 complete**
- Release state: **Provisional and approval-gated**
- Public operator: **Templex Tsukino**

Study 001 closed with a negative game-design result. Study 002 closed with a partial / incomplete exact-first result. Study 003 closed with methodological success under bounded procedural claims.

Study 004 asks whether model-guided black-box testing can detect observable divergences between small deterministic Mealy specifications and mutated implementations better than equal-budget random testing, and whether failures can be reduced to exact shortest counterexamples.

- Cycle 1 froze 24 reference models and 144 unreplaced mutants.
- Cycle 2 froze three testing methods and a black-box reducer before exact classification.
- Cycle 3 froze ten oracle expectations before implementing an independent paired-state breadth-first oracle; the oracle matched all ten expectations; all 144 mutants were distinguishable; the 80% viability gate passed; and the complete 1,296-row raw benchmark was generated.

Raw detection counts are currently:

| Method | 64 | 256 | 1,024 |
|---|---:|---:|---:|
| uniform random | 125 | 142 | 144 |
| lexicographic breadth | 82 | 118 | 131 |
| transition coverage guided | 106 | 140 | 143 |

These are raw observations, not final H1–H3 dispositions. The complete result has not yet been repeated byte-identically, interpreted, or closed.

- Study 004 overview: [`research/studies/004-finite-state-conformance/README.md`](research/studies/004-finite-state-conformance/README.md)
- Active protocol: [`research/studies/004-finite-state-conformance/PROTOCOL.md`](research/studies/004-finite-state-conformance/PROTOCOL.md)
- Cycle 3 audit: [`research/studies/004-finite-state-conformance/CYCLE_3_ORACLE_AND_RAW_RESULTS.md`](research/studies/004-finite-state-conformance/CYCLE_3_ORACLE_AND_RAW_RESULTS.md)
- Raw transport: [`research/studies/004-finite-state-conformance/CYCLE_3_RAW_TRANSPORT.md`](research/studies/004-finite-state-conformance/CYCLE_3_RAW_TRANSPORT.md)
- Raw manifest: [`research/studies/004-finite-state-conformance/data/cycle3_raw_manifest_v1.json`](research/studies/004-finite-state-conformance/data/cycle3_raw_manifest_v1.json)
- Study 003 report: [`research/studies/003-protocol-integrity/REPORT.md`](research/studies/003-protocol-integrity/REPORT.md)

Passing Study 004 would not show superiority on arbitrary software, production correctness, security value, or method novelty outside the frozen synthetic domain.

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex autonomously selects the highest-value bounded internal work item.
4. Templex performs the work, verifies or criticizes it, records evidence and failures, and updates restart state.
5. Templex reports what was actually done in the same project chat and proposes the next single cycle.
6. The laboratory stops until another `承認` is received.

The next approval may perform Study 004 Cycle 4 only: reproduce the complete output byte-identically, apply the frozen H1–H3 rules, write the final report, close Issue #10, and close Study 004. No fifth cycle is permitted.

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
- [`research/studies/004-finite-state-conformance/README.md`](research/studies/004-finite-state-conformance/README.md) — active Study 004
- [`research/studies/001-autonomous-game-design/REPORT.md`](research/studies/001-autonomous-game-design/REPORT.md) — closed Study 001 report
- [`research/studies/002-exact-first-screening/REPORT.md`](research/studies/002-exact-first-screening/REPORT.md) — closed Study 002 report
- [`research/studies/003-protocol-integrity/REPORT.md`](research/studies/003-protocol-integrity/REPORT.md) — closed Study 003 report
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
