# Span v0.2 Disposition

_Date: 2026-07-16 (Asia/Tokyo)_

## Decision

**Reject frozen Span v0.2.**

Do not alter this version in place. Preserve its frozen rules, reference implementation, agents, tests, formal data, and negative evidence.

## Decisive evidence

The formal script was committed before execution at `edac024671aeb380472e0a6a58a8eb35a134e124`.

- 10,000 random games all terminated, with first-participant wins at 51.98%. This is pathology evidence only.
- 1,000 equal-budget depth-3 games produced 1,000 second-participant wins, zero first-participant wins, and zero swaps.
- Every symmetric game ended in six placements with a White connection.
- Repeating the full configured run produced a byte-identical JSON file with SHA-256 `93f55d3c5e9cacf86aec7bbecdf351fc661f2f5ecbfdefb1f7e05c08482e56d2`.

A deterministic exhaustive test then covered every legal opening:

- C2 and C4 lose because the second participant swaps and completes the known Black central line.
- B1, B5, D1, and D5 lose because the second participant remains White and forces B3–C3–D3 or its reflection.

All required intervening first-participant replies were enumerated. The second participant has a constructive forced win after every legal first placement.

## Protocol result

The first-participant decisive win rate is 0%, outside the required 40–60% interval. The failure is stronger than a statistical balance miss because the opening is solved constructively for the second participant.

## No further repair inside Study 001

Span v0.2 was the only selected one-change revision after Relay, Span v0.1, and Keystone v0.1 failed. Repairing v0.2 would require changing anchors, opening geometry, connection distance, or adding another balancing device. That would exceed the precommitted single-change revision and start a new design project rather than complete this study.

Cancel strategic-signal tournaments and prior-art review for Span v0.2. They cannot rescue a game with a forced participant win from the initial state.

## Study consequence

Study 001 should conclude negatively after final synthesis. It succeeded as a reproducible falsification process but did not produce a surviving game that supports the target claim.
