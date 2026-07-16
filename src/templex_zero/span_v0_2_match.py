"""Participant-aware reproducible match execution for Span v0.2."""
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Literal

from templex_zero import span_v0_2_agents
from templex_zero.games import span, span_v0_2 as game

WinMode = Literal["connection", "immobilization"]


@dataclass(frozen=True, slots=True)
class Result:
    winner_participant: int
    winner_color: int
    win_mode: WinMode
    plies: int
    placements: int
    opening_move: game.Move
    swapped: bool
    final_participant_colors: tuple[game.Color, game.Color]
    legal_action_counts: tuple[int, ...]

    @property
    def mean_legal_actions(self) -> float:
        return sum(self.legal_action_counts) / len(self.legal_action_counts)

    @property
    def max_legal_actions(self) -> int:
        return max(self.legal_action_counts)


def play(
    participant_zero: span_v0_2_agents.SpanV02Agent,
    participant_one: span_v0_2_agents.SpanV02Agent,
    seed: int,
) -> Result:
    rng = random.Random(seed)
    state = game.initial_state()
    opening_move: game.Move | None = None
    swapped = False
    legal_action_counts: list[int] = []

    while True:
        outcome = game.winner(state)
        if outcome != "ongoing":
            winner_participant = int(outcome)
            winner_color = int(game.winning_color(state))
            if opening_move is None:
                raise AssertionError("Span v0.2 terminated before the first placement")
            mode: WinMode = (
                "connection"
                if span._has_connection(state.board, winner_color)
                else "immobilization"
            )
            return Result(
                winner_participant=winner_participant,
                winner_color=winner_color,
                win_mode=mode,
                plies=state.ply,
                placements=state.placements,
                opening_move=opening_move,
                swapped=swapped,
                final_participant_colors=state.participant_colors,
                legal_action_counts=tuple(legal_action_counts),
            )

        actions = game.legal_actions(state)
        legal_action_counts.append(len(actions))
        agent = participant_zero if state.participant == 0 else participant_one
        action = agent(state, rng)
        if action not in actions:
            raise ValueError(f"Agent returned illegal Span v0.2 action: {action}")
        if opening_move is None:
            if action.destination is None:
                raise AssertionError("The opening action cannot be a swap")
            opening_move = action.destination
        if action.is_swap:
            swapped = True
        state = game.apply_action(state, action)
