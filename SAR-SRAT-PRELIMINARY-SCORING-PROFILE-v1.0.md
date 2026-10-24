# SAR SRAT Preliminary Scoring Profile v1.0

**Tracking:** SAR-CODEX-079; extends SAR-CODEX-078-SRAT-02

**Status:** Independent DDS SRAT methodology, under the CISO-approved architectural direction supplied in SAR-CODEX-079. Source thresholds are retained unchanged; total-26 correction and reduced-scope N/A classification remain unapproved.

## Scope and Authority

SAR-CODEX-078 explicitly revised the scope to the supplied **ten-variable** DDS SRAT workbook, not the originally described fourteen-factor GenAI scale. At that checkpoint, numeric use was deferred. SAR-CODEX-079 supersedes that restriction for an **independent SRAT assessment**, with worksheet-specific raw calculations and mandatory evidence-gated effective scores. It does not authorize threshold corrections, a reduced-scope classification policy, or an SRAT-to-NIST crosswalk. The unrelated fourteen-factor 1/3/5 anchors and 8–15 / 16–25 / 26–40 bands are not attributed to this workbook.

This profile supplements the [document-first launcher](SAR-STAFF-START.md) and [nine-section report](SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.3.md). The reusable standard-library [calculation module](tools/srat.py) and separate [Markdown renderer](tools/sar_report.py) need no new dependencies, service or application runtime. They do not change the governed [Submitter](SUBMITTER.md), establish legal applicability, require staff to upload governance files or a workbook, duplicate answered intake, or gate preliminary analysis on reviewer completion. No final SRAT PDF is generated automatically; it remains reviewer-requested.

**Identity:** methodology `DDS-SRAT`, source version `v1r5`, implementation version `1.0.0`; this retained profile filename is documentation v1.0, not a claim that the source workbook changed. SAR orchestrates separate DDS SRAT software/vendor risk, NIST/FIPS 199 categorization, NIST SP 800-53 Rev. 5 control applicability/assessment, privacy/PHI/PII assessments and future methodologies. Never convert an SRAT number into NIST impact, let SRAT override control applicability, combine unrelated numerical results, or change SAR's qualitative matrix/conclusion.

### Reference provenance

- Supplied filename: `DDS_SRAT_v1r5_Default_High.xlsx`.
- Visible scoring-sheet title: `DDS SRAT v1r5` with Default HIGH scoring.
- SHA-256 of supplied bytes: `20d716ee47e4b504a218f28ad978454d863135ca66dc8e46ae319cb58465053c`.
- Read locally on 2026-10-23 from the requester-supplied file. Workbook XML, cell text, stored formulas, and shared-formula definitions were inspected; formulas were not recalculated in Excel. Cached results are not execution validation.
- Source locations below are worksheet names and cell addresses. This Markdown preserves descriptive summaries and formula behavior separately; it is not an authenticated DDS publication or a complete copy of the workbook.
- Publisher authority, canonical publication URL, effective date, licensing/publication permission for the workbook, and currentness were not established. The workbook is not committed. Its hash identifies bytes, not approval or authenticity.

See the [decision record](SAR-SRAT-SCORING-DECISIONS.md) for the supplied architectural authorization, superseded interim rules, discrepancies and still-open CISO decisions. Workbook publication authenticity/licensing and an institutional authorization record beyond the supplied task are not inferred from this implementation.

## One Reusable Profile, Conditional GenAI Extension

The [Source Catalog](SAR-SOURCE-CATALOG.md), [Applicability Model](SAR-APPLICABILITY-MODEL.md), and [Requirement Model](SAR-REQUIREMENT-MODEL.md) distinguish a reference from authority, facts from applicability, and safeguards from findings. Use one profile: variables I–IX are reusable review topics, and X is a conditional GenAI extension. Review individual subtopics for relevance rather than assuming every question or law applies.

