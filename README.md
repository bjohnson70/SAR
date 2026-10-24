# SAR Staff Assessment

SAR is a Markdown-native, AI-assisted security and privacy assessment framework. The canonical short staff launcher is [SAR-STAFF-START.md](SAR-STAFF-START.md). Preliminary review is **PRELIMINARY — NOT AN OFFICIAL SECURITY DETERMINATION**. The separate governed assessment process retains its authorization and human decision requirements.

## Staff Start

- [Canonical Markdown launcher](SAR-STAFF-START.md)
- [Manual KISS experience scenarios A-H](tests/submitter/scenarios/S15-staff-kiss-experience.md)
- [Independent DDS SRAT profile: ten variables with conditional GenAI coverage](SAR-SRAT-PRELIMINARY-SCORING-PROFILE-v1.0.md)
- [Open scoring decisions requiring CISO authorization](SAR-SRAT-SCORING-DECISIONS.md)
- [Historical 078 SRAT scenarios A-H](tests/submitter/scenarios/S16-srat-preliminary-scoring.md)
- [Independent SRAT calculation and A-J regression tests](tests/staff/test_srat.py)

## Assessment Boundaries

- The launcher retrieves SAR governing methodology and source references from the pinned GitHub branch and discloses retrieval limitations. Optional source failures do not block a provisional preliminary report; the launcher includes a clearly limited fallback if core methodology cannot be retrieved.
- Candidate requirements and controls are not formal applicability, validated controls, findings, approval, or authorization. Under SAR-CODEX-079's supplied CISO-approved architectural direction, DDS SRAT is an independently versioned numerical methodology, not SAR's qualitative conclusion. Applicable variables default HIGH (3) until complete responses, validated evidence and reviewer justification support a worksheet-specific reduction. A source total of 26 is UNCLASSIFIED; approved-N/A reduced-scope classification remains provisional.
- SRAT, NIST/FIPS 199 categorization, NIST SP 800-53 control applicability/assessment, privacy/PHI/PII and future methodologies retain separate results. SRAT cannot convert to NIST impact or override controls; no combined numerical score is calculated. SAR's qualitative likelihood/impact matrix is unchanged.
- Sensitive information may be submitted only through an AI environment authorized for it and the organization's use. Failure to detect identifiers does not establish safety.
- The governed SAR process retains its existing trusted execution and authorized human decision boundaries.

The v1.1/v1.2 launch documents and S13/S14 scenarios remain preserved as historical versions. S15 is a manual test definition; Microsoft Copilot Chat compatibility is not claimed until it is actually tested there.

The requester reports that the document-first workflow passed live Microsoft Copilot Chat QA before the SRAT enhancements; that is not evidence that this revision passed live QA. S16 is preserved as a historical 078 definition (live execution NOT TESTED). SAR-CODEX-079 supersedes its descriptive-only scoring with the independent DDS SRAT v1r5 module; the source threshold correction and N/A classification are still unresolved.

## Independent SRAT Library

- [Calculation and versioned question topics](tools/srat.py): `DDS-SRAT` / `v1r5`, implementation `1.0.0`; source-specific formulas, effective-score evidence gates, explicit category applicability and provisional aggregation.
- [Reusable evidence types](tools/assessment_evidence.py): reference/source/location/verification plus methodology-scoped question records.
- [Separate Markdown reporting](tools/sar_report.py): nine sections, independent supplied methodology results, no recalculation/crosswalk and **no automatic final SRAT PDF**. Final artifact generation is reviewer-requested.

These are standard-library Python tools alongside existing validators, not a new application runtime, service, mandatory intake or governed execution environment. Put the existing tools directory on the import path; see the profile's library example. Trusted callers provide reviewer/verification metadata; the library does not authenticate artifacts or grant authority. Staff chat remains document-first: if code cannot actually execute, report SRAT NOT EXECUTED without fabricated numbers and continue the qualitative assessment.

Repository validation (calculation/report tests and static checks, **not live model execution**):

```powershell
python -m unittest discover -s tests\requirements -v
python -m unittest discover -s tests\staff -v
```

Optional workbook-source checks use only the standard library and the approved local workbook, never committed source bytes:

```powershell
$env:SAR_SRAT_WORKBOOK = 'C:\path\to\DDS_SRAT_v1r5_Default_High.xlsx'
python -m unittest discover -s tests\staff -v
```

The suite covers requested cases A–J, exhaustive binary worksheet input cases, source-band boundaries including 26, N/A/reviewer/evidence guards, and separate methodology reporting. Workbook-source tests are explicitly skipped if the local path is not supplied; a skip is not an Excel formula recalculation or a live Copilot PASS.
