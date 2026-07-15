# Span — Frozen Prototype Rules v0.2

_Date frozen before v0.2 implementation or play results: 2026-07-16 (Asia/Tokyo)_

This document defines the Span v0.2 revision. Span v0.1 remains unchanged in `RULES.md`. Results may justify a later version, but they must not be used to silently alter v0.2.

## Core rules

### Equipment and setup

Span v0.2 is a deterministic two-player connection game on a 5×5 square grid. Rows are numbered 1–5 from top to bottom and columns A–E from left to right.

Place fixed Black stones at C1 and C5 and fixed White stones at A3 and E3. Black connects top to bottom; White connects left to right. Starting stones are ordinary stones and never move. The first participant initially owns Black and the second participant initially owns White.

### Connection

Stones connect only through shared sides. A **component** is a maximal side-connected group of one color. Its **bounding rectangle** is the smallest row-and-column-aligned rectangle containing it.

### Opening and swap

The first participant makes one normal Black placement. The second participant then chooses exactly one opening response:

1. place one White stone normally; or
2. swap sides.

When sides are swapped, the participants exchange colors, goals, and ownership of every stone already on the board. The board itself does not change. The swap consumes the second participant's turn. The first participant, now White, moves next. The swap option then disappears permanently.

### Normal turn

On every normal turn, place one stone of your current color on an empty cell. The placement must share a side with at least one friendly stone and satisfy one condition, measured before placement:

1. **Expansion:** all side-adjacent friendly stones belong to one component, and the new cell lies outside that component's bounding rectangle.
2. **Merge:** the new cell is side-adjacent to stones from at least two distinct friendly components.

Enemy adjacency does not affect legality. There is no movement or capture.

### End of game

After a placement, you win immediately if one component of your color touches both assigned opposite edges. If you begin a normal turn with no legal placement, you lose immediately.

Every normal turn permanently fills one cell. The optional swap occurs at most once, so the game cannot continue indefinitely.

## Frozen interpretation notes

- The core rules contain 308 words, below the Study 001 limit of 400.
- The first Black placement must be legal under the same expansion-or-merge rule as every other placement.
- The second participant may swap only instead of their first White placement and only immediately after the first Black placement.
- A swap changes participant ownership, not stone colors or board locations.
- The participant who opened the game becomes White after a swap and takes the next normal turn.
- A swap counts as a turn but not as a placement. A game with a swap can therefore contain at most twenty-one placements plus the swap turn.
- If the second participant makes a White placement, the swap option expires.
- Connectivity, bounding rectangles, edge goals, and legal placements are always evaluated by color.
- Match records and balance analysis must separately track participant identity and color ownership.
- Immobilization remains a loss. No draw rule is added.
- No anchor, opening cell, or normal placement is banned.
- No other v0.1 rule changes in v0.2.

## Revision rationale

Span v0.1 permits Black to force C2–C3–C4, or its reflection, and connect the fixed C1 and C5 anchors on ply 5. The swap rule allows the second participant to take any opening that is too valuable, forcing the first participant to choose an opening acceptable from either side.

This rule does not assume that Span becomes balanced. It creates a single-change revision whose success or failure can be measured without replacing the bounding-rectangle expansion and merger mechanism.

## Precommitted risks to test

- the swap option may overcompensate and create a second-participant advantage;
- only a small number of first placements may remain viable;
- a forced participant win may persist despite color exchange;
- the expansion rule may remain strategically shallow even if balance improves;
- a standard balancing device may repair fairness without improving the underlying game.

Do not add another balancing or termination rule before v0.2 receives a documented disposition.
