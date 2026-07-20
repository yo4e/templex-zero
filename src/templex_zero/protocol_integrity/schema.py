"""Declarative schema and canonical serialization for Study 003 traces.

This module intentionally contains no validator verdict logic. It only defines
frozen data shapes, structural validation, and deterministic serialization.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import hashlib
import json
from typing import Any, Iterable


class EventKind(str, Enum):
    BEGIN_CYCLE = "begin_cycle"
    END_CYCLE = "end_cycle"
    FREEZE_ARTIFACT = "freeze_artifact"
    SET_CAP = "set_cap"
    BEGIN_EXECUTION = "begin_execution"
    FINISH_EXECUTION = "finish_execution"
    OBSERVE = "observe"
    AUTHORIZE = "authorize"
    EXTERNAL_ACTION = "external_action"
    RECORD_DEFECT = "record_defect"
    INVALIDATE_EVIDENCE = "invalidate_evidence"
    APPLY_CORRECTION = "apply_correction"
    DISCLOSE_CORRECTION = "disclose_correction"
    ACCEPT_EVIDENCE = "accept_evidence"


class ExpectedVerdict(str, Enum):
    VALID = "valid"
    INVALID = "invalid"


class DependencyClass(str, Enum):
    D1 = "D1"
    D2 = "D2"
    D3 = "D3"
    D4 = "D4"
    D5 = "D5"
    D6 = "D6"


@dataclass(frozen=True)
class Event:
    index: int
    kind: EventKind
    subject: str
    scope: str | None = None
    token: str | None = None
    digest: str | None = None
    amount: int | None = None
    limit: int | None = None
    evidence_set: str | None = None
    defect: str | None = None
    correction: str | None = None
    reference: str | None = None

    def __post_init__(self) -> None:
        if self.index < 0:
            raise ValueError("event index must be non-negative")
        if not self.subject:
            raise ValueError("event subject must be non-empty")
        for name in ("amount", "limit"):
            value = getattr(self, name)
            if value is not None and value < 0:
                raise ValueError(f"{name} must be non-negative")

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "index": self.index,
            "kind": self.kind.value,
            "subject": self.subject,
        }
        for name in (
            "scope",
            "token",
            "digest",
            "amount",
            "limit",
            "evidence_set",
            "defect",
            "correction",
            "reference",
        ):
            value = getattr(self, name)
            if value is not None:
                result[name] = value
        return result


@dataclass(frozen=True)
class ArtifactObservationRule:
    observation: str
    artifact: str

    def to_dict(self) -> dict[str, str]:
        return {"observation": self.observation, "artifact": self.artifact}


@dataclass(frozen=True)
class EvidenceSetRule:
    evidence_set: str
    observations: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.observations:
            raise ValueError("evidence set must contain at least one observation")

    def to_dict(self) -> dict[str, Any]:
        return {"evidence_set": self.evidence_set, "observations": list(self.observations)}


@dataclass(frozen=True)
class CorrectionRule:
    defect: str
    affected_evidence_set: str
    replacement_evidence_set: str | None
    artifact: str
    require_invalidation: bool = True
    require_refreeze: bool = True
    require_reobservation: bool = True
    require_disclosure: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "defect": self.defect,
            "affected_evidence_set": self.affected_evidence_set,
            "replacement_evidence_set": self.replacement_evidence_set,
            "artifact": self.artifact,
            "require_invalidation": self.require_invalidation,
            "require_refreeze": self.require_refreeze,
            "require_reobservation": self.require_reobservation,
            "require_disclosure": self.require_disclosure,
        }


@dataclass(frozen=True)
class Contract:
    contract_id: str
    cycle_tokens: tuple[tuple[str, str], ...]
    artifact_observations: tuple[ArtifactObservationRule, ...] = ()
    evidence_sets: tuple[EvidenceSetRule, ...] = ()
    allowed_external_scopes: tuple[str, ...] = ()
    single_use_authorization: bool = True
    capped_executions: tuple[str, ...] = ()
    correction_rules: tuple[CorrectionRule, ...] = ()
    immutable_artifacts_after_observation: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.contract_id:
            raise ValueError("contract_id must be non-empty")
        if len({cycle for cycle, _ in self.cycle_tokens}) != len(self.cycle_tokens):
            raise ValueError("cycle ids must be unique")
        if len({token for _, token in self.cycle_tokens}) != len(self.cycle_tokens):
            raise ValueError("approval tokens must be unique")

    def to_dict(self) -> dict[str, Any]:
        return {
            "contract_id": self.contract_id,
            "cycle_tokens": [
                {"cycle": cycle, "approval_token": token}
                for cycle, token in self.cycle_tokens
            ],
            "artifact_observations": [rule.to_dict() for rule in self.artifact_observations],
            "evidence_sets": [rule.to_dict() for rule in self.evidence_sets],
            "allowed_external_scopes": list(self.allowed_external_scopes),
            "single_use_authorization": self.single_use_authorization,
            "capped_executions": list(self.capped_executions),
            "correction_rules": [rule.to_dict() for rule in self.correction_rules],
            "immutable_artifacts_after_observation": list(
                self.immutable_artifacts_after_observation
            ),
        }


@dataclass(frozen=True)
class ExpectedResult:
    verdict: ExpectedVerdict
    first_violation_index: int | None = None
    dependency_class: DependencyClass | None = None
    reason_code: str | None = None

    def __post_init__(self) -> None:
        if self.verdict is ExpectedVerdict.VALID:
            if any(
                value is not None
                for value in (
                    self.first_violation_index,
                    self.dependency_class,
                    self.reason_code,
                )
            ):
                raise ValueError("valid expectation cannot contain violation fields")
        else:
            if self.first_violation_index is None or self.dependency_class is None:
                raise ValueError("invalid expectation requires index and dependency class")
            if self.first_violation_index < 0:
                raise ValueError("first violation index must be non-negative")
            if not self.reason_code:
                raise ValueError("invalid expectation requires reason_code")

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {"verdict": self.verdict.value}
        if self.first_violation_index is not None:
            result["first_violation_index"] = self.first_violation_index
        if self.dependency_class is not None:
            result["dependency_class"] = self.dependency_class.value
        if self.reason_code is not None:
            result["reason_code"] = self.reason_code
        return result


@dataclass(frozen=True)
class TraceFixture:
    trace_id: str
    category: str
    contract: Contract
    events: tuple[Event, ...]
    expected: ExpectedResult
    mutation_operator: str | None = None
    source_trace_id: str | None = None

    def __post_init__(self) -> None:
        if not self.trace_id:
            raise ValueError("trace_id must be non-empty")
        if not self.events:
            raise ValueError("trace must contain at least one event")
        actual = tuple(event.index for event in self.events)
        expected = tuple(range(len(self.events)))
        if actual != expected:
            raise ValueError(f"event indices must be contiguous: {actual!r}")
        if len(self.events) > 40:
            raise ValueError("trace exceeds frozen 40-event limit")
        if self.expected.first_violation_index is not None:
            if self.expected.first_violation_index >= len(self.events):
                raise ValueError("first violation index outside trace")
        if (self.mutation_operator is None) != (self.source_trace_id is None):
            raise ValueError("mutants require both operator and source trace id")

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "trace_id": self.trace_id,
            "category": self.category,
            "contract": self.contract.to_dict(),
            "events": [event.to_dict() for event in self.events],
            "expected": self.expected.to_dict(),
        }
        if self.mutation_operator is not None:
            result["mutation_operator"] = self.mutation_operator
            result["source_trace_id"] = self.source_trace_id
        return result


@dataclass(frozen=True)
class SyntheticCorpus:
    schema_version: int
    proposal_path: str
    proposal_commit: str
    baseline_specification: dict[str, Any]
    traces: tuple[TraceFixture, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported schema version")
        if len(self.traces) != 36:
            raise ValueError("frozen corpus must contain exactly 36 traces")
        ids = [trace.trace_id for trace in self.traces]
        if len(ids) != len(set(ids)):
            raise ValueError("trace ids must be unique")
        total_events = sum(len(trace.events) for trace in self.traces)
        if total_events > 1_440:
            raise ValueError("synthetic corpus exceeds 36 x 40 event limit")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "proposal_path": self.proposal_path,
            "proposal_commit": self.proposal_commit,
            "baseline_specification": self.baseline_specification,
            "traces": [trace.to_dict() for trace in self.traces],
        }


def canonical_json_bytes(value: Any) -> bytes:
    if hasattr(value, "to_dict"):
        value = value.to_dict()
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode("utf-8")


def canonical_sha256(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def reindex(events: Iterable[Event]) -> tuple[Event, ...]:
    """Return structurally identical events with contiguous zero-based indices."""
    result: list[Event] = []
    for index, event in enumerate(events):
        payload = event.to_dict()
        payload["index"] = index
        payload["kind"] = EventKind(payload["kind"])
        result.append(Event(**payload))
    return tuple(result)
