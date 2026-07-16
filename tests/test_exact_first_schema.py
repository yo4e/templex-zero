import pytest

from templex_zero.exact_first import (
    FirstMoveScope,
    GameSpec,
    GoalKind,
    GoalRule,
    MechanismFamily,
    PlacementKind,
    PlacementRule,
    State,
    apply_action,
    initial_state,
    legal_actions,
    terminal_result,
)
from templex_zero.exact_first import grammar


def basic_spec(**overrides):
    values = {
        "name": "basic",
        "board_size": 2,
        "family": MechanismFamily.FIXTURE,
        "placement": PlacementRule(PlacementKind.ANY),
        "goal": GoalRule(GoalKind.COMPONENT_SIZE, threshold=2),
    }
    values.update(overrides)
    return GameSpec(**values)


def test_default_playable_cells_and_immutable_transition():
    spec = basic_spec()
    state = initial_state(spec)
    assert state.board == (-1, -1, -1, -1)
    assert legal_actions(spec, state) == (0, 1, 2, 3)
    child = apply_action(spec, state, 2)
    assert state.board == (-1, -1, -1, -1)
    assert child.board == (-1, -1, 0, -1)
    assert child.player == 1
    assert child.ply == 1


def test_explicit_opening_cells_are_enforced():
    spec = basic_spec(
        placement=PlacementRule(
            PlacementKind.FRIENDLY_ADJACENCY,
            first_move_scope=FirstMoveScope.EXPLICIT,
            explicit_first_cells=((0,), (3,)),
            friendly_min=1,
        )
    )
    state = initial_state(spec)
    assert legal_actions(spec, state) == (0,)
    state = apply_action(spec, state, 0)
    assert legal_actions(spec, state) == (3,)


def test_terminal_states_expose_no_legal_actions():
    spec = basic_spec(
        board_size=1,
        goal=GoalRule(GoalKind.COMPONENT_SIZE, threshold=1),
    )
    state = apply_action(spec, initial_state(spec), 0)
    assert terminal_result(spec, state) == "win:0"
    assert legal_actions(spec, state) == ()
    with pytest.raises(ValueError, match="illegal action"):
        apply_action(spec, state, 0)


def test_schema_rejects_ambiguous_or_out_of_scope_values():
    with pytest.raises(ValueError, match="between 1 and 4"):
        basic_spec(board_size=5)
    with pytest.raises(ValueError, match="unique"):
        basic_spec(playable_cells=(0, 0))
    with pytest.raises(ValueError, match="between 0 and 250"):
        basic_spec(core_rule_words=251)
    with pytest.raises(ValueError, match="cells for both players"):
        PlacementRule(
            PlacementKind.ANY,
            first_move_scope=FirstMoveScope.EXPLICIT,
        )
    with pytest.raises(ValueError, match="allow expansion or merger"):
        PlacementRule(PlacementKind.EXPAND_OR_MERGE)


def test_frozen_grammar_has_six_cells_and_eighteen_targets():
    assert grammar.GENERATION_SEED == 2026071602
    assert grammar.cell_order() == (
        (3, MechanismFamily.ADJACENCY_GROWTH),
        (3, MechanismFamily.COMPONENT_EXPANSION),
        (3, MechanismFamily.LOCAL_BLOCK_PATTERN),
        (4, MechanismFamily.ADJACENCY_GROWTH),
        (4, MechanismFamily.COMPONENT_EXPANSION),
        (4, MechanismFamily.LOCAL_BLOCK_PATTERN),
    )
    assert grammar.CANDIDATES_PER_CELL == 3
    assert grammar.TOTAL_CANDIDATES == 18


def test_expand_merge_and_enemy_limit_rules_are_declarative():
    merge_spec = GameSpec(
        name="merge",
        board_size=3,
        family=MechanismFamily.FIXTURE,
        placement=PlacementRule(
            PlacementKind.EXPAND_OR_MERGE,
            allow_merge=True,
        ),
        goal=GoalRule(GoalKind.COMPONENT_SIZE, threshold=3),
    )
    merge_state = State((0, -1, 0, -1, -1, -1, -1, -1, -1), 0, 2)
    assert 1 in legal_actions(merge_spec, merge_state)

    block_spec = GameSpec(
        name="block",
        board_size=2,
        family=MechanismFamily.FIXTURE,
        placement=PlacementRule(
            PlacementKind.ENEMY_LIMIT,
            enemy_max=0,
        ),
        goal=GoalRule(GoalKind.LINE, threshold=2),
    )
    block_state = State((1, -1, -1, -1), 0, 1)
    assert 1 not in legal_actions(block_spec, block_state)
    assert 2 not in legal_actions(block_spec, block_state)
    assert 3 in legal_actions(block_spec, block_state)


def test_candidate_schema_boundaries_are_enforced():
    with pytest.raises(ValueError, match="3x3 or 4x4"):
        GameSpec(
            name="bad_candidate",
            board_size=2,
            family=MechanismFamily.ADJACENCY_GROWTH,
            placement=PlacementRule(PlacementKind.ANY),
            goal=GoalRule(GoalKind.LINE, threshold=2),
        )
    with pytest.raises(ValueError, match="every board cell"):
        GameSpec(
            name="masked_candidate",
            board_size=3,
            family=MechanismFamily.ADJACENCY_GROWTH,
            playable_cells=(0, 1, 2),
            placement=PlacementRule(PlacementKind.ANY),
            goal=GoalRule(GoalKind.LINE, threshold=3),
        )
    with pytest.raises(ValueError, match="intended symmetry"):
        GameSpec(
            name="asymmetric_candidate",
            board_size=3,
            family=MechanismFamily.ADJACENCY_GROWTH,
            placement=PlacementRule(PlacementKind.ANY),
            goal=GoalRule(GoalKind.LINE, threshold=3),
            intended_symmetric=False,
        )
