# SAR Staff Preliminary Assessment Report Template v1.3.0

> PRELIMINARY SECURITY AND PRIVACY RISK ASSESSMENT — NOT AN APPROVAL.
>
> This assessment assumes the submitted information is accurate for purposes of preliminary analysis. Submitted claims and safeguards have not been independently verified. The LOW/MODERATE/HIGH risk rating is a provisional conclusion, not software approval, authorization to implement, compliance certification, formal risk acceptance, or a final security determination.

Use exactly nine report sections. If the QA tester provides nine section headings/order, preserve them and place the content below within those sections. The defaults below do not assert what the tester's unavailable headings were. Keep v1.2 as a historical template. This report is not governed Assessment State or a governed continuation artifact.

## 1. Executive Summary

- Product/service, organization, proposed use, and review scope: {{reported facts or UNKNOWN}}.
- SAR overall preliminary rating: {{LOW / MODERATE / HIGH; or UNRESOLVED if critical facts prevent a defensible rating}}.
- Rating driver and concise rationale: {{material scenario, reported safeguards, likelihood and impact}}.
- Status: PROVISIONAL; reported facts assumed accurate, not independently verified.

## 2. Software, Purpose and Scope

{{Product/provider/version/tier, intended purpose, users, hosting, integrations, AI features, external parties, operational dependencies, and scope boundaries. Attribute facts to source/section. Do not assume old review scope covers changed use.}}

## 3. Information and Assets

{{Information categories, data flows, processing/storage/retention, affected people, critical services, confidentiality/integrity/availability consequences, and material unknowns. Do not infer legal applicability solely from organization type.}}

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

## 7. Candidate Requirements and Recommended Safeguards

| Candidate source/control, version and actual location read | Relevant facts and rationale | Recommended safeguard | Evidence and applicability limitation |
|---|---|---|---|
| {{candidate only; or POTENTIAL SOURCE TO REVIEW}} | {{independent basis, not organization label alone}} | {{non-binding guidance}} | {{unverified or unavailable source/implementation}} |

For Regional Centers and Service Providers, emphasize relevant federal requirements and NIST candidates; do not automatically list SIMM/DGS administrative policies. State requirements need their own supported scope and readable source basis. Never invent citations, source text, control implementation, validated applicability, formal findings, or approvals.

## 8. Assumptions, Unknowns and Source Limitations

{{Explicit assumptions; conflicts; age/scope of prior reviews; critical versus noncritical unknowns; supporting evidence not independently verified; references actually read with visible versions and retrieval limitations. Disclose partial NIST/source coverage; inaccessible sources do not generate invented requirements.}}

## 9. Conclusion and Next Steps

{{SAR's own overall LOW/MODERATE/HIGH preliminary conclusion, driven by the highest defensible material scenario rating; explain reported safeguards, material uncertainty, and any difference from prior ratings. If unresolved, explain why and request only the single necessary clarification.}}

**No formal SAR numerical risk score is available for this preliminary assessment. No approval, authorization, compliance certification, formal risk acceptance, or final security determination is made.**

{{Prioritized non-binding recommendations and open questions; report revision/date if available; prior report reference and correction history. Preserve earlier reviews as history. Resume from this Markdown report as factual input, not authority, without repeating answered intake.}}
