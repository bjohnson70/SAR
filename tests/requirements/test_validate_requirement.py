from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_requirement import load_json, load_yaml, promotion_readiness, validate_record


class RequirementValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = load_json(ROOT / "schemas/sar-requirement-record.schema.json")
        cls.manifest = load_yaml(ROOT / "sources/nist-sp800-53-rev5.oscal-source.yaml")
        cls.candidates = load_yaml(ROOT / "sources/nist-sp800-53-rev5.si-12.candidate-boundaries.yaml")
        cls.source_slice = load_yaml(ROOT / "sources/nist-sp800-53-rev5.ac-2-si-12.slice.yaml")
        cls.example = load_yaml(ROOT / "requirements/examples/si-12-3.proposed.yaml")

    def validate(self, record=None, candidates=None):
        return validate_record(
            copy.deepcopy(self.example if record is None else record),
            self.schema,
            self.manifest,
            copy.deepcopy(self.candidates if candidates is None else candidates),
            self.source_slice,
        )

    @staticmethod
    def codes(diagnostics):
        return {item.code for item in diagnostics}

    def test_proposed_si_12_3_example_is_structurally_valid(self):
        self.assertEqual([], self.validate())
        self.assertEqual("PROPOSED", self.example["lifecycle"]["state"])
        self.assertEqual("NOT_APPROVED", self.example["governance"]["approval_decision"])
        self.assertEqual("UNRESOLVED", self.example["normative_content"]["parameter_dependencies"][0]["assignment_state"])

    def test_missing_logical_identity_is_rejected(self):
        record = copy.deepcopy(self.example)
        del record["identity"]["logical_id"]
        self.assertIn("REQ-SCHEMA", self.codes(self.validate(record)))

    def test_missing_immutable_version_is_rejected(self):
        record = copy.deepcopy(self.example)
        del record["identity"]["version"]
        self.assertIn("REQ-SCHEMA", self.codes(self.validate(record)))

    def test_unknown_candidate_reference_is_rejected(self):
        record = copy.deepcopy(self.example)
        record["source_provenance"]["candidate_boundary"]["candidate_boundary_id"] = "cbr-unknown-example"
        self.assertIn("REQ-CANDIDATE-REF", self.codes(self.validate(record)))

    def test_candidate_must_be_human_validated(self):
        candidates = copy.deepcopy(self.candidates)
        candidate = candidates["candidate_boundary_set"]["candidates"][-1]
        candidate["validation_status"] = "PROPOSED"
        self.assertIn("REQ-CANDIDATE-STATUS", self.codes(self.validate(candidates=candidates)))

    def test_source_object_must_match_candidate(self):
        record = copy.deepcopy(self.example)
        record["source_provenance"]["source_object_id"] = "si-12.2"
        self.assertIn("REQ-SOURCE-OBJECT", self.codes(self.validate(record)))

    def test_source_object_must_exist_in_source_slice(self):
        record = copy.deepcopy(self.example)
        record["source_provenance"]["source_object_id"] = "si-99"
        self.assertIn("REQ-SOURCE-OBJECT", self.codes(self.validate(record)))

    def test_normative_part_must_match_candidate_and_source(self):
        record = copy.deepcopy(self.example)
        record["source_provenance"]["normative_part_ids"] = ["si-12.2_smt"]
        self.assertIn("REQ-SOURCE-PART", self.codes(self.validate(record)))

    def test_parameter_reference_must_match_validated_candidate(self):
        record = copy.deepcopy(self.example)
        record["normative_content"]["parameter_dependencies"][0]["parameter_id"] = "si-12.2_prm_1"
        self.assertIn("REQ-PARAMETER-REF", self.codes(self.validate(record)))

    def test_required_parent_relationship_cannot_be_omitted(self):
        record = copy.deepcopy(self.example)
        record["source_provenance"]["source_relationships"] = []
        candidates = copy.deepcopy(self.candidates)
        candidates["candidate_boundary_set"]["candidates"][-1]["related_source_relationship_references"] = []
        self.assertIn("REQ-SOURCE-RELATIONSHIP", self.codes(self.validate(record, candidates)))

    def test_proposed_requirement_cannot_claim_approval(self):
        record = copy.deepcopy(self.example)
        record["governance"]["human_review_state"] = "REVIEWED"
        record["governance"]["approval_decision"] = "APPROVED"
        record["governance"]["approval_record"] = self.synthetic_approval(record)
        codes = self.codes(self.validate(record))
        self.assertTrue({"REQ-SCHEMA", "REQ-APPROVAL-STATE"}.intersection(codes))

    def test_approved_state_requires_human_approval_record(self):
        record = copy.deepcopy(self.example)
        record["lifecycle"]["state"] = "APPROVED"
        record["governance"]["human_review_state"] = "REVIEWED"
        record["governance"]["approval_decision"] = "APPROVED"
        self.assertIn("REQ-SCHEMA", self.codes(self.validate(record)))

    def test_reviewed_state_requires_human_review_history(self):
        record = copy.deepcopy(self.example)
        record["lifecycle"]["state"] = "HUMAN_REVIEWED"
        record["governance"]["human_review_state"] = "REVIEWED"
        self.assertIn("REQ-REVIEW-HISTORY", self.codes(self.validate(record)))

    def test_unresolved_parameter_cannot_contain_assignment(self):
        record = copy.deepcopy(self.example)
        record["normative_content"]["parameter_dependencies"][0]["assignment"] = {
            "value": "invented value",
            "authority": "invented authority",
            "scope": "example",
            "version": "1",
            "effective_date": "2026-10-08",
            "decision_reference": "invented",
        }
        self.assertIn("REQ-SCHEMA", self.codes(self.validate(record)))

    def test_malformed_source_revision_is_rejected(self):
        record = copy.deepcopy(self.example)
        record["source_provenance"]["pinned_upstream_revision"] = "not-a-commit"
        self.assertIn("REQ-SCHEMA", self.codes(self.validate(record)))

    def test_self_supersession_reference_is_rejected(self):
        record = copy.deepcopy(self.example)
        record["lifecycle"]["supersedes"] = [copy.deepcopy(record["identity"])]
        record["lifecycle"]["supersedes"][0].pop("identifier_convention_status", None)
        self.assertIn("REQ-SUPERSESSION", self.codes(self.validate(record)))

    def test_synthetic_approved_fixture_requires_and_accepts_structured_decision(self):
        record = copy.deepcopy(self.example)
        record["record_context"] = "SYNTHETIC_TEST_FIXTURE"
        record["lifecycle"]["state"] = "APPROVED"
        record["governance"]["human_review_state"] = "REVIEWED"
        record["governance"]["approval_decision"] = "APPROVED"
        approval = self.synthetic_approval(record)
        record["governance"]["approval_record"] = approval
        record["history"].append({
            "event_type": "REQUIREMENT_REVIEWED",
            "date": "2026-10-08",
            "authority": "SYNTHETIC TEST AUTHORITY - NOT A REAL APPROVER",
            "reference": "SYNTHETIC-TEST-REVIEW-NOT-REAL",
        })
        record["history"].append({
            "event_type": "REQUIREMENT_APPROVED",
            "date": "2026-10-08",
            "authority": approval["authority"],
            "reference": approval["decision_reference"],
        })
        self.assertEqual([], self.validate(record))

    def test_requirement_approval_scope_cannot_be_boundary_validation(self):
        record = copy.deepcopy(self.example)
        record["record_context"] = "SYNTHETIC_TEST_FIXTURE"
        record["lifecycle"]["state"] = "APPROVED"
        record["governance"]["human_review_state"] = "REVIEWED"
        record["governance"]["approval_decision"] = "APPROVED"
        approval = self.synthetic_approval(record)
        approval["scope"] = "SOURCE_BOUNDARY_FIDELITY_ONLY"
        record["governance"]["approval_record"] = approval
        self.assertIn("REQ-SCHEMA", self.codes(self.validate(record)))

    def test_readiness_reports_missing_human_prerequisites(self):
        diagnostics = self.validate()
        report = promotion_readiness(self.example, diagnostics)
        self.assertEqual("HUMAN_REQUIREMENT_REVIEW_REQUIRED", report["status"])
        self.assertIn("REQUIREMENT_APPROVAL_NOT_RECORDED", report["blockers"])

    def test_readiness_is_dry_run_and_does_not_mutate_record(self):
        record = copy.deepcopy(self.example)
        before = copy.deepcopy(record)
        report = promotion_readiness(record, self.validate(record))
        self.assertFalse(report["mutated"])
        self.assertEqual(before, record)
        self.assertEqual("PROPOSED", record["lifecycle"]["state"])
        self.assertEqual("NOT_APPROVED", record["governance"]["approval_decision"])

    @staticmethod
    def synthetic_approval(record):
        return {
            "decision": "APPROVE",
            "authority": "SYNTHETIC TEST AUTHORITY - NOT A REAL APPROVER",
            "date": "2026-10-08",
            "scope": "REQUIREMENT_GOVERNANCE_ONLY",
            "requirement_identity": {
                "logical_id": record["identity"]["logical_id"],
                "version": record["identity"]["version"],
            },
            "decision_provenance": "Synthetic unit-test fixture; not a real approval decision.",
            "decision_reference": "SYNTHETIC-TEST-DECISION-NOT-REAL",
        }


if __name__ == "__main__":
    unittest.main()
