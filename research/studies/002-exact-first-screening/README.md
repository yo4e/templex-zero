# Study 002 — Exact-First Screening of Compact Games

## Status

**Closed on 2026-07-18 with a partial / incomplete methodological result.**

The authoritative synthesis is [`REPORT.md`](REPORT.md).

Study 002 tested whether exact opening analysis could reveal structure concealed by random aggregate rates in a frozen family of autonomously generated compact deterministic placement games.

## Final disposition

- **H1 supported:** six candidates met the pre-defined false-reassurance condition.
- **H2 unresolved:** the required shallow-search heuristic was not frozen before exact outcomes were inspected, so no valid depth-1/2/3 comparison exists.
- **H3 supported:** exact opening values supplied structural explanations hidden by aggregate random win rates.
- Overall study disposition: **partial / incomplete**, not fully successful.

No candidate is advanced as a finished game. The study makes no claim of fun, fairness, strategic depth, teachability, accessibility, originality, or product readiness.

## Frozen sample

The manifest contains exactly eighteen candidates:

- nine on 3×3 boards and nine on 4×4 boards;
- three mechanism families;
- exactly three candidates in every board-size × mechanism-family cell;
- no manual ranking, replacement, repair, or polishing after generation.

Compact entry-list SHA-256:

`cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

## Exact result

The no-reduction memoized solver passed a frozen tiny-fixture correctness gate against an independently written retrograde oracle before candidate outcomes existed.

Formal exact experiment commit:

`9a453ccc2a2e1f30691d23028b12b3296ebb4f13`

| Measure | Result |
|---|---:|
| Candidates | 18 |
| Exactly solved | 15 |
| Time-capped | 3 |
| First-participant exact wins | 9 |
| First-participant exact losses | 6 |
| Exact draws | 0 |
| Decisive within 8 optimal plies | 14 / 15 |
| Zero non-losing openings | 6 / 15 |

Corrected repeated-run normalized SHA-256:

`9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`

## Random result

Formal random experiment commit:

`970b5a7b35b40806b8962c4a73d3841804a95e7a`

- 2,000 games per candidate; 36,000 total.
- 17,656 first-participant wins.
- 18,344 second-participant wins.
- No draws.
- 19,715 goal endings and 16,285 no-legal-action endings.
- Mean duration: 6.8161 plies.

Two complete executions produced deterministic SHA-256:

`d3726b0dff560befc4bbc86fa69b7f9aa889d0e41d16f2a54a3b1acc0df7960e`

## False reassurance

The frozen diagnostic required a random first-participant decisive rate from 40% through 60% together with either a decisive exact result within eight plies or zero non-losing openings.

Six candidates met it:

- `S2-3-AG-02`;
- `S2-3-AG-03`;
- `S2-3-CE-03`;
- `S2-4-AG-01`;
- `S2-4-AG-02`;
- `S2-4-CE-01`.

Nine candidates appeared 40–60% under random play. Seven were exactly solved, and six of those seven were false-reassurance cases.

## Procedural failure

The frozen proposal required a declarative-feature shallow heuristic to be generated before exact results were inspected. No heuristic was frozen in cycles 1–3. Exact outcomes were then inspected in cycle 4.

A post-result heuristic could not satisfy the pre-result requirement. The formal shallow screen was cancelled, H2 remained unresolved, and the study was not extended to repair the defect.

## Principal artifacts

- [`REPORT.md`](REPORT.md) — final synthesis and disposition
- [`PROTOCOL.md`](PROTOCOL.md) — frozen commitments and closure record
- [`GRAMMAR.md`](GRAMMAR.md) — grammar, seed, canonicalization, and ordering
- [`FIXTURES.md`](FIXTURES.md) — hand-audited state graphs
- [`MANIFEST_AUDIT.md`](MANIFEST_AUDIT.md) — generation audit
- [`EXACT_INSTRUMENT_AUDIT.md`](EXACT_INSTRUMENT_AUDIT.md) — solver correctness gate
- [`EXACT_SCREEN_ANALYSIS.md`](EXACT_SCREEN_ANALYSIS.md) — exact candidate analysis
- [`RANDOM_SCREEN_ANALYSIS.md`](RANDOM_SCREEN_ANALYSIS.md) — random and exact comparison
- [`CYCLE_5_VERIFICATION.md`](CYCLE_5_VERIFICATION.md) — random execution verification
- [`data/exact_screen_v1.json`](data/exact_screen_v1.json)
- [`data/random_screen_v1.json`](data/random_screen_v1.json)
- [`manifest/index.json`](manifest/index.json)

## Closure boundary

Study 002 is immutable except for factual or technical corrections. Do not add a retroactive heuristic, second grammar, candidate repair, symmetry rescue, human playtest, prior-art survey, paid compute, or product work under this study.

Study 003 was not started in the closure cycle.
