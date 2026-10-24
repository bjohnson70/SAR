# SAR Staff Assessment

SAR is a Markdown-native, AI-assisted security and privacy assessment framework. The canonical short staff launcher is [SAR-STAFF-START.md](SAR-STAFF-START.md). Preliminary review is **PRELIMINARY — NOT AN OFFICIAL SECURITY DETERMINATION**. The separate governed assessment process retains its authorization and human decision requirements.

## Staff Start

- [Canonical Markdown launcher](SAR-STAFF-START.md)
- [Manual KISS experience scenarios A-H](tests/submitter/scenarios/S15-staff-kiss-experience.md)
- [SRAT preliminary profile v1.0: ten reusable review factors with conditional GenAI coverage](SAR-SRAT-PRELIMINARY-SCORING-PROFILE-v1.0.md)
- [Open scoring decisions requiring CISO authorization](SAR-SRAT-SCORING-DECISIONS.md)
- [SRAT QA scenarios A-H and reproducibility fixture](tests/submitter/scenarios/S16-srat-preliminary-scoring.md)

## Assessment Boundaries

- The launcher retrieves SAR governing methodology and source references from the pinned GitHub branch and discloses retrieval limitations. Optional source failures do not block a provisional preliminary report; the launcher includes a clearly limited fallback if core methodology cannot be retrieved.
- Candidate requirements and controls are not formal applicability, validated controls, findings, scores, approval, or authorization. SRAT factor bands are provisional descriptive matches, not numeric SAR scores. The supplied workbook's numeric rules are documented but not adopted; SAR retains its qualitative likelihood/impact matrix and overall LOW/MODERATE/HIGH conclusion.
- Sensitive information may be submitted only through an AI environment authorized for it and the organization's use. Failure to detect identifiers does not establish safety.
- The governed SAR process retains its existing trusted execution and authorized human decision boundaries.

The v1.1/v1.2 launch documents and S13/S14 scenarios remain preserved as historical versions. S15 is a manual test definition; Microsoft Copilot Chat compatibility is not claimed until it is actually tested there.

The requester reports that the document-first workflow passed live Microsoft Copilot Chat QA before this enhancement; that is not evidence that this SRAT revision passed live QA. S16 live execution remains NOT TESTED. The requester revised SAR-CODEX-078-SRAT-02 from an unavailable fourteen-factor scale to the supplied ten-variable DDS SRAT v1r5 workbook. See the profile for descriptive anchors, source formula summaries, privacy coverage and interim nonnumeric handling; see the decision record for proposed corrections, not approved thresholds.

Repository validation (static checks, not live model execution):

```powershell
python -m unittest discover -s tests\requirements -v
python -m unittest discover -s tests\staff -v
```
