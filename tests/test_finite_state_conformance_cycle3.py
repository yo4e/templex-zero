from __future__ import annotations

import base64
import gzip
import hashlib
import json
from pathlib import Path

from templex_zero.finite_state_conformance.corpus import generate_corpus
from templex_zero.finite_state_conformance.schema import canonical_bytes

DATA = Path("research/studies/004-finite-state-conformance/data")
MANIFEST = DATA / "cycle3_raw_manifest_v1.json"
PART_GLOB = "cycle3_raw_results_v1.json.gz.b64.part*"


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_transport() -> tuple[dict, dict, bytes, bytes]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    parts = sorted(DATA.glob(PART_GLOB))
    assert [part.name[-2:] for part in parts] == [f"{index:02d}" for index in range(8)]
    encoded = "".join(part.read_text(encoding="utf-8") for part in parts)
    assert len(encoded) == 39200
    gzip_bytes = base64.b64decode(encoded, validate=True)
    json_bytes = gzip.decompress(gzip_bytes)
    payload = json.loads(json_bytes)
    return manifest, payload, gzip_bytes, json_bytes


def test_cycle3_transport_hashes_and_payload_identity() -> None:
    manifest, payload, gzip_bytes, json_bytes = _load_transport()
    assert len(gzip_bytes) == manifest["gzip_bytes"] == 29400
    assert len(json_bytes) == manifest["json_bytes"] == 899730
    assert _sha256(gzip_bytes) == manifest["gzip_file_sha256"] == (
        "3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679"
    )
    assert _sha256(json_bytes) == manifest["json_file_sha256"] == (
        "a725f287b3d3a09b5d8e991e82daf9cb8f6a719c528a2e4047524cfd289bfc3c"
    )
    complete = dict(payload)
    recorded_payload_sha = complete.pop("payload_sha256")
    assert hashlib.sha256(canonical_bytes(complete)).hexdigest() == recorded_payload_sha
    assert recorded_payload_sha == manifest["payload_sha256"]


def test_cycle3_raw_inventory_and_grid_are_complete() -> None:
    manifest, payload, _, _ = _load_transport()
    corpus = generate_corpus()
    assert payload["corpus_payload_sha256"] == corpus.payload_sha256
    assert payload["counts"] == {
        "models": 24,
        "mutants": 144,
        "distinguishable": 144,
        "equivalent": 0,
        "viability_required": 116,
        "benchmark_rows": 1296,
    }
    assert payload["viable"] is True
    assert manifest["counts"] == payload["counts"]
    classification_ids = [row["mutant_id"] for row in payload["classification"]]
    corpus_ids = [record.mutant_id for record in corpus.mutants]
    assert classification_ids == corpus_ids
    assert all(not row["equivalent"] for row in payload["classification"])

    expected_grid = {
        (mutant_id, method, budget)
        for mutant_id in corpus_ids
        for method in payload["methods"]
        for budget in payload["budgets"]
    }
    actual_grid = {
        (row["mutant_id"], row["method"], row["budget"])
        for row in payload["benchmark_rows"]
    }
    assert actual_grid == expected_grid


def test_cycle3_bundle_remains_raw_without_hypothesis_dispositions() -> None:
    _, payload, _, _ = _load_transport()
    assert payload["interpretation_status"] == (
        "raw-only; H1-H3 dispositions deferred to Cycle 4"
    )
    text = json.dumps(payload, sort_keys=True)
    for forbidden in (
        '"h1_disposition"',
        '"h2_disposition"',
        '"h3_disposition"',
        '"final_conclusion"',
        '"study_disposition"',
    ):
        assert forbidden not in text
