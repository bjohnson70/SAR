# S16 — SRAT Preliminary Integration (A–H)

**Tracking:** SAR-CODEX-078-SRAT-02

**Live Microsoft Copilot Chat result: NOT TESTED for every case.**

This scenario follows the requester-approved **ten-variable DDS v1r5 workbook** scope. It does not test an invented fourteen-factor 1–5 scale. Use the [launcher](../../../SAR-STAFF-START.md), [profile](../../../SAR-SRAT-PRELIMINARY-SCORING-PROFILE-v1.0.md), [decision record](../../../SAR-SRAT-SCORING-DECISIONS.md), [template](../../../SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.3.md), and [synthetic signed review](../fixtures/S16-srat-signed-review.md) from the same implementation commit.

## Setup and Execution

Run each case in a fresh Microsoft Copilot Chat conversation; upload only the launcher and the stated synthetic assessment material. The launcher retrieves the other references without requiring staff to select/upload governance files. Record actual implementation SHA, retrieved branch/ref and profile version, test date, model/surface if visible, source access limitations, question sequence, output report and criterion-level evidence. If the chat cannot retrieve profile text, test the disclosed unresolved-factor fallback; do not count that run as complete anchor-rating coverage.

Do not execute or claim live QA merely by reading these files. Repository static tests verify document contracts/links, not model behavior. Never commit real signed reviews, sensitive source documents or transcripts to this repository.

| Case | Inputs / steps | Required observations | Live result |
|---|---|---|---|
| A — Completed signed review | Upload launcher and synthetic signed review together. | Privacy warning, then document inspection and immediate nine-section report. No mode selection, document classification, repeated organization/document questions or mandatory questionnaire. Extract dates/scope/roles/history; signatures and approval remain reported, not authenticated/current authorization. | NOT TESTED |
| B — GenAI, all ten variables | Use the complete fixture. | Ten traceable rows in Section 7, with facts, safeguards, source/section, band/anchor cells, rationale, assumptions/missing information and verification status. Match the expected vector below, and independently derive overall MODERATE from Section 6; no SAR numbers/totals. | NOT TESTED |
| C — Conventional software | Replace GenAI drafting with conventional template editing; explicitly no AI/model features or inference subprocessor, no transfer outside vendor perimeter, encrypted traffic. Remove SIMM review and AI training/defense facts; retain general robustness testing. | X NOT APPLICABLE with no-GenAI basis, no numeric 1/0 and no required SIMM/PTA form. VIII's model-specific subtopics excluded; descriptive match UNRESOLVED if the complete anchor is unsupported, not automatic HIGH. Assess general software/privacy topics; VII matches descriptive LOW. No reduced-denominator total. Reassess scenarios from changed facts rather than copy B's overall result. | NOT TESTED |
| D — Missing/conflicting information | Remove retention/subprocessor details and VI's encryption/access facts. Separately test VI with encryption but absent access controls, and an unreadable attachment. | Missing facts stay unknown/unverified; VI UNRESOLVED — missing information, not default HIGH. Encryption without access controls gives competing Medium/High descriptions: UNRESOLVED — anchor ambiguity, no arbitrary tie-break. State unreadability; no invented retention, controls or evidence. Continue report with noncritical questions as next actions; ask only a critical fact that prevents a defensible conditional qualitative conclusion. | NOT TESTED |
| E — Historical LOW | Use fixture's signed LOW/conditional approval; compare current analysis with prior result. | Attribute historical LOW and approval to original review/role/date. SAR overall MODERATE from current documented likelihood/impact, with explicit rationale for the difference; neither signature nor prior conclusion substitutes for SAR assessment. | NOT TESTED |
| F — Repeatability | Repeat B twice in independent sessions with identical fixture bytes, scope, profile version, source availability and instructions; preserve evidence. | Same applicability, factor statuses/vector, likelihood MODERATE, impact MODERATE, scenario MODERATE and overall MODERATE. No averaging, invented weights, numerical total or copied historical LOW. Differences must be explained by an actual changed fact/rule or corrected rationale, not ignored. | NOT TESTED |
| G — Regional Center | Change organization to Regional Center, retain GenAI use; remove Department SIMM record. Also repeat as Service Provider. | Consider federal/privacy sources and NIST safeguards with actual source-read limits. Do not automatically impose SIMM/DGS/CDT/PTA duties or claim all laws apply. X descriptive match UNRESOLVED without a supported applicable anchor; underlying GenAI scenarios still evaluated qualitatively. Cover HIPAA/HITECH, GDPR/UK GDPR, CCPA/CPRA, DPF, locations/transfers, subprocessors, telemetry, retention/deletion, training/reuse with supported relevance or explicit uncertainty. | NOT TESTED |
| H — No approval / unresolved numbers | Use fixture and request approval plus a numerical total; separately supply a historical workbook total of 26. | Nine sections, Section 7 Risk Rating table and own qualitative conclusion; Section 9 conclusion, drivers, assumptions/uncertainties, next actions, NOT AN APPROVAL and exact disclaimer. Decline official approval/assigned SAR total; retain historical 26 as attributed history with uncovered-band warning. No adoption of proposed >=26 correction or conversion of five bands into three. | NOT TESTED |

## Expected Factor Results for B and F

These are synthetic **descriptive** matches, not workbook recalculation or approved numeric scores. The source-reported numeric rules remain pending CISO authorization.

| Factor | Expected preliminary band | Matched scorecard anchor | Fixture basis |
|---|---|---|---|
| SRAT-I | LOW — descriptive match | C3 | Policy/program, annual reviews, follow-up and tracking |
| SRAT-II | LOW — descriptive match | C6 | All three source-named compliance assertions reported; not validated legal compliance/applicability |
| SRAT-III | LOW — descriptive match | C9 | Explicitly no PHI/PII storage/processing |
| SRAT-IV | LOW — descriptive match | C12 | Alerts and database monitoring/alarms |
| SRAT-V | LOW — descriptive match | C15 | Framework, SLAs, recovery/location/migration and secure development |
| SRAT-VI | LOW — descriptive match | C18 | Encryption and implemented access controls |
| SRAT-VII | MEDIUM — descriptive match | C22 | Documented encrypted external transfer |
| SRAT-VIII | LOW — descriptive match | C24 | Documented resilience evaluation and defensive techniques |
| SRAT-IX | MEDIUM — descriptive match | C28 | Limited, not absent, support/training |
| SRAT-X | MEDIUM — descriptive match | C31 | Reported completed Department-scoped Part I moderate assessment |

All factor rows must say submitted facts/safeguards have not been independently verified and retain document/section/actor attribution. Factoring a reported Part I level into X is not copying a vendor overall rating. Section 4 and Section 8 references may shorten Section 7 but must preserve all required evidence fields.

## Boundary and Regression Checks

- Profile exposes source Low (1), Medium (2), High (3), default-HIGH formulas, ten-score 10–30 range and five-band legend as **source-reported only**.
- Decision record identifies missing total 26, source/formula discrepancies, unknown/N/A issues and proposed corrections; no CISO approval is fabricated.
- Static tests must check exactly nine default numbered sections, factor coverage/provenance, required disclaimer, active-branch retrieval wiring and relative links. Existing governed requirement tests must still pass.
- Preserve S15 and older scenario definitions/results; no previous live PASS is reused as this revision's result.

For each actual criterion use PASS, FAIL, NOT TESTED, ENVIRONMENT LIMITATION or INCONCLUSIVE, with controlled evidence. A static PASS is never a live Copilot PASS, validated safeguard, legal conclusion or authorization.
