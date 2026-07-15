"""Run a reproducible random-vs-random pathology screen for Keystone v0.1.

This experiment checks termination behavior and gross pathologies. Random-play
win rates are not evidence of strategic balance.

Run from the repository root:

    PYTHONPATH=src python experiments/keystone_random_screen.py \
        --games 2000 --seed-start 0 --ply-limit 200 \
        --code-version <commit>
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

from templex_zero.games import keystone

EndMode = Literal["victory", "immobilization", "repetition", "limit"]


@dataclass(frozen=True, slots=True)
class GameResult:
    seed: int
    winner: int | None
    end_mode: EndMode
    plies: int
    opening_destination: keystone.Cell
    branch_counts: tuple[int, ...]
    placements: tuple[int, int]
    shifts: tuple[int, int]
    captures: tuple[int, int]
    final_reserves: tuple[int, int]
    final_stones: tuple[int, int]
    maximum_repetition_count: int


def _position_multiplicity(state: keystone.State) -> int:
    counts = Counter(state.history)
    return max(counts.values(), default=1)


def play_random(seed: int, *, ply_limit: int) -> GameResult:
    rng = random.Random(seed)
    state = keystone.initial_state()
    branch_counts: list[int] = []
    opening_destination: keystone.Cell | None = None
    placements = [0, 0]
    shifts = [0, 0]
    captures = [0, 0]

    while True:
        outcome = keystone.winner(state)
        if outcome != "ongoing":
            if outcome is None:
                end_mode: EndMode = "repetition"
                winner: int | None = None
            else:
                winner = int(outcome)
                end_mode = (
                    "victory"
                    if keystone._has_victory(state.board, winner)
                    else "immobilization"
                )
            break

        if state.ply >= ply_limit:
            winner = None
            end_mode = "limit"
            break

        actions = keystone.legal_actions(state)
        branch_counts.append(len(actions))
        action = rng.choice(actions)
        mover = state.player
        if opening_destination is None:
            opening_destination = action.destination
        if action.is_placement:
            placements[mover] += 1
        else:
            shifts[mover] += 1
        if action.capture is not None:
            captures[mover] += 1
        state = keystone.apply_action(state, action)

    if opening_destination is None:
        raise AssertionError("Keystone terminated before the first action")

    return GameResult(
        seed=seed,
        winner=winner,
        end_mode=end_mode,
        plies=state.ply,
        opening_destination=opening_destination,
        branch_counts=tuple(branch_counts),
        placements=(placements[0], placements[1]),
        shifts=(shifts[0], shifts[1]),
        captures=(captures[0], captures[1]),
        final_reserves=state.reserves,
        final_stones=(state.board.count(0), state.board.count(1)),
        maximum_repetition_count=_position_multiplicity(state),
    )


def _percentile(values: list[int], fraction: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * fraction
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def _distribution(values: list[int]) -> dict[str, int]:
    return {str(value): count for value, count in sorted(Counter(values).items())}


def summarize(
    results: list[GameResult],
    *,
    code_version: str,
    seed_start: int,
    ply_limit: int,
) -> dict[str, object]:
    plies = [result.plies for result in results]
    all_branches = [count for result in results for count in result.branch_counts]
    branches_by_ply: dict[int, list[int]] = defaultdict(list)
    for result in results:
        for ply, count in enumerate(result.branch_counts):
            branches_by_ply[ply].append(count)

    modes = Counter(result.end_mode for result in results)
    winners = Counter(result.winner for result in results)
    openings = Counter(result.opening_destination for result in results)
    total_placements = [sum(result.placements[p] for result in results) for p in (0, 1)]
    total_shifts = [sum(result.shifts[p] for result in results) for p in (0, 1)]
    total_captures = [sum(result.captures[p] for result in results) for p in (0, 1)]
    final_black_reserves = [result.final_reserves[0] for result in results]
    final_white_reserves = [result.final_reserves[1] for result in results]
    final_black_stones = [result.final_stones[0] for result in results]
    final_white_stones = [result.final_stones[1] for result in results]
    repetitions = [result.maximum_repetition_count for result in results]

    completed = len(results) - modes["limit"]
    return {
        "experiment": "keystone-v0.1-random-pathology-screen",
        "interpretation_limit": (
            "Random play tests termination and gross pathology only; "
            "its win rates are not evidence of strategic balance."
        ),
        "configuration": {
            "games": len(results),
            "seed_start": seed_start,
            "seed_end_inclusive": seed_start + len(results) - 1,
            "independent_rng_per_game": True,
            "board_size": keystone.BOARD_SIZE,
            "stones_per_player": keystone.STONES_PER_PLAYER,
            "ply_observation_limit": ply_limit,
            "code_version": code_version,
            "python_version": platform.python_version(),
        },
        "termination": {
            "completed_games": completed,
            "completion_rate": completed / len(results),
            "structural_victories": modes["victory"],
            "immobilization_wins": modes["immobilization"],
            "threefold_repetition_draws": modes["repetition"],
            "observation_limit_hits": modes["limit"],
        },
        "results": {
            "black_wins": winners[0],
            "white_wins": winners[1],
            "draws_or_limits": winners[None],
            "black_rate_all_games": winners[0] / len(results),
            "white_rate_all_games": winners[1] / len(results),
        },
        "plies": {
            "minimum": min(plies),
            "p10": _percentile(plies, 0.10),
            "median": median(plies),
            "mean": mean(plies),
            "p90": _percentile(plies, 0.90),
            "maximum": max(plies),
            "mean_by_end_mode": {
                mode: mean(result.plies for result in results if result.end_mode == mode)
                for mode in ("victory", "immobilization", "repetition", "limit")
                if modes[mode]
            },
        },
        "branching": {
            "decision_nodes": len(all_branches),
            "minimum": min(all_branches),
            "median": median(all_branches),
            "mean": mean(all_branches),
            "maximum": max(all_branches),
            "mean_by_ply": {
                str(ply): mean(counts)
                for ply, counts in sorted(branches_by_ply.items())
            },
        },
        "actions": {
            "placements": {
                "black": total_placements[0],
                "white": total_placements[1],
                "total": sum(total_placements),
            },
            "shifts": {
                "black": total_shifts[0],
                "white": total_shifts[1],
                "total": sum(total_shifts),
            },
            "captures": {
                "black": total_captures[0],
                "white": total_captures[1],
                "total": sum(total_captures),
                "mean_per_game": sum(total_captures) / len(results),
                "games_with_no_capture": sum(sum(result.captures) == 0 for result in results),
            },
        },
        "reserves": {
            "mean_final_black": mean(final_black_reserves),
            "mean_final_white": mean(final_white_reserves),
            "black_distribution": _distribution(final_black_reserves),
            "white_distribution": _distribution(final_white_reserves),
            "both_exhausted": sum(result.final_reserves == (0, 0) for result in results),
        },
        "final_stones": {
            "mean_black": mean(final_black_stones),
            "mean_white": mean(final_white_stones),
            "black_distribution": _distribution(final_black_stones),
            "white_distribution": _distribution(final_white_stones),
        },
        "repetition_pressure": {
            "maximum_position_multiplicity": max(repetitions),
            "games_reaching_second_occurrence": sum(value >= 2 for value in repetitions),
            "games_reaching_third_occurrence": sum(value >= 3 for value in repetitions),
        },
        "opening_destinations": {
            f"{chr(column + 65)}{row + 1}": count
            for (row, column), count in sorted(openings.items())
        },
    }


def run(
    *, games: int, seed_start: int, ply_limit: int, code_version: str
) -> dict[str, object]:
    if games < 1:
        raise ValueError("games must be at least 1")
    if ply_limit < 1:
        raise ValueError("ply_limit must be at least 1")
    results = [
        play_random(seed, ply_limit=ply_limit)
        for seed in range(seed_start, seed_start + games)
    ]
    return summarize(
        results,
        code_version=code_version,
        seed_start=seed_start,
        ply_limit=ply_limit,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=2_000)
    parser.add_argument("--seed-start", type=int, default=0)
    parser.add_argument("--ply-limit", type=int, default=200)
    parser.add_argument("--code-version", default="uncommitted")
    args = parser.parse_args()
    print(
        json.dumps(
            run(
                games=args.games,
                seed_start=args.seed_start,
                ply_limit=args.ply_limit,
                code_version=args.code_version,
            ),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
