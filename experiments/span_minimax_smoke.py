"""Run a reproducible equal-depth Span minimax smoke screen.

This is an instrumentation check, not the full balance experiment.

Run from the repository root:

    PYTHONPATH=src python experiments/span_minimax_smoke.py \
        --games 200 --depth 2 --seed-start 0 --code-version <commit>
"""

from __future__ import annotations

import argparse
import json
import platform
from collections import Counter
from statistics import mean, median

from templex_zero import span_agents
from templex_zero.span_match import Result, play


def _move_name(move: tuple[int, int]) -> str:
    row, column = move
    return f"{chr(column + 65)}{row + 1}"


def summarize(
    results: list[Result], *, depth: int, seed_start: int, code_version: str
) -> dict[str, object]:
    wins = Counter(result.winner for result in results)
    modes = Counter(result.win_mode for result in results)
    openings = Counter(result.opening_move for result in results)
    plies = [result.plies for result in results]
    return {
        "experiment": "span-v0.1-equal-depth-minimax-smoke",
        "interpretation_limit": (
            "This run checks deterministic symmetric-agent instrumentation. "
            "It is too small and too shallow to establish balance or strategic depth."
        ),
        "configuration": {
            "games": len(results),
            "depth": depth,
            "seed_start": seed_start,
            "seed_end_inclusive": seed_start + len(results) - 1,
            "equal_agent_both_seats": True,
            "independent_match_rng_per_seed": True,
            "code_version": code_version,
            "python_version": platform.python_version(),
        },
        "wins": {
            "black": wins[0],
            "white": wins[1],
            "black_rate": wins[0] / len(results),
            "white_rate": wins[1] / len(results),
        },
        "win_modes": {
            "connection": modes["connection"],
            "immobilization": modes["immobilization"],
        },
        "plies": {
            "minimum": min(plies),
            "median": median(plies),
            "mean": mean(plies),
            "maximum": max(plies),
        },
        "opening_moves": {
            _move_name(move): count for move, count in sorted(openings.items())
        },
    }


def run(
    *, games: int, depth: int, seed_start: int, code_version: str
) -> dict[str, object]:
    if games < 1:
        raise ValueError("games must be at least 1")
    agent = span_agents.minimax_agent(depth)
    results = [
        play(agent, agent, seed)
        for seed in range(seed_start, seed_start + games)
    ]
    return summarize(
        results,
        depth=depth,
        seed_start=seed_start,
        code_version=code_version,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=200)
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--seed-start", type=int, default=0)
    parser.add_argument("--code-version", default="uncommitted")
    args = parser.parse_args()
    print(
        json.dumps(
            run(
                games=args.games,
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
