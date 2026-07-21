# Study 003 Cycle 4 — Reproduction, Synthesis, and Closure

_Date: 2026-07-21 (Asia/Tokyo)_

## Disposition

**Study 003 closed with methodological success under bounded claims.**

All four frozen hypotheses are supported. The final deterministic report integrates the frozen 36-trace synthetic result and four-trace historical result, verifies every consumed result row and frozen identifier, and was generated twice with byte-identical output. No Study 004 was started.

## Final artifacts

- Complete runner: `experiments/run_protocol_integrity_complete_report.py`
- Runner Git blob: `ab5bfe161ab5a39febc1ed8905d46a28016fc114`
- Targeted test: `tests/test_protocol_integrity_complete_report.py`
- Complete result: `data/complete_validation_v1.json`
- Complete result Git blob: `62b0836a3abc2ce96fa74f045b8fbf5628916e55`
- Internal deterministic SHA-256: `a52d00e08e00855ad9f43b3988e8f64bf9dc03d3d81f87c7c090f52247ec60a4`
- Complete result file SHA-256: `5f8d1e6d399957745b233f4807406a01ea0ae98af580cd3adba77becf4265904`
- Final report: `REPORT.md`

## Coverage and result

- Synthetic traces: 36; events: 528.
- Historical traces: 4; events: 44.
- Total: 40 traces; 572 events.
- H1 synthetic correctness: supported.
- H2 mutation detection: supported.
- H3 historical transfer: supported.
- H4 beyond ordering: supported.
- Methodological disposition: `success_with_bounded_claims`.

## Verification

- Targeted complete-report tests: **2 passed**.
- `compileall` for the new runner and test: passed.
- Two final report runs were byte-identical.
- The checked-in complete-result Git blob matched the locally produced bytes.
- The live runner Git blob matched the locally tested source.
- The synthetic result, historical artifact, historical result, primary, oracle, and baseline identifiers matched their frozen values.

## Reproduction boundary

Fresh checkout remained unavailable because the environment could not resolve `github.com`, and connector file results could not be mounted directly into the local runtime. The final runner was executed against a functional projection containing every live result field it consumes; connector retrieval verified the values, row ordering, and source Git blobs. Cycle 2 and Cycle 3 had already performed and repeated raw synthetic and historical validation. Cycle 4 reproduced deterministic integration and consistency, not a new fresh-checkout replay of all raw traces.

This limitation is compatible with the final bounded disposition but must remain attached to any claim of reproducibility.

## Pre-result correction

The first complete-runner draft expected all four composite valid rows before their mutants. Comparison with the frozen synthetic-result ordering showed that result rows are grouped as each composite valid trace followed by its five mutants. The expected order was corrected before formal complete output. No verdict, corpus item, historical expectation, instrument, or hypothesis disposition changed.

## Claim boundary

Passing Study 003 shows procedural enforcement only for the frozen fourteen-event vocabulary, six dependency classes, thirty-six specification-derived synthetic traces, and four preselected repository histories. It does not establish substantive truth, research value, safety, legality, novelty, autonomy, scientific quality, or completeness of the declared contract.

## Human intervention

Yoshie Yamada supplied the plain project-chat `承認`, classified as A1 access assistance. Templex selected the final runner, tests, interpretation, disposition, limitations, documentation, and closure actions. No human selected or edited a verdict or hypothesis disposition.

## Closure

- Issue #7 is to be closed as completed.
- `STATE.md` is to record no active study.
- Study 003 artifacts are archived and may receive only factual or technical corrections.
- The next approval, if any, may assess whether another study is warranted; it must not automatically start Study 004.
