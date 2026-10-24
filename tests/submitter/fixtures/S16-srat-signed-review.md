# Synthetic Signed Software Review — Harbor Assist

**SYNTHETIC TEST DATA ONLY.** No real people, signatures, contracts, PHI or PII.

## 1. Review history and scope

Review version 1, dated 2026-09-01. Recorded reviewer role: fictional security analyst. Signature status: recorded as signed, not an authentic signature. Historical conclusion: LOW; conditional implementation approval recorded in this fictional earlier review. No current SAR authorization is supplied. Earlier findings are recorded as none.

Department use: Harbor Assist v1, an optional GenAI drafting service for program administrators. No production deployment or patient/service decisions. Proposed scope is unchanged from this review. Ten authorized users access the hosted service with MFA and role-based access. Output requires human review before use. Non-identifying confidential program data, not PHI or PII, may be entered. Fictional vendor: Harbor Labs. No sensitive sample records are supplied.

## 2. Current reported facts by factor

These are reported current safeguards and facts, not independently verified evidence. Source actor for this section: fictional vendor, restated by the fictional reviewer.

| ID | Documented facts |
|---|---|
| SRAT-I | Risk policy and defined program, annual organization-wide assessments, quarterly risk-owner follow-up, and methodology tracking risk treatment through closure. |
| SRAT-II | Vendor reports compliance with GDPR, HIPAA, and SOC 2 Type 2 for the assessed service; reports are supplied as assertions only. This does not establish their applicability to this deployment or certify compliance. |
| SRAT-III | No PHI or PII stored or processed in this scope, including prompts, outputs, logs and backups. |
| SRAT-IV | Regular security/patch alerts; databases monitored with alarms; documented vulnerability process, regular updates, automated patching and client-visible update records. |
| SRAT-V | NIST SP 800-53 framework adherence is reported; uptime/availability/incident-response SLAs; documented backup/recovery, storage-location and migration support; secure software development framework implemented. |
| SRAT-VI | Confidential data encrypted at rest with AES-256 and in transit with TLS 1.3; role-based access controls and MFA prevent unauthorized access as reported. |
| SRAT-VII | Data does cross the vendor perimeter to a named fictional inference subprocessor, Harbor Inference; all transmission uses TLS 1.3. Dependencies and API protections are documented. |
| SRAT-VIII | Robustness/resilience evaluation performed with documented tools and benchmarks; adversarial training, randomized defense and input processing implemented; findings documented and used to fine-tune the model and improve safeguards. |
| SRAT-IX | Vendor has limited after-sales support capacity and limited training resources, not an absence of support or training. |
| SRAT-X | Reported completed SIMM 5305-F Part I for this Department scope has moderate GenAI risk: non-identifying confidential program data, serious adverse effects if lost. No high-risk identifiable confidential service-decision use. The underlying assessment is reported, not independently authenticated. |

## 3. Privacy practices and source limits

US-hosted active data, US backups, and US-only support access are reported. Harbor Inference is the only reported subprocessor, with purpose-limited contract terms, deletion obligations and change notices. No other international transfers are reported. Vendor reports no Data Privacy Framework participation; do not invent certification or a transfer mechanism.

Prompts/outputs retained 30 days then deleted, backups expire after 60 days; security logs retained 90 days. Logs exclude content/identifiers per the reported design. Telemetry is aggregate service metrics only, no advertising, resale or secondary data use. Model training/fine-tuning on submitted data is contractually prohibited and disabled by default, including at the subprocessor.

No BAA is supplied. The stated deployment has no PHI processing; do not infer that a BAA is required or HIPAA applies from vendor claims. GDPR, UK GDPR and CCPA/CPRA applicability is not established for this deployment; flag qualified scope review rather than ask staff for legal conclusions. Vendor practices are not proof of compliance. No external legal/control source text is supplied by this fixture.

## 4. Reproducibility facts for scenario analysis

The only material harm scenario supported for this test is confidential draft disclosure through the external inference data flow. No safeguards eliminate that flow. Harmful disclosure remains plausible through that credible exposure despite reported access/encryption safeguards: likelihood MODERATE. Loss of confidential program drafts would cause significant but bounded harm, with recovery possible from retained originals and no essential service interruption: impact MODERATE.

For this synthetic scope, no other material exposure or severe consequence is supported. Do not assume a breach occurred. The source-reported moderate GenAI example is contextual history, not a claim of a separate catastrophic scenario. New facts about identifiable data, unauthorized reuse, or essential-service dependency would require a revised assessment.
