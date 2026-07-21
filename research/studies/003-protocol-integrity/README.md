# Study 003 — Protocol Integrity Under Approval-Gated Autonomous Research

## Status

**Closed — methodological success with bounded claims.**

Study 003 tested whether a declarative research contract could distinguish valid approval-gated research traces from traces containing evidence contamination, authorization mismatch, cap violations, undisclosed correction, silent artifact mutation, or approval-token reuse.

## Final result

- H1 synthetic correctness: supported.
- H2 mutation detection: supported.
- H3 historical transfer: supported.
- H4 beyond ordering: supported.
- Frozen synthetic corpus: 36 traces, 10 valid and 26 invalid, 528 events.
- Mutants rejected: 20 / 20.
- Synthetic false accepts / false rejects: 0 / 0.
- Historical expected-verdict, first-violation, and primary/oracle matches: 4 / 4.
- Weak order-only baseline false accepts: 12.
- Final complete report: 40 traces, 572 events, byte-identical across two runs.

Final disposition: `success_with_bounded_claims`.

## Artifacts

- Proposal: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- Archived protocol: `PROTOCOL.md`
- Final report: `REPORT.md`
- Cycle 1 audit: `CYCLE_1_SETUP_AUDIT.md`
- Cycle 2 audit: `CYCLE_2_SYNTHETIC_GATE.md`
- Cycle 3 audit: `CYCLE_3_HISTORICAL_TRANSFER.md`
- Cycle 4 audit: `CYCLE_4_CLOSURE.md`
- Synthetic corpus: `data/synthetic_corpus_v1/`
- Synthetic result: `data/synthetic_gate_v1.json`
- Historical traces: `data/historical_traces_v1.json`
- Historical result: `data/historical_transfer_result_v1.json`
- Complete result: `data/complete_validation_v1.json`

## Claim boundary

The study supports procedural enforcement only for the frozen fourteen-event vocabulary, six dependency classes, specification-derived synthetic corpus, and four preselected repository histories. It does not establish substantive truth, research value, safety, legality, novelty, autonomy, or scientific quality. The artifacts are research prototypes, not production authorization or security infrastructure.

## Archive rule

Do not modify the frozen instruments, corpus, expectations, historical traces, or results except for factual or technical corrections. Do not reopen Study 003 to add cases. A later study would require a separate proposal and approval sequence.
