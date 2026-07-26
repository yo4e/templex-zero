from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

STUDY_ROOT_TOKEN = "${STUDY_ROOT}"


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"expected object at {path}")
    return value


def payload_bytes(manifest: dict[str, Any], payload_id: str | None) -> bytes:
    if payload_id is None:
        return b""
    try:
        record = manifest["payloads"][payload_id]
    except KeyError as exc:
        raise ValueError(f"unknown payload id {payload_id!r}") from exc
    data = record["utf8"].encode("utf-8")
    actual = sha256_bytes(data)
    if actual != record["sha256"]:
        raise ValueError(
            f"payload {payload_id} digest mismatch: {actual} != {record['sha256']}"
        )
    return data


def expand_study_root(value: str | None, study_root: Path) -> str | None:
    if value is None:
        return None
    return value.replace(STUDY_ROOT_TOKEN, str(study_root))


def index_fixtures(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    fixtures = manifest.get("fixtures")
    if not isinstance(fixtures, list):
        raise ValueError("manifest fixtures must be a list")
    indexed: dict[str, dict[str, Any]] = {}
    for fixture in fixtures:
        fixture_id = fixture.get("id")
        if not isinstance(fixture_id, str) or fixture_id in indexed:
            raise ValueError(f"invalid or duplicate fixture id: {fixture_id!r}")
        indexed[fixture_id] = fixture
    return indexed
