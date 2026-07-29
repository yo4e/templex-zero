#!/usr/bin/env python3
"""Structure-only validator for the frozen Study 007 TSV manifest.

This module deliberately does not import sqlite3, execute SQL, or calculate
expected relational outcomes. It validates only pre-execution structure,
resource caps, action grammar, expected-error labels, and stack shape.
"""
from __future__ import annotations
import csv, json, re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest.tsv"
FAMILIES = {"A", "B", "C", "D", "E", "F"}
ALLOWED_RELATIONS = {"immediate", "deferred", "deferred_restrict"}
ALLOWED_EXPECT = {"ok", "savepoint_not_found", "nested_begin", "foreign_key"}
TOKEN = re.compile(r"^(?P<kind>[a-z_]+)(?:\((?P<args>[^)]*)\))?(?:!(?P<expect>[a-z_]+))?$")


def fail(message: str) -> None:
    raise AssertionError(message)


def parse_action(token: str, seq_id: str, index: int) -> dict:
    match = TOKEN.fullmatch(token)
    if not match:
        fail(f"{seq_id}:{index}: malformed token {token!r}")
    kind = match.group("kind")
    raw = match.group("args")
    args = [] if raw is None or raw == "" else raw.split(",")
    expect = match.group("expect") or "ok"
    if expect not in ALLOWED_EXPECT:
        fail(f"{seq_id}:{index}: unknown expectation {expect}")
    if kind in {"begin", "rollback", "commit"}:
        if args:
            fail(f"{seq_id}:{index}: unexpected args")
        parsed = {}
    elif kind in {"savepoint", "release", "rollback_to"}:
        if len(args) != 1 or args[0] not in {"a", "b", "c", "d", "z"}:
            fail(f"{seq_id}:{index}: invalid name")
        parsed = {"name": args[0]}
    elif kind in {"insert_parent", "delete_parent"}:
        if len(args) != 1 or not args[0].isdigit():
            fail(f"{seq_id}:{index}: invalid parent id")
        parsed = {"id": int(args[0])}
    elif kind == "insert_child":
        if len(args) != 3 or args[0] not in ALLOWED_RELATIONS or not args[1].isdigit() or not args[2].isdigit():
            fail(f"{seq_id}:{index}: invalid insert_child")
        parsed = {"relation": args[0], "id": int(args[1]), "parent_id": int(args[2])}
    elif kind == "delete_child":
        if len(args) != 2 or args[0] not in ALLOWED_RELATIONS or not args[1].isdigit():
            fail(f"{seq_id}:{index}: invalid delete_child")
        parsed = {"relation": args[0], "id": int(args[1])}
    else:
        fail(f"{seq_id}:{index}: unknown action {kind}")
    return {"kind": kind, "args": parsed, "expect": expect}


def validate_stack_shape(seq_id: str, actions: list[dict]) -> int:
    stack: list[str] = []
    maximum = 0
    for index, action in enumerate(actions, start=1):
        kind, args, expect = action["kind"], action["args"], action["expect"]
        if kind == "begin":
            if expect == "nested_begin":
                if not stack:
                    fail(f"{seq_id}:{index}: nested_begin without active stack")
            elif expect == "ok":
                if stack:
                    fail(f"{seq_id}:{index}: successful BEGIN with active stack")
                stack.append("__begin__")
        elif kind == "savepoint" and expect == "ok":
            stack.append(args["name"])
        elif kind in {"release", "rollback_to"}:
            name = args["name"]
            positions = [i for i, item in enumerate(stack) if item == name]
            if expect == "savepoint_not_found":
                if positions:
                    fail(f"{seq_id}:{index}: expected missing name exists")
            elif expect == "foreign_key":
                if kind != "release" or not positions:
                    fail(f"{seq_id}:{index}: invalid failed release shape")
            elif expect == "ok":
                if not positions:
                    fail(f"{seq_id}:{index}: successful {kind} missing name")
                pos = positions[-1]
                stack = stack[:pos] if kind == "release" else stack[:pos + 1]
        elif kind in {"commit", "rollback"}:
            if not stack:
                fail(f"{seq_id}:{index}: boundary without active transaction")
            if expect == "ok":
                stack.clear()
            elif kind != "commit" or expect != "foreign_key":
                fail(f"{seq_id}:{index}: invalid boundary expectation")
        maximum = max(maximum, sum(item != "__begin__" for item in stack))
    if stack:
        fail(f"{seq_id}: active stack remains {stack}")
    return maximum


def main() -> None:
    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if len(rows) != 72:
        fail(f"exact denominator {len(rows)} != 72")
    ids = [row["id"] for row in rows]
    if len(ids) != len(set(ids)):
        fail("duplicate sequence IDs")
    family_counts = Counter(row["family"] for row in rows)
    if family_counts != Counter({f: 12 for f in FAMILIES}):
        fail(f"family counts {family_counts}")
    total_actions = 0
    max_actions = 0
    max_depth = 0
    error_counts = Counter()
    for row in rows:
        seq_id = row["id"]
        if row["family"] not in FAMILIES or seq_id[0] != row["family"]:
            fail(f"{seq_id}: family mismatch")
        hypotheses = row["hypotheses"].split(",")
        if not hypotheses or any(h not in {"H1", "H2", "H3"} for h in hypotheses):
            fail(f"{seq_id}: hypotheses")
        tokens = row["actions"].split(";")
        if not (1 <= len(tokens) <= 24):
            fail(f"{seq_id}: action cap")
        actions = [parse_action(token, seq_id, i) for i, token in enumerate(tokens, start=1)]
        created_names = {a["args"].get("name") for a in actions if a["kind"] == "savepoint"}
        if len(created_names) > 4:
            fail(f"{seq_id}: distinct name cap")
        inserts = sum(a["kind"] in {"insert_parent", "insert_child"} for a in actions)
        if inserts > 32:
            fail(f"{seq_id}: insert cap")
        max_depth = max(max_depth, validate_stack_shape(seq_id, actions))
        total_actions += len(actions)
        max_actions = max(max_actions, len(actions))
        error_counts.update(a["expect"] for a in actions)
    if max_depth > 6:
        fail(f"depth cap {max_depth}")
    print(json.dumps({
        "status": "pass",
        "sequence_count": 72,
        "family_counts": dict(sorted(family_counts.items())),
        "total_actions": total_actions,
        "maximum_actions_per_sequence": max_actions,
        "maximum_savepoint_depth": max_depth,
        "expectation_counts": dict(sorted(error_counts.items())),
        "sqlite_imported": False,
        "sql_executed": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
