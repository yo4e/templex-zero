from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
from pathlib import Path

PART_NAMES = [f"reproduction_result_v1.json.gz.b64.part{i:02d}" for i in range(1, 17)]
EXPECTED_PART_BLOBS = ['e46dcdbe4eba03eb26c7c707dd9219b3df09f48d', 'ab87d97d4e4d3fd1554230253d54b6a3105f2ab1', '675677ac13688de64e2c1e753caded4563d0b2e7', '5209aac9b7ed4b074573d6f1bc033e548d150fba', '4c3552b88269f5ebd5ee3e772676262008d83662', 'be86081bb4cd65cd8da3247a2f95b22aa172fdc3', '1282fd0b089b5ff4ef081bbd30fee21d4b31129f', 'e9a8a547d76a6bc1f02298ec3ea30a84f395b718', '72a2d4bc73e0971cfeadacf69d0914839ea85771', '45cbd51b94b338db730a66485cf253b39f93ac2a', 'ac2a166588ddfcdc4d3fdf37afecc860c6734918', '173e3e5792137cb7411fdf6a38cc806b8a4cb68a', 'ad092ae4b8b59739cbf348a93f9dac8828a90317', '529beadb76aeabf6b4e927b245f5342ab38cac7f', '950309a35ba38c11e1a976cfbf9537abf7496e05', '8edc9ef6aecc10a8c755d3d9a46026d25231c195']
EXPECTED_GZIP_BYTES = 6906
EXPECTED_GZIP_SHA256 = "10f5480625aa23645a75e19538a0f5d33a0d6009d82459dbfb46f3c8337ea0ff"
EXPECTED_JSON_BYTES = 97289
EXPECTED_JSON_SHA256 = "c43b1e6a4f5535e471ed04f9fcdca751e1a270a18c8710feafd677f53d6b3278"


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reconstruct(parts_dir: Path) -> bytes:
    encoded = []
    for name, expected_blob in zip(PART_NAMES, EXPECTED_PART_BLOBS, strict=True):
        data = (parts_dir / name).read_bytes()
        actual_blob = git_blob_sha(data)
        if actual_blob != expected_blob:
            raise ValueError(f"Git Blob mismatch for {name}: {actual_blob} != {expected_blob}")
        encoded.append(data.decode("ascii").strip())
    gzip_bytes = base64.b64decode("".join(encoded), validate=True)
    if len(gzip_bytes) != EXPECTED_GZIP_BYTES or sha256(gzip_bytes) != EXPECTED_GZIP_SHA256:
        raise ValueError("reconstructed gzip identity mismatch")
    json_bytes = gzip.decompress(gzip_bytes)
    if len(json_bytes) != EXPECTED_JSON_BYTES or sha256(json_bytes) != EXPECTED_JSON_SHA256:
        raise ValueError("reconstructed JSON identity mismatch")
    return json_bytes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parts-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = reconstruct(args.parts_dir)
    args.output.write_bytes(result)
    print({"bytes": len(result), "sha256": sha256(result)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
