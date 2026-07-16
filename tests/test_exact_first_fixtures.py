from templex_zero.exact_first import enumerate_state_graph
from templex_zero.exact_first.fixtures import AUDITED_FIXTURES


def test_four_fixtures_have_exact_hand_audited_graphs():
    assert len(AUDITED_FIXTURES) == 4
    for fixture in AUDITED_FIXTURES:
        assert enumerate_state_graph(fixture.spec) == fixture.expected_graph


def test_fixture_names_and_graphs_are_distinct():
    names = [fixture.name for fixture in AUDITED_FIXTURES]
    graphs = [fixture.expected_graph for fixture in AUDITED_FIXTURES]
    assert len(set(names)) == len(names)
    assert len({repr(graph) for graph in graphs}) == len(graphs)


def test_at_least_two_fixtures_claim_symmetry_for_later_solver_checks():
    claimed = [fixture for fixture in AUDITED_FIXTURES if fixture.symmetry_claim]
    assert len(claimed) >= 2
