# Span — Frozen Prototype Rules v0.1

_Date frozen before implementation or play results: 2026-07-15 (Asia/Tokyo)_

This document defines the baseline Span rules that must be implemented and evaluated first. Results may justify a later version, but they must not be used to silently alter v0.1.

## Core rules

### Equipment and setup

Span is a deterministic two-player connection game played on a 5×5 square grid.

Rows are numbered 1–5 from top to bottom; columns are labeled A–E from left to right.

Place four fixed starting stones:

- Black stones at C1 and C5.
- White stones at A3 and E3.

Black moves first. Black aims to connect the top and bottom edges. White aims to connect the left and right edges. Starting stones are ordinary stones for all rule purposes and never move.

### Connection

Stones of one color are connected only through shared sides, not diagonals. A **component** is a maximal side-connected group of stones of one color.

A component's **bounding rectangle** is the smallest row-and-column-aligned rectangle containing every stone in that component.

### Turn

On a turn, place one stone of your color on an empty cell. The placement is legal only if it shares a side with at least one friendly stone and satisfies one of these conditions, measured before placement:

1. **Expansion:** all side-adjacent friendly stones belong to one component, and the new cell lies outside that component's bounding rectangle.
2. **Merge:** the new cell is side-adjacent to stones belonging to at least two distinct friendly components.

Enemy adjacency has no effect on legality. A stone may not be placed without side-adjacent friendly support. There is no movement or capture.

### End of game

After placing a stone, you win immediately if one of your components touches both of your assigned opposite edges.

If you begin your turn with no legal placement, you lose immediately.

Because every completed turn permanently fills one cell, the game cannot continue indefinitely.

## Frozen interpretation notes

- Connectivity and edge contact are orthogonal.
- The bounding rectangle is evaluated on the pre-move component.
- Touching several stones from the same component is still an expansion attempt, not a merge.
- A merge is legal regardless of whether the new cell expands either old bounding rectangle.
- Black has the first move; no swap or pie rule is included in this baseline.
- Immobilization is a loss, not a pass or draw.

## Design commitments and risks

The fixed edge anchors create two initial components per player, avoiding an arbitrary exception for seed placement and making merger central from move one. The 5×5 board keeps exhaustive or near-exhaustive analysis plausible and makes this version a fast falsification target.

Known risks to test rather than repair in advance:

- the fixed center-edge anchors may create a large first-player advantage;
- bounding-box expansion may make legal play too predictable;
- immobilization may dominate connection as the practical objective;
- twenty-one available placements may be too few for strategic depth.
