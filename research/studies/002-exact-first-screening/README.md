# Study 002 — Exact-First Screening of Compact Games

## Status

**Active. Random comparison cycle 5 of at most 6 is complete.**

Study 002 was activated on 2026-07-16 from the frozen proposal at commit `68fc4c2edb93ca1363e7b7040221b5507cfeb171`.

## Research question

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

This is a methodological study, not a renewed attempt to rescue Span or to produce a publication-ready game.

## Principal artifacts

- [`PROTOCOL.md`](PROTOCOL.md) — active commitments and stopping rules
- [`GRAMMAR.md`](GRAMMAR.md) — candidate grammar, seed, canonicalization, and enumeration order
- [`FIXTURES.md`](FIXTURES.md) — four hand-audited reachable state graphs
- [`MANIFEST_AUDIT.md`](MANIFEST_AUDIT.md) — static generation record
- [`EXACT_INSTRUMENT_AUDIT.md`](EXACT_INSTRUMENT_AUDIT.md) — solver correctness gate
- [`EXACT_SCREEN_ANALYSIS.md`](EXACT_SCREEN_ANALYSIS.md) — exact candidate result and procedural audit
- [`RANDOM_SCREEN_ANALYSIS.md`](RANDOM_SCREEN_ANALYSIS.md) — random result and exact comparison
- [`CYCLE_5_VERIFICATION.md`](CYCLE_5_VERIFICATION.md) — execution and verification record
- [`data/exact_screen_v1.json`](data/exact_screen_v1.json)
- [`data/random_screen_v1.json`](data/random_screen_v1.json)
- [`manifest/index.json`](manifest/index.json)

Implementation:

- `src/templex_zero/exact_first/schema.py`
- `src/templex_zero/exact_first/manifest.py`
- `src/templex_zero/exact_first/solver.py`
- `src/templex_zero/exact_first/bruteforce.py`
- `experiments/run_study_002_exact_screen.py`
- `experiments/compare_study_002_exact_runs.py`
- `experiments/run_study_002_random_screen.py`

## Frozen sample

The manifest contains exactly 18 candidates: 9 on 3×3, 9 on 4×4, and exactly three in each board-size × mechanism-family cell. No candidate was manually ranked, replaced, repaired, or polished after generation.

Compact entry-list SHA-256:

`cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

## Exact instrument and candidate result

The no-reduction memoized solver and an independently written queue-built retrograde oracle agreed on every value in the four frozen fixture graphs before candidate outcomes existed.

The formal exact experiment was committed before candidate inspection at `9a453ccc2a2e1f30691d23028b12b3296ebb4f13`.

| Measure | Result |
|---|---:|
| Candidates | 18 |
| Exactly solved | 15 |
| Time-capped | 3 |
| First-participant exact wins | 9 |
| First-participant exact losses | 6 |
| Exact draws | 0 |
| Solved within 8 optimal plies | 14 / 15 |
| Zero non-losing openings | 6 / 15 |

The twelve-solution continuation threshold passed. Exact repeated-run normalized SHA-256:

`9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`

## Random screen

The random experiment was committed before play at `970b5a7b35b40806b8962c4a73d3841804a95e7a`.

- exactly 2,000 games per candidate;
- 36,000 games total;
- independent per-game seeds derived from the frozen manifest hash, candidate index, and game index;
- uniform selection among current legal actions;
- no exact value or candidate-specific move policy.

| Measure | Result |
|---|---:|
| First-participant wins | 17,656 |
| Second-participant wins | 18,344 |
| Draws | 0 |
| Goal endings | 19,715 |
| No-legal-action endings | 16,285 |
| Mean plies | 6.8161 |

Two byte-identical-script executions agreed on every deterministic field and produced SHA-256:

`d3726b0dff560befc4bbc86fa69b7f9aa889d0e41d16f2a54a3b1acc0df7960e`

## Exact-versus-random result

The frozen false-reassurance definition requires a 40–60% random first-participant decisive rate together with either an exact forced result within eight plies or zero non-losing openings.

Six candidates met that definition:

- `S2-3-AG-02`;
- `S2-3-AG-03`;
- `S2-3-CE-03`;
- `S2-4-AG-01`;
- `S2-4-AG-02`;
- `S2-4-CE-01`.

Nine candidates appeared 40–60% under random play. Seven were exactly solved; six of those seven were false-reassurance cases.

Current evidence supports H1 and H3: random aggregate rates concealed short forced outcomes, complete opening losses, and one-opening-only survival. H2 remains unresolved.

## Procedural limitation

The frozen proposal required the shallow-search heuristic to be generated before exact results were inspected. No heuristic was frozen before cycle 4. A post-result heuristic would not satisfy the requirement, so the formal depth-1/2/3 screen remains cancelled.

Study 002 therefore cannot receive a fully successful methodological disposition. It retains valid exact-versus-random evidence and will close as partial/incomplete.

## Verification limitations

- The random experiment script used for the final two runs was byte-identical to GitHub blob `051ab0fa3de409c38adf35d327ade8111ae597d8`.
- The local schema and manifest were functionally reconstructed and reproduced the frozen manifest hash; byte-identical identity of every dependency is not claimed.
- Four targeted random-screen tests passed and `compileall` succeeded.
- An initial combined foreground execution exceeded its outer command timeout and produced no completed result; it was excluded.
- Fresh clone remained unavailable because the execution environment could not resolve `github.com`.
- The repository has no recorded GitHub Actions workflow.

## Next bounded cycle

Create the final Study 002 report, classify H1 and H3 as supported and H2 as unresolved, separate valid evidence from procedural failure, close Issue #6, set no active study, and stop. Do not add shallow search, another grammar, candidate repair, human playtesting, or prior-art work.
