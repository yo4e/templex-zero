# Keystone — Frozen Prototype Rules v0.1

_Date frozen before implementation or play results: 2026-07-15 (Asia/Tokyo)_

This document defines the Keystone baseline that must be implemented and evaluated first. Results may justify a later version, but they must not be used to silently alter v0.1.

## Core rules

### Equipment and setup

Keystone is a deterministic two-player game on an initially empty 5×5 square grid. Rows are numbered 1–5 from top to bottom and columns A–E from left to right. The center is C3.

Each player has eight stones. Black moves first. Captured stones are removed from the game.

### Turn

On a turn, take exactly one action:

1. Place one stone from your reserve on any empty cell; or
2. Shift one of your stones already on the board to an orthogonally adjacent empty cell.

Stones do not jump. A shift may split or reconnect groups.

After the action, check only brackets completed by the stone that was just placed or shifted. An enemy stone is bracketed when it is orthogonally adjacent to that stone and a friendly stone occupies the next cell in the same direction. If one or more enemy stones are bracketed, the mover must choose exactly one of them and remove it. Other simultaneous brackets do not capture.

### Victory

After the mandatory capture, the mover wins if one orthogonally connected friendly component:

- contains the center C3; and
- contains two different friendly edge stones touching two different board edges.

The two edge contacts may be on adjacent or opposite edges. A corner stone may count as only one edge contact for a winning claim, so a second stone must touch another edge.

### Other endings

If a player begins a turn with no legal placement or shift, that player loses.

After checking victory, switch the player to move. If the resulting complete position has now occurred for the third time, the game is a draw. A complete position includes the board, both reserve counts, and the player to move.

## Frozen interpretation notes

- Connectivity, shifting, brackets, and edge contact are orthogonal; diagonals have no effect.
- Placement is legal without friendly support.
- Only the newly placed or shifted stone can complete a capture.
- A bracket requires a friendly stone immediately beyond exactly one enemy stone; longer lines do not capture.
- If several captures are available, one is mandatory and the mover chooses which one.
- Nonchosen simultaneous brackets remain on the board.
- Captured stones do not return to reserve.
- Enemy stones may be captured from the center or an edge.
- Capture is resolved before testing victory.
- Victory is resolved before repetition.
- A corner contact cannot alone satisfy both required edges.
- Black has the first move; no swap or pie rule is included.

## Precommitted risks to test

- occupation of C3 may dominate all other strategy;
- adjacent-edge victories may be too easy to force;
- the first player may secure the center too cheaply;
- a mandatory single capture may be tactically weak or create artificial choices;
- eight-stone reserves may be too generous or too restrictive;
- shifting may create excessive repetition or draw-seeking;
- the combined placement, movement, capture, and structural victory rules may exceed the teachability target.

Do not repair these risks before the frozen baseline is implemented and tested.