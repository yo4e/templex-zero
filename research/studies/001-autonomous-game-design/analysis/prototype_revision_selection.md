# Initial Prototype Comparison and Revision Selection

_Date: 2026-07-16 (Asia/Tokyo)_

## Decision

Select **Span v0.2** as the only revision target for the next Study 001 cycle.

The revision adds one opening swap rule and changes nothing else. Relay and Keystone remain rejected in their current forms and are not revised in parallel.

## Comparison method

The three prototypes are compared against the precommitted Study 001 protocol rather than by recency, aesthetic preference, or random win-rate parity. The relevant questions are:

1. How strong is the evidence that the observed failure belongs to the rules rather than the measurement?
2. Can one small, legible rule change address the diagnosed failure?
3. Does that change preserve the prototype's defining mechanism?
4. Does the revised game remain compact and falsifiable?

## Common comparison

| Prototype | Evidence strength | Confirmed useful evidence | Decisive failure | Smallest plausible repair | Repair cost and risk | Disposition |
|---|---|---|---|---|---|---|
| Relay | Moderate | Random games terminate; stronger agents clearly outperform random agents | Depth-2 symmetric play produced 129 first-player wins, 12 second-player wins, and 59 200-ply draws | A swap rule for initiative **and** a repetition or no-progress rule for cycling | At least two independent changes; one fixes balance but not cycling, the other fixes cycling but not initiative | Do not revise now |
| Span v0.1 | Strong | 10,000 random games all terminate; typical duration is short; implementation and symmetric search instrumentation pass tests | Exhaustive reply enumeration proves Black can force C2–C3–C4, or its reflection, and win on ply 5 | One opening swap rule | One standard, visible change; preserves anchors, expansion, merge, connection, immobilization, and finite duration | Select v0.2 |
| Keystone v0.1 | Strong for the tested termination criterion | Structural victories can occur at practical lengths; implementation and rule tests pass | Only 50.9% of 2,000 random games complete by 200 plies; the long population exhausts reserves and enters extended shifting | Restrict shifting, add a movement phase or no-progress limit, or add a new terminal score | Each candidate either changes the defining reversible-control mechanism, adds bookkeeping, or merely relabels censorship as a draw | Do not revise now |

## Measurement weakness versus ruleset failure

### Relay

Depth-2 minimax does not solve Relay, and the hand-built heuristic may distort the exact magnitude of the advantage. The 59 games stopped at the 200-ply limit also do not prove literal cycles.

Those limitations weaken a claim about Relay's theoretical value, but not its practical rejection under the study protocol. The strongest available symmetric instrument showed an extreme first-participant skew among decisive games and a substantial unresolved population. A swap rule alone would not address the unresolved population; a repetition rule alone would not address initiative.

### Span v0.1

The decisive evidence is not a sample estimate or heuristic preference. Every legal White reply after Black opens C2 was enumerated, and Black can still play C3 then C4. The reflected opening is equivalent. This is a constructive ruleset failure.

The earlier random screen is still useful evidence: Span terminates reliably, remains compact, and does not need a duration repair. Its failure is concentrated in opening ownership.

### Keystone v0.1

Random play cannot establish Keystone's balance or optimal duration, but random play is the protocol's deliberate gross-termination screen. Keystone missed the 98% requirement by 47.1 percentage points in a repeated fixed-seed run. The longer-horizon follow-up showed impractical duration rather than a mere 200-ply measurement accident.

The pathology is structural: after reserves empty, unrestricted shifts allow long wandering through many related positions without reaching exact threefold repetition. Adding an arbitrary ply draw would make the metric look better without making play progress better.

## Why Span receives the revision

Span's defining mechanism is bounding-rectangle expansion or component merger. The fixed anchors make that mechanism active immediately. The v0.1 failure comes from one participant receiving the right to exploit a specific opening line before the opponent can interact.

A swap rule prices that opening advantage without changing:

- the board;
- the four anchors;
- legal placement geometry;
- expansion or merger;
- connection goals;
- immobilization;
- the finite-placement termination proof.

If Black opens C2 or C4, the second participant can take the Black side and its opening stone. The first participant must therefore choose an opening that remains acceptable after the opponent's swap decision. This does not prove balance; it creates a clean, falsifiable v0.2 question.

Changing anchors or banning C2 and C4 was rejected as an overly result-specific patch. Those changes would alter the geometry while leaving no principled reason for the replacement setup or opening list.

## Frozen evaluation intent for Span v0.2

Before implementation or new play results, the following commitments apply:

1. v0.2 differs from v0.1 only by the opening swap rule in `prototypes/span/RULES_v0_2.md`.
2. Evaluation must distinguish participant identity from color. The main balance statistic is first-participant versus second-participant result, not Black versus White result.
3. The strongest available symmetric agent must decide both the first placement and whether to swap under equal computation budgets.
4. Report swap frequency, first-placement distribution, participant results, color results, termination mode, plies, and legal-action counts.
5. Re-run deterministic rule tests and add tests for swap timing, board preservation, ownership exchange, one-time availability, and post-swap turn order.
6. Do not add an opening ban, altered anchors, komi, a second balancing rule, or a new draw rule during v0.2 evaluation.
7. If v0.2 still has a forced participant win or fails the existing protocol, preserve the result rather than adding another repair inside the same version.

## Limitations

- A pie or swap rule is a known balancing device, so v0.2's originality would still belong to Span's placement mechanism rather than to its opening protocol.
- Swap may overcompensate, narrow viable openings, or expose a different forced line.
- Existing Span search code assumes fixed color ownership and must be revised carefully before its results are trusted.
- No human playtest or deliberate prior-art search has been performed.

## Conclusion

Study 001 does not yet conclude negatively. One reasonable revision remains: Span v0.2 with exactly one swap option. This is the smallest repair with high diagnostic value and the lowest risk of replacing the original game rather than revising it.
