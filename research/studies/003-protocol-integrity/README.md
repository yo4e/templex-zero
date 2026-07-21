# Study 003 — Protocol Integrity Under Approval-Gated Autonomous Research

## Status

**Active. Cycle 2 of at most 4 is complete.**

Study 003 tests whether a declarative research contract can distinguish valid approval-gated research traces from traces containing evidence contamination, authorization mismatch, cap violations, undisclosed correction, silent artifact mutation, or approval-token reuse.

## Frozen authority

- Proposal: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- Final proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- Active protocol: `PROTOCOL.md`
- Tracking issue: #7

## Cycle 1 — schema and corpus

- Schema and canonical serialization: `src/templex_zero/protocol_integrity/schema.py`
- Deterministic corpus generator: `src/templex_zero/protocol_integrity/corpus.py`
- Auditable bundle generator: `src/templex_zero/protocol_integrity/bundle.py`
- Regeneration script: `experiments/generate_protocol_integrity_corpus.py`
- Frozen corpus index: `data/synthetic_corpus_v1/index.json`
- Tests: `tests/test_protocol_integrity_corpus.py`
- Setup audit: `CYCLE_1_SETUP_AUDIT.md`

Corpus summary:

- 36 synthetic traces;
- 10 valid and 26 invalid;
- 12 minimal traces, 4 composite valid traces, and 20 mutants;
- 528 events total;
- canonical SHA-256 `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`.

## Cycle 2 — synthetic correctness gate

- Incremental primary validator: `src/templex_zero/protocol_integrity/validator.py`
- Independent whole-trace oracle: `src/templex_zero/protocol_integrity/oracle.py`
- Deliberately weak order-only baseline: `src/templex_zero/protocol_integrity/baseline.py`
- Gate aggregation: `src/templex_zero/protocol_integrity/synthetic_gate.py`
- Formal runner: `experiments/run_protocol_integrity_synthetic_gate.py`
- Tests: `tests/test_protocol_integrity_validators.py`
- Full result: `data/synthetic_gate_v1.json`
- Audit: `CYCLE_2_SYNTHETIC_GATE.md`

The first gate passed:

- false accepts: 0;
- false rejects: 0;
- first-violation-index accuracy: 100%;
- violation-class accuracy: 100%;
- reason-code accuracy: 100%;
- primary/oracle agreement: 100%;
- mutants rejected: 20 / 20;
- named beyond-ordering cases accepted by the weak baseline: `P2-I`, `P3-I`, `P5-I`, and `P6-I`.

Formal result SHA-256: `46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de`.

The validator, oracle, and baseline are now frozen. No historical trace has yet been encoded or evaluated.

## Next bounded unit

Cycle 3 may encode exactly the four precommitted historical traces from cited Study 001 and Study 002 records, then evaluate them using the frozen validator and oracle without code changes or repair. Any mismatch is a historical-transfer failure and must remain visible.
