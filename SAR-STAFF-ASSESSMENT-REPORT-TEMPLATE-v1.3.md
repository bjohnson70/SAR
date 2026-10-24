# SAR Staff Preliminary Assessment Report Template v1.3.0

> PRELIMINARY SECURITY AND PRIVACY RISK ASSESSMENT — NOT AN APPROVAL.
>
> This preliminary assessment assumes the submitted information is accurate for purposes of analysis. Submitted facts and safeguards have not been independently verified. The preliminary risk conclusion is not software approval, authorization to implement, certification of compliance, formal risk acceptance, or a final security determination.

Use exactly nine report sections. If the QA tester provides nine section headings/order, preserve them and place the content below within those sections. The defaults below do not assert what the tester's unavailable headings were. Keep v1.2 as a historical template. This report is not governed Assessment State or a governed continuation artifact.

SRAT integration revision: SAR-CODEX-078-SRAT-02. Section 7 is now Risk Rating; its previous candidate-requirements content remains in Section 6. The section count and document-first workflow are unchanged. Use [profile v1.0](SAR-SRAT-PRELIMINARY-SCORING-PROFILE-v1.0.md) and disclose [pending CISO decisions](SAR-SRAT-SCORING-DECISIONS.md); no CISO-approved numeric scheme is available.

## 1. Executive Summary

- Product/service, organization, proposed use, and review scope: {{reported facts or UNKNOWN}}.
- SAR overall preliminary rating: {{LOW / MODERATE / HIGH; or UNRESOLVED if critical facts prevent a defensible rating}}.
- Rating driver and concise rationale: {{material scenario, reported safeguards, likelihood and impact}}.
- Status: PROVISIONAL; reported facts assumed accurate, not independently verified.

## 2. Software, Purpose and Scope

{{Product/provider/version/tier, intended purpose, users, hosting, integrations, AI features, external parties, operational dependencies, and scope boundaries. Attribute facts to source/section. Do not assume old review scope covers changed use.}}

## 3. Information and Assets

{{Information categories, data flows, processing/storage/retention/deletion, affected people, critical services, confidentiality/integrity/availability consequences, and material unknowns. Examine residency/transfers, subprocessors, telemetry/secondary uses and AI training/reuse where relevant. Consider HIPAA/HITECH/BAA, GDPR, UK GDPR, CCPA/CPRA and Data Privacy Framework participation using supported scope and reported vendor practices, not blanket applicability or assumed compliance.}}

## 4. Submitted Facts and Reported Safeguards

| Fact or safeguard | Source, actor and location | Status | Preliminary assumption and limitation |
|---|---|---|---|
| {{reported item}} | {{document/section or requester/vendor}} | REPORTED — NOT INDEPENDENTLY VERIFIED | {{assume accurate for this analysis; scope/conflict/unknown}} |

Separate supporting material from assertions. Credit reported implemented safeguards in the preliminary scenario analysis; do not describe them as validated. Planned recommendations do not reduce current risk. Missing evidence is not a confirmed deficiency.

## 5. Prior Assessment and Approval History

| Prior review and scope | Date/version | Attributed findings, safeguards and rating | Documented signature/approval status and conditions | Limitations |
|---|---|---|---|---|
| {{document/author or reviewer role/source section}} | {{observed date/version or NOT AVAILABLE}} | {{prior results, attributed as historical}} | {{reported status, date, conditions, signer role if stated}} | {{authenticity, authority, currency and applicability not independently verified}} |

Recognize completed, signed, approved, and partial reviews without asking the user to classify them. Preserve prior findings and recorded resolutions; do not turn them into current SAR findings. A prior signature/approval is not current SAR authorization. Do not reproduce unnecessary personal identifiers. If none is supplied, say NOT PROVIDED rather than invent history.

## 6. Preliminary Risk Analysis

Use the qualitative rubric in [SAR-STAFF-START.md](SAR-STAFF-START.md). It follows NIST SP 800-30's assessment concepts but is a SAR preliminary three-level convention, not a NIST-mandated matrix. Do not claim source text was read when inaccessible.

| Asset and threat scenario | Reported facts, vulnerability/exposure | Reported safeguards considered | Likelihood LOW/MODERATE/HIGH and why | Impact LOW/MODERATE/HIGH and why | Preliminary risk LOW/MODERATE/HIGH and rationale |
|---|---|---|---|---|---|
| {{scenario, not asserted occurrence}} | {{source and plausible exposure}} | {{implemented as reported, not verified}} | {{after reported safeguards}} | {{people/data/service harm}} | {{matrix outcome, assumptions and limits}} |

