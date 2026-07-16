"""Run reproducible Span v0.2 random and equal-budget minimax screens.

Random play is a termination and gross-pathology screen only. Participant
balance is judged from the equal-budget symmetric minimax screen.

Run from the repository root after committing this file:

    PYTHONPATH=src python experiments/span_v0_2_formal_screen.py \
        --random-games 10000 --minimax-games 1000 --depth 3 \
        --seed-start 0 --code-version <commit>
"""
from __future__ import annotations

import argparse
import json
import platform
import random
from collections import Counter, defaultdict
from dataclasses import dataclass
from statistics import mean, median
from typing import Literal

from templex_zero import span_v0_2_agents as agents
from templex_zero.games import span, span_v0_2 as game

AgentKind = Literal["random", "minimax"]
WinMode = Literal["connection", "immobilization"]


@dataclass(frozen=True, slots=True)
class GameRecord:
    seed: int
    winner_participant: int
    winner_color: int
    win_mode: WinMode
    plies: int
    placements: int
    opening_move: game.Move
    opening_response: str
    swapped: bool
    final_participant_colors: tuple[game.Color, game.Color]
    legal_action_counts: tuple[int, ...]


def _move_name(move: game.Move) -> str:
    row, column = move
    return f"{chr(column + 65)}{row + 1}"


def _action_name(action: game.Action) -> str:
    return "swap" if action.is_swap else _move_name(action.destination)  # type: ignore[arg-type]


