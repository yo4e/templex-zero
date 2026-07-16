"""Independent fixture oracle using graph construction and retrograde evaluation."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from types import MappingProxyType
from typing import Literal, Mapping

from .schema import (
    Action,
    GameSpec,
    State,
    apply_action,
    initial_state,
    legal_actions,
    terminal_result,
)

BruteOutcome = Literal["win", "draw", "loss"]


@dataclass(frozen=True)
class BruteValue:
    outcome: BruteOutcome
    distance: int


@dataclass(frozen=True)
class BruteActionValue:
    action: Action
    value: BruteValue


@dataclass(frozen=True)
class BruteForceResult:
    root: BruteValue
    opening_values: tuple[BruteActionValue, ...]
    reachable_states: int
    values: Mapping[State, BruteValue]
    action_values: Mapping[State, tuple[BruteActionValue, ...]]


def solve_bruteforce(
    spec: GameSpec,
    root: State | None = None,
) -> BruteForceResult:
    """Build the complete reachable graph, then evaluate it backwards by ply."""

    root_state = root if root is not None else initial_state(spec)
    queue = deque([root_state])
    seen = {root_state}
    children: dict[State, tuple[tuple[Action, State], ...]] = {}

    while queue:
        state = queue.popleft()
        edges = tuple(
            (action, apply_action(spec, state, action))
            for action in legal_actions(spec, state)
        )
        children[state] = edges
        for _, child in edges:
            if child not in seen:
                seen.add(child)
                queue.append(child)

    values: dict[State, BruteValue] = {}
    action_values: dict[State, tuple[BruteActionValue, ...]] = {}

    for state in sorted(seen, key=lambda item: item.ply, reverse=True):
        terminal = terminal_result(spec, state)
        if terminal != "ongoing":
            if terminal == "draw":
                value = BruteValue("draw", 0)
            else:
                winner = int(terminal[-1])
                value = BruteValue(
                    "win" if winner == state.player else "loss",
                    0,
                )
            values[state] = value
            action_values[state] = ()
            continue

        evaluated = []
        for action, child in children[state]:
            child_value = values[child]
            reversed_outcome: BruteOutcome
            if child_value.outcome == "win":
                reversed_outcome = "loss"
            elif child_value.outcome == "loss":
                reversed_outcome = "win"
            else:
                reversed_outcome = "draw"
            evaluated.append(
                BruteActionValue(
                    action,
                    BruteValue(
                        reversed_outcome,
                        child_value.distance + 1,
                    ),
                )
            )

        ranked = {"loss": 0, "draw": 1, "win": 2}
        chosen_outcome = max(
            (item.value.outcome for item in evaluated),
            key=ranked.__getitem__,
        )
        same = [
            item.value.distance
            for item in evaluated
            if item.value.outcome == chosen_outcome
        ]
        chosen_distance = max(same) if chosen_outcome == "loss" else min(same)
        values[state] = BruteValue(
            chosen_outcome,
            chosen_distance,
        )  # type: ignore[arg-type]
        action_values[state] = tuple(evaluated)

    return BruteForceResult(
        root=values[root_state],
        opening_values=action_values[root_state],
        reachable_states=len(seen),
        values=MappingProxyType(values),
        action_values=MappingProxyType(action_values),
    )
