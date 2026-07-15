"""Deterministic baseline search agents for Span v0.1."""

from __future__ import annotations

import heapq
import random
from collections.abc import Callable
from functools import lru_cache

from templex_zero.games import span

SpanAgent = Callable[[span.State, random.Random], span.Move]
WIN_SCORE = 1_000_000.0
BLOCKED_COST = span.BOARD_SIZE**2 + 1


def random_agent(state: span.State, rng: random.Random) -> span.Move:
    moves = span.legal_moves(state)
    if not moves:
        raise ValueError("Agent asked to move in a terminal state")
    return rng.choice(moves)


def _connection_cost(board: tuple[int, ...], player: span.Player) -> int:
    """Minimum empty cells on an orthogonal edge-to-edge path.

    Friendly stones cost zero, empty cells cost one, and enemy stones are blocked.
    This is a symmetric geometric heuristic, not a proof of a legal winning line.
    """

    opponent = 1 - player
    distances = [BLOCKED_COST] * len(board)
    frontier: list[tuple[int, int]] = []

    starts = (
        (span._index(0, column) for column in range(span.BOARD_SIZE))
        if player == 0
        else (span._index(row, 0) for row in range(span.BOARD_SIZE))
    )
    for index in starts:
        if board[index] == opponent:
            continue
        cost = 0 if board[index] == player else 1
        distances[index] = cost
        heapq.heappush(frontier, (cost, index))

    while frontier:
        cost, current = heapq.heappop(frontier)
        if cost != distances[current]:
            continue
        row, column = span._rc(current)
        if (player == 0 and row == span.BOARD_SIZE - 1) or (
            player == 1 and column == span.BOARD_SIZE - 1
        ):
            return cost
        for neighbor in span._orthogonal_neighbors(current):
            if board[neighbor] == opponent:
                continue
            step = 0 if board[neighbor] == player else 1
            candidate = cost + step
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heapq.heappush(frontier, (candidate, neighbor))

    return BLOCKED_COST


def _maximum_component_span(board: tuple[int, ...], player: span.Player) -> int:
    spans = []
    for component in span._components(board, player):
        rows, columns = zip(*(span._rc(index) for index in component), strict=True)
        spans.append(
            (max(rows) - min(rows))
            if player == 0
            else (max(columns) - min(columns))
        )
    return max(spans, default=0)


def evaluate(state: span.State, root: span.Player) -> float:
    """Evaluate ``state`` from ``root``'s perspective with symmetric features."""

    outcome = span.winner(state)
    if outcome != "ongoing":
        if outcome == root:
            return WIN_SCORE - state.ply
        return -WIN_SCORE + state.ply

    opponent = 1 - root
    root_cost = _connection_cost(state.board, root)
    opponent_cost = _connection_cost(state.board, opponent)  # type: ignore[arg-type]
    root_span = _maximum_component_span(state.board, root)
    opponent_span = _maximum_component_span(state.board, opponent)  # type: ignore[arg-type]
    root_mobility = len(span._legal_moves(state.board, root))
    opponent_mobility = len(span._legal_moves(state.board, opponent))  # type: ignore[arg-type]
    root_components = len(span._components(state.board, root))
    opponent_components = len(span._components(state.board, opponent))  # type: ignore[arg-type]

    return (
        100.0 * (opponent_cost - root_cost)
        + 12.0 * (root_span - opponent_span)
        + 2.0 * (root_mobility - opponent_mobility)
        + 3.0 * (opponent_components - root_components)
    )


@lru_cache(maxsize=None)
def _minimax_value(state: span.State, depth: int, root: span.Player) -> float:
    outcome = span.winner(state)
    if outcome != "ongoing" or depth == 0:
        return evaluate(state, root)

    values = tuple(
        _minimax_value(span.apply_move(state, move), depth - 1, root)
        for move in span.legal_moves(state)
    )
    return max(values) if state.player == root else min(values)


def minimax_agent(depth: int) -> SpanAgent:
    if depth < 1:
        raise ValueError("depth must be at least 1")

    def choose(state: span.State, rng: random.Random) -> span.Move:
        moves = span.legal_moves(state)
        if not moves:
            raise ValueError("Agent asked to move in a terminal state")
        scored = [
            (
                _minimax_value(
                    span.apply_move(state, move), depth - 1, state.player
                ),
                move,
            )
            for move in moves
        ]
        best = max(score for score, _ in scored)
        return rng.choice([move for score, move in scored if score == best])

    return choose
