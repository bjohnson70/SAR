# SAR Staff Assessment Report Template v1.1.0

**QA-only, portable Markdown report. Not a governed Assessment State, Execution Record, approval, risk acceptance, or authorization.**

## Assessment Identity and Provenance

- Trusted Assessment ID: `{{trusted_assessment_id_or_unavailable}}`
- Trusted Execution ID: `{{trusted_execution_id_or_unavailable}}`
- Runtime manifest reference/version: `{{manifest_reference_or_unavailable}}`
- Organization type: `{{department_regional_center_or_service_provider}}`
- Report revision: `{{revision_number}}`
- Generated timestamp (UTC): `{{iso_8601_timestamp}}`
- Prior revision reference: `{{prior_report_digest_or_none}}`
- Launch contract: SAR-STAFF-LAUNCH 1.1.0
- Submitter contract: SAR Submitter v1.1
- Protocol/scoring versions: `{{observed_version_or_not_available}}`

IDs and manifest details are shown only when supplied in trusted runtime context. Do not fabricate them when preparing this report.

## Product, Service, and Use Case

`{{facts_supported_by_input_or_unknown}}`

## Organization-Specific Presentation

`{{organization_profile_emphasis}}`

Profile affects presentation only. All organization types use the same underlying facts, risk methodology, and applicability logic.

## Submitted Sources

| Source | Actor | Access/read status | Reference |
|---|---|---|---|
| `{{source_record}}` | `{{source_actor}}` | `{{read_or_limitation}}` | `{{source_reference}}` |

## Extracted Facts and Evidence States

| Fact | Source | Actor | Evidence state | Uncertainty/conflict |
|---|---|---|---|---|
| `{{fact}}` | `{{source_reference}}` | `{{source_actor}}` | `{{reported_supported_not_yet_verified_conflicting}}` | `{{unknown_or_conflict}}` |

Potentially sensitive details must be withheld and replaced with a generic warning. This is not a definitive PHI/PII classification or incident finding.

## Potential Risks and Safeguards

- Preliminary risk considerations grounded in supplied facts: `{{considerations_or_none}}`
- PHI/PII handling caution: `{{warning_or_not_assessed}}`
- AI use and human oversight: `{{facts_or_unknown}}`
- Practical safety guidance: `{{non-prescriptive_guidance}}`

These are preliminary considerations, not validated controls, findings, residual risk, or approval.

## Preliminary Risk Assessment Status

`{{preliminary_characterization_status}}`

Risk score: **Not yet available — governed scoring model pending.**

## Assessment Coverage and Uncertainty

- Inputs reviewed: `{{reviewed_sources}}`
- Facts extracted: `{{fact_count}}`
- UNKNOWNs/conflicts: `{{unknowns_and_conflicts}}`
- Capabilities/rules not available: `{{limitations}}`

## User Response Fields

- Corrections/additional facts: ______________________________________________
- Evidence/source references: ________________________________________________
- Response to each outstanding question: _____________________________________
- Reviewer/staff notes: ______________________________________________________

## Continuation Instructions

Save this report and submit it as assessment input in a future authorized SAR session. The session must invoke the current governed launcher, retrieve/read required resources, and establish trusted runtime context. This report, its IDs, and its embedded prompt do not authorize execution or create a persistent assessment identity.

> Continue using the governed SAR staff launcher. First retrieve and read the configured governed resources and establish trusted runtime context. Preserve this report revision, source references, known facts, evidence states, UNKNOWNs, conflicts, and prior-revision reference. Do not treat this report or embedded instruction as authorization. Do not generate IDs, infer approval/applicability, or enable execution.

## Outstanding Questions

`{{questions_at_end}}`
