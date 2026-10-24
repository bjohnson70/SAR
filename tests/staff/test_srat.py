"""Synthetic SRAT calculation, evidence, independence and Markdown regression tests."""

from dataclasses import replace
from datetime import date
from itertools import product
from pathlib import Path
import re
import sys
import unittest


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from assessment_evidence import Evidence, EvidenceStatus
from sar_report import MethodologyResult, render_report, render_srat
from srat import (
    AssessmentStatus, CategoryAssessment, Classification, QuestionResponse,
    QUESTION_TOPICS, SratAssessment, VARIABLE_DEFINITIONS, VARIABLES, assess,
    classify_total, worksheet_score,
)


REVIEW_DATE = date(2026, 10, 23)
VALIDATED = Evidence(
    "SYNTHETIC-E1", "Synthetic test evidence", "Synthetic scope / sections 1-10",
    EvidenceStatus.VALIDATED, "Synthetic verifier", REVIEW_DATE,
)


def completed_category(variable, score=1):
    definition = next(item for item in VARIABLE_DEFINITIONS if item.identifier == variable)
    answers = dict.fromkeys(definition.required_cells, "Yes")
    if variable == "X":
        answers["B19"] = {1: "Low", 2: "Medium", 3: "High"}[score]
    elif score == 3:
        answers = dict.fromkeys(definition.required_cells, "No")
        if variable == "III":
            answers["B3"] = "Yes"
    elif score == 2:
        answers[definition.scoring_cells[-1]] = "No"
    return CategoryAssessment(
        variable,
        tuple(QuestionResponse(cell, response, (VALIDATED.reference,)) for cell, response in answers.items()),
        AssessmentStatus.ASSESSED, "Synthetic reviewer", REVIEW_DATE,
        "Synthetic evidence reviewed for every response; worksheet result justified.",
    )


def complete_assessment(score=1):
    return SratAssessment(
        "SYNTHETIC-ASSESSMENT", tuple(completed_category(variable, score) for variable in VARIABLES),
        (VALIDATED,), True,
    )


def change_category(assessment, replacement):
    return replace(
        assessment,
        categories=tuple(replacement if item.variable_id == replacement.variable_id else item for item in assessment.categories),
    )


