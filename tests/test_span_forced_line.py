"""Small exhaustive consequences of the frozen Span v0.1 rules."""

from templex_zero.games import span


def test_black_c2_opening_forces_connection_on_black_third_move():
    """No legal White reply can occupy or invalidate C3 then C4 in time."""

    after_c2 = span.apply_move(span.initial_state(), (1, 2))
    assert span.winner(after_c2) == "ongoing"

    for white_first in span.legal_moves(after_c2):
        after_white_first = span.apply_move(after_c2, white_first)
        assert (2, 2) in span.legal_moves(after_white_first)
        after_c3 = span.apply_move(after_white_first, (2, 2))

        for white_second in span.legal_moves(after_c3):
            after_white_second = span.apply_move(after_c3, white_second)
            assert (3, 2) in span.legal_moves(after_white_second)
            after_c4 = span.apply_move(after_white_second, (3, 2))
            assert span.winner(after_c4) == 0
            assert after_c4.ply == 5
