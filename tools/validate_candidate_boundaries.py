"""Validate Candidate Requirement Boundary artifacts against a source slice."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError

NORMATIVE_PART_TYPES = {"statement", "item"}


@dataclass
class Diagnostic:
    severity: str
    rule_id: str
    field_path: str
    message: str
    candidate_boundary_id: str | None = None
    source_object_reference: str | None = None


class CandidateBoundaryValidator:
    """Performs only mechanically provable Candidate Boundary checks."""

    def __init__(self, candidate: dict[str, Any], source_slice: dict[str, Any], source_slice_reference: str):
        self.candidate = candidate
        self.source_metadata = source_slice["source_slice"]
        self.source_slice_reference = source_slice_reference
        self.diagnostics: list[Diagnostic] = []
        self.source_objects = {
            source_object["source_control_id"]: source_object
            for source_object in source_slice["source_objects"]
        }

    def error(
        self,
        rule_id: str,
        field_path: str,
        message: str,
        candidate: dict[str, Any] | None = None,
        source_object_reference: str | None = None,
    ) -> None:
        self.diagnostics.append(
            Diagnostic(
                severity="ERROR",
                rule_id=rule_id,
                field_path=field_path,
                message=message,
                candidate_boundary_id=candidate.get("candidate_boundary_id") if candidate else None,
                source_object_reference=source_object_reference or (candidate.get("source_object_reference") if candidate else None),
            )
        )

    def validate(self) -> list[Diagnostic]:
        boundary_set = self.candidate["candidate_boundary_set"]
        evaluated = boundary_set["evaluated_source_objects"]
        candidates = boundary_set["candidates"]
        self._validate_snapshot(boundary_set["source_snapshot"])
        self._validate_evaluated_objects(evaluated)
        self._validate_coverage(evaluated, candidates)
        self._validate_candidate_ids(candidates)
        for index, candidate in enumerate(candidates):
            self._validate_candidate(candidate, index)
        return self.diagnostics

    def _validate_snapshot(self, snapshot: dict[str, Any]) -> None:
        expected = {
            "source_family_id": self.source_metadata["source_family_id"],
            "source_content_release": self.source_metadata["source_content_release"],
            "repository_commit": self.source_metadata["repository_commit"],
            "source_artifact_path": self.source_metadata["primary_source_artifact_path"],
            "source_slice_reference": self.source_slice_reference,
        }
        for field, expected_value in expected.items():
            if snapshot[field] != expected_value:
                self.error("CBV-001", f"candidate_boundary_set.source_snapshot.{field}", f"expected {expected_value!r}; found {snapshot[field]!r}")

    def _validate_evaluated_objects(self, evaluated: list[dict[str, Any]]) -> None:
        references = [item["source_object_reference"] for item in evaluated]
        for reference, count in Counter(references).items():
            if count > 1:
                self.error("CBV-002", "candidate_boundary_set.evaluated_source_objects", f"duplicate evaluated source object {reference!r}", source_object_reference=reference)
        for index, reference in enumerate(references):
            if reference not in self.source_objects:
                self.error("CBV-002", f"candidate_boundary_set.evaluated_source_objects[{index}].source_object_reference", f"source object {reference!r} does not exist in the source slice", source_object_reference=reference)

    def _validate_coverage(self, evaluated: list[dict[str, Any]], candidates: list[dict[str, Any]]) -> None:
        declared = {item["source_object_reference"]: item["candidate_count"] for item in evaluated}
        actual = Counter(candidate["source_object_reference"] for candidate in candidates)
        for index, item in enumerate(evaluated):
            reference = item["source_object_reference"]
            if actual[reference] != item["candidate_count"]:
                self.error("CBV-003", f"candidate_boundary_set.evaluated_source_objects[{index}].candidate_count", f"declares {item['candidate_count']} candidates; found {actual[reference]}", source_object_reference=reference)
        for index, candidate in enumerate(candidates):
            reference = candidate["source_object_reference"]
            if reference not in declared:
                self.error("CBV-003", f"candidate_boundary_set.candidates[{index}].source_object_reference", f"candidate source object {reference!r} is not evaluated", candidate)

    def _validate_candidate_ids(self, candidates: list[dict[str, Any]]) -> None:
        for identifier, count in Counter(candidate["candidate_boundary_id"] for candidate in candidates).items():
            if count > 1:
                self.error("CBV-004", "candidate_boundary_set.candidates", f"duplicate candidate_boundary_id {identifier!r}")

    def _validate_candidate(self, candidate: dict[str, Any], index: int) -> None:
        source_object = self._source_object(candidate, index)
        if source_object is None:
            return
        parts = {part["part_id"]: part for part in source_object["statement_parts"]}
        root = candidate["root_source_part_reference"]
        if root not in parts:
            self.error("CBV-006", f"candidate_boundary_set.candidates[{index}].root_source_part_reference", f"root part {root!r} does not belong to source object", candidate)
        self._validate_included_parts(candidate, index, parts)
        self._validate_parameters(candidate, index, source_object)
        self._validate_relationships(candidate, index)

    def _source_object(self, candidate: dict[str, Any], index: int) -> dict[str, Any] | None:
        reference = candidate["source_object_reference"]
        source_object = self.source_objects.get(reference)
        if source_object is None:
            self.error("CBV-005", f"candidate_boundary_set.candidates[{index}].source_object_reference", f"source object {reference!r} does not exist in the source slice", candidate)
        return source_object

    def _validate_included_parts(self, candidate: dict[str, Any], index: int, parts: dict[str, dict[str, Any]]) -> None:
        included = candidate["included_source_part_references"]
        root = candidate["root_source_part_reference"]
        if len(included) != len(set(included)):
            self.error("CBV-007", f"candidate_boundary_set.candidates[{index}].included_source_part_references", "included source parts are not unique", candidate)
        if root not in included:
            self.error("CBV-007", f"candidate_boundary_set.candidates[{index}].included_source_part_references", "root source part is not included", candidate)
        positions: list[int] = []
        for part_id in included:
            part = parts.get(part_id)
            if part is None:
                self.error("CBV-007", f"candidate_boundary_set.candidates[{index}].included_source_part_references", f"included part {part_id!r} does not belong to source object", candidate)
                continue
            positions.append(list(parts).index(part_id))
            if part_id != root and not self._is_descendant(part_id, root, parts):
                self.error("CBV-008", f"candidate_boundary_set.candidates[{index}].included_source_part_references", f"included part {part_id!r} is not a descendant of root {root!r}", candidate)
        if positions != sorted(positions):
            self.error("CBV-007", f"candidate_boundary_set.candidates[{index}].included_source_part_references", "included parts do not follow authoritative source order", candidate)

    def _is_descendant(self, part_id: str, root: str, parts: dict[str, dict[str, Any]]) -> bool:
        current = parts[part_id]
        while current["parent_part_id"] is not None:
            parent_id = current["parent_part_id"]
            parent = parts.get(parent_id)
            if parent is None:
                self.error("CBV-008", "candidate_boundary_set.candidates", f"cannot establish ancestry because parent {parent_id!r} is absent from explicit source structure")
                return False
            if parent_id == root:
                return True
            current = parent
        return False

    def _validate_parameters(self, candidate: dict[str, Any], index: int, source_object: dict[str, Any]) -> None:
        included = set(candidate["included_source_part_references"])
        parameters = {parameter["parameter_id"]: parameter for parameter in source_object["parameters"]}
        expected: set[str] = set()
        for parameter_id, parameter in parameters.items():
            usages = parameter["usage_parts"]
            normative_usage = [usage for usage in usages if usage["part_type"] in NORMATIVE_PART_TYPES and usage["part_id"] in included]
            if normative_usage:
                expected.add(parameter_id)
        actual = set(candidate["normative_parameter_references"])
        for parameter_id in actual:
            parameter = parameters.get(parameter_id)
            path = f"candidate_boundary_set.candidates[{index}].normative_parameter_references"
            if parameter is None:
                self.error("CBV-009", path, f"parameter {parameter_id!r} does not exist in the candidate source object", candidate)
                continue
            normative_usage = [usage for usage in parameter["usage_parts"] if usage["part_type"] in NORMATIVE_PART_TYPES and usage["part_id"] in included]
            if not normative_usage:
                self.error("CBV-009", path, f"parameter {parameter_id!r} has no normative usage in included source parts", candidate)
            if not any(usage["part_type"] in NORMATIVE_PART_TYPES for usage in parameter["usage_parts"]):
                self.error("CBV-011", path, f"assessment-only parameter {parameter_id!r} is listed as normative", candidate)
        missing = expected - actual
        if missing:
            self.error("CBV-010", f"candidate_boundary_set.candidates[{index}].normative_parameter_references", f"missing normative parameters: {', '.join(sorted(missing))}", candidate)

    def _validate_relationships(self, candidate: dict[str, Any], index: int) -> None:
        for relationship_index, reference in enumerate(candidate.get("related_source_relationship_references", [])):
            origin = reference["origin_source_object_reference"]
            source_object = self.source_objects.get(origin)
            path = f"candidate_boundary_set.candidates[{index}].related_source_relationship_references[{relationship_index}]"
            if source_object is None:
                self.error("CBV-012", f"{path}.origin_source_object_reference", f"relationship origin {origin!r} does not exist", candidate)
                continue
            expected = {"rel": reference["relationship_type"], "href": reference["target"]}
            if expected not in source_object["relationships"]:
                self.error("CBV-012", path, "relationship reference does not resolve to source provenance", candidate)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        document = yaml.safe_load(stream)
    if not isinstance(document, dict):
        raise ValueError(f"{path}: expected a YAML object")
    return document


def source_slice_reference(path: Path) -> str:
    resolved_path = path.resolve()
    result = subprocess.run(
        ["git", "-C", str(resolved_path.parent), "rev-parse", "--show-toplevel"],
        capture_output=True,
        check=True,
        text=True,
    )
    repository_root = Path(result.stdout.strip()).resolve()
    return resolved_path.relative_to(repository_root).as_posix()


def structural_diagnostics(candidate: dict[str, Any], schema: dict[str, Any]) -> list[Diagnostic]:
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    diagnostics = []
    for error in sorted(validator.iter_errors(candidate), key=lambda item: list(item.absolute_path)):
        path = ".".join(str(part) for part in error.absolute_path) or "$"
        diagnostics.append(Diagnostic("ERROR", "SCHEMA", path, error.message))
    return diagnostics


def print_diagnostics(diagnostics: list[Diagnostic]) -> None:
    for diagnostic in diagnostics:
        print(json.dumps(asdict(diagnostic), sort_keys=True))


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True, type=Path, help="Candidate Boundary YAML artifact")
    parser.add_argument("--schema", required=True, type=Path, help="Candidate Boundary JSON Schema")
    parser.add_argument("--source-slice", required=True, type=Path, help="Source slice YAML artifact")
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    try:
        candidate = load_yaml(arguments.candidate)
        source_slice = load_yaml(arguments.source_slice)
        with arguments.schema.open(encoding="utf-8") as stream:
            schema = json.load(stream)
        diagnostics = structural_diagnostics(candidate, schema)
        if diagnostics:
            print("VALIDATION: FAIL")
            print_diagnostics(diagnostics)
            return 1
        source_reference = source_slice_reference(arguments.source_slice)
        diagnostics = CandidateBoundaryValidator(candidate, source_slice, source_reference).validate()
    except (KeyError, OSError, subprocess.CalledProcessError, TypeError, ValueError, yaml.YAMLError, json.JSONDecodeError, SchemaError) as error:
        print(f"VALIDATION: ERROR\n{error}", file=sys.stderr)
        return 2
    if diagnostics:
        print("VALIDATION: FAIL")
        print_diagnostics(diagnostics)
        return 1
    print("VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())