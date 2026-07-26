from __future__ import annotations

import argparse
import base64
import gzip
from pathlib import Path

from study006_common import sha256_bytes

PART_NAMES = [
    "gate_result_v1.json.gz.b64.part01",
    "gate_result_v1.json.gz.b64.part02",
    "gate_result_v1.json.gz.b64.part03",
    "gate_result_v1.json.gz.b64.part04",
]
EXPECTED_GZIP_BYTES = 2649
EXPECTED_GZIP_SHA256 = "5c69e291ee91a7c16eab4cf51fc793f7d82696dd3647e3b39521d299b7a528bc"
EXPECTED_JSON_BYTES = 40633
EXPECTED_JSON_SHA256 = "cae28021659b53fb2ea946f0d76cf64b33e85c8480974848f7f52b9a7834b2f2"


def reconstruct(parts_dir: Path) -> bytes:
    encoded = "".join((parts_dir / name).read_text(encoding="ascii").strip() for name in PART_NAMES)
    compressed = base64.b64decode(encoded, validate=True)
    if len(compressed) != EXPECTED_GZIP_BYTES:
        raise ValueError(f"gzip byte count mismatch: {len(compressed)}")
    if sha256_bytes(compressed) != EXPECTED_GZIP_SHA256:
        raise ValueError("gzip SHA-256 mismatch")
    raw = gzip.decompress(compressed)
    if len(raw) != EXPECTED_JSON_BYTES:
        raise ValueError(f"JSON byte count mismatch: {len(raw)}")
    if sha256_bytes(raw) != EXPECTED_JSON_SHA256:
        raise ValueError("JSON SHA-256 mismatch")
    return raw


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parts-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = reconstruct(args.parts_dir)
    args.output.write_bytes(raw)
    print(f"{len(raw)} bytes {EXPECTED_JSON_SHA256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