For conventional software, propose X as **Not Applicable - Pending Review** with a documented no-GenAI basis; it remains applicable at effective HIGH until explicitly approved. Approval requires a reviewer, review date, exclusion justification and an established no-GenAI scope (`genai_use=False`). Unknown GenAI scope cannot justify exclusion or score reduction. For mixed software, record component/data-flow scope. Never manufacture a SIMM assessment. VIII's general robustness topic can be relevant to conventional software, but model training/fine-tuning portions need their own basis; unsupported per-question N/A does not lower the category.

Retain all ten rows, including exclusions. Supported category statuses are **Not Assessed**, **In Progress**, **Assessed**, **Not Applicable - Pending Review**, and **Not Applicable - Approved**. All applicable categories begin at effective **3 (HIGH)**. Proposed N/A never reduces a score. An approved exclusion has effective score `None` (not 0 or 1) and is excluded from the sum. Sum the remaining effective integers, disclose the applicable count and exclusion list, and mark the total **PROVISIONAL** with **no overall band assigned** while N/A classification policy awaits CISO approval. Do not normalize, prorate, choose a denominator or reuse the ten-category thresholds for a shorter assessment. If none apply, total is undefined, never zero/LOW. An invalid exclusion approval remains included at HIGH with explicit gaps.

## Source-Reported Descriptive Anchors

Stable profile-local identifiers `SRAT-I` through `SRAT-X` identify review factors, **not governed Requirement IDs**; module variable IDs are `I`–`X`. Names below summarize the source variable questions. Columns summarize `RAT SCORECARD!C3:C32` and adjacent `J` labels: **Low Risk (1), Medium Risk (2), High Risk (3)**. Preserve the source's word **Medium**; it is not a conversion to SAR's overall MODERATE. Descriptions remain reference explanations, not substitute calculation formulas.

| Factor ID and name | Low Risk (1), source summary | Medium Risk (2), source summary | High Risk (3), source summary | Source cells |
|---|---|---|---|---|
| SRAT-I — Vendor risk management | Policy and program; annual organization-wide assessments, periodic risk-owner follow-up, and risk-treatment tracking methodology | Policy exists, program undefined | Neither policy nor program | Scorecard C3:C5; VARIABLE I A3:A5, D6 |
| SRAT-II — Compliance and certifications | Reported compliance with GDPR, HIPAA, and SOC 2 Type 2 | Reported compliance with a subset | Reported compliance with none | Scorecard C6:C8; VARIABLE II A3:A8, D9 |
| SRAT-III — PHI/PII exposure and encryption | No PHI/PII stored | PHI/PII stored with TLS 1.2 minimum/secure ciphers in transit and AES-256 at rest | PHI/PII stored, security controls undefined | Scorecard C9:C11; VARIABLE III A3:A6, D7 |
| SRAT-IV — Alerts and vulnerability management | Regular patch/security alerts plus database monitoring and alarms | Limited regular patch-alert capability | No such alert capability | Scorecard C12:C14; VARIABLE IV A3:A8, D9 |
| SRAT-V — Vendor security/privacy practices | Framework adherence, uptime/availability/incident SLAs, backup/recovery/location/migration details, and secure development framework | Limited SLA/secure-development capability, threat awareness/adaptation, contractual security assurances | Security practices undocumented and no contractual security assurance | Scorecard C15:C17; VARIABLE V A3:A7, D8 |
| SRAT-VI — Sensitive-data safeguards | Encryption at rest/in transit and access controls | Encryption at rest/in transit but no access controls | Encryption or access-control standards absent | Scorecard C18:C20; VARIABLE VI A3:A10, D11 |
| SRAT-VII — Third parties and APIs | No transfer outside vendor perimeter; encrypted transmission | Transfer outside vendor perimeter; encrypted transmission | Dependencies/API protections undocumented | Scorecard C21:C23; VARIABLE VII A3:A8, D9 |
| SRAT-VIII — Adversarial robustness | Documented resilience evaluation/tools/benchmarks and defensive techniques | Incomplete robustness evaluation but some adversarial training/randomized defense | No evidence of adversarial evaluation | Scorecard C24:C26; VARIABLE VIII A3:A4, D5 |
| SRAT-IX — Vendor viability/support | Good reputation and support track record with extensive training | Limited after-sales support/training | No after-sales support and/or training | Scorecard C27:C29; VARIABLE IX A3:A5, D6 |
| SRAT-X — GenAI assessment | No GenAI (source says N/A), or completed SIMM 5305-F Part I with low GenAI risk; example: non-human data, limited harm | Completed Part I with moderate GenAI risk; example: non-identifying confidential program data, serious harm | Completed Part I with high GenAI risk; example: identifiable confidential program/service-decision data, catastrophic harm | Scorecard C30:C32; VARIABLE X (GenAI QUESTIONS) A26:B28, D20 |

