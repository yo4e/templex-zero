# State

_Last updated: 2026-07-21_

## Phase

**Study 003 active / first synthetic gate passed / validators frozen / cycle 2 of at most 4 complete**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

- Study 001: negative autonomous-game-design conclusion; do not reopen or create Span v0.3.
- Study 002: partial / incomplete exact-first result; H1 and H3 supported, H2 unresolved; do not add its missing shallow heuristic or replace its frozen candidates.

## Active Study 003

- Title: **Protocol Integrity Under Approval-Gated Autonomous Research**
- Frozen proposal: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- Final proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- Active protocol: `research/studies/003-protocol-integrity/PROTOCOL.md`
- Tracking issue: #7
- Cycle limit: 4 approval-driven cycles including closure.

Research question:

> Can a machine-readable research contract accept valid approval-gated research-event traces and reject evidence-contaminating, unauthorized, over-cap, or undisclosed-correction traces at the first violating event without study-specific rules?

## Frozen corpus

- Exactly 36 synthetic traces: 10 valid and 26 invalid.
- Composition: 12 minimal traces, 4 composite valid traces, 20 deterministic mutants.
- Five mutation operators, each represented four times.
- Total events: 528; maximum trace length: 20.
- Canonical corpus SHA-256: `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`.

## Cycle 2 result

The first synthetic correctness gate passed.

- Result: `research/studies/003-protocol-integrity/data/synthetic_gate_v1.json`
- Audit: `research/studies/003-protocol-integrity/CYCLE_2_SYNTHETIC_GATE.md`
- Result SHA-256: `46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de`.
- False accepts: 0.
- False rejects: 0.
- First-violation-index accuracy: 100%.
- Violation-class accuracy: 100%.
- Reason-code accuracy: 100%.
- Primary/oracle agreement: 100%.
- Mutants rejected: 20 / 20.
- The weak baseline accepted twelve invalid traces, including `P2-I`, `P3-I`, `P5-I`, and `P6-I`.
- Source-level study-, path-, candidate-, or trace-ID-specific verdict branches found: 0.

Targeted validator tests passed 8 cases; `compileall` passed. Two formal runs produced byte-identical result files.

## Frozen instruments

- Primary validator blob: `71080f1051acc015e74b42de19d56ce8782b9f25`.
- Independent oracle blob: `74159c7a7502975b1bcd376510d5dad0283e03cd`.
- Weak baseline blob: `7af3b9e1db56a90e08b93690a14d90ee541b9d18`.

These instruments may not change inside Study 003. The single correction cycle is unused because the first gate passed.

## Verification limits

- The formal gate used frozen bundle files whose hashes matched the corpus index.
- Fresh clone, full-repository regression, and GitHub Actions verification were not performed.
- The earlier Cycle 1 corpus-test suite was not rerun in the same functional reconstruction.
- No historical trace has been encoded or evaluated.

## Next action

Cycle 3 only:

1. encode exactly the four precommitted historical traces with repository source paths and commits;
2. keep the validator, oracle, baseline, synthetic corpus, and historical expectations unchanged;
3. evaluate the historical traces with the frozen primary and oracle;
4. report any mismatch without repair or new event kinds;
5. do not begin final synthesis or Study 004.

## Human action currently needed

None.
