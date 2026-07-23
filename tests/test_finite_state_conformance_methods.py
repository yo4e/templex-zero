from __future__ import annotations

import ast
from itertools import islice
from pathlib import Path

import pytest

from templex_zero.finite_state_conformance.execution import execute_trace
from templex_zero.finite_state_conformance.methods import (
    campaign_lengths,
    lexicographic_sequences,
    random_campaign_seed,
    random_campaign_traces,
    run_lexicographic_breadth,
    run_transition_coverage_guided,
    run_uniform_random,
    shortest_reference_paths,
    transition_pair_target_traces,
    transition_target_traces,
)
from templex_zero.finite_state_conformance.reducer import reduce_counterexample
from templex_zero.finite_state_conformance.schema import (
    MealyModel,
    Transition,
    canonical_bytes,
    sha256_hex,
)


def _row(*items: tuple[int, str]) -> tuple[Transition, ...]:
    return tuple(Transition(target, output) for target, output in items)


def _reference_model() -> MealyModel:
    return MealyModel(
        model_id="fixture-reference",
        family="cyclic",
        state_count=4,
        variant=1,
        transitions=(
            _row((1, "o0"), (0, "o0"), (0, "o0")),
            _row((2, "o0"), (0, "o0"), (1, "o0")),
            _row((3, "o0"), (0, "o0"), (2, "o0")),
            _row((0, "o0"), (0, "o0"), (3, "o0")),
        ),
    )


class OpaqueSystem:
    """Hand-authored black box with no model or transition-table attribute."""

    def __init__(self, outputs: dict[tuple[int, str], str] | None = None) -> None:
        self._state = 0
        self._outputs = outputs or {}

    def reset(self) -> None:
        self._state = 0

    def step(self, action: str) -> str:
        transitions = {
            (0, "a0"): 1,
            (0, "a1"): 0,
            (0, "a2"): 0,
            (1, "a0"): 2,
            (1, "a1"): 0,
            (1, "a2"): 1,
            (2, "a0"): 3,
            (2, "a1"): 0,
            (2, "a2"): 2,
            (3, "a0"): 0,
            (3, "a1"): 0,
            (3, "a2"): 3,
        }
        output = self._outputs.get((self._state, action), "o0")
        self._state = transitions[(self._state, action)]
        return output


class PatternMismatchSystem:
    """Mismatch on a2 after an earlier a1, independent of intervening actions."""

    def __init__(self) -> None:
        self._armed = False

    def reset(self) -> None:
        self._armed = False

    def step(self, action: str) -> str:
        if action == "a1":
            self._armed = True
        if action == "a2" and self._armed:
            return "o1"
        return "o0"


def test_execute_trace_stops_at_first_mismatch() -> None:
    execution = execute_trace(
        _reference_model(),
        OpaqueSystem({(0, "a1"): "o2"}),
        ("a0", "a1", "a2"),
    )
    # a0 moves the black box to state 1, so this configured mismatch is not hit.
    assert not execution.detected

    execution = execute_trace(
        _reference_model(),
        OpaqueSystem({(1, "a1"): "o2"}),
        ("a0", "a1", "a2"),
    )
    assert execution.detected
    assert execution.mismatch_index == 1
    assert execution.failing_trace == ("a0", "a1")
    assert execution.actions_executed == 2
    assert execution.expected_output == "o0"
    assert execution.observed_output == "o2"


def test_random_campaign_partition_and_seed_are_frozen_and_deterministic() -> None:
    digest = "1" * 64
    assert campaign_lengths(64) == (8,) * 8
    assert campaign_lengths(66) == (9, 9, 8, 8, 8, 8, 8, 8)
    first = random_campaign_traces(digest, "M-1", 64)
    second = random_campaign_traces(digest, "M-1", 64)
    assert first == second
    assert len(first) == 8
    assert sum(map(len, first)) == 64
    assert len({random_campaign_seed(digest, "M-1", 64, index) for index in range(8)}) == 8


def test_uniform_random_uses_full_budget_on_identical_opaque_system() -> None:
    result = run_uniform_random(
        _reference_model(),
        OpaqueSystem(),
        budget=64,
        corpus_digest="2" * 64,
        mutant_id="fixture-mutant",
    )
    assert not result.detected
    assert result.actions_executed == 64
    assert result.tests_executed == 8
    assert result.resets == 8


def test_lexicographic_breadth_order_and_detection() -> None:
    assert list(islice(lexicographic_sequences(), 12)) == [
        ("a0",),
        ("a1",),
        ("a2",),
        ("a0", "a0"),
        ("a0", "a1"),
        ("a0", "a2"),
        ("a1", "a0"),
        ("a1", "a1"),
        ("a1", "a2"),
        ("a2", "a0"),
        ("a2", "a1"),
        ("a2", "a2"),
    ]
    result = run_lexicographic_breadth(
        _reference_model(),
        OpaqueSystem({(0, "a2"): "o1"}),
        budget=3,
    )
    assert result.detected
    assert result.failing_trace == ("a2",)
    assert result.actions_executed == 3
    assert result.tests_executed == 3


def test_breadth_never_partially_executes_a_trace() -> None:
    result = run_lexicographic_breadth(_reference_model(), OpaqueSystem(), budget=4)
    # Three length-one tests consume 3 actions. The next length-two test does not fit.
    assert result.actions_executed == 3
    assert result.tests_executed == 3


