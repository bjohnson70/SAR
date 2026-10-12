from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_requirement_registry import (
    DuplicateJsonKeyError,
    canonicalize_content,
    content_digest,
    load_json_strict,
    validate_append_only,
    validate_registry,
)


class RequirementRegistryContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = load_json_strict(ROOT / "schemas/sar-requirement-registry.schema.json")
        cls.fixture = load_json_strict(ROOT / "requirements/registry-fixtures/basic-registry.fixture.json")

    def validate(self, snapshot=None):
        return validate_registry(copy.deepcopy(self.fixture if snapshot is None else snapshot), self.schema)

    @staticmethod
    def codes(diagnostics):
        return {item.code for item in diagnostics}

    @staticmethod
    def append_event(snapshot, event_type, target_version, *, successors=None, event_id=None):
        sequence = len(snapshot["lifecycle_events"]) + 1
        target_reference = {
            "issuer_namespace": target_version["issuer_namespace"],
            "logical_id": target_version["logical_id"],
            "version_id": target_version["version_id"],
        }
        event = {
            "record_type": "SAR_REQUIREMENT_LIFECYCLE_EVENT",
            "record_schema_version": "1.0.0",
            "event_id": event_id or f"fixture-event-{sequence:03d}",
            "sequence": sequence,
            "previous_event_id": snapshot["lifecycle_events"][-1]["event_id"],
            "event_type": event_type,
            "target_identity": {
                "issuer_namespace": target_reference["issuer_namespace"],
                "logical_id": target_reference["logical_id"],
            },
            "target_version": target_reference,
            "actor_reference": "synthetic:test-actor-not-authenticated",
            "occurred_at": f"2026-10-11T12:00:{sequence:02d}Z",
        }
        if successors is not None:
            event["successor_versions"] = [
                {
                    "issuer_namespace": item["issuer_namespace"],
                    "logical_id": item["logical_id"],
                    "version_id": item["version_id"],
                }
                for item in successors
            ]
        if event_type == "VERSION_WITHDRAWN":
            event["reason"] = "Synthetic lifecycle fixture only."
        if event_type == "APPROVAL_EVIDENCE_REFERENCED":
            content_id = next(
                version["content_reference_id"]
                for version in snapshot["versions"]
                if version["issuer_namespace"] == target_reference["issuer_namespace"]
                and version["logical_id"] == target_reference["logical_id"]
                and version["version_id"] == target_reference["version_id"]
            )
            content_reference = next(
                reference for reference in snapshot["content_references"]
                if reference["content_reference_id"] == content_id
            )
            event["evidence_reference"] = "fixture-only-evidence-reference"
            event["approval_content_digest"] = content_reference["digest_value"]
        snapshot["lifecycle_events"].append(event)
        return event

    def test_non_operational_fixture_is_valid_and_unapproved(self):
        self.assertEqual([], self.validate())
        self.assertEqual("NON_OPERATIONAL_FIXTURE", self.fixture["snapshot_context"])
        self.assertFalse(any(event["event_type"] == "APPROVED" for event in self.fixture["lifecycle_events"]))
        self.assertFalse(any("approval_status" in version for version in self.fixture["versions"]))
        self.assertFalse(any("execution_state" in version for version in self.fixture["versions"]))

    def test_fixture_digest_values_are_reproducible(self):
        for reference in self.fixture["content_references"]:
            self.assertEqual(content_digest(reference["content_envelope"], self.schema), reference["digest_value"])

    def test_lifecycle_and_locator_metadata_are_outside_content_digest(self):
        snapshot = copy.deepcopy(self.fixture)
        reference = snapshot["content_references"][0]
        digest_before = content_digest(reference["content_envelope"], self.schema)
        reference["immutable_locator"] = "fixture://relocated/content"
        self.append_event(snapshot, "ADMINISTRATIVE_CORRECTION", snapshot["versions"][0])
        self.assertEqual(digest_before, content_digest(reference["content_envelope"], self.schema))

    def test_canonicalization_is_deterministic_and_sorts_object_members(self):
        envelope = self.fixture["content_references"][0]["content_envelope"]

        def reverse_object_members(value):
            if isinstance(value, dict):
                return {key: reverse_object_members(item) for key, item in reversed(list(value.items()))}
            if isinstance(value, list):
                return [reverse_object_members(item) for item in value]
            return value

        reordered = reverse_object_members(envelope)
        canonical = canonicalize_content(envelope, self.schema)
        self.assertEqual(canonical, canonicalize_content(reordered, self.schema))
        self.assertEqual(content_digest(envelope, self.schema), content_digest(reordered, self.schema))

    def test_rfc8785_utf8_and_member_order_vector(self):
        envelope = self.fixture["content_references"][0]["content_envelope"]
        canonical = canonicalize_content(envelope, self.schema)
        self.assertIsInstance(canonical, bytes)
        self.assertEqual(canonical, canonical.decode("utf-8").encode("utf-8"))
        self.assertLess(canonical.index(b'"identity"'), canonical.index(b'"normative_content"'))

    def test_unicode_is_preserved_without_normalization(self):
        composed = copy.deepcopy(self.fixture["content_references"][0]["content_envelope"])
        decomposed = copy.deepcopy(composed)
        composed["normative_content"]["statement"] = "caf\u00e9"
        decomposed["normative_content"]["statement"] = "cafe\u0301"
        composed_bytes = canonicalize_content(composed, self.schema)
        decomposed_bytes = canonicalize_content(decomposed, self.schema)
        self.assertIn("\u00e9".encode("utf-8"), composed_bytes)
        self.assertNotEqual(composed_bytes, decomposed_bytes)

    def test_duplicate_json_object_member_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"a": 1, "a": 2}', encoding="utf-8")
            with self.assertRaises(DuplicateJsonKeyError):
                load_json_strict(path)

    def test_digest_mismatch_is_rejected(self):
        snapshot = copy.deepcopy(self.fixture)
        snapshot["content_references"][0]["digest_value"] = "0" * 64
        self.assertIn("REGISTRY_CONTENT_DIGEST", self.codes(self.validate(snapshot)))

    def test_content_envelope_identity_must_match_immutable_version(self):
        snapshot = copy.deepcopy(self.fixture)
        snapshot["content_references"][0]["content_envelope"]["identity"]["version_id"] = 2
        self.assertIn("REGISTRY_CONTENT_IDENTITY", self.codes(self.validate(snapshot)))

    def test_identity_collision_is_rejected(self):
        snapshot = copy.deepcopy(self.fixture)
        snapshot["identities"].append(copy.deepcopy(snapshot["identities"][0]))
        self.assertIn("REGISTRY_IDENTITY_COLLISION", self.codes(self.validate(snapshot)))

    def test_version_collision_is_rejected(self):
        snapshot = copy.deepcopy(self.fixture)
        snapshot["versions"].append(copy.deepcopy(snapshot["versions"][0]))
        self.assertIn("REGISTRY_VERSION_COLLISION", self.codes(self.validate(snapshot)))

    def test_content_reference_collision_is_rejected(self):
        snapshot = copy.deepcopy(self.fixture)
        snapshot["content_references"].append(copy.deepcopy(snapshot["content_references"][0]))
        self.assertIn("REGISTRY_CONTENT_REFERENCE_COLLISION", self.codes(self.validate(snapshot)))

    def test_dangling_identity_reference_is_rejected(self):
        snapshot = copy.deepcopy(self.fixture)
        snapshot["versions"][0]["logical_id"] = "fixture-missing-identity"
        self.assertIn("REGISTRY_IDENTITY_REFERENCE", self.codes(self.validate(snapshot)))

    def test_version_sequence_must_be_contiguous(self):
        snapshot = copy.deepcopy(self.fixture)
        snapshot["versions"][1]["version_id"] = 3
        self.assertIn("REGISTRY_VERSION_SEQUENCE", self.codes(self.validate(snapshot)))

    def test_unsupported_approval_transition_is_rejected(self):
        snapshot = copy.deepcopy(self.fixture)
        snapshot["lifecycle_events"][2]["event_type"] = "VERSION_APPROVED"
        self.assertIn("REGISTRY_SCHEMA", self.codes(self.validate(snapshot)))

    def test_parameter_assignment_cannot_be_smuggled_into_content(self):
        snapshot = copy.deepcopy(self.fixture)
        dependency = snapshot["content_references"][0]["content_envelope"]["normative_content"]["parameter_dependencies"][0]
        dependency["assigned_value"] = "synthetic-value"
        self.assertIn("REGISTRY_SCHEMA", self.codes(self.validate(snapshot)))

    def test_event_sequence_and_previous_link_are_enforced(self):
        snapshot = copy.deepcopy(self.fixture)
        snapshot["lifecycle_events"][2]["previous_event_id"] = "fixture-event-001"
        self.assertIn("REGISTRY_EVENT_CHAIN", self.codes(self.validate(snapshot)))
        snapshot = copy.deepcopy(self.fixture)
        snapshot["lifecycle_events"][3]["sequence"] = 9
        self.assertIn("REGISTRY_EVENT_SEQUENCE", self.codes(self.validate(snapshot)))
        snapshot = copy.deepcopy(self.fixture)
        snapshot["lifecycle_events"][3]["event_id"] = snapshot["lifecycle_events"][2]["event_id"]
        self.assertIn("REGISTRY_EVENT_ID_COLLISION", self.codes(self.validate(snapshot)))

    def test_version_events_must_follow_registration(self):
        snapshot = copy.deepcopy(self.fixture)
        events = snapshot["lifecycle_events"]
        snapshot["lifecycle_events"] = [events[0], events[2], events[1], events[3]]
        for index, event in enumerate(snapshot["lifecycle_events"], start=1):
            event["sequence"] = index
            if index > 1:
                event["previous_event_id"] = snapshot["lifecycle_events"][index - 2]["event_id"]
        codes = self.codes(self.validate(snapshot))
        self.assertIn("REGISTRY_EVENT_ORDER", codes)

    def test_supersession_cycles_are_rejected(self):
        snapshot = copy.deepcopy(self.fixture)
        first = snapshot["versions"][0]
        second = snapshot["versions"][1]
        self.append_event(snapshot, "VERSION_SUPERSEDED", first, successors=[second])
        self.append_event(snapshot, "VERSION_SUPERSEDED", second, successors=[first])
        self.assertIn("REGISTRY_SUPERSESSION_CYCLE", self.codes(self.validate(snapshot)))

    def test_supersession_must_follow_successor_registration(self):
        snapshot = copy.deepcopy(self.fixture)
        self.append_event(snapshot, "VERSION_SUPERSEDED", snapshot["versions"][0], successors=[snapshot["versions"][1]])
        events = snapshot["lifecycle_events"]
        snapshot["lifecycle_events"] = [*events[:3], events[4], events[3]]
        for index, event in enumerate(snapshot["lifecycle_events"], start=1):
            event["sequence"] = index
            if index > 1:
                event["previous_event_id"] = snapshot["lifecycle_events"][index - 2]["event_id"]
        self.assertIn("REGISTRY_EVENT_ORDER", self.codes(self.validate(snapshot)))

    def test_terminal_lifecycle_event_cannot_be_repeated(self):
        snapshot = copy.deepcopy(self.fixture)
        first = snapshot["versions"][0]
        second = snapshot["versions"][1]
        self.append_event(snapshot, "VERSION_WITHDRAWN", first)
        self.append_event(snapshot, "VERSION_SUPERSEDED", first, successors=[second])
        self.assertIn("REGISTRY_EVENT_TRANSITION", self.codes(self.validate(snapshot)))

    def test_approval_evidence_reference_binds_digest_without_approving(self):
        snapshot = copy.deepcopy(self.fixture)
        self.append_event(snapshot, "APPROVAL_EVIDENCE_REFERENCED", snapshot["versions"][0])
        self.assertEqual([], self.validate(snapshot))
        self.assertNotIn("approval_status", snapshot["versions"][0])

        snapshot["lifecycle_events"][-1]["approval_content_digest"] = "0" * 64
        self.assertIn("REGISTRY_APPROVAL_DIGEST_MISMATCH", self.codes(self.validate(snapshot)))

    def test_append_only_extension_is_accepted(self):
        prior = copy.deepcopy(self.fixture)
        updated = copy.deepcopy(prior)
        self.append_event(updated, "ADMINISTRATIVE_CORRECTION", updated["versions"][1])
        self.assertEqual([], validate_append_only(prior, updated, self.schema))

    def test_mutating_prior_content_or_event_is_rejected(self):
        prior = copy.deepcopy(self.fixture)
        changed_content = copy.deepcopy(prior)
        changed_content["content_references"][0]["content_envelope"]["normative_content"]["statement"] += " changed"
        codes = self.codes(validate_append_only(prior, changed_content, self.schema))
        self.assertIn("REGISTRY_IMMUTABLE_RECORD_CHANGED", codes)
        self.assertIn("REGISTRY_CONTENT_DIGEST", codes)

        changed_event = copy.deepcopy(prior)
        changed_event["lifecycle_events"][2]["reason"] = "rewritten history"
        self.assertIn("REGISTRY_EVENT_HISTORY_CHANGED", self.codes(validate_append_only(prior, changed_event, self.schema)))

    def test_removing_prior_records_or_events_is_rejected(self):
        prior = copy.deepcopy(self.fixture)
        changed = copy.deepcopy(prior)
        changed["versions"].pop()
        changed["lifecycle_events"].pop()
        codes = self.codes(validate_append_only(prior, changed, self.schema))
        self.assertIn("REGISTRY_HISTORY_REMOVED", codes)
        self.assertIn("REGISTRY_EVENT_HISTORY_CHANGED", codes)


if __name__ == "__main__":
    unittest.main()
