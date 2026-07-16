"""Frozen candidate-grammar constants for Study 002.

This module intentionally does not emit candidates. Candidate generation and the
18-entry manifest belong to the next approval cycle.
"""

from __future__ import annotations

from .schema import MechanismFamily

GENERATION_SEED = 2026071602
BOARD_SIZES = (3, 4)
FAMILY_ORDER = (
    MechanismFamily.ADJACENCY_GROWTH,
    MechanismFamily.COMPONENT_EXPANSION,
    MechanismFamily.LOCAL_BLOCK_PATTERN,
)
CANDIDATES_PER_CELL = 3
TOTAL_CANDIDATES = len(BOARD_SIZES) * len(FAMILY_ORDER) * CANDIDATES_PER_CELL

ADJACENCY_GROWTH_OPTIONS = {
    "neighborhood": ("orthogonal", "king"),
    "first_move_scope": ("any", "home_edge"),
    "friendly_requirement": ("at_least_one", "exactly_one", "at_least_two"),
    "goal": ("connect_edges", "component_size_board"),
}

COMPONENT_EXPANSION_OPTIONS = {
    "neighborhood": ("orthogonal", "king"),
    "first_move_scope": ("any", "home_edge"),
    "expansion_policy": ("expand_only", "merge_only", "expand_or_merge"),
    "goal": ("connect_edges", "component_size_board"),
}

LOCAL_BLOCK_PATTERN_OPTIONS = {
    "neighborhood": ("orthogonal", "king"),
    "first_move_scope": ("any", "home_edge"),
    "enemy_neighbor_max": (0, 1),
    "line_directions": ("orthogonal", "all"),
}


def cell_order() -> tuple[tuple[int, MechanismFamily], ...]:
    return tuple((size, family) for size in BOARD_SIZES for family in FAMILY_ORDER)
