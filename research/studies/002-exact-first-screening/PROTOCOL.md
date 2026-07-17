# Study 002 Protocol — Exact-First Screening of Compact Games

_Date activated: 2026-07-16 (Asia/Tokyo)_  
_Status: **Active — random comparison cycle 5 of at most 6 completed**_

## Authority and frozen source

This protocol implements the frozen proposal:

- `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`
- final pre-result proposal commit: `68fc4c2edb93ca1363e7b7040221b5507cfeb171`

The research question, candidate family, exact caps, random-game count, false-reassurance definition, stopping boundaries, and six-cycle limit remain frozen. Recorded procedural defects do not authorize retroactive repair.

## Research question

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

The study evaluates a screening method. It does not treat exact solvability or random win rates as evidence of fun, elegance, fairness, strategic depth, teachability, or originality.

## Precommitted hypotheses

- **H1:** Some candidates that appear approximately balanced under random play will contain short exact forced outcomes or highly concentrated optimal openings.
- **H2:** Increasing shallow search depth will reduce, but not necessarily eliminate, disagreement with exact opening analysis.
- **H3:** Exact-first analysis will provide a clearer rejection reason than aggregate win rates for at least some candidates.

## Frozen candidate family

The sample contains exactly 18 deterministic placement games:

- 9 on 3×3 and 9 on 4×4;
- three mechanism families;
- exactly three candidates in every board-size × family cell;
- no movement, capture, swap, chance, scoring, repetition, or pass;
- at most 16 placements;
- core rules at or below 250 words.

The grammar, seed `2026071602`, enumeration, canonicalization, and tuples were committed before any result. Manual ranking or replacement is prohibited.

Frozen manifest:

- `research/studies/002-exact-first-screening/manifest/index.json`
- compact entry-list SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

## Exact-analysis instrument

The standard-library-only memoized full-width solver returns outcome from the participant-to-move perspective, outcome-preserving terminal distance, every legal opening value, opening counts, expanded-state count, and explicit cap status.

Outcome order is `win > draw > loss`. Wins use the shortest outcome-preserving distance, losses the longest, and draws the shortest as a deterministic convention. A capped solve publishes no partial root value.

Before candidate solving, this solver agreed with an independently written queue-built retrograde oracle on all twelve reachable states of four frozen fixtures, all action values, state counts, and the retained symmetry claims.

Audit:

- `research/studies/002-exact-first-screening/EXACT_INSTRUMENT_AUDIT.md`

## Frozen exact resource boundaries

- Maximum 2,000,000 expanded states per candidate.
- Maximum 30 measured seconds per candidate.
- Maximum 25,000,000 expanded states across the study.
- Frozen manifest order.
- At least 12 exact solutions required.
- Capped candidates remain unsolved; caps may not be raised.

## Exact candidate result

Cycle 4 formal experiment commit:

`9a453ccc2a2e1f30691d23028b12b3296ebb4f13`

Artifacts:

- `research/studies/002-exact-first-screening/data/exact_screen_v1.json`
- `research/studies/002-exact-first-screening/EXACT_SCREEN_ANALYSIS.md`

Results:

- 15 of 18 solved exactly;
- 9 of 9 on 3×3 and 6 of 9 on 4×4 solved;
- 9 first-participant exact wins, 6 losses, no draws;
- 14 of 15 solved candidates had a decisive exact result within 8 plies;
- 6 had zero non-losing openings;
- 3 reached the 30-second time cap;
- the minimum-solved threshold passed;
- the trivial-majority failure condition did not trigger.

Two runs agreed on all exact and classification fields. A post-run comparator removed only wall-clock-dependent state counts from the reproducibility projection and produced identical normalized SHA-256:

`9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`

## Frozen random screen

The random screen was specified before exact inspection:

- 2,000 games per candidate;
- independent fixed seeds derived from the frozen candidate index;
- uniform random choice among current legal actions;
- participant results, duration, terminal reason, opening distribution, and branching recorded;
- no exact value or candidate-specific policy used in move selection.

Random play is termination and gross-pathology evidence plus an approximate signal. It is not balance evidence.

Cycle 5 formal experiment commit:

`970b5a7b35b40806b8962c4a73d3841804a95e7a`

Artifacts:

- `research/studies/002-exact-first-screening/data/random_screen_v1.json`
- `research/studies/002-exact-first-screening/RANDOM_SCREEN_ANALYSIS.md`

Results:

- 36,000 games completed;
- 17,656 first-participant wins;
- 18,344 second-participant wins;
- no draws;
- 19,715 goal endings;
- 16,285 no-legal-action endings;
- mean duration 6.8161 plies.

Two complete runs used a GitHub-byte-identical experiment script and produced the same deterministic SHA-256:

`d3726b0dff560befc4bbc86fa69b7f9aa889d0e41d16f2a54a3b1acc0df7960e`

## Exact-versus-random comparison

A false-reassurance case is an exactly solved candidate where random play gives a 40–60% first-participant decisive rate while exact analysis finds either a decisive forced result within 8 plies or zero non-losing openings.

Six candidates met the frozen definition:

- `S2-3-AG-02`;
- `S2-3-AG-03`;
- `S2-3-CE-03`;
- `S2-4-AG-01`;
- `S2-4-AG-02`;
- `S2-4-CE-01`.

Nine candidates appeared in the 40–60% random interval. Seven were exactly solved; six of those seven were false-reassurance cases.

## Shallow screen — formally unavailable

The frozen proposal requires the shallow-search heuristic to be generated from declarative rule features before exact results are inspected. No heuristic was frozen in cycles 1–3. Exact results are now known.

Therefore:

- no post-result heuristic will be represented as precommitted;
- the formal depth-1/2/3 shallow screen is cancelled;
- H2 remains unresolved;
- the full methodological-success condition cannot be met.

This is a protocol-design failure, not permission to change the proposal.

## Hypothesis disposition before final report

- **H1: supported by valid evidence.** Six pre-defined false-reassurance cases were observed.
- **H2: unresolved.** The required pre-result heuristic does not exist.
- **H3: supported by valid evidence.** Exact opening analysis supplied clearer structural explanations than aggregate random rates for several candidates.

Cycle 6 must confirm these classifications in the final report and close the study as partial/incomplete.

## Cycle limit

- Cycle 1: protocol, schema, fixtures, grammar, seed — complete.
- Cycle 2: deterministic manifest freeze — complete.
- Cycle 3: exact-instrument correctness gate — complete.
- Cycle 4: frozen exact candidate screen — complete.
- Cycle 5: frozen random screen and exact comparison — complete.
- Cycle 6: synthesis and closure as partial/incomplete.

The study may not expand into a repaired heuristic, second grammar, candidate replacement, game polishing, prior-art review, human playtesting, paid compute, or product development.

## Verification limitations

- Fresh clone remained unavailable because the execution environment could not resolve `github.com`.
- The random experiment script was byte-identical to live GitHub; the reconstructed dependencies reproduced the frozen manifest hash, but byte-identical identity of every dependency is not claimed.
- The repository has no recorded GitHub Actions workflow.

## Intervention model

A plain project-chat `承認` is A1 access assistance for one bounded cycle. Templex selects implementation details, interpretation, and stopping decisions. External communication, publication, spending, permission changes, third-party actions, and human-subject activity remain separately gated.
