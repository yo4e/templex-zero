"""Generate the deterministic Study 004 Cycle 3 raw result bundle.

The runner verifies frozen Cycle 1 identities, classifies the unreplaced corpus
with the independent Cycle 3 oracle, applies the 80% viability gate, and only
then executes the frozen Cycle 2 methods and reducer. It records raw evidence
without assigning H1-H3 dispositions.
"""
from __future__ import annotations

from collections import Counter
import gzip
import hashlib
import json
from math import ceil
from pathlib import Path
from typing import Any, Callable

from templex_zero.finite_state_conformance.corpus import generate_corpus
from templex_zero.finite_state_conformance.execution import ModelBlackBox, execute_trace
from templex_zero.finite_state_conformance.methods import (
    METHOD_LEXICOGRAPHIC_BREADTH,
    METHOD_TRANSITION_COVERAGE,
    METHOD_UNIFORM_RANDOM,
    run_lexicographic_breadth,
    run_transition_coverage_guided,
    run_uniform_random,
)
from templex_zero.finite_state_conformance.oracle import exact_shortest_counterexample
from templex_zero.finite_state_conformance.reducer import reduce_counterexample
from templex_zero.finite_state_conformance.schema import canonical_bytes, sha256_hex

BUDGETS = (64, 256, 1024)
CORPUS_PAYLOAD_SHA256 = "c9897631050b937d31a3273ba8cdabc55b79be1d66a0f4ca2e5c6df9f7c79fdb"
CORPUS_FILE_SHA256 = "82fcd584661e4860167ff114041868b923adb6861395a249564af4ff771b8fa2"
MODELS_PAYLOAD_SHA256 = "7925911d9f834d71a360defc862d8d67262989eb2e957cf334b94a1b3a58202b"
MODELS_FILE_SHA256 = "bf3eab9884381a634d90803d3367c4700c8553ac43ec112355b2881dc4aaa902"
FIXTURE_FILE = Path("research/studies/004-finite-state-conformance/data/oracle_fixtures_v1.json")
FIXTURE_FILE_SHA256 = "c3dbd66b2260918f1f3b0071d39655d00f4734f3ef427dd2dd0796c4d4e3281e"
OUTPUT_GZIP = Path("research/studies/004-finite-state-conformance/data/cycle3_raw_results_v1.json.gz")
OUTPUT_MANIFEST = Path("research/studies/004-finite-state-conformance/data/cycle3_raw_manifest_v1.json")
SOURCE_BLOBS = {
    "schema": "9989f19fa46e9529cb8e9b5fbd877c90a4726b68",
    "corpus": "9727ccc358c35faaec34e310e612068c55791526",
    "execution": "f02c1cf1f46ccd4240ce4159b64c6c5872adb607",
    "methods": "a26c20add82b6794301fb4a0de6c83e5158015da",
    "reducer": "e7df33ec3bab54c8bc0ef5ee22e0d1a7cd21e39b",
    "oracle": "6eb6205dc32877446201b34d5a591e9851cfd69f",
}
METHODS: tuple[tuple[str, Callable[..., Any]], ...] = (
    (METHOD_UNIFORM_RANDOM, run_uniform_random),
    (METHOD_LEXICOGRAPHIC_BREADTH, run_lexicographic_breadth),
    (METHOD_TRANSITION_COVERAGE, run_transition_coverage_guided),
)


def _trace(value: tuple[str, ...] | None) -> list[str] | None:
    return None if value is None else list(value)


def _method_result(
    method_name: str,
    method: Callable[..., Any],
    reference,
    mutant,
    budget: int,
    corpus_digest: str,
):
    system = ModelBlackBox(mutant.model)
    if method_name == METHOD_UNIFORM_RANDOM:
        return method(
            reference,
            system,
            budget=budget,
            corpus_digest=corpus_digest,
            mutant_id=mutant.mutant_id,
        )
    return method(reference, system, budget=budget)


