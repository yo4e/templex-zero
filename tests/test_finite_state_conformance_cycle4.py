from __future__ import annotations

import json
from pathlib import Path

from experiments.analyze_finite_state_conformance_cycle4 import build_analysis

DATA = Path("research/studies/004-finite-state-conformance/data")


def test_complete_rerun_is_byte_identical_and_dispositions_are_frozen() -> None:
    result = build_analysis()
    assert result["reproduction"]["byte_identical"] is True
    assert result["reproduction"]["gzip_sha256"] == (
        "3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679"
    )
    assert result["hypotheses"]["H1"]["disposition"] == "unsupported"
    assert result["hypotheses"]["H2"]["disposition"] == "supported"
    assert result["hypotheses"]["H3"]["disposition"] == "unresolved"
    assert result["study_disposition"] == "partial result"


def test_checked_in_analysis_matches_deterministic_rebuild() -> None:
    checked = json.loads((DATA / "final_analysis_v1.json").read_text())
    assert checked == build_analysis()


def test_h3_sensitivity_preserves_ambiguity_and_no_invalid_outputs() -> None:
    h3 = build_analysis()["hypotheses"]["H3"]
    assert h3["invalid_reducer_outputs"] == 0
    assert h3["sensitivity"]["at_least_one_exact_output"]["percent"] == "100.000000"
    assert h3["sensitivity"]["all_detected_outputs_exact"]["percent"] == "68.750000"
    assert h3["sensitivity"]["earliest_detection_in_frozen_grid_exact"]["percent"] == "84.722222"
