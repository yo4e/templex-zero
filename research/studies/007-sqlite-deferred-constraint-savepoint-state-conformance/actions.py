from __future__ import annotations

from dataclasses import dataclass
import re

_NAMES = frozenset({"a", "b", "c", "d", "z"})
_CREATED_NAMES = frozenset({"a", "b", "c", "d"})
_RELATIONS = frozenset({"immediate", "deferred", "deferred_restrict"})
_SIMPLE = frozenset({"begin", "rollback", "commit"})
_PATTERN = re.compile(r"^(?P<kind>[a-z_]+)(?:\((?P<args>.*)\))?$")


@dataclass(frozen=True, slots=True)
class Action:
    kind: str
    name: str | None = None
    relation: str | None = None
    row_id: int | None = None
    parent_id: int | None = None

    def to_dict(self) -> dict[str, object]:
        return {
            "kind": self.kind,
            "name": self.name,
            "relation": self.relation,
            "row_id": self.row_id,
            "parent_id": self.parent_id,
        }

    def token(self) -> str:
        if self.kind in _SIMPLE:
            return self.kind
        if self.kind in {"savepoint", "release", "rollback_to"}:
            return f"{self.kind}({self.name})"
        if self.kind in {"insert_parent", "delete_parent"}:
            return f"{self.kind}({self.row_id})"
        if self.kind == "insert_child":
            return f"insert_child({self.relation},{self.row_id},{self.parent_id})"
        if self.kind == "delete_child":
            return f"delete_child({self.relation},{self.row_id})"
        raise ValueError(f"unsupported action kind: {self.kind}")


def parse_action(token: str) -> Action:
    match = _PATTERN.fullmatch(token.strip())
    if not match:
        raise ValueError(f"invalid action token: {token!r}")
    kind = match.group("kind")
    arg_text = match.group("args")
    args = [] if arg_text is None or arg_text == "" else [part.strip() for part in arg_text.split(",")]
    if kind in _SIMPLE and not args:
        return Action(kind=kind)
    if kind in {"savepoint", "release", "rollback_to"} and len(args) == 1:
        name = args[0]
        if name not in _NAMES or (kind == "savepoint" and name not in _CREATED_NAMES):
            raise ValueError(f"invalid savepoint name for {kind}: {name!r}")
        return Action(kind=kind, name=name)
    if kind in {"insert_parent", "delete_parent"} and len(args) == 1:
        return Action(kind=kind, row_id=_parse_int(args[0]))
    if kind == "insert_child" and len(args) == 3:
        relation = _parse_relation(args[0])
        return Action(kind=kind, relation=relation, row_id=_parse_int(args[1]), parent_id=_parse_int(args[2]))
    if kind == "delete_child" and len(args) == 2:
        relation = _parse_relation(args[0])
        return Action(kind=kind, relation=relation, row_id=_parse_int(args[1]))
    raise ValueError(f"invalid action arity: {token!r}")


def _parse_int(value: str) -> int:
    if not re.fullmatch(r"-?(0|[1-9][0-9]*)", value):
        raise ValueError(f"invalid integer: {value!r}")
    result = int(value)
    if not -(2**31) <= result <= 2**31 - 1:
        raise ValueError(f"integer outside frozen range: {value!r}")
    return result


def _parse_relation(value: str) -> str:
    if value not in _RELATIONS:
        raise ValueError(f"invalid relation: {value!r}")
    return value
