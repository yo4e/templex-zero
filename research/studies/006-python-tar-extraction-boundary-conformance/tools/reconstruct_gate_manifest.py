from __future__ import annotations

import argparse
import base64
from pathlib import Path

from study006_common import sha256_bytes

EXPECTED_SHA256 = "8a4b86f70729da59e20266042d6b5d8b8ef6a8e482885341c4c7f094122073a9"
PART_NAMES = [
    "gate_manifest_v1.b64.part01",
    "gate_manifest_v1.b64.part02",
    "gate_manifest_v1.b64.part03",
    "gate_manifest_v1.b64.part04",
]


def reconstruct(parts_dir: Path) -> bytes:
    encoded = "".join((parts_dir / name).read_text(encoding="ascii").strip() for name in PART_NAMES)
    raw = base64.b64decode(encoded, validate=True)
    actual = sha256_bytes(raw)
    if actual != EXPECTED_SHA256:
        raise ValueError(f"gate manifest digest mismatch: {actual} != {EXPECTED_SHA256}")
    return raw


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parts-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = reconstruct(args.parts_dir)
    args.output.write_bytes(raw)
    print(f"{len(raw)} bytes {EXPECTED_SHA256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
