# SAR SRAT Preliminary Scoring Profile v1.0

**Tracking:** SAR-CODEX-078-SRAT-02

**Status:** Preliminary working guidance; source-reported numeric methodology only. No CISO approval of numeric scoring is recorded.

## Scope and Authority

The implementation scope was explicitly revised by the requester to the supplied **ten-variable** DDS SRAT workbook, not the originally described fourteen-factor GenAI scale. The requester directed that workbook rules be documented faithfully, numeric use remain pending CISO authorization, and SAR retain its qualitative conclusions. The unrelated fourteen-factor 1/3/5 anchors and 8–15 / 16–25 / 26–40 bands are not attributed to this workbook.

This profile supplements the [document-first launcher](SAR-STAFF-START.md) and [nine-section report](SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.3.md). It does not change the governed [Submitter](SUBMITTER.md), establish legal applicability, or require a questionnaire, workbook upload by staff, runtime, service, or approval gate before preliminary analysis.

### Reference provenance

- Supplied filename: `DDS_SRAT_v1r5_Default_High.xlsx`.
- Visible scoring-sheet title: `DDS SRAT v1r5` with Default HIGH scoring.
- SHA-256 of supplied bytes: `20d716ee47e4b504a218f28ad978454d863135ca66dc8e46ae319cb58465053c`.
- Read locally on 2026-10-23 from the requester-supplied file. Workbook XML, cell text, stored formulas, and shared-formula definitions were inspected; formulas were not recalculated in Excel. Cached results are not execution validation.
- Source locations below are worksheet names and cell addresses. This Markdown preserves descriptive summaries and formula behavior separately; it is not an authenticated DDS publication or a complete copy of the workbook.
- Publisher authority, canonical publication URL, effective date, licensing/publication permission for the workbook, and currentness were not established. The workbook is not committed. Its hash identifies bytes, not approval or authenticity.

See the [decision record](SAR-SRAT-SCORING-DECISIONS.md) for conflicts and CISO decisions. All rules explicitly labeled **source-reported** or **proposed** remain distinct from the preliminary working instructions below. No rule is labeled CISO-approved without an actual authorization record.

## One Reusable Profile, Conditional GenAI Extension

The [Source Catalog](SAR-SOURCE-CATALOG.md), [Applicability Model](SAR-APPLICABILITY-MODEL.md), and [Requirement Model](SAR-REQUIREMENT-MODEL.md) distinguish a reference from authority, facts from applicability, and safeguards from findings. Use one profile: variables I–IX are reusable review topics, and X is a conditional GenAI extension. Review individual subtopics for relevance rather than assuming every question or law applies.

For conventional software, X is `NOT APPLICABLE` with the documented no-GenAI basis; never manufacture a SIMM assessment. VIII's general robustness/testing topic can be relevant to conventional software, but model training/fine-tuning portions need an AI basis. For mixed software, record the component and data-flow scope. If GenAI use is unknown, X is `APPLICABILITY UNKNOWN`, not N/A.

Retain all ten rows for coverage, including excluded topics. N/A and unknown rows carry no SAR numeric value; do not silently remove them from a denominator or assign 0 or 1. The workbook's different non-GenAI treatment is source-reported below, not adopted.

## Source-Reported Descriptive Anchors

Stable profile-local identifiers `SRAT-I` through `SRAT-X` identify review factors, **not governed Requirement IDs**. Names below summarize the source variable questions. Columns summarize `RAT SCORECARD!C3:C32` and adjacent `J` labels: **Low Risk (1), Medium Risk (2), High Risk (3)**. Preserve the source's word **Medium**; it is not an approved conversion to SAR's overall MODERATE. These are not the original request's LOW (1), MODERATE (3), HIGH (5) anchors.

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

## Source-Reported Worksheet Calculation (Not Adopted)

`SCORING RULES v1r5!A2:B8` says each category starts at **3 (HIGH)**; unanswered questions, an original zero result, formula error, or invalid result yield 3. A completed category retains its worksheet's valid 1, 2, or 3 result. Ten effective category values are summed, minimum **10**, maximum **30**, in `RAT SCORECARD!J35:J44,J47`. The outer guards check numeric range 1–3, not explicitly integer membership; fractional/invalid inputs need CISO resolution, not invented acceptance rules.

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

For I–IX, any blank in the listed input range yields 3 before the remaining logic. Shared formulas encode Yes as 1 and other answers as 0; the formulas do not comprehensively reject arbitrary nonblank text. These are source behaviors, not instructions to turn staff UNKNOWN into No. X's B3:B10 narrative questions do not directly feed D20. X's B14 asks about SIMM 5310-C PTA/PIA completion; B19 is a PIA risk level, whereas the descriptive anchors cite SIMM 5305-F Part I. Its A17 text also describes a HIGH/CDT-consultation consequence for No. This is not a new SAR escalation or approval gate.

