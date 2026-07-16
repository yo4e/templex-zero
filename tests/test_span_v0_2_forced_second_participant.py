from templex_zero.games import span_v0_2 as game


def test_second_participant_forces_a_win_after_every_legal_opening():
    initial = game.initial_state()
    openings = game.legal_actions(initial)
    assert {action.destination for action in openings} == {
        (0, 1),
        (0, 3),
        (1, 2),
        (3, 2),
        (4, 1),
        (4, 3),
    }

    for opening in openings:
        after_opening = game.apply_action(initial, opening)
        destination = opening.destination
        assert destination is not None

        if destination in ((1, 2), (3, 2)):
            # Take Black, then complete the known C2-C3-C4 forced line.
            after_response = game.apply_action(after_opening, game.SWAP)
            middle = game.Action((2, 2))
            finish = game.Action(
                (3, 2) if destination == (1, 2) else (1, 2)
            )
        else:
            # Remain White and complete B3-C3-D3, reflected when needed.
            if destination[1] == 1:
                response = game.Action((2, 1))
                finish = game.Action((2, 3))
            else:
                response = game.Action((2, 3))
                finish = game.Action((2, 1))
            after_response = game.apply_action(after_opening, response)
            middle = game.Action((2, 2))

        for first_participant_reply in game.legal_actions(after_response):
            after_reply = game.apply_action(
                after_response, first_participant_reply
            )
            assert middle in game.legal_actions(after_reply)
            after_middle = game.apply_action(after_reply, middle)

            for second_reply in game.legal_actions(after_middle):
                before_finish = game.apply_action(after_middle, second_reply)
                assert finish in game.legal_actions(before_finish)
                terminal = game.apply_action(before_finish, finish)
                assert game.winner(terminal) == 1
