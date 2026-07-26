from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "studies"
    / "006-python-tar-extraction-boundary-conformance"
    / "tools"
)
sys.path.insert(0, str(TOOLS))

from filesystem_oracle import destination_nodes, snapshot
from generate_tar import build_archive_bytes
from study006_common import sha256_bytes


class Study006GateToolTests(unittest.TestCase):
    def test_generator_is_deterministic_for_fixed_root(self):
        manifest = {
            "defaults": {"uid": 1, "gid": 2, "uname": "u", "gname": "g", "mtime": 0},
            "payloads": {"p": {"utf8": "x\n", "sha256": sha256_bytes(b"x\n")}},
        }
        fixture = {
            "id": "T",
            "members": [["file", "x", None, "0644", "p", "A", None, "x", None, "0644"]],
        }
        root = Path("/tmp/fixed-study-root")
        self.assertEqual(
            build_archive_bytes(manifest, fixture, root),
            build_archive_bytes(manifest, fixture, root),
        )

    def test_oracle_assigns_hardlink_groups_and_does_not_follow_symlink(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "destination").mkdir()
            target = root / "destination" / "target"
            target.write_bytes(b"x")
            os.link(target, root / "destination" / "copy")
            os.symlink("target", root / "destination" / "link")
            records = destination_nodes(snapshot(root))
            by_path = {record["path"]: record for record in records}
            self.assertEqual(by_path["target"]["hardlink_group"], "h1")
            self.assertEqual(by_path["copy"]["hardlink_group"], "h1")
            self.assertEqual(by_path["link"]["type"], "symlink")
            self.assertEqual(by_path["link"]["symlink_target"], "target")
            self.assertEqual(by_path["link"]["mode_octal"], "0777")

    def test_snapshot_excludes_timestamps_and_inode_numbers(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "destination").mkdir()
            (root / "destination" / "x").write_text("x", encoding="utf-8")
            record = destination_nodes(snapshot(root))[0]
            forbidden = {"atime", "mtime", "ctime", "inode", "dev", "st_ino", "st_dev"}
            self.assertFalse(forbidden.intersection(record))


if __name__ == "__main__":
    unittest.main()
