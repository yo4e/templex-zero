"""Deterministic generator for the frozen Study 004 Cycle 1 corpus.

The generator creates structural reference models and six deterministic mutants
per model. It deliberately performs no equivalence classification, black-box
campaign, counterexample reduction, or exact-oracle search.
"""
from __future__ import annotations

import hashlib
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

from .schema import (
    ACTIONS,
    FAMILIES,
    MUTATION_OPERATORS,
    OUTPUTS,
    STATE_SIZES,
    Corpus,
    MealyModel,
    MutationRecord,
    Transition,
    replace_row,
    replace_transition,
)

SEED = 2026072104
PROPOSAL_PATH = "research/proposals/STUDY_004_FINITE_STATE_CONFORMANCE.md"
PROPOSAL_BLOB_SHA = "0b16048ad8e96dcaf147f033205ad76069430776"
DEFAULT_OUTPUT_PATH = Path(
    "research/studies/004-finite-state-conformance/data/corpus_v1.json"
)
DEFAULT_MODELS_PATH = Path(
    "research/studies/004-finite-state-conformance/data/models_v1.json"
)

FAMILY_CODES = {
    "reset-chain": "RC",
    "clustered": "CL",
    "cyclic": "CY",
}


def _digest(*parts: object) -> str:
    text = "\x1f".join(str(part) for part in parts)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _index(modulus: int, *parts: object) -> int:
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    return int(_digest(*parts), 16) % modulus


def _output(family: str, state_count: int, variant: int, state: int, action: int) -> str:
    return OUTPUTS[
        _index(len(OUTPUTS), SEED, "output", family, state_count, variant, state, action)
    ]


def _extra_target(
    family: str, state_count: int, variant: int, state: int, action: int
) -> int:
    return _index(
        state_count, SEED, "target", family, state_count, variant, state, action
    )


def _reset_chain_targets(state_count: int, variant: int, state: int) -> tuple[int, int, int]:
    reset = 0
    advance = state + 1 if state + 1 < state_count else 0
    extra = _extra_target("reset-chain", state_count, variant, state, 2)
    return reset, advance, extra


def _clustered_targets(state_count: int, variant: int, state: int) -> tuple[int, int, int]:
    cluster_size = state_count // 2
    cluster = 0 if state < cluster_size else 1
    start = cluster * cluster_size
    local = state - start
    first = start + ((local + 1) % cluster_size)
    second = start + ((local + 1 + (variant % cluster_size)) % cluster_size)

    bridge_local = (variant - 1) % cluster_size
    if local == bridge_local:
        third = (1 - cluster) * cluster_size + ((local + variant) % cluster_size)
    else:
        third = start + ((local + 2 + variant) % cluster_size)
    return first, second, third


def _cyclic_targets(state_count: int, variant: int, state: int) -> tuple[int, int, int]:
    cycle = (state + 1) % state_count
    second = _extra_target("cyclic", state_count, variant, state, 1)
    third = _extra_target("cyclic", state_count, variant, state, 2)
    return cycle, second, third


def generate_model(family: str, state_count: int, variant: int) -> MealyModel:
    if family not in FAMILIES:
        raise ValueError(f"unknown family: {family}")
    if state_count not in STATE_SIZES:
        raise ValueError(f"unsupported state_count: {state_count}")
    if variant not in (1, 2, 3, 4):
        raise ValueError("variant must be 1..4")

    rows: list[tuple[Transition, ...]] = []
    for state in range(state_count):
        if family == "reset-chain":
            targets = _reset_chain_targets(state_count, variant, state)
        elif family == "clustered":
            targets = _clustered_targets(state_count, variant, state)
        else:
            targets = _cyclic_targets(state_count, variant, state)
        rows.append(
            tuple(
                Transition(target, _output(family, state_count, variant, state, action))
                for action, target in enumerate(targets)
            )
        )

    model_id = f"S4-{state_count}-{FAMILY_CODES[family]}-{variant:02d}"
    model = MealyModel(model_id, family, state_count, variant, tuple(rows))
    validate_family(model)
    return model


def validate_family(model: MealyModel) -> None:
    """Check only frozen structural family membership."""
    if model.family == "reset-chain":
        if any(row[0].target != 0 for row in model.transitions):
            raise ValueError("reset-chain a0 must always return to reset")
        for state in range(model.state_count - 1):
            if model.transitions[state][1].target != state + 1:
                raise ValueError("reset-chain a1 must advance through the chain")
    elif model.family == "clustered":
        split = model.state_count // 2
        cross = 0
        for state, row in enumerate(model.transitions):
            source_cluster = state // split
            for transition in row:
                if transition.target // split != source_cluster:
                    cross += 1
        if cross != 2:
            raise ValueError("clustered family must contain exactly two cross-group transitions")
    elif model.family == "cyclic":
        visited = {0}
        state = 0
        for _ in range(model.state_count):
            state = model.transitions[state][0].target
            visited.add(state)
        if state != 0 or len(visited) != model.state_count:
            raise ValueError("cyclic a0 must form a full-state cycle")
    else:
        raise ValueError(f"unknown family: {model.family}")


def generate_models() -> tuple[MealyModel, ...]:
    return tuple(
        generate_model(family, state_count, variant)
        for state_count in STATE_SIZES
        for family in FAMILIES
        for variant in range(1, 5)
    )


def _selection(model: MealyModel, operator: str) -> tuple[str, int]:
    digest = _digest(SEED, model.digest, operator)
    return digest, int(digest, 16)


