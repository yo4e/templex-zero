import pytest

from templex_zero.games import span


def make_state(*, black=(), white=(), player=0, ply=0):
    board = [span.EMPTY] * (span.BOARD_SIZE * span.BOARD_SIZE)
    for row, column in black:
        board[row * span.BOARD_SIZE + column] = 0
    for row, column in white:
        board[row * span.BOARD_SIZE + column] = 1
    return span.State(tuple(board), player, ply)


def test_initial_setup_and_legal_expansions():
    state = span.initial_state()
    assert state.player == 0
    assert state.board[2] == 0
    assert state.board[22] == 0
    assert state.board[10] == 1
    assert state.board[14] == 1
    assert span.legal_moves(state) == (
        (0, 1),
        (0, 3),
        (1, 2),
        (3, 2),
        (4, 1),
        (4, 3),
    )


def test_expansion_outside_component_bounding_rectangle_is_legal():
    state = make_state(black=((1, 1), (1, 2), (2, 1)))
    assert (3, 1) in span.legal_moves(state)


def test_interior_fill_inside_one_component_bounding_rectangle_is_illegal():
    state = make_state(black=((1, 1), (1, 2), (2, 1)))
    assert (2, 2) not in span.legal_moves(state)
    with pytest.raises(ValueError, match="Illegal Span move"):
        span.apply_move(state, (2, 2))


def test_merge_of_two_components_is_legal_without_rectangle_expansion():
    state = make_state(black=((2, 1), (2, 3)))
    assert (2, 2) in span.legal_moves(state)


def test_placement_without_friendly_support_is_illegal():
    state = make_state(black=((2, 2),))
    assert (0, 0) not in span.legal_moves(state)


def test_black_connection_wins_immediately_after_merge():
    state = make_state(
        black=((0, 2), (1, 2), (3, 2), (4, 2)),
        white=((2, 0), (2, 4)),
        player=0,
    )
    next_state = span.apply_move(state, (2, 2))
    assert span.winner(next_state) == 0


def test_white_connection_wins_immediately_after_merge():
    state = make_state(
        black=((0, 2), (4, 2)),
        white=((2, 0), (2, 1), (2, 3), (2, 4)),
        player=1,
    )
    next_state = span.apply_move(state, (2, 2))
    assert span.winner(next_state) == 1


def test_player_with_no_legal_placement_loses():
    state = make_state(
        black=((2, 2),),
        white=((1, 2), (2, 1), (2, 3), (3, 2)),
        player=0,
    )
    assert span.legal_moves(state) == ()
    assert span.winner(state) == 1


def test_render_includes_coordinates_and_fixed_anchors():
    assert span.render(span.initial_state()) == (
        "    A B C D E\n"
        " 1  . . B . .\n"
        " 2  . . . . .\n"
        " 3  W . . . W\n"
        " 4  . . . . .\n"
        " 5  . . B . ."
    )
