"""Study 004 finite-state conformance research components."""

from .corpus import generate_corpus, generate_models, generate_mutants, validate_family
from .execution import BlackBoxSystem, ModelBlackBox, TraceExecution, execute_trace
from .methods import (
    MethodResult,
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
from .reducer import ReductionResult, reduce_counterexample
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
)

__all__ = [
    "ACTIONS",
    "FAMILIES",
    "MUTATION_OPERATORS",
    "OUTPUTS",
    "STATE_SIZES",
    "BlackBoxSystem",
    "Corpus",
    "MealyModel",
    "MethodResult",
    "ModelBlackBox",
    "MutationRecord",
    "ReductionResult",
    "TraceExecution",
    "Transition",
    "campaign_lengths",
    "execute_trace",
    "generate_corpus",
    "generate_models",
    "generate_mutants",
    "lexicographic_sequences",
    "random_campaign_seed",
    "random_campaign_traces",
    "reduce_counterexample",
    "run_lexicographic_breadth",
    "run_transition_coverage_guided",
    "run_uniform_random",
    "shortest_reference_paths",
    "transition_pair_target_traces",
    "transition_target_traces",
    "validate_family",
]
