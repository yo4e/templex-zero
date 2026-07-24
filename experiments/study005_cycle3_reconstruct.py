"""Reconstruct the exact Study 005 Cycle 3 canonical result without rerunning zoneinfo."""
from __future__ import annotations

import argparse
import json
import lzma
from pathlib import Path

from templex_zero.tzif_reader import read_tzif
from templex_zero.zoneinfo_harness import (
    canonical_json,
    gap_wall_samples,
    repeated_wall_samples,
    retained_positions,
    sha256,
    utc_witnesses,
)

H1_COLUMNS = ["zone_index", "transition_timestamp", "witness_code", "utc_timestamp", "expected_offset", "observed_offset", "expected_isdst", "observed_dst_seconds", "observed_isdst", "expected_abbreviation", "observed_abbreviation", "expected_wall_epoch", "observed_wall_epoch", "observed_fold", "mismatch_mask"]
H2_COLUMNS = ["zone_index", "transition_timestamp", "sample_code", "wall_epoch", "pre_offset", "post_offset", "earlier_utc", "later_utc", "earlier_observed_wall", "later_observed_wall", "earlier_fold", "later_fold", "fold0_roundtrip_utc", "fold1_roundtrip_utc", "mismatch_mask"]
H3_COLUMNS = ["zone_index", "transition_timestamp", "sample_code", "wall_epoch", "expected_valid", "observed_valid", "fold0_attempt", "fold1_attempt", "mismatch_mask"]


def reconstruct(tzdir: Path, manifest_path: Path, package_path: Path) -> bytes:
    manifest = json.loads(manifest_path.read_bytes())
    package = json.loads(lzma.decompress(package_path.read_bytes()))
    h1_nonzero = dict(package["h1_nonzero"])
    h2_nonzero = dict(package["h2_nonzero"])
    h3_nonzero = dict(package["h3_nonzero"])
    h1 = []
    h2 = []
    h3 = []
    i1 = i2 = i3 = 0

    for zi, row in enumerate(manifest["zones"]):
        name = row[0]
        parsed = read_tzif(tzdir / name)
        retained = retained_positions(parsed)
        for retained_index, position in enumerate(retained):
            transition = parsed.transitions[position]
            pre_index = 0 if position == 0 else parsed.transitions[position - 1].type_index
            post_index = transition.type_index
            pre = parsed.local_time_types[pre_index]
            post = parsed.local_time_types[post_index]
            delta = post.utoff - pre.utoff

            for code, utc_timestamp in utc_witnesses(parsed, position, retained, retained_index):
                if i1 in h1_nonzero:
                    record = h1_nonzero[i1]
                else:
                    expected = parsed.type_at(utc_timestamp)
                    dst_seconds, fold = package["h1_extras"][i1]
                    wall = utc_timestamp + expected.utoff
                    record = [zi, transition.timestamp, code, utc_timestamp, expected.utoff, expected.utoff, int(expected.isdst), dst_seconds, int(bool(dst_seconds)), expected.abbreviation, expected.abbreviation, wall, wall, fold, 0]
                h1.append(record)
                i1 += 1

            if delta < 0:
                for code, wall in repeated_wall_samples(transition.timestamp, pre.utoff, post.utoff):
                    if i2 in h2_nonzero:
                        record = h2_nonzero[i2]
                    else:
                        earlier = wall - pre.utoff
                        later = wall - post.utoff
                        record = [zi, transition.timestamp, code, wall, pre.utoff, post.utoff, earlier, later, wall, wall, 0, 1, earlier, later, 0]
                    h2.append(record)
                    i2 += 1
            elif delta > 0:
                for code, wall, expected_valid in gap_wall_samples(transition.timestamp, pre.utoff, post.utoff):
                    if i3 in h3_nonzero:
                        record = h3_nonzero[i3]
                    else:
                        attempts = package["h3_attempts"][i3]
                        record = [zi, transition.timestamp, code, wall, expected_valid, expected_valid, attempts[0], attempts[1], 0]
                    h3.append(record)
                    i3 += 1

    result = {
        "environment": package["environment"],
        "h1": {"columns": H1_COLUMNS, "rows": h1},
        "h2": {"columns": H2_COLUMNS, "rows": h2},
        "h3": {"attempt_columns": ["fold", "utc_timestamp", "roundtrip_wall_epoch", "roundtrip_fold", "valid"], "columns": H3_COLUMNS, "rows": h3},
        "manifest": package["manifest"],
        "reference_context": package["reference_context"],
        "schema": "templex-zero.study005.zoneinfo-formal-results.v1",
        "zones": package["zones"],
    }
    raw = canonical_json(result)
    if len(raw) != package["result_bytes"] or sha256(raw) != package["result_sha256"]:
        raise RuntimeError("reconstructed formal result identity mismatch")
    return raw


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tzdir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_bytes(reconstruct(args.tzdir, args.manifest, args.package))


if __name__ == "__main__":
    main()
