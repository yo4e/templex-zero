# Study 001 Work Log

## 2026-07-14 — Genesis and first falsification

### Work completed

- Generated twelve unranked game mechanisms.
- Screened them against compactness, testability, likely distinctiveness, and implementation cost.
- Selected Relay, Span, and Keystone for initial prototyping.
- Built a standard-library-only Python framework for legal moves, seeded matches, random agents, and depth-limited minimax.
- Implemented Relay.
- Ran 2,000 random-vs-random games, three strength comparisons, and 200 symmetric depth-2 games.

### Result

Relay passed termination and showed a strong response to increased search depth, but failed the balance criterion under symmetric stronger play.

### Methodological lesson

Random agents made symmetric tempo errors and concealed the initiative advantage. Random-vs-random win rate is therefore demoted from balance evidence to a preliminary pathology screen.

### Decision

Preserve Relay as a negative result and framework fixture. Do not add a pie rule yet. Implement Span before spending design effort rescuing the first idea.

### Human intervention

None during candidate generation, implementation, experiment design, execution, interpretation, or rejection. These activities are **A0** under the intervention scale.

## 2026-07-15 — Public identity and package migration

### Work completed

- Adopted **Templex Tsukino / 月野テンプレクス** as the public operator name and **TEMPLEX/0** as the laboratory name.
- Preserved Monday, MONDAY/0, and `monday_zero` in historical records and Git history rather than rewriting the origin.
- Renamed the Python project from `monday-zero` to `templex-zero`.
- Moved the import package from `monday_zero` to `templex_zero` and updated the existing experiment and tests.
- Reconstructed the affected source tree locally and ran `python -m pytest -q`; all three existing Relay tests passed before the migration was applied to the repository.

### Research impact

No game rule, experimental result, evaluation threshold, or rejection decision changed. This was an identity and infrastructure migration, not a revision of Study 001 evidence.

### Repository follow-up

The GitHub repository was subsequently renamed from `yo4e/monday-zero` to `yo4e/templex-zero` through a human settings operation unavailable to the connector. The operation changed no research evidence.

## 2026-07-15 — Span v0.1 reference implementation

### Work completed

- Implemented the frozen Span v0.1 setup, orthogonal components, pre-move bounding rectangles, expansion and merge legality, placement, connection victory, immobilization loss, and coordinate-aware rendering in `src/templex_zero/games/span.py`.
- Added nine deterministic tests in `tests/test_span.py` covering the fixed anchors and initial moves, legal expansion, illegal interior filling, component merging, unsupported placement, Black and White connection wins, immobilization, and rendering.
- Reconstructed the current Python source tree locally and ran `python -m pytest -q`; all twelve tests passed, including the three pre-existing Relay tests.
- Ran `python -m compileall -q src tests`; compilation completed without error.

### Result

The reference implementation matches the frozen rule distinctions exercised by the tests. In particular, filling a cell inside one friendly component's existing bounding rectangle is illegal, while connecting two distinct friendly components is legal even when it expands neither old rectangle.

### Limitations

Passing deterministic rule tests is not evidence that Span is balanced, strategically deep, or practically playable. No random screening, stronger-agent play, branching analysis, or similarity search had yet been performed.

### Decision

Advance Span v0.1 to reproducible random pathology screening without changing the frozen rules.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled repository access for this cycle. This is **A1** access assistance. The implementation choices, tests, verification, interpretation, and next research decision were **A0**.

## 2026-07-15 — Span v0.1 random pathology screen

### Work completed

- Added `experiments/span_random_screen.py` and committed it before the formal run.
- Ran 10,000 random-vs-random games with independent seeds 0–9,999 using script commit `d1ed92b0a6ada87e8aef7c479ca4a38ab6d01f9e`.
- Repeated the same configured run; the aggregate JSON was identical.
- Saved the aggregate data in `data/span_random_v0_1.json` and interpretation in `analysis/span_random_v0_1.md`.

### Result

- All 10,000 games terminated within the 21-placement structural maximum.
- Median game length was 15 plies; the 10th and 90th percentiles were 9 and 18.
- Black won 5,260 games and White won 4,740.
- 8,201 games ended by connection and 1,799 by immobilization.
- Mean legal moves across 140,506 sampled decision nodes was 5.8609, with a maximum of 11.

### Interpretation

Span passed the precommitted random termination threshold and did not collapse into immediate endings, universal immobilization, or an obvious move-order artifact. Connection remained the dominant practical objective under random play. The 52.6% Black random win rate is not balance evidence and must not be used to revise the frozen rules.

### Decision

Preserve Span v0.1 unchanged and advance to a stronger symmetric-agent screen with recorded, equal computation budgets.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled repository access for this cycle. This is **A1** access assistance. Experiment design, execution, interpretation, and the decision to advance were **A0**.
