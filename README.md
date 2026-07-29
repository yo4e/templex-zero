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

- Phase: **Active Study 007 / Cycle 1 complete**
- Visibility: **Public**
- Closed studies: **Study 001 through Study 006**
- Active issue: **#13**
- Release state: **Approval-gated**
- Public operator: **Templex Tsukino**

Study 001 closed with a negative game-design result. Study 002 closed with a partial / incomplete exact-first result. Study 003 closed with methodological success under bounded procedural claims. Study 004 closed as a valid partial finite-state-conformance result. Study 005 closed as a positive bounded TZDB transition-round-trip conformance result. Study 006 closed as a valid partial Python tar extraction boundary-conformance result.

## Active Study 007

**SQLite Deferred-Constraint and Savepoint State Conformance** was activated unchanged on 2026-07-29 after live environment revalidation.

The study asks whether one exact local CPython 3.13.5 / SQLite 3.46.1 distribution build follows documented transaction-stack, nested-savepoint, failed-boundary, deferred-foreign-key, and recovery behavior across exactly 72 frozen original declarative sequences when compared with an independently implemented relational and savepoint-state model.

Cycle 1 froze:

- the active protocol, exact schema, action grammar, observations, error mapping, and resource caps;
- exactly 72 sequences in six equal families and 439 total actions;
- manifest SHA-256 `16a01c109b196a1127d7783f110e492e4609713f8f527e50e95d7ef254678b4c`;
- the exact runtime, source ID, compile options, package identities, paths, and binary digests;
- the four-cycle limit and protected-execution boundary.

A material correction was recorded at activation. The local Debian SQLite source ID ends in `alt1`, not the vanilla SQLite 3.46.1 release suffix `1e33`. The study is therefore scoped to package `libsqlite3-0 3.46.1-7+deb13u1` and its exact pinned binary, not the vanilla release artifact or SQLite generally.

Structure-only validation and setup capability preflight passed. No independent model, harness, comparator, hand-gate result, protected sequence result, mismatch, or hypothesis disposition exists yet.

- Active study: [`research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/README.md`](research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/README.md)
- Protocol: [`research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/PROTOCOL.md`](research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/PROTOCOL.md)
- Activation decision: [`research/decisions/2026-07-29-study-007-activation.md`](research/decisions/2026-07-29-study-007-activation.md)
- Tracking issue: [#13](https://github.com/yo4e/templex-zero/issues/13)

The next approval may perform Study 007 Cycle 2 only: implement the independent model, SQLite harness, and comparator; freeze twelve hand-audited traces; pass the correctness gate with at most one bounded implementation correction; freeze the instruments; and stop before the complete 72-sequence matrix.

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
- [`research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/README.md`](research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/README.md) — active Study 007
- [`research/proposals/007-sqlite-deferred-constraint-savepoint-state-conformance.md`](research/proposals/007-sqlite-deferred-constraint-savepoint-state-conformance.md) — frozen pre-activation proposal
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
