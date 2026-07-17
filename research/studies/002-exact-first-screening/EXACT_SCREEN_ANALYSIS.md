# Study 002 Exact Candidate Screen

_Date: 2026-07-17 (Asia/Tokyo)_  
_Status: **15 of 18 solved; continuation threshold passed; shallow-screen precommit defect discovered**_

## Scope

This cycle ran only the frozen exact candidate screen. It did not run random games, shallow search, candidate replacement, symmetry reduction, or rule repair.

The formal experiment was committed before candidate outcomes were inspected:

- experiment commit: `9a453ccc2a2e1f30691d23028b12b3296ebb4f13`;
- frozen manifest SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`;
- per-candidate cap: 2,000,000 expanded states and 30 measured seconds;
- study-wide cap: 25,000,000 expanded states;
- minimum exact solutions: 12.

The complete compact result is `data/exact_screen_v1.json`.

## Exact result

| Measure | Result |
|---|---:|
| Frozen candidates | 18 |
| Exactly solved | 15 |
| Unsolved at time cap | 3 |
| Solved 3×3 candidates | 9 / 9 |
| Solved 4×4 candidates | 6 / 9 |
| Root wins for first participant | 9 |
| Root losses for first participant | 6 |
| Root draws | 0 |
| Exact distances at or below 2 plies | 4 / 15 |
| Exact distances at or below 8 plies | 14 / 15 |
| Candidates with zero non-losing openings | 6 / 15 |

The continuation threshold passed: 15 is greater than the precommitted minimum of 12. The degenerate-grammar failure condition did not trigger because only 4 of 15 solved candidates terminated on or before ply 2.

All nine 3×3 candidates solved. The three unsolved entries were:

- `S2-4-CE-02`;
- `S2-4-LB-01`;
- `S2-4-LB-03`.

Each reached the 30-second time cap rather than the state cap. The study-wide state cap was not approached.

## Opening structure

Six solved candidates were exact losses for the first participant and had no non-losing legal opening:

- `S2-3-AG-01` — loss in 2;
- `S2-3-AG-02` — loss in 6;
- `S2-3-CE-02` — loss in 2;
- `S2-3-CE-03` — loss in 6;
- `S2-4-AG-03` — loss in 2;
- `S2-4-CE-03` — loss in 2.

Among exact first-participant wins, opening concentration varied:

- four candidates had every opening winning;
- `S2-3-LB-01` and `S2-3-LB-02` had five winning and four losing openings;
- `S2-4-AG-01` and `S2-4-CE-01` had only one winning opening among four;
- `S2-4-LB-02` had twelve winning and four losing openings and was the only solved candidate whose optimal root distance exceeded eight plies.

These are game-theoretic opening results. They do not establish fun, fairness, depth, or originality.

## Repeated execution and correction

The formal script was executed twice under the same configuration.

Run summaries agreed on:

- 15 solved and 3 unsolved candidates;
- every solved root outcome and distance;
- every solved opening-action value;
- every solved reachable-state count;
- all cap classifications;
- all aggregate classifications except timing-dependent state totals.

The raw projection hashes differed:

- run 1: `f2bbf7441eb20c940e7c835c478caca1bf0b58740555a66e86a396ba8b839890`;
- run 2: `f40fd7317abdba180da38615b327eccdc43ed05805bb503aa8147fc56e585e2b`.

The cause was isolated within this cycle. The original experiment projection incorrectly treated the number of states expanded before a wall-clock time cap as deterministic. The three time-capped candidates expanded slightly different numbers of states between runs, while all exact and classification fields remained identical.

A separate comparator was committed after this discrepancy was observed. It preserves the raw measurements but excludes only elapsed time, total expanded states across a time-limited run, and per-candidate expanded states when the candidate ended specifically at the time cap. The corrected normalized hash was identical in both runs:

`9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`

This is a transparent post-run correction to reproducibility classification, not a change to candidate rules, solver values, caps, or outcomes.

## Procedural defect discovered after exact inspection

A final protocol audit found a more serious sequencing defect.

The frozen proposal requires the shallow-search heuristic to be generated from declarative rule features **before exact results are inspected**. The activation plan then scheduled:

1. exact instrument;
2. exact candidate solves;
3. approximate screens.

No heuristic definition or implementation was frozen in cycles 1–3. Exact outcomes have now been inspected. Therefore a heuristic created from this point onward cannot honestly satisfy the frozen pre-result requirement, even if its code uses only declarative fields.

No post-result shallow heuristic will be represented as precommitted evidence. The shallow depth-1/2/3 screen is cancelled as a formal Study 002 measurement.

This defect does not invalidate the exact values or the preconfigured random screen. Random play requires no heuristic and remains capable of testing the random false-reassurance part of H1 and contributing to H3. It does prevent Study 002 from meeting its full methodological-success condition and leaves H2 unresolved.

## Decision

Study 002 remains active for two final bounded cycles:

- **Cycle 5:** run the frozen random screen only, for all 18 candidates, without consulting exact values in move selection and without creating a shallow heuristic;
- **Cycle 6:** synthesize exact-versus-random evidence, classify H1 and H3, mark H2 unresolved, record the sequencing failure, and close the study as partial/incomplete rather than fully successful.

The study will not be extended beyond cycle 6 to repair the heuristic precommit defect.