def _percentile(values: list[int], fraction: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * fraction
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def play(seed: int, *, kind: AgentKind, depth: int) -> GameRecord:
    rng = random.Random(seed)
    state = game.initial_state()
    agent = agents.random_agent if kind == "random" else agents.minimax_agent(depth)
    opening_move: game.Move | None = None
    opening_response: str | None = None
    swapped = False
    legal_action_counts: list[int] = []

    while True:
        outcome = game.winner(state)
        if outcome != "ongoing":
            winner_participant = int(outcome)
            winner_color = int(game.winning_color(state))
            if opening_move is None or opening_response is None:
                raise AssertionError("Span v0.2 terminated before the opening response")
            win_mode: WinMode = (
                "connection"
                if span._has_connection(state.board, winner_color)
                else "immobilization"
            )
            return GameRecord(
                seed=seed,
                winner_participant=winner_participant,
                winner_color=winner_color,
                win_mode=win_mode,
                plies=state.ply,
                placements=state.placements,
                opening_move=opening_move,
                opening_response=opening_response,
                swapped=swapped,
                final_participant_colors=state.participant_colors,
                legal_action_counts=tuple(legal_action_counts),
            )

        actions = game.legal_actions(state)
        legal_action_counts.append(len(actions))
        action = agent(state, rng)
        if action not in actions:
            raise ValueError(f"Agent returned illegal action: {action}")
        if opening_move is None:
            if action.destination is None:
                raise AssertionError("Opening action cannot be swap")
            opening_move = action.destination
        elif opening_response is None:
            opening_response = _action_name(action)
        if action.is_swap:
            swapped = True
        state = game.apply_action(state, action)


def summarize(
    records: list[GameRecord],
    *,
    kind: AgentKind,
    depth: int,
    seed_start: int,
) -> dict[str, object]:
    participants = Counter(record.winner_participant for record in records)
    colors = Counter(record.winner_color for record in records)
    modes = Counter(record.win_mode for record in records)
    openings = Counter(_move_name(record.opening_move) for record in records)
    responses = Counter(record.opening_response for record in records)
    ownership = Counter(record.final_participant_colors for record in records)
    terminal_signatures = Counter(
        (
            _move_name(record.opening_move),
            record.opening_response,
            record.winner_participant,
            record.winner_color,
            record.plies,
        )
        for record in records
    )
    plies = [record.plies for record in records]
    placements = [record.placements for record in records]
    branch_counts = [
        count for record in records for count in record.legal_action_counts
    ]
    branches_by_ply: dict[int, list[int]] = defaultdict(list)
    for record in records:
        for ply, count in enumerate(record.legal_action_counts):
            branches_by_ply[ply].append(count)

    return {
        "agent_kind": kind,
        "depth": depth if kind == "minimax" else None,
        "games": len(records),
        "seed_start": seed_start,
        "seed_end_inclusive": seed_start + len(records) - 1,
        "independent_rng_per_game": True,
        "all_completed": True,
        "within_200_plies": sum(record.plies <= 200 for record in records),
        "participant_results": {
            "first": participants[0],
            "second": participants[1],
            "first_rate": participants[0] / len(records),
            "second_rate": participants[1] / len(records),
        },
        "color_results": {
            "black": colors[0],
            "white": colors[1],
            "black_rate": colors[0] / len(records),
            "white_rate": colors[1] / len(records),
        },
        "win_modes": {
            "connection": modes["connection"],
            "immobilization": modes["immobilization"],
        },
        "swap": {
            "count": sum(record.swapped for record in records),
            "rate": mean(record.swapped for record in records),
        },
        "plies": {
            "minimum": min(plies),
            "p10": _percentile(plies, 0.10),
            "median": median(plies),
            "mean": mean(plies),
            "p90": _percentile(plies, 0.90),
            "maximum": max(plies),
        },
        "placements": {
            "minimum": min(placements),
            "median": median(placements),
            "mean": mean(placements),
            "maximum": max(placements),
        },
        "branching": {
            "decision_nodes": len(branch_counts),
            "minimum": min(branch_counts),
            "median": median(branch_counts),
            "mean": mean(branch_counts),
            "maximum": max(branch_counts),
            "mean_by_ply": {
                str(ply): mean(counts)
                for ply, counts in sorted(branches_by_ply.items())
            },
        },
        "opening_moves": dict(sorted(openings.items())),
        "opening_responses": dict(sorted(responses.items())),
        "final_ownership": {
            "first_black_second_white": ownership[(0, 1)],
            "first_white_second_black": ownership[(1, 0)],
        },
        "terminal_signatures": {
            f"{opening}|{response}|P{winner_participant + 1}|"
            f"{'B' if winner_color == 0 else 'W'}|{plies}": count
            for (
                opening,
                response,
                winner_participant,
                winner_color,
                plies,
            ), count in sorted(terminal_signatures.items())
        },
    }


def run(
    *,
    random_games: int,
    minimax_games: int,
    depth: int,
    seed_start: int,
    code_version: str,
) -> dict[str, object]:
    if random_games < 1 or minimax_games < 1:
        raise ValueError("game counts must be at least 1")
    if depth < 1:
        raise ValueError("depth must be at least 1")

    random_records = [
        play(seed, kind="random", depth=depth)
        for seed in range(seed_start, seed_start + random_games)
    ]
    minimax_records = [
        play(seed, kind="minimax", depth=depth)
        for seed in range(seed_start, seed_start + minimax_games)
    ]
    return {
        "experiment": "span-v0.2-formal-screen",
        "interpretation": {
            "random": "termination and gross pathology only; not balance evidence",
            "minimax": (
                "primary participant-balance screen using the same agent and depth "
                "for opening placement, swap, and later placements"
            ),
            "precommitted_first_participant_interval": [0.40, 0.60],
        },
        "configuration": {
            "random_games": random_games,
            "minimax_games": minimax_games,
            "minimax_depth": depth,
            "seed_start": seed_start,
            "code_version": code_version,
            "python_version": platform.python_version(),
            "board_size": game.BOARD_SIZE,
            "maximum_placements": game.BOARD_SIZE**2 - 4,
            "maximum_action_plies": game.BOARD_SIZE**2 - 3,
            "manual_exclusions": 0,
        },
        "random_screen": summarize(
            random_records, kind="random", depth=depth, seed_start=seed_start
        ),
        "symmetric_minimax_screen": summarize(
            minimax_records, kind="minimax", depth=depth, seed_start=seed_start
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--random-games", type=int, default=10_000)
    parser.add_argument("--minimax-games", type=int, default=1_000)
    parser.add_argument("--depth", type=int, default=3)
    parser.add_argument("--seed-start", type=int, default=0)
    parser.add_argument("--code-version", default="uncommitted")
    args = parser.parse_args()
    print(
        json.dumps(
            run(
                random_games=args.random_games,
                minimax_games=args.minimax_games,
                depth=args.depth,
                seed_start=args.seed_start,
                code_version=args.code_version,
            ),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
