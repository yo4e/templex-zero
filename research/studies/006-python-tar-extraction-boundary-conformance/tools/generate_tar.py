from __future__ import annotations

import io
import tarfile
from pathlib import Path
from typing import Any

from study006_common import expand_study_root, payload_bytes, sha256_bytes

_MEMBER_TYPES = {
    "file": tarfile.REGTYPE,
    "dir": tarfile.DIRTYPE,
    "symlink": tarfile.SYMTYPE,
    "hardlink": tarfile.LNKTYPE,
    "fifo": tarfile.FIFOTYPE,
}


def build_archive_bytes(
    manifest: dict[str, Any], fixture: dict[str, Any], study_root: Path
) -> bytes:
    defaults = manifest["defaults"]
    output = io.BytesIO()
    with tarfile.open(fileobj=output, mode="w", format=tarfile.USTAR_FORMAT) as archive:
        for member_record in fixture["members"]:
            if len(member_record) != 10:
                raise ValueError(f"{fixture['id']}: member tuple must have 10 fields")
            (
                member_type,
                raw_name,
                raw_link_target,
                mode_octal,
                payload_id,
                _action,
                _exception_class,
                _normalized_name,
                _normalized_link_target,
                _normalized_mode,
            ) = member_record
            if member_type not in _MEMBER_TYPES:
                raise ValueError(f"{fixture['id']}: unsupported member type {member_type}")
            name = expand_study_root(raw_name, study_root)
            if not isinstance(name, str):
                raise ValueError(f"{fixture['id']}: member name must be text")
            link_target = expand_study_root(raw_link_target, study_root)
            payload = payload_bytes(manifest, payload_id)

            info = tarfile.TarInfo(name)
            info.type = _MEMBER_TYPES[member_type]
            info.mode = int(mode_octal, 8)
            info.uid = int(defaults["uid"])
            info.gid = int(defaults["gid"])
            info.uname = str(defaults["uname"])
            info.gname = str(defaults["gname"])
            info.mtime = int(defaults["mtime"])
            if link_target is not None:
                info.linkname = link_target

            if member_type == "file":
                info.size = len(payload)
                archive.addfile(info, io.BytesIO(payload))
            else:
                if payload_id is not None:
                    raise ValueError(
                        f"{fixture['id']}: non-file member unexpectedly has payload"
                    )
                info.size = 0
                archive.addfile(info)

    data = output.getvalue()
    if len(data) > 1024 * 1024:
        raise ValueError(f"{fixture['id']}: archive exceeds frozen 1 MiB cap")
    return data


def write_archive(
    manifest: dict[str, Any], fixture: dict[str, Any], study_root: Path, path: Path
) -> dict[str, Any]:
    data = build_archive_bytes(manifest, fixture, study_root)
    path.write_bytes(data)
    return {"bytes": len(data), "sha256": sha256_bytes(data)}
