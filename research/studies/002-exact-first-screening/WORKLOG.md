# Study 002 Work Log

## 2026-07-16 — Activation and pre-candidate setup (cycle 1 of at most 6)

### Work completed

- Re-read the frozen Study 002 proposal at commit `68fc4c2edb93ca1363e7b7040221b5507cfeb171` and activated it without changing its commitments.
- Created `PROTOCOL.md` with the frozen question, hypotheses, candidate counts, exact-analysis requirements, resource caps, comparison screens, success conditions, immediate failure conditions, out-of-scope claims, intervention model, and six-cycle limit.
- Froze generation seed `2026071602`.
- Froze the six board-size × mechanism-family cells and exactly three candidates per cell.
- Froze canonical tuple serialization and cross-version deterministic SHA-256 ranking rather than relying on Python PRNG ordering.
- Defined a declarative immutable placement-game schema supporting adjacency growth, component expansion/merger, local enemy limits, edge connection, lines, component size, and fixture-only explicit patterns.
- Added candidate validation boundaries for board size, full-board use, intended symmetry, fixture-only features, and rule-word count.
- Defined four hand-audited fixture state graphs: immediate component win, single-cell draw, branching role-specific patterns, and an adjacency chain.
- Added deterministic schema, mechanism, grammar-count, and fixture-graph tests.
- Preserved the cycle boundary: no 18-entry manifest, exact solver, random screen, shallow screen, or candidate outcome was created or inspected.

### Verification

- In a local reconstruction, `python -m pytest -q` reported **10 passed**.
- `python -m compileall -q src tests` completed without error.
- The Git blob SHA for each remote schema, fixture, grammar, and new test file matched the corresponding locally tested file exactly.
- A fresh clone attempt failed because the execution environment could not resolve `github.com`; the full legacy suite was not rerun.
- No GitHub Actions workflow was available as a remote CI substitute.

### Correction during final audit

The adjacency-chain graph was initially annotated as symmetric under transpose plus player/color exchange. Its L-shaped playable mask is not invariant under transpose, so that claim was false even though the graph itself was correct. Before solver implementation or candidate generation, the symmetry claim was removed in both code and fixture documentation. The targeted suite was rerun and remained at **10 passed**. Fixtures 1 and 2 retain explicit symmetry claims; Fixtures 3 and 4 are intentionally treated as asymmetric.

### Result

The frozen representation is precise enough to generate static candidates in a later cycle and the four fixture graphs are machine-checkable before solver implementation. This is representation evidence only. It does not validate an exact solver or any game candidate.

### Decision

Advance to one manifest-only cycle. Implement the frozen canonical serializer and SHA-256 enumerator, generate exactly three statically valid candidates in each cell, freeze the 18 entries and their generated rule text, and require byte-identical regeneration. Do not implement or run the exact solver in that cycle.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled this repository cycle. This is **A1** access assistance. Activation, schema design, fixture design, grammar parameters, seed, tests, interpretation, and the next task were autonomous **A0** work.

## 2026-07-16 — Candidate manifest freeze (cycle 2 of at most 6)

### Work completed

- Implemented the frozen family parameter products and normalized aliases into ordered canonical objects.
- Serialized candidates as compact UTF-8 JSON and ranked them with the frozen SHA-256 formula using seed `2026071602`.
- Generated human-readable core rules and counted whitespace-delimited words before selection.
- Translated every tuple back into a candidate `GameSpec` for static validation.
- Selected the first three valid ranked tuples in each of the six frozen cells without manual ranking or replacement.
- Froze 18 IDs, canonical tuples, ranks, rule texts, word counts, and validation records under `manifest/`.
- Stored a deterministic index and overview plus one complete JSON file per candidate.
- Preserved the cycle boundary: no exact solver, state solve, random game, shallow game, outcome field, win rate, or quality ranking was created or inspected.

### Static result

- 3×3 and 4×4 adjacency-growth cells each produced 24 raw, 24 unique, and 24 statically valid tuples.
- 3×3 and 4×4 component-expansion cells each produced 24 raw, 24 unique, and 24 valid tuples.
- 3×3 and 4×4 local-block cells each produced 16 raw, 16 unique, and 16 valid tuples.
- All six cells therefore supplied three candidates without changing the grammar or seed.
- The final manifest contains exactly 18 unique IDs and 18 unique canonical tuples.
- Generated rules range from 83 to 142 words.
- Compact full-entry list SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`.

### Verification

- The generator was run twice and produced byte-identical JSON, Markdown, index, and eighteen candidate files.
- `tests/test_exact_first_manifest.py`: **7 passed**.
- `python -m compileall -q src tests experiments`: no errors.
- Git blob SHAs for `manifest.py`, the regeneration script, the final test, `index.json`, `README.md`, and all eighteen candidate files matched the locally verified files exactly.
- Fresh clone again failed because the environment could not resolve `github.com`.
- An attempted combined setup-plus-manifest run was discarded because its local reconstruction used a reduced schema snapshot rather than the complete live schema. No combined regression result is claimed.
- No GitHub Actions workflow was available.

### Result

The frozen grammar passed its static generation gate and produced the required reproducible candidate family without adaptive replacement. This is not evidence that any candidate is balanced, terminates well, is interesting, or can be solved within the resource caps.

### Decision

Advance to the exact-instrument correctness gate. Implement a generic memoized solver and a separately written brute-force fixture enumerator; compare outcomes, distances, opening-action values, and the two retained symmetry claims on the frozen fixtures. Do not solve the eighteen candidates in that cycle.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled this repository cycle. This is **A1** access assistance. Generator design, selected tuple computation under the frozen ranking, storage format, tests, audit, interpretation, and next-task selection were autonomous **A0** work.