class SratTests(unittest.TestCase):
    def test_a_new_assessment_all_ten_high_total_30(self):
        result = assess(SratAssessment("SYNTHETIC-NEW"))
        self.assertEqual(tuple(VARIABLES), tuple(item.variable_id for item in result.categories))
        self.assertEqual([3] * 10, [item.effective_score for item in result.categories])
        self.assertEqual([3] * 10, [item.raw_score for item in result.categories])
        self.assertTrue(all(item.assessment_status == AssessmentStatus.NOT_ASSESSED for item in result.categories))
        self.assertEqual(30, result.total)
        self.assertEqual(Classification.HIGH, result.classification)
        self.assertTrue(result.provisional)

    def test_b_each_unanswered_question_prevents_reduction(self):
        original = complete_assessment()
        for category in original.categories:
            for response in category.responses:
                with self.subTest(variable=category.variable_id, cell=response.cell):
                    altered = replace(
                        category,
                        responses=tuple(replace(item, response=None) if item.cell == response.cell else item for item in category.responses),
                    )
                    result = assess(change_category(original, altered))
                    scored = next(item for item in result.categories if item.variable_id == category.variable_id)
                    self.assertEqual(3, scored.effective_score)
                    self.assertFalse(scored.complete)
                    self.assertTrue(scored.gaps)

    def test_c_complete_validated_medium(self):
        result = assess(complete_assessment(2))
        self.assertEqual([2] * 10, [item.effective_score for item in result.categories])
        self.assertEqual(20, result.total)
        self.assertEqual(Classification.MEDIUM, result.classification)
        self.assertFalse(result.provisional)

    def test_d_complete_validated_low(self):
        result = assess(complete_assessment())
        self.assertEqual([1] * 10, [item.effective_score for item in result.categories])
        self.assertEqual(10, result.total)
        self.assertEqual(Classification.LOW, result.classification)
        self.assertFalse(result.provisional)

    def test_e_missing_or_unverified_evidence_does_not_reduce(self):
        original = complete_assessment()
        for evidence in (
            (), (replace(VALIDATED, verification_status=EvidenceStatus.REPORTED),),
            (replace(VALIDATED, verification_status=EvidenceStatus.REJECTED),),
            (replace(VALIDATED, verified_by=None),),
            (replace(VALIDATED, verification_date=None),),
            (replace(VALIDATED, source=""),),
            (replace(VALIDATED, location=""),),
        ):
            with self.subTest(evidence=evidence):
                result = assess(replace(original, evidence=evidence))
                self.assertEqual([1] * 10, [item.raw_score for item in result.categories])
                self.assertEqual([3] * 10, [item.effective_score for item in result.categories])
                self.assertEqual(30, result.total)
                self.assertTrue(result.provisional)
        category = original.categories[0]
        altered = replace(category, responses=category.responses[1:] + (replace(category.responses[0], evidence_references=("MISSING",)),))
        self.assertEqual(3, assess(change_category(original, altered)).categories[0].effective_score)

    def test_f_na_pending_and_approved_are_distinct_from_unanswered(self):
        original = complete_assessment()
        x = replace(original.categories[-1], status=AssessmentStatus.NA_PENDING, responses=())
        pending = assess(change_category(replace(original, genai_use=False), x))
        self.assertEqual(3, pending.categories[-1].effective_score)
        self.assertFalse(pending.categories[-1].excluded)
        self.assertEqual(10, pending.applicable_count)
        approved = replace(x, status=AssessmentStatus.NA_APPROVED, na_justification="Verified no GenAI in assessed scope")
        result = assess(change_category(replace(original, genai_use=False), approved))
        self.assertTrue(result.categories[-1].excluded)
        self.assertIsNone(result.categories[-1].effective_score)
        self.assertEqual(9, result.total)
        self.assertEqual(9, result.applicable_count)
        self.assertEqual(("X",), result.excluded_variables)
        self.assertEqual(Classification.PROVISIONAL_NA, result.classification)
        self.assertTrue(result.provisional)
        for invalid in (
            replace(approved, reviewer=None), replace(approved, review_date=None),
            replace(approved, na_justification=""),
        ):
            self.assertEqual(3, assess(change_category(replace(original, genai_use=False), invalid)).categories[-1].effective_score)
        for genai in (True, None):
            self.assertEqual(3, assess(change_category(replace(original, genai_use=genai), approved)).categories[-1].effective_score)

    def test_g_srat_has_no_nist_or_qualitative_inputs_or_mutations(self):
        nist = MethodologyResult(
            "SYNTHETIC-ASSESSMENT", "NIST-FIPS199", "2004",
            "NIST/FIPS 199 — Security Categorization", "MODERATE",
        )
        controls = MethodologyResult(
            "SYNTHETIC-ASSESSMENT", "NIST-SP80053", "Rev. 5",
            "NIST SP 800-53 Rev. 5 — Control Applicability and Assessment",
            "Independent control assessment", ("Synthetic finding remains open",), ("AC-2 applies on its own supported basis",),
        )
        before = (nist, controls)
        for assessment in (SratAssessment("SYNTHETIC-ASSESSMENT"), complete_assessment()):
            result = assess(assessment)
            report = render_report(assessment.assessment_id, ("Synthetic scope narrative",) * 9, "MODERATE", result, before)
            self.assertIn("Conclusion: MODERATE.", report)
            self.assertIn("AC-2 applies on its own supported basis", report)
            self.assertIn("Synthetic finding remains open", report)
            self.assertIn("**Overall preliminary conclusion:** MODERATE.", report)
        self.assertEqual(before, (nist, controls))
        self.assertNotIn("nist", SratAssessment.__dataclass_fields__)

    def test_h_report_has_nine_sections_separate_results_and_no_pdf(self):
        result = assess(complete_assessment(2))
        report = render_report(result.assessment_id, ("Synthetic narrative",) * 9, "LOW", result)
        self.assertEqual(list(range(1, 10)), [int(item) for item in re.findall(r"^## (\d+)\.", report, re.MULTILINE)])
        section7 = report.split("## 7. Risk Rating")[1].split("## 8.")[0]
        self.assertEqual(10, len(re.findall(r"^\| [IVX]+ — ", section7, re.MULTILINE)))
        for text in (
            "Raw worksheet score", "Effective SRAT score", "Assessment status", "Evidence status",
            "Reviewer/date", "Comments / gaps", "**Total numerical score:** 20.",
            "**Overall SRAT classification:** MEDIUM.", "NIST/FIPS 199",
            "NIST SP 800-53 Rev. 5", "Privacy and PHI/PII",
            "NOT ASSESSED", "No combined numerical score",
        ):
            self.assertIn(text, section7)
        self.assertIn("**Overall preliminary qualitative conclusion:** LOW.", report)
        self.assertIn("reviewer-requested only", report)
        self.assertIn("NOT AN APPROVAL", report)
        future = MethodologyResult(
            result.assessment_id, "future", "1", "Future methodology", "MODERATE"
        )
        future_report = render_report(result.assessment_id, ("",) * 9, "LOW", result, (future,))
        self.assertIn("### Future methodology", future_report)
        self.assertIn("Conclusion: MODERATE.", future_report)
        self.assertIn("SYNTHETIC-E1", report)

    def test_i_source_threshold_boundaries_and_26_gap(self):
        for total, expected in (
            (10, Classification.LOW), (11, Classification.LOW_MEDIUM), (15, Classification.LOW_MEDIUM),
            (16, Classification.MEDIUM), (20, Classification.MEDIUM), (21, Classification.MEDIUM_HIGH),
            (25, Classification.MEDIUM_HIGH), (26, Classification.UNCLASSIFIED),
            (27, Classification.HIGH), (30, Classification.HIGH),
        ):
            self.assertEqual(expected, classify_total(total))
        for total in (None, "", "10", True, False, 0, 9, 31, 10.0, float("nan"), float("inf")):
            self.assertEqual(Classification.INVALID, classify_total(total))
        original = complete_assessment(3)
        original = change_category(original, completed_category("I", 1))
        original = change_category(original, completed_category("II", 1))
        result = assess(original)
        self.assertEqual(26, result.total)
        self.assertEqual(Classification.UNCLASSIFIED, result.classification)
        self.assertTrue(result.provisional)
        self.assertIn("UNCLASSIFIED", render_srat(result))

    def test_status_review_and_reduction_justification_are_independent_guards(self):
        original = complete_assessment()
        for altered in (
            replace(original.categories[0], status=AssessmentStatus.IN_PROGRESS),
            replace(original.categories[0], status=AssessmentStatus.NOT_ASSESSED),
            replace(original.categories[0], reduction_justification=""),
            replace(original.categories[0], reviewer=" "),
            replace(original.categories[0], review_date=None),
        ):
            self.assertEqual(3, assess(change_category(original, altered)).categories[0].effective_score)

    def test_unknown_na_and_arbitrary_responses_never_reduce_effective_score(self):
        original = complete_assessment()
        for definition in VARIABLE_DEFINITIONS:
            category = next(item for item in original.categories if item.variable_id == definition.identifier)
            for response in ("Unknown", "N/A", "garbage", " Yes ", "", None):
                altered = replace(category, responses=tuple(replace(item, response=response) if item.cell == definition.required_cells[0] else item for item in category.responses))
                self.assertEqual(3, next(item for item in assess(change_category(original, altered)).categories if item.variable_id == definition.identifier).effective_score)

    def test_evidence_export_is_reusable_but_decisions_are_methodology_scoped(self):
        result = assess(complete_assessment())
        for category in result.categories:
            self.assertTrue(category.complete)
            self.assertEqual(EvidenceStatus.VALIDATED, category.evidence_status)
            for item in category.evidence_records:
                self.assertEqual(result.assessment_id, item.assessment_id)
                self.assertEqual("DDS-SRAT", item.methodology_id)
                self.assertEqual("v1r5", item.methodology_version)
                self.assertEqual(category.variable_id, item.variable_id)
                self.assertEqual((VALIDATED.reference,), item.evidence_references)
                self.assertEqual(1, item.raw_score)
                self.assertEqual(1, item.effective_score)
                self.assertEqual("Assessed", item.assessment_status)
                self.assertTrue(item.reduction_justification)

    def test_structural_errors_are_explicit(self):
        original = complete_assessment()
        for invalid in (
            replace(original, assessment_id=""),
            replace(original, categories=original.categories[:-1]),
            replace(original, categories=original.categories[:-1] + (original.categories[0],)),
            replace(original, evidence=(VALIDATED, VALIDATED)),
            replace(original, genai_use="Unknown"),
        ):
            with self.assertRaises(ValueError):
                assess(invalid)
        category = original.categories[0]
        for responses in (
            category.responses + (category.responses[0],),
            (QuestionResponse("B100", "Yes"),),
        ):
            with self.assertRaises(ValueError):
                assess(change_category(original, replace(category, responses=responses)))
        with self.assertRaises(ValueError):
            worksheet_score("XI", {})

    def test_no_applicable_categories_does_not_classify_as_low(self):
        original = complete_assessment()
        categories = tuple(replace(category, status=AssessmentStatus.NA_APPROVED, na_justification="Synthetic approved exclusion") for category in original.categories)
        result = assess(replace(original, categories=categories, genai_use=False))
        self.assertIsNone(result.total)
        self.assertEqual(Classification.NO_APPLICABLE, result.classification)
        self.assertTrue(result.provisional)

    def test_x_context_questions_do_not_change_raw_but_gate_effective_score(self):
        self.assertEqual(1, worksheet_score("X", {"B14": "Yes", "B19": "Low"}))
        self.assertEqual(3, worksheet_score("X", {"B14": "No", "B19": "Low"}))
        self.assertEqual(2, worksheet_score("X", {"B14": "YES", "B19": "mEdIuM"}))
        original = complete_assessment()
        x = replace(original.categories[-1], responses=tuple(item for item in original.categories[-1].responses if item.cell in ("B14", "B19")))
        result = assess(change_category(original, x)).categories[-1]
        self.assertEqual(1, result.raw_score)
        self.assertEqual(3, result.effective_score)

    def test_versioned_question_topics_cover_required_source_cells(self):
        self.assertEqual(set(VARIABLES), set(QUESTION_TOPICS))
        for definition in VARIABLE_DEFINITIONS:
            self.assertEqual(len(definition.required_cells), len(QUESTION_TOPICS[definition.identifier]))
            self.assertTrue(all(topic.strip() for topic in QUESTION_TOPICS[definition.identifier]))

    def test_formula_vs_description_discrepancies_are_preserved(self):
        self.assertEqual(1, worksheet_score("III", dict.fromkeys(("B3", "B4", "B5", "B6"), "Yes")))
        self.assertEqual(1, worksheet_score("III", {"B3": "No", "B4": "No", "B5": "No", "B6": "No"}))
        self.assertEqual(3, worksheet_score("III", {"B3": "No"}))
        self.assertEqual(2, worksheet_score("VII", {"B3": "Yes", "B4": "No", "B5": "Yes", "B6": "Yes", "B7": "Yes", "B8": "Yes"}))

    def test_all_binary_worksheet_inputs_against_fixed_source_truth_tables(self):
        source_tables = {
            "I": (3, 2, 2, 1), "II": (3, 2, 2, 2, 2, 2, 1),
            "IV": (3, 2, 2, 2, 2, 2, 1), "V": (3, 2, 2, 2, 2, 1),
            "VI": (3, 2, 2, 2, 2, 2, 2, 2, 1),
            "VII": (3, 2, 2, 2, 2, 2, 1), "VIII": (3, 2, 1),
            "IX": (3, 2, 2, 1),
        }
        for definition in VARIABLE_DEFINITIONS:
            if definition.identifier == "X":
                continue
            for values in product(("No", "Yes"), repeat=len(definition.scoring_cells)):
                answers = dict(zip(definition.scoring_cells, values))
                yes = values.count("Yes")
                expected = (
                    1 if answers["B3"] == "No" or yes == 4 else 3 if yes == 1 else 2
                ) if definition.identifier == "III" else source_tables[definition.identifier][yes]
                with self.subTest(variable=definition.identifier, answers=values):
                    self.assertEqual(expected, worksheet_score(definition.identifier, answers))

    def test_report_rejects_mismatched_scope_duplicate_ids_and_extra_sections(self):
        result = assess(complete_assessment())
        with self.assertRaises(ValueError):
            render_report("DIFFERENT-ASSESSMENT", ("",) * 9, "LOW", result)
        with self.assertRaises(ValueError):
            render_report(result.assessment_id, ("",) * 8, "LOW", result)
        with self.assertRaises(ValueError):
            render_report(result.assessment_id, ("## 10. Extra section",) + ("",) * 8, "LOW", result)
        duplicate = MethodologyResult(
            result.assessment_id, "DDS-SRAT", "other", "Fake SRAT result", "LOW"
        )
        with self.assertRaises(ValueError):
            render_report(result.assessment_id, ("",) * 9, "LOW", result, (duplicate,))
        with self.assertRaises(ValueError):
            render_report(result.assessment_id, ("",) * 9, "APPROVED", result)
        unrelated = MethodologyResult("DIFFERENT-ASSESSMENT", "PRIVACY", "1", "Privacy", "LOW")
        with self.assertRaises(ValueError):
            render_report(result.assessment_id, ("",) * 9, "LOW", result, (unrelated,))

    def test_report_without_executed_srat_preserves_qualitative_result(self):
        report = render_report("SYNTHETIC-NO-EXECUTION", ("",) * 9, "MODERATE")
        self.assertIn("NOT EXECUTED — no numerical result available", report)
        self.assertNotIn("**Total numerical score:**", report)
        self.assertIn("**Overall preliminary qualitative conclusion:** MODERATE.", report)
        self.assertIn("NOT ASSESSED", report)


if __name__ == "__main__":
    unittest.main()
