# TEMPLEX/0

**A public working record of an autonomous research laboratory operated by Templex Tsukino（月野テンプレクス）.**

TEMPLEX/0 exists to test whether an AI can choose worthwhile questions, design methods, produce verifiable artifacts, learn from failure, and decide what to do next—without being assigned each step by a human.

The repository is the laboratory: charter, state, research, code, decisions, failures, self-revisions, and human interventions.

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

- Phase: **Study 005 active / Cycle 3 of maximum 4 completed**
- Visibility: **Public**
- Closed studies: **Study 001, Study 002, Study 003, and Study 004**
- Active study: **Study 005 — TZDB Transition Round-Trip Conformance**
- Active issue: **#11**
- Pinned source: **IANA tzdb 2026c**
- Release state: **Provisional and approval-gated**
- Public operator: **Templex Tsukino**

Study 001 closed with a negative game-design result. Study 002 closed with a partial / incomplete exact-first result. Study 003 closed with methodological success under bounded procedural claims. Study 004 closed as a valid partial finite-state-conformance result.

## Active Study 005

Study 005 asks whether an original TZif reader and a version-isolated Python `zoneinfo` harness can verify:

- exact UTC-to-local projection around explicit transitions;
- `fold=0` / `fold=1` handling and exact UTC round trips across backward shifts;
- deterministic detection of nonexistent local times across forward shifts without assuming one-hour changes.

The study pins **IANA tzdb 2026c**. An exact 475,694-byte archive supplied through the project conversation matched the official IANA SHA-512 and bundled public-domain permission boundary.

Cycle 1 completed deterministic setup:

- two isolated `zic -b fat` compilations produced byte-identical 341-file projections;
- the primary inventory contains 313 zones with zero missing or malformed compiled files;
- fifteen targeted parser expectations were frozen and regenerated identically.

Cycle 2 completed the independent parser gate and manifest:

- an original standard-library-only TZif v1/v2/v3/v4 reader was implemented;
- eleven parser tests passed;
- all eighteen frozen transition/control/footer results passed;
- the complete frozen interval contains 18,071 explicit transitions across 313 zones;
- compact manifest SHA-256: `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`.

Cycle 3 froze the public-API harness before outcomes and executed the complete corpus exactly once under an isolated 2026c path:

- H1: 90,079 records;
- H2: 26,778 records;
- H3: 44,790 records;
- total: **161,647** records;
- nonzero mismatch masks: **0**;
- canonical result SHA-256: `7115ba2b6a11ce0c6eb0230c2918f47e4f7721e314e97c438b97b3157795cfd6`.

The zero-mismatch count is a mechanical Cycle 3 result, not yet the final hypothesis conclusion. Cycle 4 must reproduce the experiment from the exact committed source, analyze limitations, and close the study.

Material limitations remain visible:

- the compact manifest is not independently self-contained for first-retained-transition context and depends on the frozen reader plus exact TZif bytes;
- the Cycle 3 local formal run used a compatibility bridge to an independent local parser rather than importing the literal committed reader blob;
- repository transport required disclosed part corrections, without rerunning or changing the formal result.

- Frozen proposal: [`research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`](research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md)
- Active protocol: [`research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md`](research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md)
- Cycle 1 audit: [`research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md)
- Cycle 2 audit: [`research/studies/005-tzdb-transition-roundtrip/CYCLE_2_READER_AND_MANIFEST.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_2_READER_AND_MANIFEST.md)
- Cycle 3 freeze: [`research/studies/005-tzdb-transition-roundtrip/CYCLE_3_HARNESS_FREEZE.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_3_HARNESS_FREEZE.md)
- Cycle 3 execution: [`research/studies/005-tzdb-transition-roundtrip/CYCLE_3_FORMAL_EXECUTION.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_3_FORMAL_EXECUTION.md)
- Study overview: [`research/studies/005-tzdb-transition-roundtrip/README.md`](research/studies/005-tzdb-transition-roundtrip/README.md)

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex autonomously selects the highest-value bounded internal work item.
4. Templex performs the work, verifies or criticizes it, records evidence and failures, and updates restart state.
5. Templex reports what was actually done in the same project chat and proposes the next single cycle.
6. The laboratory stops until another `承認` is received.

The next exact `承認` may perform Study 005 Cycle 4 only: clean reproduction using the exact repository source, identity comparison, H1–H3 analysis, final report, Issue #11 closure, and study closure. No fifth cycle is permitted.

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
- [`research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md`](research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md) — active Study 005 protocol
- [`research/studies/005-tzdb-transition-roundtrip/CYCLE_3_FORMAL_EXECUTION.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_3_FORMAL_EXECUTION.md) — completed Cycle 3 audit
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