def test_reference_planning_is_shortest_and_lexicographic() -> None:
    reference = _reference_model()
    assert shortest_reference_paths(reference) == {
        0: (),
        1: ("a0",),
        2: ("a0", "a0"),
        3: ("a0", "a0", "a0"),
    }
    transition_candidates = transition_target_traces(reference)
    assert [trace for _, trace in transition_candidates[:6]] == [
        ("a0",),
        ("a1",),
        ("a2",),
        ("a0", "a0"),
        ("a0", "a1"),
        ("a0", "a2"),
    ]
    pair_candidates = transition_pair_target_traces(reference)
    assert [trace for _, trace in pair_candidates[:6]] == [
        ("a0", "a0"),
        ("a0", "a1"),
        ("a0", "a2"),
        ("a1", "a0"),
        ("a1", "a1"),
        ("a1", "a2"),
    ]


def test_transition_guidance_uses_reference_only_and_detects_in_frozen_order() -> None:
    system = OpaqueSystem({(0, "a1"): "o1"})
    assert not hasattr(system, "model")
    result = run_transition_coverage_guided(_reference_model(), system, budget=64)
    assert result.detected
    # First candidate is a0, second is a1.
    assert result.failing_trace == ("a1",)
    assert result.actions_executed == 2
    assert result.tests_executed == 2


def test_transition_guidance_repeats_pair_rounds_until_no_test_fits() -> None:
    result = run_transition_coverage_guided(
        _reference_model(), OpaqueSystem(), budget=160
    )
    assert not result.detected
    assert 0 < result.actions_executed <= 160
    assert result.actions_executed >= 156
    assert result.tests_executed == result.resets
    assert len(result.transition_coverage) == 12
    assert len(result.transition_pair_coverage) == 36


def test_reducer_applies_prefix_chunk_and_individual_deletion() -> None:
    reference = MealyModel(
        model_id="reducer-reference",
        family="cyclic",
        state_count=4,
        variant=1,
        transitions=tuple(
            _row((state, "o0"), (state, "o0"), (state, "o0"))
            for state in range(4)
        ),
    )
    result = reduce_counterexample(
        reference,
        PatternMismatchSystem(),
        ("a0", "a1", "a0", "a0", "a2", "a0"),
    )
    assert result.reduced_trace == ("a1", "a2")
    assert result.unique_executions > 1
    assert result.failing_candidates >= 2
    assert execute_trace(reference, PatternMismatchSystem(), result.reduced_trace).detected


def test_reducer_rejects_nonfailing_input() -> None:
    with pytest.raises(ValueError, match="does not produce"):
        reduce_counterexample(
            _reference_model(), OpaqueSystem(), ("a0", "a1")
        )


def test_cycle_two_modules_have_no_corpus_or_oracle_imports() -> None:
    root = Path(__file__).parents[1] / "src" / "templex_zero" / "finite_state_conformance"
    for filename in ("execution.py", "methods.py", "reducer.py"):
        tree = ast.parse((root / filename).read_text(encoding="utf-8"))
        imported = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.append(node.module)
        assert not any(name.endswith("corpus") or name.endswith("oracle") for name in imported)


def test_hand_fixture_projection_is_frozen() -> None:
    reference = _reference_model()
    campaigns = random_campaign_traces("3" * 64, "fixture-mutant", 64)
    uniform = run_uniform_random(
        reference,
        OpaqueSystem(),
        budget=64,
        corpus_digest="3" * 64,
        mutant_id="fixture-mutant",
    )
    breadth = run_lexicographic_breadth(
        reference, OpaqueSystem({(0, "a2"): "o1"}), budget=64
    )
    guided = run_transition_coverage_guided(
        reference, OpaqueSystem({(0, "a1"): "o1"}), budget=64
    )
    reducer_reference = MealyModel(
        model_id="reducer-reference",
        family="cyclic",
        state_count=4,
        variant=1,
        transitions=tuple(
            _row((state, "o0"), (state, "o0"), (state, "o0"))
            for state in range(4)
        ),
    )
    reduction = reduce_counterexample(
        reducer_reference,
        PatternMismatchSystem(),
        ("a0", "a1", "a0", "a0", "a2", "a0"),
    )
    projection = {
        "random_campaigns_sha256": sha256_hex(canonical_bytes(campaigns)),
        "uniform": [
            uniform.detected,
            uniform.actions_executed,
            uniform.resets,
            uniform.tests_executed,
            len(uniform.transition_coverage),
            len(uniform.transition_pair_coverage),
        ],
        "breadth": [
            breadth.detected,
            list(breadth.failing_trace or ()),
            breadth.actions_executed,
            breadth.resets,
        ],
        "guided": [
            guided.detected,
            list(guided.failing_trace or ()),
            guided.actions_executed,
            guided.resets,
        ],
        "paths": [
            [state, list(trace)]
            for state, trace in shortest_reference_paths(reference).items()
        ],
        "transition_targets": [
            [list(key), list(trace)]
            for key, trace in transition_target_traces(reference)[:12]
        ],
        "pair_targets": [
            [list(key), list(trace)]
            for key, trace in transition_pair_target_traces(reference)[:12]
        ],
        "reducer": [
            list(reduction.reduced_trace),
            reduction.unique_executions,
            reduction.cache_hits,
            reduction.failing_candidates,
        ],
    }
    assert sha256_hex(canonical_bytes(projection)) == (
        "6eddea3466f3f4ceb4a77a687a45ac6965e31f1039e3a6433d1c3ba34046abd6"
    )
