# Study 003 Protocol — Protocol Integrity Under Approval-Gated Autonomous Research

_Date activated: 2026-07-21 (Asia/Tokyo)_  
_Status: **Active — cycle 2 of at most 4 complete**_

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

## Frozen event vocabulary

Exactly fourteen event kinds are permitted:

`begin_cycle`, `end_cycle`, `freeze_artifact`, `set_cap`, `begin_execution`, `finish_execution`, `observe`, `authorize`, `external_action`, `record_defect`, `invalidate_evidence`, `apply_correction`, `disclose_correction`, and `accept_evidence`.

No new semantic event kind may be added inside Study 003.

## Frozen dependency classes

1. **D1:** artifact freeze before protected observation.
2. **D2:** exact-scope authorization before external action, with single-use token consumption.
3. **D3:** governing cap before execution and recorded usage within that cap.
4. **D4:** defect recording, invalidation, correction, required rerun or re-observation, and disclosure before corrected evidence acceptance.
5. **D5:** no silent digest change after protected observation; dependent evidence must be invalidated and replacement evidence regenerated.
6. **D6:** fresh matching approval token for every non-overlapping bounded cycle.

## Frozen synthetic corpus

Cycle 1 generated the proposal-defined corpus without verdict execution:

- 12 minimal traces: one valid and one invalid for each dependency class;
- 4 composite valid traces;
- 20 deterministic mutants from five operators applied once to each composite trace;
- **36 traces total: 10 valid and 26 invalid**;
- 528 total events; maximum 20 events in one trace.

Mutation operators are fixed to prerequisite omission, adjacent dependency inversion, unauthorized insertion, cap violation, and undisclosed correction.

Machine-readable artifact:

- `data/synthetic_corpus_v1/index.json`
- canonical SHA-256: `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`

## Frozen validation instruments

Cycle 2 implemented and froze:

- incremental state-machine validator: `src/templex_zero/protocol_integrity/validator.py` — Git blob `71080f1051acc015e74b42de19d56ce8782b9f25`;
- independently written whole-trace prefix oracle: `src/templex_zero/protocol_integrity/oracle.py` — Git blob `74159c7a7502975b1bcd376510d5dad0283e03cd`;
- deliberately weak order-only baseline: `src/templex_zero/protocol_integrity/baseline.py` — Git blob `7af3b9e1db56a90e08b93690a14d90ee541b9d18`.

The oracle does not import the primary module and does not share its transition, state, verdict, reason-code, or first-violation helpers. The baseline checks only whether prerequisite event kinds occur earlier and ignores identities, values, scopes, token consumption, digests, evidence lineage, and correction state.

These instruments are frozen after the passing first synthetic gate. Historical-transfer mismatches may not be repaired by changing them.

## First synthetic correctness gate

Result:

- file: `data/synthetic_gate_v1.json`;
- audit: `CYCLE_2_SYNTHETIC_GATE.md`;
- result SHA-256: `46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de`;
- gate passed on the first attempt.

Metrics:

- zero false accepts;
- zero false rejects;
- 100% first-violation-index accuracy;
- 100% violation-class accuracy;
- 100% reason-code accuracy;
- 100% primary/oracle agreement;
- all twenty mutants rejected;
- no source-level study-, path-, candidate-, or trace-ID-specific verdict branch found.

The weak baseline accepted twelve invalid traces, including the four frozen beyond-ordering examples `P2-I`, `P3-I`, `P5-I`, and `P6-I`. H1, H2, and the synthetic component of H4 are supported at this stage. H3 remains untested.

Because the first gate passed, the single permitted correction cycle is unused. Cycle 3 is historical transfer only.

## Historical transfer boundary

Cycle 3 may encode and evaluate exactly four frozen historical cases:

1. `H1-SPAN-FORMAL-VALID` — expected valid;
2. `H2-EXACT-SUBSTUDY-VALID` — expected valid;
3. `H3-STUDY002-SHALLOW-CONTAMINATED` — expected invalid at `observe(exact_results)`, D1;
4. `H4-EXACT-PROJECTION-CORRECTION-VALID` — expected valid.

Each trace must cite repository source paths and commits. It must use only the frozen event vocabulary and generic contract data. After the first historical trace is encoded, no validator, oracle, baseline, synthetic fixture, or historical expectation may change. Any mismatch, new semantic requirement, or identifier-specific exception is a historical-transfer failure and is reported without repair.

## Resource boundaries

- standard-library-only implementation;
- exactly 36 synthetic and 4 historical traces;
- at most 40 events per trace and 1,600 events per complete final run;
- no network, paid compute, external service, third-party action, or human subjects;
- at most four approval-driven cycles after activation, including final synthesis.

## Cycle record

- **Cycle 1 — schema and corpus freeze: complete.** Active protocol created; schema, canonical serialization, deterministic generator, 36-trace artifact, and tests added. No verdict logic or historical traces were created.
- **Cycle 2 — validators and first synthetic gate: complete.** The primary, oracle, and weak baseline were implemented; the first gate passed; instruments are frozen; no historical trace was encoded.
- Cycle 3 — historical transfer: pending.
- Cycle 4 — reproduction, synthesis, and closure: pending.

## Intervention model

A plain project-chat `承認` is A1 access assistance for one bounded cycle. Templex selects implementation, interpretation, debugging, failure diagnosis, and stopping decisions within this protocol. External communication, publication, spending, permissions, and human-subject activity remain separately gated.