def _changed_target(original: int, state_count: int, selector: int) -> int:
    choices = [state for state in range(state_count) if state != original]
    return choices[selector % len(choices)]


def _changed_output(original: str, selector: int) -> str:
    choices = [label for label in OUTPUTS if label != original]
    return choices[selector % len(choices)]


def _mutant_model(
    source: MealyModel,
    operator: str,
    transitions: tuple[tuple[Transition, ...], ...],
) -> MealyModel:
    suffix = MUTATION_OPERATORS.index(operator) + 1
    return MealyModel(
        model_id=f"{source.model_id}-M{suffix:02d}",
        family=source.family,
        state_count=source.state_count,
        variant=source.variant,
        transitions=transitions,
    )


def mutate(model: MealyModel, operator: str) -> MutationRecord:
    if operator not in MUTATION_OPERATORS:
        raise ValueError(f"unknown mutation operator: {operator}")
    selection_digest, selector = _selection(model, operator)
    transitions = model.transitions
    cell_count = model.state_count * len(ACTIONS)

    if operator == "transition-target-substitution":
        cell = selector % cell_count
        state, action = divmod(cell, len(ACTIONS))
        old = transitions[state][action]
        new_target = _changed_target(old.target, model.state_count, selector // cell_count)
        changed = replace_transition(transitions, state, action, Transition(new_target, old.output))
        metadata = {
            "state": state,
            "action": ACTIONS[action],
            "old_target": old.target,
            "new_target": new_target,
        }

    elif operator == "output-label-substitution":
        cell = selector % cell_count
        state, action = divmod(cell, len(ACTIONS))
        old = transitions[state][action]
        new_output = _changed_output(old.output, selector // cell_count)
        changed = replace_transition(transitions, state, action, Transition(old.target, new_output))
        metadata = {
            "state": state,
            "action": ACTIONS[action],
            "old_output": old.output,
            "new_output": new_output,
        }

    elif operator == "action-column-swap":
        candidates: list[tuple[int, int, int]] = []
        for state, row in enumerate(transitions):
            for left, right in combinations(range(len(ACTIONS)), 2):
                if row[left] != row[right]:
                    candidates.append((state, left, right))
        state, left, right = candidates[selector % len(candidates)]
        rows = [list(row) for row in transitions]
        rows[state][left], rows[state][right] = rows[state][right], rows[state][left]
        changed = tuple(tuple(row) for row in rows)
        metadata = {
            "state": state,
            "left_action": ACTIONS[left],
            "right_action": ACTIONS[right],
        }

    elif operator == "state-row-transplant":
        candidates = [
            (destination, source)
            for destination in range(model.state_count)
            for source in range(model.state_count)
            if destination != source and transitions[destination] != transitions[source]
        ]
        destination, source = candidates[selector % len(candidates)]
        changed = replace_row(transitions, destination, transitions[source])
        metadata = {"destination_state": destination, "source_state": source}

    elif operator == "self-loop-injection":
        candidates = [
            (state, action)
            for state, row in enumerate(transitions)
            for action, transition in enumerate(row)
            if transition.target != state
        ]
        state, action = candidates[selector % len(candidates)]
        old = transitions[state][action]
        changed = replace_transition(transitions, state, action, Transition(state, old.output))
        metadata = {
            "state": state,
            "action": ACTIONS[action],
            "old_target": old.target,
            "new_target": state,
        }

    else:  # paired-transition-mutation
        cells = [
            (state, action)
            for state in range(model.state_count)
            for action in range(len(ACTIONS))
        ]
        pairs = [
            (first, second)
            for first, second in combinations(cells, 2)
            if first[0] != second[0]
        ]
        first, second = pairs[selector % len(pairs)]
        rows = [list(row) for row in transitions]
        details: list[dict[str, Any]] = []
        for offset, (state, action) in enumerate((first, second), start=1):
            old = rows[state][action]
            new_target = _changed_target(
                old.target,
                model.state_count,
                selector // (len(pairs) + offset),
            )
            rows[state][action] = Transition(new_target, old.output)
            details.append(
                {
                    "state": state,
                    "action": ACTIONS[action],
                    "old_target": old.target,
                    "new_target": new_target,
                }
            )
        changed = tuple(tuple(row) for row in rows)
        metadata = {"changes": details}

    mutant = _mutant_model(model, operator, changed)
    if mutant.transitions == model.transitions:
        raise AssertionError(f"mutation produced no structural change: {model.model_id} {operator}")
    return MutationRecord(
        mutant_id=mutant.model_id,
        source_model_id=model.model_id,
        source_model_digest=model.digest,
        operator=operator,
        selection_digest=selection_digest,
        mutation=metadata,
        model=mutant,
    )


def generate_mutants(models: Iterable[MealyModel]) -> tuple[MutationRecord, ...]:
    return tuple(
        mutate(model, operator)
        for model in models
        for operator in MUTATION_OPERATORS
    )


def generate_corpus() -> Corpus:
    models = generate_models()
    mutants = generate_mutants(models)
    return Corpus(
        schema_version=1,
        proposal_path=PROPOSAL_PATH,
        proposal_blob_sha=PROPOSAL_BLOB_SHA,
        seed=SEED,
        models=models,
        mutants=mutants,
    )


def write_corpus(
    path: Path = DEFAULT_OUTPUT_PATH,
    models_path: Path | None = None,
) -> Corpus:
    corpus = generate_corpus()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(corpus.to_bytes())
    target_models = models_path or path.with_name("models_v1.json")
    target_models.parent.mkdir(parents=True, exist_ok=True)
    target_models.write_bytes(corpus.models_to_bytes())
    return corpus
