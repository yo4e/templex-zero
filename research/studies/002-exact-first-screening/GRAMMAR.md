# Study 002 Frozen Candidate Grammar

_Date frozen: 2026-07-16 before candidate generation_  
_Status: **Frozen. No candidate manifest has been emitted.**_

## 1. Fixed counts

- Generation seed: `2026071602`
- Board sizes, in order: `3`, `4`
- Mechanism families, in order:
  1. `adjacency_growth`
  2. `component_expansion`
  3. `local_block_pattern`
- Candidates per board-size × family cell: `3`
- Total manifest size: `2 × 3 × 3 = 18`

Cell order is therefore:

1. 3×3 adjacency growth
2. 3×3 component expansion
3. 3×3 local block/pattern
4. 4×4 adjacency growth
5. 4×4 component expansion
6. 4×4 local block/pattern

## 2. Shared candidate boundaries

Every generated candidate must:

- use every cell of a 3×3 or 4×4 square board;
- begin empty with participant 0 to move;
- alternate deterministic placements;
- fill exactly one empty cell per normal action;
- have no movement, capture, swap, chance, hidden information, scoring, repetition, or pass;
- state intended symmetry under participant/color exchange with board transpose where roles differ by axis;
- terminate when the previous mover satisfies the goal or when the next participant has no legal action;
- use `previous_player_wins` for no-legal-action resolution;
- be expressible by `templex_zero.exact_first.schema.GameSpec`;
- have generated core rules at or below 250 words.

Fixture-only explicit opening cells and explicit winning-cell patterns are prohibited in candidates.

## 3. Parameter grammar

Parameter fields are listed in canonical serialization order. Values are listed in their unseeded lexical source order.

### A. Adjacency-constrained growth

- `neighborhood`: `orthogonal`, `king`
- `first_move_scope`: `any`, `home_edge`
- `friendly_requirement`:
  - `at_least_one` → `friendly_min=1`, no maximum
  - `exactly_one` → `friendly_min=1`, `friendly_max=1`
  - `at_least_two` → `friendly_min=2`, no maximum
- `goal`:
  - `connect_edges`
  - `component_size_board` → component threshold equals board size

Translation:

- placement kind: `friendly_adjacency`
- later placements must satisfy the selected friendly-neighbor count in the selected neighborhood
- a participant with no stones uses the selected first-move scope instead of the friendly-neighbor minimum

### B. Component expansion or merger

- `neighborhood`: `orthogonal`, `king`
- `first_move_scope`: `any`, `home_edge`
- `expansion_policy`:
  - `expand_only` → expansion true, merger false
  - `merge_only` → expansion false, merger true
  - `expand_or_merge` → both true
- `goal`:
  - `connect_edges`
  - `component_size_board`

Translation:

- placement kind: `expand_or_merge`
- a participant with existing stones must place adjacent to at least one friendly component
- expansion means the new cell lies outside the pre-placement bounding rectangle of at least one joined component
- merger means the placement joins at least two distinct pre-placement friendly components

### C. Local blocking and pattern completion

- `neighborhood`: `orthogonal`, `king`
- `first_move_scope`: `any`, `home_edge`
- `enemy_neighbor_max`: `0`, `1`
- `line_directions`: `orthogonal`, `all`

Translation:

- placement kind: `enemy_limit`
- `friendly_min=0`
- the number of adjacent enemy stones may not exceed the selected maximum
- goal kind: `line`
- line threshold equals board size
- `orthogonal` allows horizontal and vertical lines
- `all` additionally allows both diagonal directions

## 4. Home-edge convention

For `home_edge` first moves:

- participant/color 0 may place on the top row;
- participant/color 1 may place on the left column.

For `connect_edges` goals:

- participant/color 0 connects top to bottom;
- participant/color 1 connects left to right.

The transpose-plus-player/color-exchange mapping is the intended symmetry.

## 5. Canonical tuple

Each raw parameter product is translated before ranking into a canonical object with fields in this exact order:

1. `board_size`
2. `family`
3. `neighborhood`
4. `first_move_scope`
5. family-specific normalized parameters
6. normalized goal parameters
7. `no_move_outcome=previous_player_wins`
8. `intended_symmetric=true`

Aliases are removed during translation. For example, `exactly_one` is serialized only as normalized minimum and maximum values, and expansion policies are serialized only as `allow_expand` and `allow_merge` booleans.

The canonical object is encoded as compact UTF-8 JSON with separators `(',', ':')`, no ASCII escaping, and insertion order exactly as listed above. Duplicate canonical byte strings are removed before manifest selection. No state graph, game result, heuristic, or play trace is used by canonicalization.

## 6. Seeded deterministic order

For every canonical candidate tuple in one cell, calculate:

```text
rank = SHA256(
  "2026071602|<board_size>|<family>|" + canonical_json
).hexdigest()
```

Sort ascending by `(rank, canonical_json)`.

This SHA-256 order is the seeded generator order. It avoids dependence on Python's pseudorandom implementation or dictionary hashing.

Within each cell, the manifest selects the first three distinct tuples that pass static schema validation and generated-rule word count. There is no manual ranking, aesthetic filtering, outcome inspection, or replacement.

## 7. Candidate identifiers

Manifest identifiers are assigned only after selection:

```text
S2-<board_size>-<family_code>-<cell_rank>
```

Family codes:

- `AG` — adjacency growth
- `CE` — component expansion
- `LB` — local block/pattern

`cell_rank` is `01`, `02`, or `03` in the frozen seeded order.

## 8. Static failure rule

If any cell yields fewer than three distinct valid candidates, candidate generation fails and Study 002 closes without:

- changing this grammar;
- changing the seed;
- adding a fourth candidate family;
- manually writing replacements;
- inspecting play results.

## 9. Cycle boundary

This file freezes the grammar only. The current cycle does not calculate the 18 selected tuples, write a manifest, solve a state, or run a game. Manifest generation belongs to the next approval-driven cycle.
