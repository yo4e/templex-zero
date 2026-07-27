from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
from pathlib import Path

PART_NAMES = [
    "formal_result_v1.json.gz.b64.part01",
    "formal_result_v1.json.gz.b64.part02",
    "formal_result_v1.json.gz.b64.part03",
    "formal_result_v1.json.gz.b64.part04",
]
EXPECTED_PART_BLOBS = [
    "726aae92af31f17d1f5d8e9788e4d51cbc281eb9",
    "156dc8501a48866d3331218cb6dfb07fd15cc06d",
    "d3028634baa6aab5200e10629cac8c6f9430ac54",
    "283876c66aea3ded08306c887a06a33a81e675a0",
]
EXPECTED_GZIP_BYTES = 6905
EXPECTED_GZIP_SHA256 = "23f00a304e5d76797ead9278f6372bc6145f4c5df62498fc8b885517c523bb6c"
EXPECTED_JSON_BYTES = 97289
EXPECTED_JSON_SHA256 = "07cac72ab1d29394ef82b71280b12b78370fff94e84f428fb3617221c61faabd"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def reconstruct(parts_dir: Path) -> tuple[bytes, bytes]:
    encoded_parts: list[bytes] = []
    for name, expected_blob in zip(PART_NAMES, EXPECTED_PART_BLOBS, strict=True):
        data = (parts_dir / name).read_bytes()
        actual_blob = git_blob_sha1(data)
        if actual_blob != expected_blob:
            raise ValueError(f"transport blob drift for {name}: {actual_blob}")
        encoded_parts.append(data.strip())
    compressed = base64.b64decode(b"".join(encoded_parts), validate=True)
    if len(compressed) != EXPECTED_GZIP_BYTES or sha256(compressed) != EXPECTED_GZIP_SHA256:
        raise ValueError("compressed result identity mismatch")
    raw = gzip.decompress(compressed)
    if len(raw) != EXPECTED_JSON_BYTES or sha256(raw) != EXPECTED_JSON_SHA256:
        raise ValueError("JSON result identity mismatch")
    return compressed, raw


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parts-dir", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-gzip", type=Path)
    args = parser.parse_args()
    compressed, raw = reconstruct(args.parts_dir)
    args.output_json.write_bytes(raw)
    if args.output_gzip is not None:
        args.output_gzip.write_bytes(compressed)
    print(f"json_bytes={len(raw)} json_sha256={sha256(raw)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
