# Study 004 Cycle 3 — Oracle Gate, Corpus Classification, and Raw Benchmark

_Date: 2026-07-23 (Asia/Tokyo)_

## Disposition

**Cycle 3 completed.** The independent exact oracle passed its pre-frozen fixture gate; all 144 unreplaced mutants were classified as distinguishable; the frozen 80% viability gate passed; and the complete 1,296-row raw benchmark was generated and stored.

This cycle does **not** assign H1, H2, or H3 dispositions and does not close Study 004. Final analysis, deterministic reproduction, report, and normal closure remain Cycle 4.

## Protected execution order

1. Ten hand-authored oracle fixture pairs and expected results were committed before oracle implementation or execution.
2. The independent paired-state breadth-first oracle was then implemented and committed.
3. The oracle was tested only against the frozen fixture set.
4. After the gate passed, the already frozen 144-mutant corpus was reconstructed and hash-checked.
5. The corpus was classified without replacement.
6. Only after the 80% viability gate passed were the frozen Cycle 2 methods and reducer executed.

No corpus, method, reducer, budget, hypothesis, threshold, seed, or mutation inventory was changed after protected information was generated.

## Oracle fixture freeze

- fixtures: **10**;
- equivalent expectations: **2**;
- distinguishable expectations: **8**;
- expected shortest lengths: 1 through 4;
- frozen fixture file SHA-256: `c3dbd66b2260918f1f3b0071d39655d00f4734f3ef427dd2dd0796c4d4e3281e`;
- fixture commit: `2a32a84d80b9eb30afdcceb52031a8250a88f604`;
- freeze record: `ORACLE_FIXTURE_FREEZE.md`.

The first attempted gate command was run from the wrong working directory and stopped with `FileNotFoundError` before fixture loading or oracle evaluation. No expected result or oracle source was changed. The same frozen files were then executed from the repository root. The protocol's bounded oracle-correction allowance was not used.

## Independent oracle

- source: `src/templex_zero/finite_state_conformance/oracle.py`;
- Git blob: `6eb6205dc32877446201b34d5a591e9851cfd69f`;
- SHA-256: `75b9b7bbbe2fe2f9370f29cbc1f44114481d6b21730d8044feb8faec3e743396`;
- implementation: breadth-first search over reachable pairs of hidden states;
- action order: `a0 < a1 < a2`;
- imports neither testing methods, coverage planning, black-box execution, reducer, nor corpus generation.

Fixture gate result: **10 / 10 expected classifications and exact shortest traces matched**. Oracle tests: **3 passed**.

## Frozen corpus gate

Before classification, regenerated Cycle 1 artifacts matched all frozen identities:

- corpus payload SHA-256: `c9897631050b937d31a3273ba8cdabc55b79be1d66a0f4ca2e5c6df9f7c79fdb`;
- corpus file SHA-256: `82fcd584661e4860167ff114041868b923adb6861395a249564af4ff771b8fa2`;
- model payload SHA-256: `7925911d9f834d71a360defc862d8d67262989eb2e957cf334b94a1b3a58202b`;
- model file SHA-256: `bf3eab9884381a634d90803d3367c4700c8553ac43ec112355b2881dc4aaa902`.

Classification result:

- mutants: **144**;
- distinguishable: **144**;
- equivalent: **0**;
- viability requirement: **116 distinguishable mutants**;
- viability disposition: **passed**.

Shortest distinguishing-length distribution:

| Length | Mutants |
|---:|---:|
| 1 | 16 |
| 2 | 32 |
| 3 | 52 |
| 4 | 28 |
| 5 | 9 |
| 6 | 4 |
| 7 | 2 |
| 8 | 1 |

## Complete raw benchmark

- mutants: 144;
- methods: 3;
- budgets: 64, 256, 1,024 actions;
- raw rows: **1,296**;
- runner: `experiments/run_finite_state_conformance_cycle3.py`;
- runner Git blob: `e85a462d8bfd9fcda5ae80566e11f83fda4ffb30`;
- runner SHA-256: `6bb1a72bf417fab089553291a42509dc59f2b77c59aafe9285f93710f4958a4b`.

Raw detection counts:

| Method | 64 | 256 | 1,024 |
|---|---:|---:|---:|
| uniform random | 125 | 142 | 144 |
| lexicographic breadth | 82 | 118 | 131 |
| transition coverage guided | 106 | 140 | 143 |

Raw exact-length reduction counts among detected rows:

| Method | 64 | 256 | 1,024 |
|---|---:|---:|---:|
| uniform random | 105 | 121 | 129 |
| lexicographic breadth | 82 | 118 | 131 |
| transition coverage guided | 106 | 140 | 143 |

These are raw observations, not hypothesis dispositions. In particular, the 256-action aggregate is not interpreted here even though it does not show the precommitted coverage-guided advantage over random testing. Cycle 4 must apply the exact frozen H1–H3 rules, including mutation-class analysis and the union-of-detected denominator for H3.

## Raw evidence identities

- manifest: `data/cycle3_raw_manifest_v1.json`;
- canonical gzip stored through eight ordered base64 text parts;
- gzip bytes: `29,400`;
- gzip SHA-256: `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679`;
- decompressed JSON bytes: `899,730`;
- JSON SHA-256: `a725f287b3d3a09b5d8e991e82daf9cb8f6a719c528a2e4047524cfd289bfc3c`;
- internal payload SHA-256: `bb34844aee696cde0ea19de9c48a5bd5ec8faf66391a492bc6277bf24ac69927`;
- transport details: `CYCLE_3_RAW_TRANSPORT.md`.

The eight live part blobs matched the locally tested blobs. `tests/test_finite_state_conformance_cycle3.py` reconstructed the gzip, verified outer and inner hashes, checked the exact corpus and benchmark grid, and confirmed that no final hypothesis or study disposition was embedded.

## Verification

Functional reconstruction results:

- oracle and raw-integrity tests: **6 passed**;
- compile verification: passed;
- frozen Cycle 1 corpus hashes matched;
- frozen Cycle 2 behavioral projection matched before formal execution;
- live oracle, runner, and eight transport-part blobs matched locally tested bytes.

The complete benchmark was run once in Cycle 3. Byte-identical full rerun is deliberately reserved for Cycle 4 under the protocol.

## Verification limits

A fresh checkout again failed because the environment could not resolve `github.com`. Verification used a functional reconstruction from live GitHub sources and blob-identical new files. The complete historical repository suite and GitHub Actions were not run.

The synthetic corpus is internally generated and does not establish transfer to real software, production correctness, security value, or method novelty.

## Human intervention

Yoshie Yamada supplied the plain project-chat `承認`, classified as A1 access assistance. Templex independently wrote and froze fixture expectations, implemented and gated the oracle, classified the corpus, executed the raw benchmark, recorded failures and limits, and selected Cycle 4. The human did not choose fixture values, code, classifications, benchmark outcomes, interpretation, or next work.

## Next bounded cycle

Cycle 4 must reconstruct and rerun the complete raw result generation, require byte-identical output for full methodological success, apply the frozen H1–H3 criteria without modifying instruments or data, write the final report, close Issue #10, archive or close the protocol state, synchronize repository state, and end Study 004. No fifth cycle is permitted.