The descriptive anchors overlap or omit cases. For example, VI's Medium and High descriptions can overlap when access controls are absent. A missing attachment is not proof that a vendor has no documentation, no controls, or no evaluation. Do not use the table to declare legal compliance or confirmed deficiencies.

## Worksheet-Specific Raw Calculation

`SCORING RULES v1r5!A2:B8` says each category starts at **3 (HIGH)**; unanswered questions, an original zero result, formula error, or invalid result yield 3. A completed category retains its worksheet's valid 1, 2, or 3 result. Ten effective category values are summed, minimum **10**, maximum **30**, in `RAT SCORECARD!J35:J44,J47`. The module reproduces the guarded D-cell raw results below and then applies the separate completion/evidence/reviewer checks. It computes scores rather than accepting caller-supplied numbers. Only integer 1/2/3 results may become effective scores; source outer guards merely check numeric range and therefore do not themselves enforce this stricter invariant.

| Worksheet | Inputs / score cell | Stored-formula behavior for complete, valid source responses |
|---|---|---|
| VARIABLE I | B3:B5 / D6 | 3 Yes -> 1; 1–2 Yes -> 2; 0 Yes -> 3 |
| VARIABLE II | B3:B8 / D9 | 6 Yes -> 1; 1–5 Yes -> 2; 0 Yes -> 3 |
| VARIABLE III | B3:B6 / D7 | B3 No -> 1; otherwise 4 Yes -> 1, total 1 Yes -> 3, 2–3 Yes -> 2; invalid/zero -> 3 |
| VARIABLE IV | B3:B8 / D9 | 6 Yes -> 1; 1–5 Yes -> 2; 0 Yes -> 3 |
| VARIABLE V | B3:B7 / D8 | 5 Yes -> 1; 1–4 Yes -> 2; 0 Yes -> 3 |
| VARIABLE VI | B3:B10 / D11 | 8 Yes -> 1; 1–7 Yes -> 2; 0 Yes -> 3 |
| VARIABLE VII | B3:B8 / D9 | 6 Yes -> 1; 1–5 Yes -> 2; 0 Yes -> 3 |
| VARIABLE VIII | B3:B4 / D5 | 2 Yes -> 1; 1 Yes -> 2; 0 Yes -> 3 |
| VARIABLE IX | B3:B5 / D6 | 3 Yes -> 1; 1–2 Yes -> 2; 0 Yes -> 3 |
| VARIABLE X (GenAI QUESTIONS) | B14, B19 / D20 | B14 Yes and B19 Low/Medium/High -> 1/2/3; B14 No -> 3; either blank -> 3; invalid result/error -> 3 |

For I–IX, any blank in the listed input range yields 3 before the remaining logic. Shared formulas encode Yes as 1 and other answers as 0; Excel comparisons are case-insensitive and whitespace is not trimmed. These source behaviors are retained in **raw** results, not used to turn UNKNOWN into verified No. The module's effective guard permits only explicit Yes/No, or Low/Medium/High for X.B19; source dropdown Unknown/N/A values prevent reductions pending a supported category-level decision. Structural errors (unknown/duplicate IDs, missing categories, duplicate evidence references) raise explicit errors, not success-shaped results.

