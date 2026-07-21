from __future__ import annotations

import ast
import json
from pathlib import Path

from templex_zero.protocol_integrity.baseline import inspect_order
from templex_zero.protocol_integrity.oracle import inspect_trace
from templex_zero.protocol_integrity.synthetic_gate import canonical_bytes, load_bundle, run_gate
from templex_zero.protocol_integrity.validator import validate_trace

DATA = Path("research/studies/003-protocol-integrity/data/synthetic_corpus_v1")
SOURCES = [
    Path("src/templex_zero/protocol_integrity/validator.py"),
    Path("src/templex_zero/protocol_integrity/oracle.py"),
    Path("src/templex_zero/protocol_integrity/baseline.py"),
]


def by_id(trace_id: str):
    for contract, trace in load_bundle(DATA):
        if trace["trace_id"] == trace_id:
            return contract, trace
    raise AssertionError(trace_id)


def test_primary_and_oracle_match_all_frozen_expectations() -> None:
    for contract, trace in load_bundle(DATA):
        expected = trace["expected"]
        primary = validate_trace(contract, trace["events"]).to_dict()
        oracle = inspect_trace(contract, trace["events"]).to_dict()
        assert primary == oracle
        assert primary["verdict"] == expected["verdict"]
        if expected["verdict"] == "invalid":
            assert primary["first_violation_index"] == expected["first_violation_index"]
            assert primary["dependency_class"] == expected["dependency_class"]
            assert primary["reason_code"] == expected["reason_code"]


def test_all_mutants_are_rejected() -> None:
    mutants = 0
    for contract, trace in load_bundle(DATA):
        if trace.get("mutation_operator"):
            mutants += 1
            assert validate_trace(contract, trace["events"]).valid is False
    assert mutants == 20


def test_weak_baseline_accepts_named_stateful_invalid_traces() -> None:
    for trace_id in ("P2-I", "P3-I", "P5-I", "P6-I"):
        contract, trace = by_id(trace_id)
        assert inspect_order(trace["events"]).accepted is True
        assert validate_trace(contract, trace["events"]).valid is False


def test_weak_baseline_still_catches_simple_missing_order_dependencies() -> None:
    for trace_id in ("P1-I", "P4-I", "C1-M1", "C1-M2", "C1-M5"):
        _, trace = by_id(trace_id)
        assert inspect_order(trace["events"]).accepted is False


def test_oracle_does_not_import_primary_module() -> None:
    tree = ast.parse(SOURCES[1].read_text(encoding="utf-8"))
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    assert not any("validator" in name for name in imported)


def test_full_gate_passes_and_is_byte_deterministic() -> None:
    first = run_gate(DATA, SOURCES)
    second = run_gate(DATA, SOURCES)
    assert first["passed"] is True
    assert first["metrics"]["false_accept_count"] == 0
    assert first["metrics"]["false_reject_count"] == 0
    assert first["metrics"]["first_violation_accuracy"] == 1.0
    assert first["metrics"]["violation_class_accuracy"] == 1.0
    assert first["metrics"]["primary_oracle_agreement"] == 1.0
    assert first["metrics"]["mutants_rejected"] == 20
    assert first["metrics"]["named_baseline_false_accepts"] == ["P2-I", "P3-I", "P5-I", "P6-I"]
    assert canonical_bytes(first) == canonical_bytes(second)
    assert json.loads(canonical_bytes(first)) == first


def test_bundle_is_exactly_frozen_36_trace_input() -> None:
    loaded = load_bundle(DATA)
    assert len(loaded) == 36
    assert sum(len(trace["events"]) for _, trace in loaded) == 528


def test_validator_sources_contain_no_frozen_trace_ids() -> None:
    text = "\n".join(path.read_text(encoding="utf-8") for path in SOURCES)
    for token in ("P1-V", "P2-I", "P6-I", "C1-M1", "C4-M5", "S2-"):
        assert token not in text
