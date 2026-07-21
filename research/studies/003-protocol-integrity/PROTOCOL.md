# Study 003 Protocol — Protocol Integrity Under Approval-Gated Autonomous Research

_Date activated: 2026-07-21 (Asia/Tokyo)_  
_Date closed: 2026-07-21 (Asia/Tokyo)_  
_Status: **Closed — methodological success with bounded claims**_

## Authority and frozen source

Study 003 activated the unchanged frozen proposal:

- `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- final proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- proposal freeze audit: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY_AUDIT.md`

The research question, hypotheses, fourteen-event vocabulary, six dependency classes, synthetic corpus, mutation inventory, historical expectations, metrics, resource limits, and four-cycle stop rule remained fixed through closure.

## Research question

> Can a machine-readable research contract accept valid approval-gated research-event traces and reject evidence-contaminating, unauthorized, over-cap, or undisclosed-correction traces at the first violating event without study-specific rules?

The protocol evaluated enforcement of declared procedural commitments. It did not determine substantive truth, value, safety, legality, novelty, autonomy, or scientific quality.

## Hypothesis disposition

- **H1 — synthetic correctness: supported.** Thirty-six of thirty-six frozen synthetic traces matched with zero false accepts and false rejects and complete primary/oracle agreement.
- **H2 — mutation detection: supported.** Twenty of twenty frozen mutations were rejected at their precommitted first violation.
- **H3 — historical transfer: supported.** Four of four precommitted repository histories matched after instrument freeze without repair, semantic expansion, or special cases.
- **H4 — beyond ordering: supported.** The full validators rejected all four named stateful invalid traces accepted by the order-only baseline.

## Frozen language and instruments

Exactly fourteen event kinds and six dependency classes were used. No new event kind was added after activation.

Frozen instrument Git blobs:

- primary validator: `71080f1051acc015e74b42de19d56ce8782b9f25`;
- independent oracle: `74159c7a7502975b1bcd376510d5dad0283e03cd`;
- weak order-only baseline: `7af3b9e1db56a90e08b93690a14d90ee541b9d18`.

## Synthetic corpus and gate

- 36 traces: 10 valid and 26 invalid;
- 12 minimal traces, 4 composite valid traces, and 20 deterministic mutants;
- 528 events;
- corpus SHA-256: `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`;
- synthetic result SHA-256: `46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de`;
- false accepts / false rejects: 0 / 0;
- first-index, class, reason, and primary/oracle agreement: 100%;
- mutants rejected: 20 / 20;
- weak baseline false accepts: 12.

## Historical transfer

Exactly four frozen cases were encoded before evaluation.

- `H1-SPAN-FORMAL-VALID`: valid;
- `H2-EXACT-SUBSTUDY-VALID`: valid;
- `H3-STUDY002-SHALLOW-CONTAMINATED`: invalid at index 5, D1, `artifact-not-frozen`;
- `H4-EXACT-PROJECTION-CORRECTION-VALID`: valid.

Historical artifact and result:

- trace Git blob: `840a7779a1cee3ba4f3f88e62342269b804c2719`;
- trace canonical SHA-256: `8cdaec94de2e8a7aff3158924db5e570f4af3008bcb33f18602f584b29b41053`;
- result SHA-256: `c59c621a1efad82ba95ca6eb92465a062b9b412b4fd8f4a05d69dccfcdcdac4a`;
- expected verdict, first violation, and primary/oracle matches: 4 / 4.

## Final deterministic report

The complete report integrates the 36 synthetic and 4 historical result rows.

- coverage: 40 traces and 572 events;
- runner Git blob: `ab5bfe161ab5a39febc1ed8905d46a28016fc114`;
- internal deterministic SHA-256: `a52d00e08e00855ad9f43b3988e8f64bf9dc03d3d81f87c7c090f52247ec60a4`;
- file SHA-256: `5f8d1e6d399957745b233f4807406a01ea0ae98af580cd3adba77becf4265904`;
- result Git blob: `62b0836a3abc2ce96fa74f045b8fbf5628916e55`;
- two final runs: byte-identical.

The final integration used a functional projection of connector-verified live result fields because a fresh checkout and direct connector-file mounting were unavailable. The raw synthetic and historical validations had already been performed and repeated in Cycles 2 and 3.

## Final disposition and claim boundary

Study 003 met its frozen methodological-success criteria within four activation cycles. The supported claim is limited to the frozen trace language, corpus, mutations, and four historical episodes.

A valid trace does not establish that the represented research is true, valuable, safe, legal, ethical, novel, unbiased, autonomous, complete, or scientifically sound. A contract can omit an important dependency and still be followed perfectly.

## Cycle record

- Cycle 1 — schema and 36-trace corpus freeze: complete.
- Cycle 2 — validators, baseline, and first synthetic gate: complete; passed on first attempt.
- Cycle 3 — four-trace historical transfer: complete; 4 / 4 matched without repair.
- Cycle 4 — deterministic integration, synthesis, final report, and closure: complete.

## Archive rule

Study 003 is closed. Its corpus, instruments, expectations, historical traces, and results may receive only factual or technical corrections. Later work may cite them but may not silently expand the study or reinterpret procedural validation as substantive validation of the underlying research.

Final report: `REPORT.md`.

No Study 004 was started during closure.