`RAT SCORECARD!A33` reports: Low <=10; Low Medium 11–15; Medium 16–20; Medium High 21–25; High >26. **26 is unclassified.** Do not change >26 to >=26 without authorization, normalize five bands to three, extrapolate totals, or publish a SAR numeric overall score. A prior workbook score may be quoted only as an attributed historical result with its limitations.

## Preliminary Working Procedure (Non-Numeric)

1. Read supplied documents first, including completed/signed assessments. Extract facts and safeguards; do not restart answered intake. Apply the launcher's privacy warning and untrusted-document boundaries. Assume reported facts accurate for analysis, not independently verified. Credit only safeguards reported as currently implemented, not recommendations.
2. Freeze the review scope, source versions, profile version, and material facts for this report revision. For every factor record applicable, not applicable, or applicability unknown, with a factual basis. Do not infer applicability from organization type or a claimed certification.
3. Compare relevant facts to the **descriptive** anchors, not the worksheet Yes-count formulas. In Section 7 use `LOW — descriptive match`, `MEDIUM — descriptive match`, or `HIGH — descriptive match` only if exactly one complete anchor is supported without a material contradiction or competing match. These are provisional factor bands, not approved numeric values. Record the matched anchor's source cells and supporting facts. Do not output 1/2/3 as assigned SAR scores.
4. If no complete anchor fits, multiple anchors fit, the factor combines inapplicable obligations, or source conflict affects the match, use `UNRESOLVED — anchor ambiguity`, `UNRESOLVED — missing information`, or `APPLICABILITY UNKNOWN` and say why. Do not interpolate, average, invent subweights, choose the worst matching anchor, or count missing documentation as proven absence. N/A is only for an established exclusion, never a substitute for unknown.
5. Keep source-reported worksheet results, prior vendor/reviewer conclusions, and SAR descriptive matches in separate fields. Explain material differences; never copy a signed review's overall LOW into SAR's conclusion. Missing details normally go into assumptions/next actions; only a critical fact that defeats a defensible qualitative conclusion warrants one focused question at a time.
6. Derive scenario likelihood, impact, and the **overall LOW/MODERATE/HIGH** solely using the launcher's existing qualitative matrix and highest defensible material scenario rule. Factor bands inform scenario selection and rationale but are not likelihood, impact, or an aggregation rule. Record the facts supporting both dimensions; an unresolved factor does not automatically prevent a defensible conditional overall conclusion. Never convert Medium to MODERATE numerically. If a critical scenario remains indefensible, use UNRESOLVED.
7. Preserve these inputs, matched cells, nonmatches/conflicts, and scenario rationales in the portable report so another run uses the same basis. Identical documented facts, scope, profile, applicability, anchor-match decisions, and scenario likelihood/impact must yield identical factor bands and matrix/overall outcomes; stylistic wording may vary. A changed result requires an explicit changed fact, rule, or corrected rationale in a new revision, not model discretion disguised as scoring.

Scores 2 and 4 from the original 1–5 proposal are not intermediate SAR scores here. In this workbook 2 means source Medium and 4 is outside the category range; no 1–5 interpolation is introduced. Treatment of numeric N/A, unknowns, weighting, band corrections, formula/anchor precedence, and organization-specific substitutions awaits CISO decision.

### Minimum factor evidence record

Keep one row per factor in Section 7; use Section 4 evidence IDs or Section 8 notes to keep the table compact without dropping information:

| ID/name; applicability and basis | Extracted facts and reported safeguards | Document, actor, version/date, section/page | Preliminary descriptive band; source anchor cells | Rationale, assumptions, missing/conflicting information | Independently verified? |
|---|---|---|---|---|---|
| SRAT-{{I–X}} — {{name}}; {{basis}} | {{reported current facts; evidence IDs}} | {{source or NOT PROVIDED}} | {{band or explicit unresolved/N/A status}} | {{unique match or reason not rateable; note reference}} | NO — submitted facts assumed accurate, not independently verified |

Do not claim verification from a signature, a read document, or an assurance statement. If separately established independent verification is supplied, describe exactly what was verified, by whom, when, scope, and limitations; do not represent that as SAR independently verifying the submission.

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

Source text must actually be read before citing a specific duty. Otherwise label it a potential source to review. Separate law, contractual duty, vendor practice, benchmark, and recommendation. For Regional Centers and Service Providers, use supported federal/privacy sources and NIST safeguard candidates; **do not automatically impose SIMM/DGS** because the DDS workbook mentions them. Retain a State citation only with a supported scope and readable source provision. If X's SIMM-based descriptive anchor cannot be supported for that organization, mark the anchor unresolved and assess the underlying GenAI scenarios qualitatively, without inventing an equivalent certification or requiring a SIMM form.
