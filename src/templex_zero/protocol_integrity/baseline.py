"""Deliberately weak event-kind ordering baseline."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class BaselineDecision:
    accepted: bool
    first_violation_index: int | None = None
    reason_code: str | None = None

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {"verdict": "valid" if self.accepted else "invalid"}
        if not self.accepted:
            data["first_violation_index"] = self.first_violation_index
            data["reason_code"] = self.reason_code
        return data


_REQUIRED_EARLIER_KINDS: dict[str, tuple[str, ...]] = {
    "end_cycle": ("begin_cycle",),
    "observe": ("freeze_artifact",),
    "external_action": ("authorize",),
    "begin_execution": ("set_cap",),
    "finish_execution": ("begin_execution",),
    "invalidate_evidence": ("record_defect",),
    "apply_correction": ("record_defect",),
    "disclose_correction": ("apply_correction",),
    "accept_evidence": ("observe",),
}


def inspect_order(events: list[dict[str, Any]]) -> BaselineDecision:
    """Check only whether prerequisite event kinds appeared somewhere earlier."""
    seen: set[str] = set()
    for position, event in enumerate(events):
        kind = str(event.get("kind"))
        required_kinds = list(_REQUIRED_EARLIER_KINDS.get(kind, ()))
        if kind == "accept_evidence" and "apply_correction" in seen:
            required_kinds.append("disclose_correction")
        for required in required_kinds:
            if required not in seen:
                return BaselineDecision(
                    False,
                    int(event.get("index", position)),
                    f"missing-earlier-{required}",
                )
        seen.add(kind)
    return BaselineDecision(True)
