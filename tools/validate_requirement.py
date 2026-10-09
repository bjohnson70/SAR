"""Validate provisional SAR Requirement governance records without promoting them."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REQUIREMENT = REPOSITORY_ROOT / "requirements/examples/si-12-3.proposed.yaml"
DEFAULT_SCHEMA = REPOSITORY_ROOT / "schemas/sar-requirement-record.schema.json"
DEFAULT_SOURCE_MANIFEST = REPOSITORY_ROOT / "sources/nist-sp800-53-rev5.oscal-source.yaml"
DEFAULT_CANDIDATE_SET = REPOSITORY_ROOT / "sources/nist-sp800-53-rev5.si-12.candidate-boundaries.yaml"
DEFAULT_SOURCE_SLICE = REPOSITORY_ROOT / "sources/nist-sp800-53-rev5.ac-2-si-12.slice.yaml"


@dataclass(frozen=True)
class Diagnostic:
    severity: str
    code: str
    path: str
    message: str


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = yaml.safe_load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return value


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def _schema_diagnostics(record: dict[str, Any], schema: dict[str, Any]) -> list[Diagnostic]:
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(record), key=lambda error: list(error.absolute_path))
    return [
        Diagnostic(
            severity="ERROR",
            code="REQ-SCHEMA",
            path=".".join(str(part) for part in error.absolute_path) or "$",
            message=error.message,
        )
        for error in errors
    ]


def _find_candidate(candidate_set: dict[str, Any], candidate_id: str) -> dict[str, Any] | None:
    candidates = candidate_set.get("candidate_boundary_set", {}).get("candidates", [])
    return next(
        (candidate for candidate in candidates if candidate.get("candidate_boundary_id") == candidate_id),
        None,
    )


def _find_source_object(source_slice: dict[str, Any], source_id: str) -> dict[str, Any] | None:
    return next(
        (item for item in source_slice.get("source_objects", []) if item.get("source_control_id") == source_id),
        None,
    )


def _catalog_artifact(source_manifest: dict[str, Any]) -> dict[str, Any] | None:
    return next(
        (item for item in source_manifest.get("artifacts", []) if item.get("artifact_type") == "catalog"),
        None,
    )


def validate_record(
    record: dict[str, Any],
    requirement_schema: dict[str, Any],
    source_manifest: dict[str, Any],
    candidate_set: dict[str, Any],
    source_slice: dict[str, Any],
) -> list[Diagnostic]:
    """Check schema and mechanical provenance links; never make a human decision."""
    diagnostics = _schema_diagnostics(record, requirement_schema)
    if diagnostics:
        return diagnostics
    source_provenance = record.get("source_provenance", {})
    boundary_ref = source_provenance.get("candidate_boundary", {})
    candidate_id = boundary_ref.get("candidate_boundary_id")
    candidate = _find_candidate(candidate_set, candidate_id) if candidate_id else None

    def error(code: str, path: str, message: str) -> None:
        diagnostics.append(Diagnostic("ERROR", code, path, message))

    if not candidate_id:
        error("REQ-CANDIDATE-REF", "source_provenance.candidate_boundary", "candidate boundary reference is missing")
    elif candidate is None:
        error("REQ-CANDIDATE-REF", "source_provenance.candidate_boundary.candidate_boundary_id", f"candidate {candidate_id!r} does not exist in the supplied candidate set")
    else:
        if candidate.get("validation_status") != "VALIDATED":
            error("REQ-CANDIDATE-STATUS", "source_provenance.candidate_boundary.validation_status", "the referenced candidate boundary is not VALIDATED")

        source_id = source_provenance.get("source_object_id")
        part_ids = source_provenance.get("normative_part_ids", [])
        if source_id != candidate.get("source_object_reference"):
            error("REQ-SOURCE-OBJECT", "source_provenance.source_object_id", "source object does not match the candidate boundary")
        candidate_parts = candidate.get("included_source_part_references", [])
        if set(part_ids) != set(candidate_parts):
            error("REQ-SOURCE-PART", "source_provenance.normative_part_ids", "normative parts do not exactly match the candidate boundary's included parts")
        if candidate.get("root_source_part_reference") not in part_ids:
            error("REQ-SOURCE-PART", "source_provenance.normative_part_ids", "candidate root source part is not represented")

        required_relationships = {
            (item.get("origin_source_object_reference"), item.get("relationship_type"), item.get("target"))
            for item in candidate.get("related_source_relationship_references", [])
        }
        candidate_source_object = _find_source_object(source_slice, candidate.get("source_object_reference"))
        source_required_relationships = {
            (candidate.get("source_object_reference"), item.get("rel"), item.get("href"))
            for item in (candidate_source_object or {}).get("relationships", [])
            if item.get("rel") == "required"
        }
        for relationship in source_required_relationships - required_relationships:
            error("REQ-SOURCE-RELATIONSHIP", "source_provenance.candidate_boundary", f"candidate does not preserve source-required relationship {relationship!r}")
        record_relationships = {
            (item.get("origin_source_object_reference"), item.get("relationship_type"), item.get("target"))
            for item in source_provenance.get("source_relationships", [])
        }
        if record_relationships != required_relationships:
            error("REQ-SOURCE-RELATIONSHIP", "source_provenance.source_relationships", "source relationships must exactly preserve those recorded by the validated candidate")

    snapshot = candidate_set.get("candidate_boundary_set", {}).get("source_snapshot", {})
    artifact = _catalog_artifact(source_manifest) or {}
    manifest_values = {
        "source_catalog_identity": source_manifest.get("source_family_id"),
        "source_version": source_manifest.get("content_release"),
        "pinned_upstream_revision": source_manifest.get("repository_commit"),
        "source_artifact_path": artifact.get("path"),
    }
    for field, expected in manifest_values.items():
        if expected is None:
            error("REQ-SOURCE-MANIFEST", f"source_provenance.{field}", f"required source manifest value for {field} is unavailable")
        elif source_provenance.get(field) != expected:
            error("REQ-SOURCE-MANIFEST", f"source_provenance.{field}", f"does not match pinned source manifest value {expected!r}")
    if snapshot:
        snapshot_map = {
            "source_catalog_identity": snapshot.get("source_family_id"),
            "source_version": snapshot.get("source_content_release"),
            "pinned_upstream_revision": snapshot.get("repository_commit"),
            "source_artifact_path": snapshot.get("source_artifact_path"),
        }
        for field, expected in snapshot_map.items():
            if expected is not None and source_provenance.get(field) != expected:
                error("REQ-CANDIDATE-SNAPSHOT", f"source_provenance.{field}", f"does not match candidate-set source snapshot value {expected!r}")

    source_id = source_provenance.get("source_object_id")
    source_object = _find_source_object(source_slice, source_id) if source_id else None
    if source_object is None:
        error("REQ-SOURCE-OBJECT", "source_provenance.source_object_id", f"source object {source_id!r} does not exist in the supplied source slice")
    else:
        source_parts = {item.get("part_id"): item for item in source_object.get("statement_parts", [])}
        for part_id in source_provenance.get("normative_part_ids", []):
            if part_id not in source_parts:
                error("REQ-SOURCE-PART", "source_provenance.normative_part_ids", f"source part {part_id!r} does not exist in source object {source_id!r}")
        obligation_ref = record.get("normative_content", {}).get("source_bound_obligation_reference", {})
        if obligation_ref.get("source_object_id") != source_id:
            error("REQ-OBLIGATION-REF", "normative_content.source_bound_obligation_reference.source_object_id", "obligation reference source object does not match source provenance")
        if obligation_ref.get("part_id") not in source_provenance.get("normative_part_ids", []):
            error("REQ-OBLIGATION-REF", "normative_content.source_bound_obligation_reference.part_id", "obligation reference part is not in the validated normative part set")

        for index, relation in enumerate(source_provenance.get("source_relationships", [])):
            origin = relation.get("origin_source_object_reference")
            source_origin = _find_source_object(source_slice, origin)
            relation_tuple = (relation.get("relationship_type"), relation.get("target"))
            if source_origin is None or relation_tuple not in {
                (item.get("rel"), item.get("href")) for item in source_origin.get("relationships", [])
            }:
                error("REQ-RELATIONSHIP-REF", f"source_provenance.source_relationships[{index}]", "relationship does not resolve to the supplied source slice")
        if source_id == source_object.get("source_control_id"):
            parameters = {item.get("parameter_id"): item for item in source_object.get("parameters", [])}
            expected_parameters = set(candidate.get("normative_parameter_references", [])) if candidate else set()
            record_parameters = {
                item.get("parameter_id") for item in record.get("normative_content", {}).get("parameter_dependencies", [])
            }
            if record_parameters != expected_parameters:
                error("REQ-PARAMETER-REF", "normative_content.parameter_dependencies", "parameter dependencies must exactly match the validated candidate's normative parameter references")
            for index, dependency in enumerate(record.get("normative_content", {}).get("parameter_dependencies", [])):
                parameter_id = dependency.get("parameter_id")
                parameter = parameters.get(parameter_id)
                if parameter is None:
                    error("REQ-PARAMETER-REF", f"normative_content.parameter_dependencies[{index}].parameter_id", f"parameter {parameter_id!r} does not exist in the source object")
                    continue
                usage_parts = {
                    usage.get("part_id")
                    for usage in parameter.get("usage_parts", [])
                    if usage.get("part_type") in {"statement", "item"}
                }
                if not usage_parts.intersection(source_provenance.get("normative_part_ids", [])):
                    error("REQ-PARAMETER-REF", f"normative_content.parameter_dependencies[{index}].parameter_id", "parameter is not used by an included normative source part")

    identity = record.get("identity", {})
    lifecycle = record.get("lifecycle", {})
    governance = record.get("governance", {})
    approval = governance.get("approval_record")
    if approval:
        approved_identity = approval.get("requirement_identity", {})
        if approved_identity != {"logical_id": identity.get("logical_id"), "version": identity.get("version")}:
            error("REQ-APPROVAL-IDENTITY", "governance.approval_record.requirement_identity", "approval record must identify this exact Requirement logical identity and version")
        if governance.get("approval_decision") == "APPROVED" and approval.get("decision") != "APPROVE":
            error("REQ-APPROVAL-DECISION", "governance.approval_record.decision", "approved state requires an explicit APPROVE decision")
        if approval.get("decision_reference") and not any(
            event.get("event_type") in {"REQUIREMENT_APPROVED", "REQUIREMENT_REJECTED"}
            and event.get("reference") == approval.get("decision_reference")
            for event in record.get("history", [])
        ):
            error("REQ-APPROVAL-HISTORY", "history", "approval decision reference is not represented in Requirement history")
    if governance.get("human_review_state") == "REVIEWED" and not any(
        event.get("event_type") == "REQUIREMENT_REVIEWED" for event in record.get("history", [])
    ):
        error("REQ-REVIEW-HISTORY", "history", "REVIEWED state requires a human review history event")
    if governance.get("approval_decision") == "APPROVED" and lifecycle.get("state") not in {"APPROVED", "SUPERSEDED", "RETIRED"}:
        error("REQ-APPROVAL-STATE", "lifecycle.state", "approved decision is inconsistent with Requirement lifecycle state")
    if lifecycle.get("state") in {"APPROVED", "SUPERSEDED", "RETIRED"} and governance.get("approval_decision") != "APPROVED":
        error("REQ-APPROVAL-STATE", "governance.approval_decision", "approved or derived lifecycle state requires an explicit Requirement approval decision")
    if lifecycle.get("state") == "SUPERSEDED" and lifecycle.get("currentness_state") != "SUPERSEDED":
        error("REQ-CURRENTNESS", "lifecycle.currentness_state", "SUPERSEDED lifecycle state requires SUPERSEDED currentness state")

    for relation_name in ("supersedes", "superseded_by"):
        for index, reference in enumerate(lifecycle.get(relation_name, [])):
            if reference.get("logical_id") == identity.get("logical_id") and reference.get("version") == identity.get("version"):
                error("REQ-SUPERSESSION", f"lifecycle.{relation_name}[{index}]", "Requirement cannot supersede or be superseded by itself at the same identity and version")

    return diagnostics


def promotion_readiness(record: dict[str, Any], diagnostics: list[Diagnostic]) -> dict[str, Any]:
    """Return a read-only prerequisite report; never mutate or approve a record."""
    errors = [item for item in diagnostics if item.severity == "ERROR"]
    if errors:
        return {"status": "BLOCKED", "blockers": sorted({item.code for item in errors}), "mutated": False}

    state = record.get("lifecycle", {}).get("state")
    if state == "PROPOSED":
        return {
            "status": "HUMAN_REQUIREMENT_REVIEW_REQUIRED",
            "blockers": ["REQUIREMENT_HUMAN_REVIEW_NOT_RECORDED", "REQUIREMENT_APPROVAL_NOT_RECORDED"],
            "mutated": False,
        }
    if state == "HUMAN_REVIEWED":
        return {"status": "HUMAN_REQUIREMENT_APPROVAL_REQUIRED", "blockers": ["REQUIREMENT_APPROVAL_NOT_RECORDED"], "mutated": False}
    if state in {"APPROVED", "SUPERSEDED", "RETIRED"}:
        return {"status": "APPROVAL_ALREADY_RECORDED_NO_CHANGE", "blockers": [], "mutated": False}
    return {"status": "HUMAN_REVIEW_OR_DISPOSITION_REQUIRED", "blockers": ["REVIEW_OR_DISPOSITION_REQUIRED"], "mutated": False}


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--requirement", type=Path, default=DEFAULT_REQUIREMENT)
    parser.add_argument("--requirement-schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--source-manifest", type=Path, default=DEFAULT_SOURCE_MANIFEST)
    parser.add_argument("--candidate-set", type=Path, default=DEFAULT_CANDIDATE_SET)
    parser.add_argument("--source-slice", type=Path, default=DEFAULT_SOURCE_SLICE)
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    try:
        record = load_yaml(arguments.requirement)
        schema = load_json(arguments.requirement_schema)
        source_manifest = load_yaml(arguments.source_manifest)
        candidate_set = load_yaml(arguments.candidate_set)
        source_slice = load_yaml(arguments.source_slice)
        diagnostics = validate_record(record, schema, source_manifest, candidate_set, source_slice)
    except (OSError, ValueError, TypeError, KeyError, yaml.YAMLError, json.JSONDecodeError, SchemaError) as error:
        print(json.dumps({"status": "VALIDATION_INPUT_ERROR", "message": str(error)}, sort_keys=True))
        return 2

    print(json.dumps({"status": "STRUCTURAL_VALIDATION_PASS" if not diagnostics else "STRUCTURAL_VALIDATION_FAIL"}, sort_keys=True))
    for diagnostic in diagnostics:
        print(json.dumps(asdict(diagnostic), sort_keys=True))
    print(json.dumps({"promotion_readiness": promotion_readiness(record, diagnostics)}, sort_keys=True))
    return 0 if not diagnostics else 1


if __name__ == "__main__":
    raise SystemExit(main())
