# Span v0.1 Disposition

_Date: 2026-07-15 (Asia/Tokyo)_

## Decision

**Rejected in its frozen v0.1 form.**

## Evidence

- The reference implementation and deterministic rule tests pass.
- A 10,000-game random pathology screen terminated reliably and did not reveal the decisive defect.
- A symmetric depth-2 minimax smoke screen produced 200 Black wins in 200 games, all by connection on ply 5.
- Exploratory equal-depth checks at depths 1–4 produced the same five-ply Black result in 100 games per depth.
- Most importantly, `tests/test_span_forced_line.py` exhaustively enumerates every legal White reply after Black opens C2 and confirms that Black can always continue C3 and C4 to connect the fixed C1 and C5 anchors on ply 5. C4–C3–C2 is the reflected equivalent.

## Criterion failure

Study 001 precommitted that first-player win rate under the strongest available symmetric agent should fall between 40% and 60%, excluding draws. A constructive forced first-player win is a stronger failure than an out-of-range sample estimate.

## Rule preservation

`RULES.md` remains the frozen v0.1 baseline and must not be edited to conceal this result. Any future repair must create a new version with its own precommitted evaluation.

## Next action

Do not spend the next cycle rescuing Span. Recover the existing Keystone candidate description, resolve any ambiguity, and freeze Keystone v0.1 rules before implementation or play results.

## Evidence links

- `../../analysis/span_minimax_smoke_v0_1.md`
- `../../data/span_minimax_smoke_v0_1.json`
- `../../../../../src/templex_zero/span_agents.py`
- `../../../../../tests/test_span_forced_line.py`
- `../../../../../experiments/span_minimax_smoke.py`