def generate_cycle3_payload() -> dict[str, Any]:
    corpus = generate_corpus()
    if corpus.payload_sha256 != CORPUS_PAYLOAD_SHA256:
        raise AssertionError("frozen corpus payload changed")
    if sha256_hex(corpus.to_bytes()) != CORPUS_FILE_SHA256:
        raise AssertionError("frozen corpus file changed")
    if corpus.model_payload_sha256 != MODELS_PAYLOAD_SHA256:
        raise AssertionError("frozen model payload changed")
    if sha256_hex(corpus.models_to_bytes()) != MODELS_FILE_SHA256:
        raise AssertionError("frozen model file changed")
    if sha256_hex(FIXTURE_FILE.read_bytes()) != FIXTURE_FILE_SHA256:
        raise AssertionError("frozen oracle fixtures changed")

    by_model = {model.model_id: model for model in corpus.models}
    classification: list[dict[str, Any]] = []
    oracle_by_mutant: dict[str, Any] = {}

    for mutant in corpus.mutants:
        reference = by_model[mutant.source_model_id]
        result = exact_shortest_counterexample(reference, mutant.model)
        oracle_by_mutant[mutant.mutant_id] = result
        classification.append(
            {
                "mutant_id": mutant.mutant_id,
                "source_model_id": mutant.source_model_id,
                "family": reference.family,
                "state_count": reference.state_count,
                "operator": mutant.operator,
                "equivalent": result.equivalent,
                "shortest_trace": _trace(result.shortest_trace),
                "shortest_length": None if result.shortest_trace is None else len(result.shortest_trace),
                "visited_pairs": result.visited_pairs,
            }
        )

    distinguishable = sum(not row["equivalent"] for row in classification)
    viability_required = ceil(0.80 * len(classification))
    viable = distinguishable >= viability_required
    benchmark_rows: list[dict[str, Any]] = []

    if viable:
        for mutant in corpus.mutants:
            reference = by_model[mutant.source_model_id]
            oracle = oracle_by_mutant[mutant.mutant_id]
            for budget in BUDGETS:
                for method_name, method in METHODS:
                    result = _method_result(
                        method_name,
                        method,
                        reference,
                        mutant,
                        budget,
                        corpus.payload_sha256,
                    )
                    if oracle.equivalent and result.detected:
                        raise AssertionError(
                            f"method detected oracle-equivalent mutant {mutant.mutant_id}"
                        )
                    reduction = None
                    if result.detected:
                        reduced = reduce_counterexample(
                            reference,
                            ModelBlackBox(mutant.model),
                            result.failing_trace,
                        )
                        if not execute_trace(
                            reference,
                            ModelBlackBox(mutant.model),
                            reduced.reduced_trace,
                        ).detected:
                            raise AssertionError("reducer returned a non-failing trace")
                        reduction = {
                            "trace": list(reduced.reduced_trace),
                            "length": len(reduced.reduced_trace),
                            "exact_length_match": len(reduced.reduced_trace)
                            == len(oracle.shortest_trace),
                            "unique_executions": reduced.unique_executions,
                            "cache_hits": reduced.cache_hits,
                            "failing_candidates": reduced.failing_candidates,
                        }
                    benchmark_rows.append(
                        {
                            "mutant_id": mutant.mutant_id,
                            "source_model_id": mutant.source_model_id,
                            "family": reference.family,
                            "state_count": reference.state_count,
                            "operator": mutant.operator,
                            "oracle_equivalent": oracle.equivalent,
                            "oracle_shortest_trace": _trace(oracle.shortest_trace),
                            "oracle_shortest_length": None
                            if oracle.shortest_trace is None
                            else len(oracle.shortest_trace),
                            "method": method_name,
                            "budget": budget,
                            "detected": result.detected,
                            "failing_trace": _trace(result.failing_trace),
                            "failing_trace_length": None
                            if result.failing_trace is None
                            else len(result.failing_trace),
                            "mismatch_index": result.mismatch_index,
                            "expected_output": result.expected_output,
                            "observed_output": result.observed_output,
                            "actions_executed": result.actions_executed,
                            "resets": result.resets,
                            "tests_executed": result.tests_executed,
                            "transition_coverage_count": len(result.transition_coverage),
                            "transition_pair_coverage_count": len(
                                result.transition_pair_coverage
                            ),
                            "reduction": reduction,
                        }
                    )

    detected_counts = Counter(
        (row["method"], row["budget"])
        for row in benchmark_rows
        if row["detected"] and not row["oracle_equivalent"]
    )
    exact_reduction_counts = Counter(
        (row["method"], row["budget"])
        for row in benchmark_rows
        if row["reduction"] is not None
        and row["reduction"]["exact_length_match"]
    )

    return {
        "schema_version": 1,
        "study": "Study 004 — Finite-State Conformance Counterexamples",
        "cycle": 3,
        "source_blobs": SOURCE_BLOBS,
        "fixture_file_sha256": FIXTURE_FILE_SHA256,
        "corpus_payload_sha256": corpus.payload_sha256,
        "models_payload_sha256": corpus.model_payload_sha256,
        "budgets": list(BUDGETS),
        "methods": [name for name, _ in METHODS],
        "counts": {
            "models": len(corpus.models),
            "mutants": len(corpus.mutants),
            "distinguishable": distinguishable,
            "equivalent": len(corpus.mutants) - distinguishable,
            "viability_required": viability_required,
            "benchmark_rows": len(benchmark_rows),
        },
        "viable": viable,
        "classification": classification,
        "benchmark_rows": benchmark_rows,
        "raw_detection_counts": [
            {"method": method, "budget": budget, "count": detected_counts[(method, budget)]}
            for method, _ in METHODS
            for budget in BUDGETS
        ],
        "raw_exact_reduction_counts": [
            {"method": method, "budget": budget, "count": exact_reduction_counts[(method, budget)]}
            for method, _ in METHODS
            for budget in BUDGETS
        ],
        "interpretation_status": "raw-only; H1-H3 dispositions deferred to Cycle 4",
    }


def build_files() -> tuple[bytes, bytes]:
    payload = generate_cycle3_payload()
    payload_bytes = canonical_bytes(payload)
    complete = dict(payload)
    complete["payload_sha256"] = sha256_hex(payload_bytes)
    json_bytes = canonical_bytes(complete)
    gzip_bytes = gzip.compress(json_bytes, compresslevel=9, mtime=0)
    manifest = {
        "schema_version": 1,
        "raw_path": str(OUTPUT_GZIP),
        "compression": "gzip",
        "json_bytes": len(json_bytes),
        "gzip_bytes": len(gzip_bytes),
        "payload_sha256": complete["payload_sha256"],
        "json_file_sha256": sha256_hex(json_bytes),
        "gzip_file_sha256": sha256_hex(gzip_bytes),
        "counts": payload["counts"],
        "viable": payload["viable"],
        "raw_detection_counts": payload["raw_detection_counts"],
        "raw_exact_reduction_counts": payload["raw_exact_reduction_counts"],
        "interpretation_status": payload["interpretation_status"],
    }
    return gzip_bytes, canonical_bytes(manifest)


def main() -> None:
    gzip_bytes, manifest_bytes = build_files()
    OUTPUT_GZIP.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_GZIP.write_bytes(gzip_bytes)
    OUTPUT_MANIFEST.write_bytes(manifest_bytes)
    print(OUTPUT_GZIP, len(gzip_bytes), sha256_hex(gzip_bytes))
    print(OUTPUT_MANIFEST, len(manifest_bytes), sha256_hex(manifest_bytes))


if __name__ == "__main__":
    main()
