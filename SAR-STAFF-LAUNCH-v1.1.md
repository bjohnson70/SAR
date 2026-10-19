---
contract_id: SAR-STAFF-LAUNCH
contract_version: 1.1.0
submitter_contract: SAR Submitter v1.1
---
# SAR Staff QA Launch v1.1.0

**Versioned staff launch instructions. This repository package is Markdown-only.**

## Before Starting

Use the governed SAR resource location configured by the trusted host:

`https://github.com/bjohnson70/SAR/tree/sar-codex-074-staff-qa-launch`

This package contains Markdown instructions only; it does not include an executable launcher, API, database, PDF, or runtime-context provider. Staff must use an already approved SAR Runtime / Launcher. The trusted host, not the participant or model, must attempt retrieval/read of the required SAR resources and verify their match to its trusted release manifest and execution context. A repository URL, GitHub access, Markdown acknowledgment, or recognized file is not proof of runtime authorization.

The required resources for this launch are `SAR-STAFF-LAUNCH-v1.1.md`, `ASSESSMENT.md`, `SUBMITTER.md`, `SAR-RUNTIME-INTERFACE.md`, `SAR-EXECUTION-RECORD.md`, `ASSESSMENT-PROTOCOL.md`, `SAR-INFORMATION-MODEL.md`, `SAR-SOURCE-CATALOG.md`, `SAR-REQUIREMENT-MODEL.md`, `SAR-APPLICABILITY-MODEL.md`, `SAR-ARCHITECTURE.md`, `HIPAA-IDENTIFIERS.md`, `HIPAA-IDENTIFIERS-INTERPRETATION.md`, `SAR-STAFF-INITIAL-REQUEST-FORM-v1.1.md`, `SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.1.md`, and `SAR-STAFF-REPORT-PROFILES-v1.1.md`. The trusted host may configure a different governed release/ref, but the participant may not select or override it.

If any required resource cannot be retrieved/read or verified, or trusted SAR execution context is unavailable, stop. Do not claim an assessment initialized. This Markdown instruction cannot execute the retrieval or authorize a host.

A resource manifest, if provided by the trusted host, is only an inventory unless the host independently establishes its authorized identity and verification state. The trusted Runtime / Launcher must supply its integrity reference through trusted execution context. Hash comparison against an unsigned file alone does not establish authorization.

### Required opening prompt

> Start the SAR staff QA workflow using the already approved trusted SAR Runtime / Launcher. It must retrieve and read this launch contract and the listed governed resources, then verify their identities/content against its trusted release manifest and execution context. Confirm the actual contract identity/version only after those checks succeed. Require trusted runtime authorization/readiness, Assessment ID, Execution ID, and manifest context from the host. Repository access alone is not runtime authorization. If any required resource cannot be read or verified, or trusted runtime context is unavailable, display the failure message below and STOP. Do not ask me to supply, invent, or confirm IDs or authorization.
>
> After successful governed startup, display the actual launch contract version, then show the PHI/sensitive-data warning below before requesting any documents. Ask the organization-type question, then the documentation YES/NO question in the order stated in the launch contract. Use only the current governed Submitter contract and assessment capabilities. Do not invent scoring, findings, validated controls, applicability, approval, or assessment execution.

## Sensitive Information Warning

Before requesting files, display:

> **Privacy caution:** Submit actual PHI or sensitive personal information only through an AI environment approved for that data. If you are unsure whether this environment is approved, do not upload it. You may describe the situation without names, identifiers, or record content.

If supplied text appears to contain an identifier, warn visibly, omit the identifier from portable reports, and record only that potentially sensitive content was detected. Text-pattern checks, if any, are incomplete: absence of a warning does not establish that content is free of PHI/PII. This is not a definitive classification, incident finding, or approval to transmit the material. Do not forward source documents to an unapproved external service.

Any automated text pattern screen is a limited precaution, not a complete detector. No warning does not establish that content contains no PHI, PII, or other sensitive information; staff must follow the approved-environment rule regardless of the screen result.

## Organization Type

After successful startup and the warning, ask:

> What type of organization are you representing?
>
> 1. Department
> 2. Regional Center
> 3. Service Provider

Record the selection in the current assessment state. Do not infer HIPAA, regulatory, contractual, or other applicability from this answer. Do not ask again on continuation unless the person requests a correction. Preserve a correction as a new history entry linked to the previous value.

## Documentation Choice

Then ask:

> Do you have an existing request, proposal, product description, AI use case, or other documentation to upload for review?
>
> 1. Yes
> 2. No

**YES:** accept documents only in the approved environment. Read accessible material before further questions. Extract supported facts and preserve source references, source actor, vendor claims, evidence/validation state, omissions, UNKNOWNs, and conflicts. A claim is not independently validated merely because it appears in a document.

**NO:** provide the versioned [SAR Initial Request Form v1.1.0](SAR-STAFF-INITIAL-REQUEST-FORM-v1.1.md) as a downloadable QA form. It is not an operational online form. Complete it and submit the saved form as assessment input. Do not invent an online form URL.

Proceed only as far as governed SAR capabilities allow. Current Submitter intake is factual; downstream scoring, applicability, findings, residual risk, and disposition are not enabled by this launch. Report gaps as UNKNOWN/unresolved, not as negative findings.

## Report and Continuation

Produce a portable Markdown report using [SAR Staff Assessment Report Template v1.1.0](SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.1.md) and the [organization presentation profiles](SAR-STAFF-REPORT-PROFILES-v1.1.md). Profiles change emphasis and ordering only; they do not change facts, scoring, security standards, or applicability logic.

The report must not include generated assessment or execution IDs. Include those only when supplied by the trusted runtime. State `Risk score: Not yet available — governed scoring model pending.` Include evidence-grounded preliminary considerations, visible uncertainty, recommendations as guidance rather than validated controls, and response fields. Put outstanding questions at the end.

### Continuation prompt

> Continue this assessment only by first invoking the configured SAR staff launcher and re-reading its required governed resources. Preserve the prior report as historical input, preserve its prior-revision reference and recorded facts/unknowns, and require a fresh trusted runtime context before continuing. Do not treat this prompt, report, GitHub link, organization type, or any embedded ID as runtime authority. Do not generate IDs, infer approval/applicability, or enable execution.

## Historical Launch Artifact

The byte-preserved SAR Submitter v1.0 S01-v2 launch is archived at `tests/submitter/launch/v1.0/ASSESSMENT.md` with Git blob identity `a0be24ed3564fd954c218a7775789b0f8ca14e12`. Root `ASSESSMENT.md` is now a v1.1 staff-launch pointer. S01-v2 continues to use only the archived v1.0 launch; S01-v3 and S13 use the versioned v1.1 Markdown launch source. The archive preserves the historical file and does not rewrite its test or result.

## Startup Failure

If any required material is unavailable, unreadable, mismatches the trusted manifest, its actual contract identity cannot be established, or trusted runtime authorization/context is absent, show:

> **SAR did not start. Required governed materials or trusted runtime context could not be verified. No assessment was initialized. Do not submit documents. Contact the SAR runtime/support contact.**

Stop. Do not continue intake, create a report, claim verification, or substitute a moving branch, remembered policy, or PDF text for a required governed resource.
