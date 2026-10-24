"""Optional local-source verification, not an Excel recalculation test."""

import hashlib
import os
from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from srat import VARIABLE_DEFINITIONS, WORKBOOK_SHA256


WORKBOOK = os.environ.get("SAR_SRAT_WORKBOOK")
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


@unittest.skipUnless(WORKBOOK, "Set SAR_SRAT_WORKBOOK to verify the approved local source")
class WorkbookSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(WORKBOOK)
        cls.digest = hashlib.sha256(path.read_bytes()).hexdigest()
        cls.sheets = {}
        with ZipFile(path) as archive:
            strings = [
                "".join(item.itertext())
                for item in ET.fromstring(archive.read("xl/sharedStrings.xml")).findall("s:si", NS)
            ]
            relationships = {
                item.get("Id"): item.get("Target")
                for item in ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
            }
            workbook = ET.fromstring(archive.read("xl/workbook.xml"))
            for sheet in workbook.findall("s:sheets/s:sheet", NS):
                key = sheet.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
                target = relationships[key]
                target = target.lstrip("/") if target.startswith("/") else f"xl/{target}"
                root = ET.fromstring(archive.read(target))
                cells = {}
                for cell in root.findall(".//s:sheetData/s:row/s:c", NS):
                    value = cell.find("s:v", NS)
                    text = value.text if value is not None else ""
                    if cell.get("t") == "s":
                        text = strings[int(text)]
                    formula = cell.find("s:f", NS)
                    cells[cell.get("r")] = (text, formula)
                cls.sheets[sheet.get("name")] = cells

    def formula(self, sheet, cell):
        formula = self.sheets[sheet][cell][1]
        self.assertIsNotNone(formula, f"{sheet}!{cell} has no formula")
        return re.sub(r"\s+", "", formula.text or "")

    def test_reference_hash_and_all_source_score_cells(self):
        self.assertEqual(WORKBOOK_SHA256, self.digest)
        for row, definition in enumerate(VARIABLE_DEFINITIONS, 35):
            self.assertIn(definition.score_cell, self.sheets[definition.worksheet])
            reference = re.sub(r"\s+", "", f"'{definition.worksheet}'!{definition.score_cell}")
            self.assertIn(reference, self.formula("RAT SCORECARD", f"J{row}"))
        self.assertEqual("SUM(J35:J44)", self.formula("RAT SCORECARD", "J47"))

    def test_binary_formula_thresholds_and_shared_response_scoring(self):
        for definition in VARIABLE_DEFINITIONS[:-1]:
            with self.subTest(variable=definition.identifier):
                formula = self.formula(definition.worksheet, definition.score_cell)
                first, last = definition.scoring_cells[0], definition.scoring_cells[-1]
                self.assertTrue(formula.startswith(f"IF(COUNTBLANK({first}:{last})>0,3,IFERROR("))
                total_cell = "C" + definition.score_cell[1:]
                count = len(definition.scoring_cells)
                self.assertIn(f"IF({total_cell}={count},1,", formula)
                if definition.identifier == "III":
                    self.assertIn('IF(B3="No",1,', formula)
                    self.assertIn(f"IF({total_cell}=1,3,", formula)
                else:
                    self.assertIn(f"IF({total_cell}=0,3,", formula)
                self.assertEqual(
                    f"SUM(C{first[1:]}:C{last[1:]})",
                    self.formula(definition.worksheet, total_cell),
                )
                shared = {}
                for row, cell in self.sheets[definition.worksheet].items():
                    element = cell[1]
                    if element is not None and element.get("t") == "shared" and element.text:
                        shared[element.get("si")] = element.text
                for input_cell in definition.scoring_cells:
                    score_cell = "C" + input_cell[1:]
                    element = self.sheets[definition.worksheet][score_cell][1]
                    self.assertIsNotNone(element)
                    text = element.text or shared[element.get("si")]
                    self.assertRegex(text, r'^IF\(B\d+="Yes",1,0\)$')

    def test_x_source_formula_and_non_scoring_context_questions(self):
        sheet = "VARIABLE X (GenAI QUESTIONS)"
        self.assertEqual('IF(B14="Yes",1,0)', self.formula(sheet, "C14"))
        self.assertEqual('IF(B19="Low",1,IF(B19="Medium",2,IF(B19="High",3,"")))', self.formula(sheet, "C19"))
        self.assertEqual('IFERROR(C14*C19,"")', self.formula(sheet, "C20"))
        formula = self.formula(sheet, "D20")
        self.assertTrue(formula.startswith('IF(OR(B14="",B19=""),3,'))
        for branch in ("IF(C20=0,3,", "IF(C20=3,3,", "IF(C20=2,2,", "IF(C20=1,1)"):
            self.assertIn(branch, formula)
        for cell in VARIABLE_DEFINITIONS[-1].context_cells:
            self.assertTrue(self.sheets[sheet]["A" + cell[1:]][0])
            self.assertNotIn(cell + "=", formula)

    def test_source_band_legend_preserves_gap_26(self):
        legend = self.sheets["RAT SCORECARD"]["A33"][0]
        for text in ("<=10", ">=11 & <=15", ">=16 & <=20", ">= 21 & <=25", "> 26"):
            self.assertIn(text, legend)
        self.assertNotIn(">=26", legend.replace(" ", ""))


if __name__ == "__main__":
    unittest.main()
