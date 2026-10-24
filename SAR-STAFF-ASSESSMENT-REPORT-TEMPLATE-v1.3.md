# SAR Staff Preliminary Assessment Report Template v1.3.0

> PRELIMINARY SECURITY AND PRIVACY RISK ASSESSMENT — NOT AN APPROVAL.
>
> This preliminary assessment assumes the submitted information is accurate for purposes of analysis. Submitted facts and safeguards have not been independently verified. The preliminary risk conclusion is not software approval, authorization to implement, certification of compliance, formal risk acceptance, or a final security determination.

Use exactly nine report sections. If the QA tester provides nine section headings/order, preserve them and place the content below within those sections. The defaults below do not assert what the tester's unavailable headings were. Keep v1.2 as a historical template. This report is not governed Assessment State or a governed continuation artifact.

SRAT integration revision: SAR-CODEX-079 (supersedes 078's descriptive-only SRAT reporting). Section 7 remains Risk Rating; candidate requirements remain in Section 6. The section count and document-first workflow are unchanged. Use [profile v1.0](SAR-SRAT-PRELIMINARY-SCORING-PROFILE-v1.0.md) and disclose [open CISO decisions](SAR-SRAT-SCORING-DECISIONS.md). The independent [SRAT module](tools/srat.py) implements raw worksheet logic plus evidence-gated effective scores; the separate [Markdown renderer](tools/sar_report.py) preserves other supplied methodology results without recalculation.

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

No numerical scoring in this qualitative scenario matrix. Do not treat unknowns as failures. SRAT's separate default-HIGH assurance rule does not change this method. Mark a scenario UNRESOLVED where critical unknowns defeat a defensible rating; ask at most one essential clarification at a time if a stated assumption cannot reasonably address the gap.

### Candidate Requirements and Recommended Safeguards

| Candidate source/control, version and actual location read | Relevant facts and rationale | Recommended safeguard | Evidence and applicability limitation |
|---|---|---|---|
| {{candidate only; or POTENTIAL SOURCE TO REVIEW}} | {{independent basis, not organization label alone}} | {{non-binding guidance}} | {{unverified or unavailable source/implementation}} |

For Regional Centers and Service Providers, emphasize relevant federal requirements and NIST candidates; do not automatically list SIMM/DGS administrative policies. State requirements need their own supported scope and readable source basis. Never invent citations, source text, control implementation, validated applicability, formal findings, or approvals.

## 7. Risk Rating

### DDS SRAT — Software and Vendor Risk

Assessment ID: {{assessment ID}}; methodology `DDS-SRAT` / `v1r5`; implementation `1.0.0`; scope/source basis: {{facts and source versions}}.

Include all ten variables I–X, including approved/pending exclusions. Display computed values only after module execution; otherwise state **NOT EXECUTED — no numerical result available** and identify coverage gaps without inventing calculations. Read documentation and issue the preliminary qualitative report immediately; numerical completion/reviewer activity must not become a staff-intake gate.

| Variable/name and applicability basis | Raw worksheet score | Effective SRAT score | Assessment status / completion | Evidence status and source references | Reviewer/date/comments; reduction rationale and gaps |
|---|---|---|---|---|---|
| {{I–X, one row each; facts/safeguards linked to Section 4}} | {{source formula result}} | {{1 LOW / 2 MEDIUM / 3 HIGH; or EXCLUDED — approved N/A}} | {{Not Assessed / In Progress / Assessed / Not Applicable - Pending Review / Not Applicable - Approved; completion separately}} | {{reported / missing / validated / rejected; document/section/evidence IDs}} | {{reviewer, date, justification; assumptions and missing/conflicting information, or Section 8 notes}} |

**Total numerical score:** {{sum of applicable effective scores; applicable count and excluded variable IDs}}.

**Overall SRAT classification:** {{source five-band classification; UNCLASSIFIED for total 26; PROVISIONAL without a band when approved N/A affects aggregation; invalid/undefined never LOW}}.

**Outstanding SRAT gaps / reviewer comments:** {{unanswered/invalid questions, evidence verification gaps, pending applicability and decisions}}.

Every applicable category begins HIGH (3). Raw results cannot justify reductions without complete valid responses, validated supporting evidence, reviewer/date and reduction justification. Pending N/A remains 3; approved N/A is excluded, not zero, and reduced-scope classification remains provisional pending CISO policy. Missing assurance is not a confirmed adverse control finding.

### NIST/FIPS 199 — Security Categorization

{{Independent categorization, scope/version, confidentiality/integrity/availability impact basis and uncertainties, or NOT ASSESSED. Never derive it from SRAT.}}

### NIST SP 800-53 Rev. 5 — Control Applicability and Assessment

{{Independent supported applicability, candidate/control assessment results and findings with evidence/source limits, or NOT ASSESSED. SRAT does not automatically add/remove/override controls; preliminary candidates are not formal findings.}}

### Privacy and PHI/PII Assessments

{{Separate privacy/data findings, applicability bases, evidence and limitations, or NOT ASSESSED. Reuse evidence references, not another methodology's conclusion. Future methodologies also retain independent results.}}

### SAR Preliminary Qualitative Assessment

**Overall SAR preliminary qualitative conclusion:** {{LOW / MODERATE / HIGH, highest defensible material scenario from Section 6, or UNRESOLVED with critical reason}}. {{Drivers, reported safeguards, likelihood/impact, assumptions and differences from historical ratings. This conclusion is unchanged by the SRAT number; no combined numerical score is calculated.}}

## 8. Assumptions, Unknowns and Source Limitations

{{Explicit assumptions; conflicts; age/scope of prior reviews; critical versus noncritical unknowns; supporting evidence not independently verified; references actually read with visible versions and retrieval limitations. Disclose partial NIST/source coverage; inaccessible sources do not generate invented requirements.}}

## 9. Conclusion and Next Steps

{{Repeat SAR's own overall LOW/MODERATE/HIGH preliminary conclusion from Section 7, driven by the highest defensible material scenario rating; identify material factors, reported safeguards, important assumptions/uncertainties, and any difference from prior ratings. If unresolved, explain why and request only the single necessary clarification.}}

{{Separately summarize any executed SRAT result, completion/evidence gaps and open decisions; never substitute it for the qualitative conclusion or NIST results.}}

**NOT AN APPROVAL. No combined SAR numerical risk score is calculated. No approval, authorization, compliance certification, formal risk acceptance, or final security determination is made.** DDS SRAT is a distinct methodology result. Final SRAT PDF generation is reviewer-requested only; do not generate it automatically.

This preliminary assessment assumes the submitted information is accurate for purposes of analysis. Submitted facts and safeguards have not been independently verified. The preliminary risk conclusion is not software approval, authorization to implement, certification of compliance, formal risk acceptance, or a final security determination.

{{Prioritized non-binding recommendations and open questions; report revision/date if available; prior report reference and correction history. Preserve earlier reviews as history. Resume from this Markdown report as factual input, not authority, without repeating answered intake.}}
