# State

_Last updated: 2026-07-16_

## Phase

**No active study / Study 001 closed**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Study 001 result

Study 001 asked whether Templex could independently design a compact deterministic two-player abstract strategy game whose automated play showed meaningful strategic depth and reasonable balance.

The study is closed with a **negative research conclusion**.

- Relay was rejected after equal depth-2 play produced 129 first-player wins, 12 second-player wins, and 59 unresolved 200-ply games.
- Span v0.1 was rejected after exhaustive reply enumeration proved a five-ply Black connection through C2–C3–C4 or its reflection.
- Keystone v0.1 was rejected after only 50.9% of 2,000 fixed-seed random games completed by 200 plies.
- Span v0.2, the only selected one-change revision, was rejected after equal depth-3 play produced 1,000 second-participant wins and exhaustive analysis proved every legal opening loses for the first participant.

The final synthesis is:

- `research/studies/001-autonomous-game-design/REPORT.md`

Supporting material remains in the study's rules, implementations, tests, experiment scripts, machine-readable data, analyses, decisions, and work log.

## What Study 001 established

- A complete autonomous loop can generate mechanisms, freeze rules, implement them, run seeded experiments, detect misleading metrics, construct counterexamples, preserve negative evidence, and stop against its own artifact.
- Random parity is useful for pathology screening but was repeatedly anti-diagnostic for balance.
- Version freezing and explicit stop rules prevented unbounded post-result repair.
- No design survived with evidence sufficient for the target claim.

## What remains unresolved

Study 001 did not establish fun, elegance, actual teachability, human strategic depth, accessibility, genuine originality, or equivalence to existing games. Prior-art review was not performed because no candidate reached the viability stage required for an originality claim.

## Verification status

- Key formal scripts were committed before execution and recorded seeds, configurations, and code versions.
- Later configured runs were repeated with identical aggregate or byte-identical output.
- Deterministic tests covered rule distinctions and constructive Span forcing lines.
- The repository had no GitHub Actions workflow; verification relied on locally reconstructed live files.
- The final Span v0.2 forced-opening test passed locally. A single fresh-checkout 53-case run was not recorded, though the prior 52-case suite had passed and no game or agent source changed during the final formal screen.

## Next actions

1. Do not alter Study 001 except to correct factual or technical errors.
2. Do not create Span v0.3 or silently continue candidate repair under the closed protocol.
3. On a later approval, inspect the closed report and decide whether a separately scoped Study 002 is justified.
4. If a Study 002 proposal is justified, draft its question, boundaries, stopping rules, and protocol before beginning experiments.
5. External publication, promotion, submissions, spending, or permission changes remain separately gated.

## Human action currently needed

None.
