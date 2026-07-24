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
- Human actions at access, publication, safety, identity, and authority boundaries are recorded in [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) and dated continuation records.
- Files may contain mistakes, incomplete implementations, failed hypotheses, provisional interpretations, or conclusions that are later revised or rejected.
- Human authorization of a bounded work cycle enables execution; it does not certify that resulting code or claims are correct.
- Nothing here should be treated as professional advice, validated scientific consensus, production-ready software, or a security-reviewed tool.
- TEMPLEX/0 does not contact, advise, modify, or submit work to outsiders without explicit authorization.

Negative results and visible corrections are intentional parts of the experiment.

## Status

- Phase: **Study 005 active / Cycle 2 of maximum 4 completed**
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

Cycle 1 completed setup without inspecting formal Python outcomes:

- two isolated `zic -b fat` compilations each produced 341 files / 397,559 bytes;
- their complete projections were byte-identical, SHA-256 `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2`;
- the primary inventory contains 313 zones with zero missing or malformed compiled files;
- fifteen targeted parser expectations were frozen and regenerated identically.

Cycle 2 completed the independent parser gate and manifest:

- an original standard-library-only TZif v1/v2/v3/v4 reader was implemented;
- eleven parser tests passed;
- all eighteen frozen transition/control/footer results passed on the first formal gate run;
- the complete frozen interval contains 18,071 explicit transitions across 313 zones;
- backward / zero / forward counts are 8,926 / 187 / 8,958;
- compact manifest SHA-256 is `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`.

The long Cycle 2 persistence path exposed and corrected a truncated base64 part during final validation. The final eight-part layout reconstructs the exact 354,993-byte canonical manifest. Reader behavior and manifest semantic content did not change.

No formal Python `zoneinfo` comparison or H1–H3 result exists yet.

- Frozen proposal: [`research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`](research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md)
- Active protocol: [`research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md`](research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md)
- Cycle 1 audit: [`research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md)
- Cycle 2 audit: [`research/studies/005-tzdb-transition-roundtrip/CYCLE_2_READER_AND_MANIFEST.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_2_READER_AND_MANIFEST.md)
- Study overview: [`research/studies/005-tzdb-transition-roundtrip/README.md`](research/studies/005-tzdb-transition-roundtrip/README.md)

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex autonomously selects the highest-value bounded internal work item.
4. Templex performs the work, verifies or criticizes it, records evidence and failures, and updates restart state.
5. Templex reports what was actually done in the same project chat and proposes the next single cycle.
6. The laboratory stops until another `承認` is received.

The next exact `承認` may perform Study 005 Cycle 3 only: freeze the isolated public-API `zoneinfo` comparison and fold/gap round-trip harness before formal outcomes, prove isolated data-path resolution, execute the complete frozen corpus once, preserve every result, and stop before clean reproduction or final analysis.

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
- [`research/studies/005-tzdb-transition-roundtrip/CYCLE_2_READER_AND_MANIFEST.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_2_READER_AND_MANIFEST.md) — completed Cycle 2 audit
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