| Likelihood / Impact | LOW | MODERATE | HIGH |
|---|---|---|---|
| LOW | LOW | LOW | MODERATE |
| MODERATE | LOW | MODERATE | HIGH |
| HIGH | MODERATE | HIGH | HIGH |

No numerical scoring. Do not treat unknowns as failures. Mark a scenario UNRESOLVED where critical unknowns defeat a defensible rating; ask at most one essential clarification at a time if a stated assumption cannot reasonably address the gap.

### Candidate Requirements and Recommended Safeguards

| Candidate source/control, version and actual location read | Relevant facts and rationale | Recommended safeguard | Evidence and applicability limitation |
|---|---|---|---|
| {{candidate only; or POTENTIAL SOURCE TO REVIEW}} | {{independent basis, not organization label alone}} | {{non-binding guidance}} | {{unverified or unavailable source/implementation}} |

For Regional Centers and Service Providers, emphasize relevant federal requirements and NIST candidates; do not automatically list SIMM/DGS administrative policies. State requirements need their own supported scope and readable source basis. Never invent citations, source text, control implementation, validated applicability, formal findings, or approvals.

## 7. Risk Rating

Use the [SRAT profile's nonnumeric working procedure](SAR-SRAT-PRELIMINARY-SCORING-PROFILE-v1.0.md). State profile version, assessment scope and source basis. Include all ten factor IDs/names, including reasoned N/A or unresolved rows; X is conditional on GenAI use. A descriptive factor match is not a numeric assignment, a verified control, or the overall SAR rating. Do not substitute a prior review's rating.

| Factor ID/name; applicability and basis | Extracted facts and reported safeguards | Document/actor/version/date/section or evidence reference | Preliminary descriptive band and source anchor cells | Rationale, assumptions and missing/conflicting information | Independently verified? |
|---|---|---|---|---|---|
| {{SRAT-I through SRAT-X; one row each}} | {{reported current facts/safeguards; Section 4 evidence IDs if needed}} | {{source/section, or NOT PROVIDED}} | {{LOW / MEDIUM / HIGH — descriptive match; UNRESOLVED with reason; NOT APPLICABLE; APPLICABILITY UNKNOWN}} | {{unique supported anchor match, or explicit ambiguity/gap; Section 8 note if needed}} | NO — reported, not independently verified |

Keep the table compact by cross-referencing Sections 4 and 8 without omitting evidence fields. Use UNRESOLVED for partial/competing descriptive matches; no interpolation or worst-match default. If the profile is unavailable, disclose that and leave factor bands unresolved rather than inventing anchors. N/A and unknowns have no numeric value. Do not calculate totals, apply workbook defaults, or silently fix thresholds.

**Overall SAR preliminary qualitative conclusion:** {{LOW / MODERATE / HIGH, highest defensible material scenario from Section 6, or UNRESOLVED with critical reason}}. {{Identify driving scenarios, reported safeguards, likelihood/impact basis, material uncertainties and any difference from attributed historical ratings. Factor bands do not replace or numerically aggregate into this conclusion.}}

## 8. Assumptions, Unknowns and Source Limitations

{{Explicit assumptions; conflicts; age/scope of prior reviews; critical versus noncritical unknowns; supporting evidence not independently verified; references actually read with visible versions and retrieval limitations. Disclose partial NIST/source coverage; inaccessible sources do not generate invented requirements.}}

## 9. Conclusion and Next Steps

{{Repeat SAR's own overall LOW/MODERATE/HIGH preliminary conclusion from Section 7, driven by the highest defensible material scenario rating; identify material factors, reported safeguards, important assumptions/uncertainties, and any difference from prior ratings. If unresolved, explain why and request only the single necessary clarification.}}

**NOT AN APPROVAL. No formal SAR numerical risk score is available for this preliminary assessment. No approval, authorization, compliance certification, formal risk acceptance, or final security determination is made.** Source-reported workbook rules are not adopted scoring; numeric use remains pending CISO authorization.

This preliminary assessment assumes the submitted information is accurate for purposes of analysis. Submitted facts and safeguards have not been independently verified. The preliminary risk conclusion is not software approval, authorization to implement, certification of compliance, formal risk acceptance, or a final security determination.

{{Prioritized non-binding recommendations and open questions; report revision/date if available; prior report reference and correction history. Preserve earlier reviews as history. Resume from this Markdown report as factual input, not authority, without repeating answered intake.}}