X's B3:B10 contextual questions do not feed the source D20 formula. They must nevertheless be answered and supported for an **effective** reduction, consistent with the worksheet instruction to complete all sections. Blank template-only B11/B12 and VII.B9 dropdown cells have no question and are not additional required inputs. X.B14 asks about SIMM 5310-C PTA/PIA completion; B19 is a PIA risk level, whereas descriptive anchors cite SIMM 5305-F Part I. A17's HIGH/CDT consequence is not a new SAR approval gate or universal organizational obligation.

`RAT SCORECARD!A33` reports: Low <=10; Low Medium 11–15; Medium 16–20; Medium High 21–25; High >26. **26 is unclassified.** The module applies these five bands only to integer totals 10–30 with all ten categories applicable: 10 LOW; 11–15 LOW MEDIUM; 16–20 MEDIUM; 21–25 MEDIUM HIGH; 27–30 HIGH. Total 26 returns an explicit **UNCLASSIFIED** provisional result. Out-of-domain, fractional, boolean or undefined totals return **INVALID**, never LOW. The proposed >=26 correction is not implemented; no five-to-three-band crosswalk exists. A new ten-applicable-category assessment totals **30 (HIGH)** and remains provisional while incomplete.

## Independent Assessment Procedure

1. Inspect documents first and reuse extracted facts/evidence references; never restart answered intake. Submitted facts remain accurate assumptions for **qualitative preliminary analysis**, not independently validated evidence for numerical reduction. A supplied signed report does not authenticate itself or confer current approval.
2. Build `SratAssessment` with its assessment ID, all ten `CategoryAssessment` records, shared evidence and explicit GenAI scope. `QuestionResponse.cell` uses source coordinates (for example B3); exported question IDs are `I.B3`, `X.B19`, etc. Record source/section, reported safeguard, current scope, response, missingness and reviewer comments. Default status is Not Assessed; unanswered input is never silently No.
3. Run `worksheet_score` for each variable's **raw worksheet score**, preserving its actual formula even when it differs from descriptive anchors. Do not replace III's exposure branch, X's PIA formula, or any variable's threshold with a generic formula or a vendor conclusion.
4. `assess` derives the **effective score** independently. A reduction below 3 requires Assessed status, every required question answered with valid values, a resolvable evidence reference for every response, every cited artifact explicitly Validated with source/location/verifier/date, an identified reviewer and review date, and nonempty reduction justification. X additionally requires established GenAI use. Otherwise retain 3 and list all unmet checks. Report raw/effective scores, declared assessment status, calculated completion and evidence state separately. Marked-Assessed but unanswered input remains incomplete.
5. Validated here is an explicit reviewer/verification record supplied by a trusted caller, not validation performed by Python, an AI, a signature detector or a file read. Conflicting/rejected, missing or reported-only evidence cannot justify reduction. Role authorization, artifact verification, secure storage and access control remain the calling organization's responsibilities; no trusted governed runtime is claimed. Record reference reuse across methodologies, but do not inherit another methodology's applicability, finding or conclusion.
6. Sum only effective applicable scores. Keep proposed N/A included at HIGH; exclude only supported approved N/A and apply the provisional policy above. Completion/evidence/reviewer gaps and 26 remain visible even with a displayed total. All-high due to incomplete assurance is not a confirmed adverse safeguard finding.
7. Render the nine-section report with a distinct DDS SRAT subsection in Section 7 alongside separate qualitative, NIST/FIPS 199, NIST SP 800-53 and privacy results. Show actual computed numbers only after the module was executed; if unavailable, disclose **NOT EXECUTED — no numerical result available** and continue the document-first qualitative assessment. Never claim an execution or validation based on reading code. Record outstanding question/evidence gaps and review tasks without forcing a staff questionnaire.
8. Derive the overall **SAR qualitative LOW/MODERATE/HIGH** solely from existing scenario likelihood/impact and highest defensible material scenario. Numerical SRAT HIGH can coexist with qualitative LOW/MODERATE and independently supported NIST categories/control applicability. In Section 9 preserve drivers, assumptions, next actions and the exact non-approval disclaimer. Generate a final SRAT PDF only on reviewer request, not automatically.

