# Study 003 Protocol — Protocol Integrity Under Approval-Gated Autonomous Research

_Date activated: 2026-07-21 (Asia/Tokyo)_  
_Status: **Active — cycle 3 of at most 4 complete**_

## Authority and frozen source

Study 003 activates the unchanged frozen proposal:

- `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- final proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- proposal freeze audit: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY_AUDIT.md`

The activation decision did not alter the research question, hypotheses, event vocabulary, dependency classes, expected verdicts, mutation inventory, historical expectations, metrics, resource limits, or four-cycle stop rule.

## Research question

> Can a machine-readable research contract accept valid approval-gated research-event traces and reject evidence-contaminating, unauthorized, over-cap, or undisclosed-correction traces at the first violating event without study-specific rules?

The study evaluates enforcement of declared procedural commitments. It does not determine whether research is true, worthwhile, creative, safe, unbiased, novel, autonomous, or publication-ready.

## Frozen hypotheses

- **H1 — synthetic correctness:** the primary validator and independent oracle classify all frozen synthetic traces correctly, agree on first violation and class, and produce zero false accepts and false rejects after at most one correction cycle.
- **H2 — mutation detection:** all twenty frozen contamination mutations are rejected at their precommitted first violating event.
- **H3 — historical transfer:** after the synthetic gate and validator freeze, four Study 001/002 traces match their frozen dispositions without validator changes or identifier-specific rules.
- **H4 — beyond ordering:** the full validators reject at least four stateful invalid traces accepted by the frozen order-only baseline.

## Frozen event vocabulary and dependencies

Exactly fourteen event kinds are permitted:

`begin_cycle`, `end_cycle`, `freeze_artifact`, `set_cap`, `begin_execution`, `finish_execution`, `observe`, `authorize`, `external_action`, `record_defect`, `invalidate_evidence`, `apply_correction`, `disclose_correction`, and `accept_evidence`.

No new semantic event kind may be added inside Study 003.

Dependency classes remain:

1. **D1:** artifact freeze before protected observation.
2. **D2:** exact-scope authorization before external action, with single-use token consumption.
3. **D3:** governing cap before execution and recorded usage within that cap.
4. **D4:** defect recording, invalidation, correction, required rerun or re-observation, and disclosure before corrected evidence acceptance.
5. **D5:** no silent digest change after protected observation; dependent evidence must be invalidated and replacement evidence regenerated.
6. **D6:** fresh matching approval token for every non-overlapping bounded cycle.

## Frozen synthetic corpus

- 12 minimal traces, 4 composite valid traces, and 20 deterministic mutants.
- **36 traces total: 10 valid and 26 invalid.**
- 528 events; maximum 20 events in one trace.
- Artifact: `data/synthetic_corpus_v1/index.json`.
- Canonical SHA-256: `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`.

## Frozen validation instruments

- Primary validator: `src/templex_zero/protocol_integrity/validator.py` — Git blob `71080f1051acc015e74b42de19d56ce8782b9f25`.
- Independent oracle: `src/templex_zero/protocol_integrity/oracle.py` — Git blob `74159c7a7502975b1bcd376510d5dad0283e03cd`.
- Weak order-only baseline: `src/templex_zero/protocol_integrity/baseline.py` — Git blob `7af3b9e1db56a90e08b93690a14d90ee541b9d18`.

These instruments are frozen. Historical-transfer mismatches may not be repaired by changing them.

## First synthetic correctness gate

- Result: `data/synthetic_gate_v1.json`.
- Audit: `CYCLE_2_SYNTHETIC_GATE.md`.
- Result SHA-256: `46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de`.
- Passed on the first attempt.
- False accepts and false rejects: zero.
- First-index, class, reason, and primary/oracle agreement: 100%.
- Mutants rejected: 20 / 20.
- Weak baseline accepted twelve invalid traces, including `P2-I`, `P3-I`, `P5-I`, and `P6-I`.
- Source-level identifier-specific verdict branches found: zero.

The single permitted correction cycle is unused.

## Historical transfer

Cycle 3 encoded and evaluated exactly the four frozen cases:

1. `H1-SPAN-FORMAL-VALID` — valid;
2. `H2-EXACT-SUBSTUDY-VALID` — valid;
3. `H3-STUDY002-SHALLOW-CONTAMINATED` — invalid at event index 5, D1, `artifact-not-frozen`;
4. `H4-EXACT-PROJECTION-CORRECTION-VALID` — valid.

Artifacts:

- Trace file: `data/historical_traces_v1.json`.
- Trace Git blob: `840a7779a1cee3ba4f3f88e62342269b804c2719`.
- Trace internal canonical SHA-256: `8cdaec94de2e8a7aff3158924db5e570f4af3008bcb33f18602f584b29b41053`.
- Result: `data/historical_transfer_result_v1.json`.
- Result SHA-256: `c59c621a1efad82ba95ca6eb92465a062b9b412b4fd8f4a05d69dccfcdcdac4a`.
- Audit: `CYCLE_3_HISTORICAL_TRANSFER.md`.

Result:

- expected-verdict matches: 4 / 4;
- first-violation matches: 4 / 4;
- primary/oracle agreement: 4 / 4;
- no new event kind, validator change, expectation change, or identifier-specific exception was required.

H1, H2, H3, and H4 have now met their precommitted component conditions. Final disposition remains pending Cycle 4 reproduction and synthesis.

## Resource boundaries

- standard-library-only implementation;
- exactly 36 synthetic and 4 historical traces;
- at most 40 events per trace and 1,600 events per complete final run;
- no network, paid compute, external service, third-party action, or human subjects;
- at most four approval-driven cycles after activation, including final synthesis.

## Cycle record

- **Cycle 1 — schema and corpus freeze: complete.**
- **Cycle 2 — validators and first synthetic gate: complete.** The gate passed and instruments were frozen.
- **Cycle 3 — historical transfer: complete.** All four frozen expectations matched without repair.
- Cycle 4 — complete deterministic reproduction, synthesis, final report, and closure: pending.

## Intervention model

A plain project-chat `承認` is A1 access assistance for one bounded cycle. Templex selects implementation, interpretation, debugging, failure diagnosis, and stopping decisions within this protocol. External communication, publication, spending, permissions, and human-subject activity remain separately gated.
