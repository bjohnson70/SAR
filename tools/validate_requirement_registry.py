"""Validate non-operational SAR Requirement Registry contract snapshots."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Protocol, runtime_checkable

import rfc8785
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = REPOSITORY_ROOT / "schemas/sar-requirement-registry.schema.json"
DEFAULT_FIXTURE = REPOSITORY_ROOT / "requirements/registry-fixtures/basic-registry.fixture.json"


@dataclass(frozen=True)
class Diagnostic:
    code: str
    path: str
    message: str


class DuplicateJsonKeyError(ValueError):
    """Raised when JSON contains duplicate object member names."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonKeyError(f"duplicate JSON object member: {key!r}")
        result[key] = value
    return result


def _reject_non_json_constant(value: str) -> None:
    raise ValueError(f"non-JSON numeric constant is not allowed: {value}")


def load_json_strict(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(
            stream,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_non_json_constant,
        )
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def _validator_for(schema: dict[str, Any]) -> Draft202012Validator:
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_errors(
    instance: Any,
    schema: dict[str, Any],
    path_prefix: str = "",
) -> list[Diagnostic]:
    errors = sorted(
        _validator_for(schema).iter_errors(instance),
        key=lambda error: (tuple(str(part) for part in error.absolute_path), error.message),
    )
    return [
        Diagnostic(
            code="REGISTRY_SCHEMA",
            path=".".join([path_prefix, *(str(part) for part in error.absolute_path)]).strip(".") or "$",
            message=error.message,
        )
        for error in errors
    ]


def _content_envelope_schema(registry_schema: dict[str, Any]) -> dict[str, Any]:
    return {
        "$schema": registry_schema["$schema"],
        "$defs": registry_schema["$defs"],
        "$ref": "#/$defs/contentEnvelope",
    }


def canonicalize_content(
    envelope: dict[str, Any],
    registry_schema: dict[str, Any],
) -> bytes:
    """Return RFC 8785 JCS bytes for the versioned immutable content envelope."""
    diagnostics = _schema_errors(envelope, _content_envelope_schema(registry_schema), "content_envelope")
    if diagnostics:
        raise ValueError("content envelope does not match the canonical profile: " + diagnostics[0].message)
    try:
        return rfc8785.dumps(envelope)
    except (rfc8785.CanonicalizationError, TypeError, ValueError) as error:
        raise ValueError(f"content envelope cannot be canonicalized under RFC 8785: {error}") from error


def content_digest(envelope: dict[str, Any], registry_schema: dict[str, Any]) -> str:
    """Return lowercase SHA-256 hex for the RFC 8785 canonical envelope bytes."""
    return hashlib.sha256(canonicalize_content(envelope, registry_schema)).hexdigest()


def _identity_key(record: dict[str, Any]) -> tuple[str, str]:
    return (record.get("issuer_namespace", ""), record.get("logical_id", ""))


def _version_key(record: dict[str, Any]) -> tuple[str, str, int]:
    return (*_identity_key(record), record.get("version_id", 0))


def _reference_identity_key(reference: dict[str, Any]) -> tuple[str, str]:
    return (reference.get("issuer_namespace", ""), reference.get("logical_id", ""))


def _reference_version_key(reference: dict[str, Any]) -> tuple[str, str, int]:
    return (*_reference_identity_key(reference), reference.get("version_id", 0))


def _append_error(
    diagnostics: list[Diagnostic],
    code: str,
    path: str,
    message: str,
) -> None:
    diagnostics.append(Diagnostic(code, path, message))


def validate_registry(
    snapshot: dict[str, Any],
    registry_schema: dict[str, Any],
) -> list[Diagnostic]:
    """Validate records, cross-record references, content digests, and event order.

    Validation establishes structural consistency only. It does not authenticate
    actors, authorize registration, verify source fidelity, approve a Requirement,
    determine applicability, or enable assessment execution.
    """
    diagnostics = _schema_errors(snapshot, registry_schema)
    if diagnostics:
        return diagnostics

    identities = snapshot["identities"]
    versions = snapshot["versions"]
    content_references = snapshot["content_references"]
    events = snapshot["lifecycle_events"]

    identity_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for index, record in enumerate(identities):
        key = _identity_key(record)
        if key in identity_by_key:
            _append_error(diagnostics, "REGISTRY_IDENTITY_COLLISION", f"identities[{index}]", f"duplicate logical identity {key!r}")
        else:
            identity_by_key[key] = record

    version_by_key: dict[tuple[str, str, int], dict[str, Any]] = {}
    versions_by_identity: dict[tuple[str, str], list[int]] = {}
    for index, record in enumerate(versions):
        key = _version_key(record)
        if key in version_by_key:
            _append_error(diagnostics, "REGISTRY_VERSION_COLLISION", f"versions[{index}]", f"duplicate immutable version {key!r}")
        else:
            version_by_key[key] = record
        versions_by_identity.setdefault(_identity_key(record), []).append(record.get("version_id", 0))

    for identity_key, version_ids in versions_by_identity.items():
        ordered = sorted(version_ids)
        if ordered != list(range(1, len(ordered) + 1)):
            _append_error(
                diagnostics,
                "REGISTRY_VERSION_SEQUENCE",
                "versions",
                f"versions for identity {identity_key!r} must be a contiguous sequence beginning at 1",
            )

    content_by_id: dict[str, dict[str, Any]] = {}
    for index, record in enumerate(content_references):
        content_id = record.get("content_reference_id", "")
        if content_id in content_by_id:
            _append_error(diagnostics, "REGISTRY_CONTENT_REFERENCE_COLLISION", f"content_references[{index}]", f"duplicate content reference {content_id!r}")
        else:
            content_by_id[content_id] = record

    referenced_content_ids: set[str] = set()
    for index, version in enumerate(versions):
        key = _version_key(version)
        identity_key = _identity_key(version)
        if identity_key not in identity_by_key:
            _append_error(diagnostics, "REGISTRY_IDENTITY_REFERENCE", f"versions[{index}]", f"version refers to missing identity {identity_key!r}")
        based_on = version.get("based_on_version")
        if based_on is not None:
            base_key = (*identity_key, based_on)
            if base_key not in version_by_key or based_on >= version.get("version_id", 0):
                _append_error(diagnostics, "REGISTRY_BASE_VERSION_REFERENCE", f"versions[{index}].based_on_version", "base version must exist under the same identity and precede this version")

        content_id = version.get("content_reference_id", "")
        referenced_content_ids.add(content_id)
        content_record = content_by_id.get(content_id)
        if content_record is None:
            _append_error(diagnostics, "REGISTRY_CONTENT_REFERENCE", f"versions[{index}].content_reference_id", f"missing content reference {content_id!r}")
            continue
        envelope_identity = content_record.get("content_envelope", {}).get("identity", {})
        if _reference_version_key(envelope_identity) != key:
            _append_error(diagnostics, "REGISTRY_CONTENT_IDENTITY", f"content_references.{content_id}.content_envelope.identity", "content envelope identity/version does not match the immutable version record")
        try:
            actual_digest = content_digest(content_record["content_envelope"], registry_schema)
        except (KeyError, ValueError) as error:
            _append_error(diagnostics, "REGISTRY_CONTENT_CANONICALIZATION", f"content_references.{content_id}.content_envelope", str(error))
        else:
            if actual_digest != content_record.get("digest_value"):
                _append_error(diagnostics, "REGISTRY_CONTENT_DIGEST", f"content_references.{content_id}.digest_value", "digest does not match the RFC 8785/SHA-256 canonical content envelope")

    for content_id in content_by_id.keys() - referenced_content_ids:
        _append_error(diagnostics, "REGISTRY_ORPHAN_CONTENT_REFERENCE", f"content_references.{content_id}", "content reference is not attached to an immutable version")

    event_by_id: dict[str, dict[str, Any]] = {}
    identity_registration_events: dict[tuple[str, str], list[dict[str, Any]]] = {}
    version_registration_events: dict[tuple[str, str, int], list[dict[str, Any]]] = {}
    terminal_events: dict[tuple[str, str, int], str] = {}
    lifecycle_state: dict[tuple[str, str, int], str] = {}
    supersession_edges: set[tuple[tuple[str, str, int], tuple[str, str, int]]] = set()

    for index, event in enumerate(events):
        event_id = event.get("event_id", "")
        if event_id in event_by_id:
            _append_error(diagnostics, "REGISTRY_EVENT_ID_COLLISION", f"lifecycle_events[{index}].event_id", f"duplicate event ID {event_id!r}")
        event_by_id[event_id] = event
        expected_sequence = index + 1
        if event.get("sequence") != expected_sequence:
            _append_error(diagnostics, "REGISTRY_EVENT_SEQUENCE", f"lifecycle_events[{index}].sequence", f"expected append-only sequence {expected_sequence}")
        if index > 0 and event.get("previous_event_id") != events[index - 1].get("event_id"):
            _append_error(diagnostics, "REGISTRY_EVENT_CHAIN", f"lifecycle_events[{index}].previous_event_id", "event must reference the immediately preceding event")

        identity_key = _reference_identity_key(event.get("target_identity", {}))
        event_type = event.get("event_type")
        target_version = event.get("target_version")
        version_key = _reference_version_key(target_version) if target_version else None

        if identity_key not in identity_by_key:
            _append_error(diagnostics, "REGISTRY_EVENT_IDENTITY_TARGET", f"lifecycle_events[{index}].target_identity", f"event targets missing identity {identity_key!r}")
        if target_version and version_key not in version_by_key:
            _append_error(diagnostics, "REGISTRY_EVENT_VERSION_TARGET", f"lifecycle_events[{index}].target_version", f"event targets missing version {version_key!r}")
        if target_version and _reference_identity_key(target_version) != identity_key:
            _append_error(diagnostics, "REGISTRY_EVENT_TARGET_MISMATCH", f"lifecycle_events[{index}].target_version", "event version target must belong to its identity target")

        if event_type == "IDENTITY_REGISTERED":
            identity_registration_events.setdefault(identity_key, []).append(event)
        elif event_type == "VERSION_REGISTERED":
            if version_key:
                version_registration_events.setdefault(version_key, []).append(event)
                lifecycle_state[version_key] = "REGISTERED"
        elif version_key and event_type == "VERSION_REVIEW_REQUIRED":
            if lifecycle_state.get(version_key) in {"WITHDRAWN", "SUPERSEDED"}:
                _append_error(diagnostics, "REGISTRY_EVENT_TRANSITION", f"lifecycle_events[{index}]", "terminal version cannot return to review-required")
            else:
                lifecycle_state[version_key] = "REVIEW_REQUIRED"
        elif version_key and event_type in {"VERSION_WITHDRAWN", "VERSION_SUPERSEDED"}:
            prior_terminal = terminal_events.get(version_key)
            if prior_terminal is not None:
                _append_error(diagnostics, "REGISTRY_EVENT_TRANSITION", f"lifecycle_events[{index}]", f"version already ended by {prior_terminal}")
            else:
                terminal_events[version_key] = event_type
                lifecycle_state[version_key] = event_type.removeprefix("VERSION_")
            if event_type == "VERSION_SUPERSEDED":
                for successor in event.get("successor_versions", []):
                    successor_key = _reference_version_key(successor)
                    if successor_key not in version_by_key:
                        _append_error(diagnostics, "REGISTRY_SUPERSESSION_REFERENCE", f"lifecycle_events[{index}].successor_versions", f"supersession target does not resolve: {successor_key!r}")
                    elif successor_key == version_key:
                        _append_error(diagnostics, "REGISTRY_SUPERSESSION_REFERENCE", f"lifecycle_events[{index}].successor_versions", "version cannot supersede itself")
                    else:
                        supersession_edges.add((version_key, successor_key))

    for key, identity in identity_by_key.items():
        matching = identity_registration_events.get(key, [])
        if len(matching) != 1 or (matching and matching[0].get("event_id") != identity.get("registration_event_id")):
            _append_error(diagnostics, "REGISTRY_IDENTITY_REGISTRATION_EVENT", f"identities.{key!r}.registration_event_id", "identity must have exactly one matching IDENTITY_REGISTERED event")
    for key, version in version_by_key.items():
        matching = version_registration_events.get(key, [])
        if len(matching) != 1 or (matching and matching[0].get("event_id") != version.get("registration_event_id")):
            _append_error(diagnostics, "REGISTRY_VERSION_REGISTRATION_EVENT", f"versions.{key!r}.registration_event_id", "version must have exactly one matching VERSION_REGISTERED event")
        if matching and identity_registration_events.get(_identity_key(version)):
            if matching[0].get("sequence", 0) <= identity_registration_events[_identity_key(version)][0].get("sequence", 0):
                _append_error(diagnostics, "REGISTRY_EVENT_ORDER", f"versions.{key!r}.registration_event_id", "version registration must follow identity registration")
        based_on = version.get("based_on_version")
        if matching and based_on is not None:
            base_registration = version_registration_events.get((*_identity_key(version), based_on), [])
            if base_registration and base_registration[0].get("sequence", 0) >= matching[0].get("sequence", 0):
                _append_error(diagnostics, "REGISTRY_EVENT_ORDER", f"versions.{key!r}.based_on_version", "base version must be registered before the version that references it")

    for index, event in enumerate(events):
        target_version = event.get("target_version")
        if not target_version or event.get("event_type") == "VERSION_REGISTERED":
            continue
        key = _reference_version_key(target_version)
        registrations = version_registration_events.get(key, [])
        if registrations and registrations[0].get("sequence", 0) >= event.get("sequence", 0):
            _append_error(diagnostics, "REGISTRY_EVENT_ORDER", f"lifecycle_events[{index}]", "version event must follow VERSION_REGISTERED")
        if event.get("event_type") == "APPROVAL_EVIDENCE_REFERENCED":
            version = version_by_key.get(key)
            content_record = content_by_id.get(version.get("content_reference_id", "")) if version else None
            if content_record is None or event.get("approval_content_digest") != content_record.get("digest_value"):
                _append_error(diagnostics, "REGISTRY_APPROVAL_DIGEST_MISMATCH", f"lifecycle_events[{index}].approval_content_digest", "approval evidence reference must bind the exact content digest of its target version")
        if event.get("event_type") == "VERSION_SUPERSEDED":
            for successor in event.get("successor_versions", []):
                successor_key = _reference_version_key(successor)
                registrations = version_registration_events.get(successor_key, [])
                if registrations and registrations[0].get("sequence", 0) >= event.get("sequence", 0):
                    _append_error(diagnostics, "REGISTRY_EVENT_ORDER", f"lifecycle_events[{index}].successor_versions", "supersession successor must be registered before the supersession event")

    if _has_cycle(supersession_edges):
        _append_error(diagnostics, "REGISTRY_SUPERSESSION_CYCLE", "lifecycle_events", "supersession relationships must be acyclic")

    return diagnostics


def _has_cycle(edges: set[tuple[tuple[str, str, int], tuple[str, str, int]]]) -> bool:
    graph: dict[tuple[str, str, int], set[tuple[str, str, int]]] = {}
    in_degree: dict[tuple[str, str, int], int] = {}
    for source, target in edges:
        graph.setdefault(source, set()).add(target)
        graph.setdefault(target, set())
        in_degree.setdefault(source, 0)
        in_degree[target] = in_degree.get(target, 0) + 1
    ready = deque(node for node in graph if in_degree.get(node, 0) == 0)
    visited_count = 0
    while ready:
        node = ready.popleft()
        visited_count += 1
        for target in graph[node]:
            in_degree[target] -= 1
            if in_degree[target] == 0:
                ready.append(target)
    return visited_count != len(graph)


def validate_append_only(
    previous_snapshot: dict[str, Any],
    candidate_snapshot: dict[str, Any],
    registry_schema: dict[str, Any],
) -> list[Diagnostic]:
    """Require immutable records to be retained and lifecycle events appended."""
    diagnostics = validate_registry(candidate_snapshot, registry_schema)
    for previous_error in validate_registry(previous_snapshot, registry_schema):
        _append_error(
            diagnostics,
            "REGISTRY_PREVIOUS_SNAPSHOT_INVALID",
            previous_error.path,
            previous_error.message,
        )
    for field, key_function in (
        ("identities", lambda item: _identity_key(item)),
        ("versions", lambda item: _version_key(item)),
        ("content_references", lambda item: item.get("content_reference_id", "")),
    ):
        previous_records = {key_function(item): item for item in previous_snapshot.get(field, [])}
        candidate_records = {key_function(item): item for item in candidate_snapshot.get(field, [])}
        for key, prior_record in previous_records.items():
            if key not in candidate_records:
                _append_error(diagnostics, "REGISTRY_HISTORY_REMOVED", field, f"previous immutable record removed: {key!r}")
            elif candidate_records[key] != prior_record:
                _append_error(diagnostics, "REGISTRY_IMMUTABLE_RECORD_CHANGED", field, f"previous immutable record changed: {key!r}")

    previous_events = previous_snapshot.get("lifecycle_events", [])
    candidate_events = candidate_snapshot.get("lifecycle_events", [])
    if len(candidate_events) < len(previous_events) or candidate_events[: len(previous_events)] != previous_events:
        _append_error(diagnostics, "REGISTRY_EVENT_HISTORY_CHANGED", "lifecycle_events", "existing lifecycle events must remain an unchanged prefix")
    return diagnostics


@runtime_checkable
class RequirementRegistryPort(Protocol):
    """Technology-neutral type contract only; this module provides no adapter.

    Implementations must authenticate/authorize the opaque context outside this
    structural contract; actor strings inside records are audit references only.
    Registration does not approve or enable a Requirement. This interface exposes
    no approval, applicability, parameter-assignment, or execution operation.
    """

    def read_snapshot(self, *, access_context: object) -> dict[str, Any]: ...

    def register_identity(
        self,
        record: dict[str, Any],
        *,
        authorization_context: object,
        idempotency_key: str,
    ) -> dict[str, Any]: ...

    def register_version(
        self,
        record: dict[str, Any],
        *,
        authorization_context: object,
        idempotency_key: str,
    ) -> dict[str, Any]: ...

    def append_lifecycle_event(
        self,
        event: dict[str, Any],
        *,
        authorization_context: object,
        idempotency_key: str,
    ) -> dict[str, Any]: ...

    def export_snapshot(self, *, access_context: object) -> dict[str, Any]: ...


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--registry", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--previous", type=Path, help="previous non-operational snapshot for append-only validation")
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    try:
        schema = load_json_strict(arguments.schema)
        snapshot = load_json_strict(arguments.registry)
        if arguments.previous:
            previous = load_json_strict(arguments.previous)
            diagnostics = validate_append_only(previous, snapshot, schema)
        else:
            diagnostics = validate_registry(snapshot, schema)
    except (OSError, ValueError, TypeError, json.JSONDecodeError, SchemaError) as error:
        print(json.dumps({"status": "REGISTRY_VALIDATION_INPUT_ERROR", "message": str(error)}, sort_keys=True))
        return 2

    print(json.dumps({"status": "REGISTRY_CONTRACT_VALID" if not diagnostics else "REGISTRY_CONTRACT_INVALID"}, sort_keys=True))
    for diagnostic in diagnostics:
        print(json.dumps(asdict(diagnostic), sort_keys=True))
    return 0 if not diagnostics else 1


if __name__ == "__main__":
    raise SystemExit(main())
