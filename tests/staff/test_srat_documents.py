"""Static document contracts only; these tests do not execute Copilot or score risk."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[2]
PROFILE = "SAR-SRAT-PRELIMINARY-SCORING-PROFILE-v1.0.md"
DECISIONS = "SAR-SRAT-SCORING-DECISIONS.md"
LAUNCHER = "SAR-STAFF-START.md"
TEMPLATE = "SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.3.md"
SCENARIO = "tests/submitter/scenarios/S16-srat-preliminary-scoring.md"
FIXTURE = "tests/submitter/fixtures/S16-srat-signed-review.md"
BRANCH = "sar-codex-078-srat-preliminary-scoring"
DISCLAIMER = (
    "This preliminary assessment assumes the submitted information is accurate "
    "for purposes of analysis. Submitted facts and safeguards have not been "
    "independently verified. The preliminary risk conclusion is not software "
    "approval, authorization to implement, certification of compliance, formal "
    "risk acceptance, or a final security determination."
)
FACTORS = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X")


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


class SratDocumentTests(unittest.TestCase):
    def test_template_has_exactly_nine_numbered_sections(self):
        headings = re.findall(r"^## (\d+)\. (.+)$", read(TEMPLATE), re.MULTILINE)
        self.assertEqual(list(range(1, 10)), [int(number) for number, _ in headings])
        self.assertEqual("Risk Rating", dict(headings)["7"])
        self.assertIn("### Candidate Requirements and Recommended Safeguards", read(TEMPLATE))

    def test_exact_disclaimer_and_nonapproval_boundaries(self):
        for path in (LAUNCHER, TEMPLATE):
            with self.subTest(path=path):
                self.assertIn(DISCLAIMER, read(path))
                self.assertIn("NOT AN APPROVAL", read(path))
                self.assertIn("No formal SAR numerical risk score", read(path))

    def test_ten_factor_coverage_and_source_cells(self):
        rows = re.findall(r"^\| SRAT-([IVX]+) — .+$", read(PROFILE), re.MULTILINE)
        self.assertEqual(list(FACTORS), rows)
        for factor in FACTORS:
            with self.subTest(factor=factor):
                self.assertRegex(read(FIXTURE), rf"\| SRAT-{factor} \|")
                self.assertRegex(read(SCENARIO), rf"\| SRAT-{factor} \|")
        for row in read(PROFILE).splitlines():
            if re.match(r"^\| SRAT-[IVX]+ — ", row):
                self.assertIn("Scorecard C", row)
                self.assertIn("VARIABLE ", row)

    def test_source_provenance_and_unapproved_method_are_explicit(self):
        profile = read(PROFILE)
        for text in (
            "20d716ee47e4b504a218f28ad978454d863135ca66dc8e46ae319cb58465053c",
            "DDS_SRAT_v1r5_Default_High.xlsx",
            "formulas were not recalculated in Excel",
            "minimum **10**, maximum **30**",
            "**26 is unclassified.**",
            "Low Risk (1), Medium Risk (2), High Risk (3)",
            "No CISO approval of numeric scoring is recorded",
            "Do not output 1/2/3 as assigned SAR scores",
            "exactly one complete anchor",
            "UNRESOLVED — anchor ambiguity",
        ):
            self.assertIn(text, profile)
        for decision in range(1, 9):
            self.assertIn(f"CISO-{decision:02}", read(DECISIONS))
        self.assertIn("PROPOSED ONLY", read(DECISIONS))

    def test_document_first_and_qualitative_fallback_remain(self):
        launcher = read(LAUNCHER)
        self.assertLess(
            launcher.index("### Inspect Supplied Documents First"),
            launcher.index("### Only Ask for Missing Intake"),
        )
        for text in (
            "Do not restart the intake questionnaire",
            "ask only one focused clarification at a time",
            "highest defensible material scenario rating",
            "UNRESOLVED — profile unavailable",
            "LOW -> LOW / LOW / MODERATE",
            "MODERATE -> LOW / MODERATE / HIGH",
            "HIGH -> MODERATE / HIGH / HIGH",
        ):
            self.assertIn(text, launcher)

    def test_privacy_and_organization_coverage(self):
        profile = read(PROFILE)
        for text in (
            "HIPAA/HITECH", "GDPR / UK GDPR", "CCPA/CPRA",
            "Data Privacy Framework", "Residency and international transfers",
            "Subprocessors", "Telemetry / secondary uses", "Retention / deletion",
            "AI training / reuse", "do not automatically impose SIMM/DGS",
            "APPLICABILITY UNKNOWN", "NOT APPLICABLE",
        ):
            self.assertIn(text, profile)

    def test_qa_cases_have_no_fabricated_live_results(self):
        rows = re.findall(r"^\| ([A-H]) — .+$", read(SCENARIO), re.MULTILINE)
        self.assertEqual(list("ABCDEFGH"), rows)
        for row in read(SCENARIO).splitlines():
            if re.match(r"^\| [A-H] — ", row):
                self.assertTrue(row.endswith("| NOT TESTED |"))

    def test_updated_document_links_and_launch_ref(self):
        documents = (
            PROFILE, DECISIONS, LAUNCHER, TEMPLATE, SCENARIO, FIXTURE,
            "README.md", "SAR-SOURCE-CATALOG.md", "tests/submitter/README.md",
        )
        checked = 0
        for relative in documents:
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", read(relative)):
                target = unquote(target.strip("<>"))
                parsed = urlparse(target)
                if parsed.scheme:
                    if parsed.netloc != "github.com":
                        continue
                    prefix = f"/bjohnson70/SAR/blob/{BRANCH}/"
                    if relative == LAUNCHER and "/blob/" in parsed.path:
                        self.assertTrue(parsed.path.startswith(prefix), target)
                    if not parsed.path.startswith(prefix):
                        continue
                    destination = ROOT / parsed.path[len(prefix):]
                elif parsed.path:
                    destination = (ROOT / relative).parent / parsed.path
                else:
                    continue
                with self.subTest(document=relative, link=target):
                    self.assertTrue(destination.exists(), f"Missing link: {destination}")
                checked += 1
        self.assertGreater(checked, 35)
        self.assertIn(f"Launch reference: `{BRANCH}`", read(LAUNCHER))
        for document in (PROFILE, DECISIONS, TEMPLATE):
            self.assertIn(f"/blob/{BRANCH}/{document}", read(LAUNCHER))


if __name__ == "__main__":
    unittest.main()
