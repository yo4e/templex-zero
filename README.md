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

- Phase: **No active study / portfolio assessment pending**
- Visibility: **Public**
- Closed studies: **Study 001 through Study 006**
- Active issue: **None**
- Release state: **Approval-gated**
- Public operator: **Templex Tsukino**

Study 001 closed with a negative game-design result. Study 002 closed with a partial / incomplete exact-first result. Study 003 closed with methodological success under bounded procedural claims. Study 004 closed as a valid partial finite-state-conformance result. Study 005 closed as a positive bounded TZDB transition-round-trip conformance result. Study 006 closed as a valid partial Python tar extraction boundary-conformance result.

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

The retained mismatch was `META-NONEXEC-01`: expected mode `0600`, observed mode `0644` in both runs. File bytes, ownership, successful extraction, destination containment, and sentinel integrity matched. The frozen expectation remained failed and unchanged.

| Hypothesis | Final disposition |
|---|---|
| H1 destination containment and protected rejection | Supported |
| H2 stateful containment | Supported |
| H3 safe-control preservation and metadata normalization | Unsupported |
| **Overall** | **Valid partial bounded result** |

The result is specific to the pinned local runtime, filesystem, non-privileged boundary, explicit filter, and synthetic matrix. It does not certify arbitrary tar archives or general extraction safety.

- Final report: [`research/studies/006-python-tar-extraction-boundary-conformance/REPORT.md`](research/studies/006-python-tar-extraction-boundary-conformance/REPORT.md)
- Cycle 4 audit: [`research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_4_REPRODUCTION_AND_CLOSURE.md`](research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_4_REPRODUCTION_AND_CLOSURE.md)
- Reproduction artifacts: [`research/studies/006-python-tar-extraction-boundary-conformance/results/cycle4/README.md`](research/studies/006-python-tar-extraction-boundary-conformance/results/cycle4/README.md)
- Closed issue: [#12](https://github.com/yo4e/templex-zero/issues/12)

## Study 005 final result

Study 005 pinned IANA tzdb 2026c and compared an original TZif reader with isolated public-API Python `zoneinfo` behavior across 313 canonical zones and 18,071 explicit transitions.

| Hypothesis | Records | Mismatches | Final disposition |
|---|---:|---:|---|
| H1 UTC projection | 90,079 | 0 | Supported |
| H2 backward fold and UTC round trip | 26,778 | 0 | Supported |
| H3 forward gap classification | 44,790 | 0 | Supported |
| **Total** | **161,647** | **0** | **Positive bounded result** |

- Final report: [`research/studies/005-tzdb-transition-roundtrip/REPORT.md`](research/studies/005-tzdb-transition-roundtrip/REPORT.md)
- Cycle 4 audit: [`research/studies/005-tzdb-transition-roundtrip/CYCLE_4_REPRODUCTION_AND_CLOSURE.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_4_REPRODUCTION_AND_CLOSURE.md)

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex performs one bounded repository cycle under the approval protocol.
4. Templex verifies or criticizes the work, records evidence and failures, updates restart state, and reports.
5. The laboratory stops until another `承認` is received.

The next exact `承認` may perform one post-Study-006 portfolio assessment only: predeclare a threshold, compare multiple distinct directions plus inactivity, freeze at most one inactive proposal, and stop before activation, implementation, or experiment.

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
- [`research/studies/006-python-tar-extraction-boundary-conformance/REPORT.md`](research/studies/006-python-tar-extraction-boundary-conformance/REPORT.md) — latest closed-study report
- [`research/studies/005-tzdb-transition-roundtrip/REPORT.md`](research/studies/005-tzdb-transition-roundtrip/REPORT.md) — preceding closed-study report
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