Identical inputs and methodology/implementation version produce identical raw/effective results. Do not persist real assessment data in this public repository. The module is a library, not a workflow runtime, legal determination, control assessment engine or PDF publisher.

### Reusable evidence contract and library entry points

The shared [evidence types](tools/assessment_evidence.py) preserve reusable artifact reference/source/location/verification status/verifier/date. Methodology-specific `AssessmentEvidence` output records assessment ID, methodology ID/version, variable/question IDs, response, evidence references/status, raw/effective scores, assessment status, reviewer/date and score-reduction justification. `CategoryResult` separately retains completion, exclusion, reviewer comments and gaps. These are not governed Requirement IDs or automatic findings.

`tools` is the existing repository Python-tool location. With it on the Python import path:

```python
from srat import SratAssessment, assess
from sar_report import render_report

result = assess(SratAssessment("SYNTHETIC-EXAMPLE"))
# result.total == 30; classification HIGH; provisional because not assessed.
report = render_report(
    result.assessment_id, ("",) * 9, "UNRESOLVED", srat_result=result
)
```

Calculation is pure and accepts no NIST or qualitative result as an input. Rendering is separate and returns Markdown without writing files, changing conclusions, or generating a PDF. Callers supply scope-specific section narratives and independent methodology results; absent methodologies display NOT ASSESSED, not inferred results. Evidence reuse avoids duplicate intake questions but never makes an assertion validated across unrelated scopes.

## Privacy Coverage Without New Mandatory Intake

Examine these topics in supplied documents even when the ten variables do not expressly name them. Record relevance, facts/source/section, vendor practice, safeguards, uncertainty, and non-binding actions in Sections 3, 4, 6–8. These are coverage prompts, not added numeric factors or assertions of legal duties:

| Topic | Basis to examine; reusable review topics |
|---|---|
| HIPAA/HITECH and BAA | Health-data use, covered-entity/business-associate relationships, contracts and actual processing scope; III, VI, VII. Identifier presence alone does not establish PHI or HIPAA applicability. |
| GDPR / UK GDPR | Relevant establishment, people, processing/targeting/monitoring and controller/processor roles; II, V, VII. Determine each regime separately; do not demand compliance where unsupported. |
| CCPA/CPRA | Relevant business/service-provider/contractor relationships, scope and applicable conditions; II, V, VII. Do not equate a California organization with universal applicability. |
| Data Privacy Framework | Reported participation, entity/scope/current listing if actually checked, destination and transfer basis; V, VII. Participation is not universal compliance or authority for every transfer; disclose unverified status. |
| Residency and international transfers | Hosting/support/backup locations, remote access, destinations, contract restrictions and supported transfer mechanisms; V–VII. |
| Subprocessors | Identity, roles, locations, onward transfers, terms, change notices and oversight as reported; V, VII. |
| Telemetry / secondary uses | Data collected, destinations, purposes, opt-outs/controls, vendor reuse and disclosure; III, V–VII. |
| Retention / deletion | Active/backup/log retention, deletion process and exceptions, contract/end-of-service handling; III, V–VII. |
| AI training / reuse | Model/provider, prompts/outputs, training/fine-tuning permissions, opt-in/out, isolation and retention; V–VII and X only where AI is relevant. |

Source text must actually be read before citing a specific duty. Otherwise label it a potential source to review. Separate law, contractual duty, vendor practice, benchmark, and recommendation. For Regional Centers and Service Providers, use supported federal/privacy sources and NIST safeguard candidates; **do not automatically impose SIMM/DGS** because the DDS workbook mentions them. Retain a State citation only with a supported scope and readable source provision. If a SIMM-based question is unsupported for that organization, keep its response and applicability uncertainty explicit: no invented equivalent certification or compulsory SIMM intake. The applicable category remains effective HIGH until evidence-supported completion or a supported approved exclusion; that numerical default does not alter qualitative findings or establish a State legal duty.
