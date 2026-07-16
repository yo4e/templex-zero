# Span v0.2 Formal Cycle Verification Note

_Date: 2026-07-16 (Asia/Tokyo)_

## Executed checks

- Compiled `experiments/span_v0_2_formal_screen.py` locally before the formal run.
- Ran the formal configuration twice: 10,000 random games and 1,000 equal-budget depth-3 games per run.
- Verified byte-identical JSON output with SHA-256 `93f55d3c5e9cacf86aec7bbecdf351fc661f2f5ecbfdefb1f7e05c08482e56d2`.
- Ran the new exhaustive opening test locally: one test passed, covering all six openings and all required intervening replies.
- The previous complete reconstructed suite contained 52 passing cases. No game, agent, or match source changed in this cycle; the only Python additions were the experiment script and the exhaustive regression test.

## Environment limitation

A fresh `git clone` was attempted but the execution container could not resolve `github.com`. The repository has no GitHub Actions workflow. Therefore this cycle did not rerun the complete 53-case suite in one fresh checkout. The new test and experiment were verified against locally reconstructed current Span v0.2 modules, while the unchanged prior 52 cases retain their previous recorded pass result.

This limitation does not affect the experiment output or the constructive opening diagnosis, but it is recorded to avoid presenting a nonexistent remote-CI result.
