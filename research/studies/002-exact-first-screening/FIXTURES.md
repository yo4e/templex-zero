# Study 002 Hand-Audited Solver Fixtures

_Date frozen: 2026-07-16 before exact-solver implementation and candidate generation_

These fixtures are not Study 002 candidates. They may use fixture-only playable-cell masks, explicit opening cells, or explicit winning patterns in order to create tiny state graphs whose outcomes can be audited by inspection.

The exact solver must later agree with an independently written brute-force enumerator on every node, outcome, distance, and opening-action value derived from these graphs.

## Notation

State keys use:

```text
p<next-player>:<ply>:<row-major board>
```

Board symbols:

- `.` — empty playable cell
- `#` — non-playable cell
- `X` — participant/color 0 stone
- `O` — participant/color 1 stone

Actions use spreadsheet-style coordinates: `A1`, `B1`, `A2`, and so on.

Terminal labels are `ongoing`, `draw`, `win:0`, or `win:1`.

## Fixture 1 — Immediate component win

Purpose: verify a one-action win and terminal precedence over no-move resolution.

- Board: one playable cell
- Placement: unrestricted
- Goal: friendly component size at least 1
- Intended symmetry: color-role symmetric

Graph:

```text
p0:0:. --A1--> p1:1:X

p0:0:.   = ongoing
p1:1:X   = win:0
```

Machine-readable form:

```text
p0:0:.  actions {A1: p1:1:X}
p1:1:X  actions {}
```

## Fixture 2 — Single-cell draw

Purpose: verify draw resolution when the board has no legal action and no goal was reached.

- Board: one playable cell
- Placement: unrestricted
- Goal: friendly component size at least 2, impossible on the fixture
- No-move outcome: draw
- Intended symmetry: color-role symmetric

Graph:

```text
p0:0:. --A1--> p1:1:X

p0:0:.   = ongoing
p1:1:X   = draw
```

## Fixture 3 — Branching pattern

Purpose: verify that two legal openings can lead to different winners and that the enumerator preserves both branches.

- Board: two playable cells, `A1` and `B1`
- Placement: unrestricted
- Participant 0 wins immediately by owning `A1`
- Participant 1 wins immediately by owning `B1`
- Otherwise, previous player wins when no legal action remains
- Intended symmetry: not claimed; the role-specific patterns are deliberately asymmetric

Graph:

```text
                    A1
p0:0:..## -----------------> p1:1:X.## = win:0
     |
     | B1
     v
p1:1:.X## --A1--> p0:2:OX## = win:1
```

Exact node table:

```text
p0:0:..##  = ongoing; actions {A1: p1:1:X.##, B1: p1:1:.X##}
p1:1:X.##  = win:0; actions {}
p1:1:.X##  = ongoing; actions {A1: p0:2:OX##}
p0:2:OX##  = win:1; actions {}
```

## Fixture 4 — Adjacency chain

Purpose: verify explicit fixture openings, later friendly-adjacency legality, immutable alternating placement, and a three-placement forced path.

- Board: playable `A1`, `B1`, and `B2`; `A2` is blocked
- Participant 0's first placement is fixed at `A1`
- Participant 1's first placement is fixed at `B2`
- Later placements must have exactly one orthogonally adjacent friendly stone
- Participant 0 wins with `A1+B1`
- Participant 1 wins with `B1+B2`
- Intended symmetry: not claimed; the L-shaped playable mask is not invariant under transpose

Graph:

```text
p0:0:..#. --A1--> p1:1:X.#. --B2--> p0:2:X.#O --B1--> p1:3:XX#O

p0:0:..#.  = ongoing
p1:1:X.#.  = ongoing
p0:2:X.#O  = ongoing
p1:3:XX#O  = win:0
```

## Frozen audit requirements

Before any Study 002 candidate is solved, the future exact instrument must:

1. reproduce these four reachable graphs exactly;
2. agree with a separately implemented brute-force enumerator;
3. agree on root outcome, terminal distance, and every opening-action value;
4. verify the stated symmetry on every reachable state of Fixtures 1 and 2;
5. treat Fixtures 3 and 4 as intentionally asymmetric rather than forcing false symmetry assertions.

If disagreement remains after one bounded implementation-debugging cycle, Study 002 closes as an instrument failure.
