import json
from collections import Counter
from hashlib import sha256
from pathlib import Path

from templex_zero.exact_first import grammar
from templex_zero.exact_first.manifest import (
    canonical_json,
    manifest_files,
    manifest_json,
    manifest_markdown,
    manifest_object,
    normalized_candidates,
    seeded_rank,
    selected_candidates,
)

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_DIR = (
    ROOT / "research" / "studies" / "002-exact-first-screening" / "manifest"
)


def test_each_frozen_cell_has_enough_distinct_static_candidates():
    for board_size, family in grammar.cell_order():
        candidates = normalized_candidates(board_size, family)
        serializations = [canonical_json(candidate) for candidate in candidates]
        assert len(candidates) >= grammar.CANDIDATES_PER_CELL
        assert len(serializations) == len(set(serializations))


def test_seeded_rank_matches_frozen_formula():
    candidate = normalized_candidates(3, grammar.FAMILY_ORDER[0])[0]
    payload = (
        f"{grammar.GENERATION_SEED}|{candidate['board_size']}|"
        f"{candidate['family']}|{canonical_json(candidate)}"
    )
    assert seeded_rank(candidate) == sha256(payload.encode("utf-8")).hexdigest()


def test_selected_manifest_has_exact_cell_distribution_and_unique_ids():
    selected = selected_candidates()
    assert len(selected) == 18
    assert [item.manifest_index for item in selected] == list(range(1, 19))
    assert len({item.candidate_id for item in selected}) == 18
    assert len({item.canonical_json for item in selected}) == 18
    counts = Counter((item.spec.board_size, item.spec.family) for item in selected)
    assert counts == {
        cell: grammar.CANDIDATES_PER_CELL for cell in grammar.cell_order()
    }


def test_every_selected_candidate_passes_frozen_static_boundaries():
    for item in selected_candidates():
        assert item.spec.board_size in (3, 4)
        assert len(item.spec.playable_cells) == item.spec.board_size**2
        assert item.spec.intended_symmetric is True
        assert item.spec.core_rule_words == item.word_count
        assert 0 < item.word_count <= 250
        assert len(item.rule_text.split()) == item.word_count


def test_manifest_generation_is_byte_identical_and_self_consistent():
    first_json = manifest_json()
    second_json = manifest_json()
    first_md = manifest_markdown()
    second_md = manifest_markdown()
    assert first_json.encode("utf-8") == second_json.encode("utf-8")
    assert first_md.encode("utf-8") == second_md.encode("utf-8")
    parsed = json.loads(first_json)
    compact_entries = json.dumps(
        parsed["entries"], ensure_ascii=False, separators=(",", ":")
    )
    assert parsed["entries_sha256"] == sha256(
        compact_entries.encode("utf-8")
    ).hexdigest()
    assert parsed["entry_count"] == len(parsed["entries"]) == 18
    assert len(parsed["cells"]) == 6
    assert all(len(cell["selected_ids"]) == 3 for cell in parsed["cells"])
    assert all(
        cell["raw_count"] >= cell["canonical_unique_count"]
        >= cell["statically_valid_count"]
        >= 3
        for cell in parsed["cells"]
    )


def test_committed_manifest_files_equal_regeneration():
    expected = manifest_files()
    actual_names = {path.name for path in MANIFEST_DIR.iterdir() if path.is_file()}
    assert actual_names == set(expected)
    for filename, content in expected.items():
        assert (MANIFEST_DIR / filename).read_text(encoding="utf-8") == content


def test_no_game_state_or_outcome_fields_appear_in_manifest():
    manifest = manifest_object()
    forbidden = {"winner", "outcome", "state_count", "play_trace", "win_rate"}
    for entry in manifest["entries"]:
        assert forbidden.isdisjoint(entry)
        assert forbidden.isdisjoint(entry["canonical"])
