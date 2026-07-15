import random

import pytest

from templex_zero import span_agents
from templex_zero.games import span
from templex_zero.span_match import play


def make_state(*, black=(), white=(), player=0, ply=0):
    board = [span.EMPTY] * (span.BOARD_SIZE * span.BOARD_SIZE)
    for row, column in black:
        board[span._index(row, column)] = 0
    for row, column in white:
        board[span._index(row, column)] = 1
    return span.State(tuple(board), player, ply)


def transpose_and_swap(state: span.State) -> span.State:
    board = [span.EMPTY] * len(state.board)
    for index, value in enumerate(state.board):
        row, column = span._rc(index)
        board[span._index(column, row)] = (
            span.EMPTY if value == span.EMPTY else 1 - value
        )
    return span.State(tuple(board), 1 - state.player, state.ply)


def test_terminal_scoring_dominates_heuristic():
    black_win = make_state(
        black=((0, 2), (1, 2), (2, 2), (3, 2), (4, 2)),
        white=((2, 0), (2, 4)),
        player=1,
        ply=9,
    )
    assert span_agents.evaluate(black_win, 0) > 900_000
    assert span_agents.evaluate(black_win, 1) < -900_000


def test_evaluation_is_symmetric_under_transpose_and_color_swap():
    state = make_state(
        black=((0, 2), (1, 2), (3, 3), (4, 2)),
        white=((1, 4), (2, 0), (2, 1), (2, 4)),
        player=0,
        ply=6,
    )
    mirrored = transpose_and_swap(state)
    assert span_agents.evaluate(state, 0) == span_agents.evaluate(mirrored, 1)
    assert span_agents.evaluate(state, 1) == span_agents.evaluate(mirrored, 0)


def test_minimax_selects_immediate_connection_win():
    state = make_state(
        black=((0, 2), (1, 2), (3, 2), (4, 2)),
        white=((2, 0), (2, 4)),
        player=0,
        ply=4,
    )
    assert span_agents.minimax_agent(1)(state, random.Random(0)) == (2, 2)


def test_minimax_always_returns_legal_move():
    state = span.initial_state()
    for depth in (1, 2, 3):
        move = span_agents.minimax_agent(depth)(state, random.Random(7))
        assert move in span.legal_moves(state)


def test_minimax_tie_breaking_is_reproducible_for_same_seed():
    agent = span_agents.minimax_agent(2)
    assert agent(span.initial_state(), random.Random(1234)) == agent(
        span.initial_state(), random.Random(1234)
    )


def test_match_is_reproducible_and_terminates():
    agent = span_agents.minimax_agent(2)
    first = play(agent, agent, seed=17)
    second = play(agent, agent, seed=17)
    assert first == second
    assert first.winner in (0, 1)
    assert first.win_mode in ("connection", "immobilization")
    assert 1 <= first.plies <= 21


def test_invalid_depth_and_terminal_agent_call_are_rejected():
    with pytest.raises(ValueError, match="depth must be at least 1"):
        span_agents.minimax_agent(0)

    terminal = make_state(
        black=((2, 2),),
        white=((1, 2), (2, 1), (2, 3), (3, 2)),
        player=0,
    )
    with pytest.raises(ValueError, match="terminal state"):
        span_agents.minimax_agent(1)(terminal, random.Random(0))
