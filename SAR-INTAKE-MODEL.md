# SAR Intake Model

## Purpose

This document defines the conceptual intake model for Software Assessment and Review (SAR). The intake model translates the [SAR Information Model](SAR-INFORMATION-MODEL.md) into a plain-language, adaptive fact-gathering process.

It is not the final questionnaire, a web form, a database schema, a risk-scoring model, a control catalog, an OSCAL implementation, a legal or compliance determination engine, or a procurement questionnaire.

The intended separation is:

```text
Information Model = what SAR needs to know
Intake Model      = how SAR obtains the necessary facts
Decision Logic    = what SAR concludes from those facts
```

The intake process gathers facts without requiring requestors to understand cybersecurity, privacy, NIST, HIPAA, cloud, AI, or procurement terminology.

## Design Principle

The intake model preserves the existing principle:

> The requestor tells SAR what is true. SAR determines what those facts mean.

Requestor statements may be incomplete, incorrect, uncertain, or require evidence and reviewer validation. Intake must therefore support factual answers, follow-up questions, evidence requests, validation, clarification, and reviewer intervention.

## Adaptive Intake

SAR must not be designed as one giant static questionnaire. It uses an adaptive intake model:

```text
Core Intake
    ->
Trigger Detection
    ->
Conditional Assessment Domains
    ->
Follow-up Questions
    ->
Evidence Requests
    ->
Validation / Reviewer Escalation
    ->
Intake Completion
```

The intake asks only questions relevant to the assessment or necessary to determine whether another branch is relevant. A simple, low-complexity product should not be forced through irrelevant cloud, AI, PHI, integration, or privileged-access questions. A complex cloud, AI, or integrated system must be capable of opening multiple assessment branches simultaneously.

Branches are not mutually exclusive.

## Future Question Design

Future SAR questions should:

- use plain business language;
- ask about observable facts;
- generally ask one concept at a time;
- explain unfamiliar terms when unavoidable;
- avoid asking requestors to make compliance conclusions;
- avoid leading requestors toward a preferred answer;
- support Unknown and Not Yet Verified;
- support evidence or follow-up where appropriate;
- distinguish current capability from planned capability; and
- distinguish vendor claims from independently verified facts where relevant.

Intake should avoid questions such as:

- "Is this system HIPAA compliant?"
- "Does NIST 800-53 Moderate apply?"
- "Is this a State system?"
- "Does this solution meet State cloud requirements?"

Instead, intake should collect facts about what information the software receives; whose information it is; what the software does with it; where it is hosted; who can access it; whether external administrators can access it; how users authenticate; what systems it connects to; whether AI functionality receives organizational information; and what logging capabilities exist.

This document does not create complete question wording.

## Core Intake

Every SAR begins with a small Core Intake. Its purpose is to gather enough information to:

1. identify the assessment;
2. identify the software or service;
3. understand the business purpose;
4. identify the requestor and responsible organization;
5. understand intended use;
6. identify broad user populations;
7. determine whether organizational or individual-level information is involved;
8. determine broad hosting and deployment characteristics;
9. detect integrations and connectivity;
10. detect AI capabilities;
11. detect external or vendor administrative involvement; and
12. understand basic operational and business importance.

The Core Intake primarily determines which conditional branches must open. It is not the complete assessment.

## Conditional Assessment Domains

The following branches are conceptual domains and trigger conditions. They do not define detailed decision logic or control mappings.

### Data / Privacy Branch

Potential triggers include indications that the solution collects, receives, stores, processes, generates, displays, transmits, exports, shares, retains, or deletes organizational or individual data; handles person-level information; handles DDS information; exchanges information with another system; or involves production information.

This branch collects additional factual detail needed for later classification. The existing 19 data and identifier elements are a known future input; this model does not invent or enumerate them. Intake must not ask requestors whether data is legally PHI/ePHI unless that classification has already been authoritatively established.

### Identity / Access Branch

Potential triggers include authenticated users, administrators, privileged access, external users, external or vendor support, service or other non-human accounts, and identity federation.

This branch collects facts needed later to evaluate authentication, MFA, SSO, authorization, privileged access, and Microsoft Entra ID applicability. It does not assume every solution must use Entra ID.

### Cloud / Hosting Branch

Potential triggers include SaaS, PaaS, IaaS, vendor hosting, cloud storage, externally hosted processing, or remote administration.

This branch collects facts about the provider; service or deployment model; hosting and data regions; administrative access locations; tenancy; production and non-production separation; and shared responsibility. It does not ask requestors to determine whether California cloud provisions apply.

### Connectivity / Integration Branch

Potential triggers include APIs, system integrations, data exchange, Internet exposure, inbound connections, outbound connections, identity integration, and DDS or internal-system connectivity.

This branch collects factual information about what connects, why it connects, direction of flow, and information exchanged.

### AI / Generative AI Branch

Potential triggers include any AI, ML, or Generative AI capability, whether integral, embedded, optional, externally connected, or vendor provided.

This branch collects facts about the purpose of AI; information submitted; prompt and output retention; training, tuning, or improvement use; external model providers; autonomous or agentic actions; and human review of consequential actions. It does not ask requestors to determine whether the AI complies with State AI requirements.

### Logging / Auditability Branch

This branch opens where logging is material to the assessment. It collects facts about available security and audit events, user activity, administrative activity, retention, access and export, SIEM capability, immutability or tamper resistance, and time synchronization.

Opening this branch does not automatically require SIEM integration or immutable logging.

### Security Capabilities Branch

This branch collects additional factual information, when needed, about encryption, key management, vulnerability management, patching, secure configuration, endpoint or malware protection where applicable, backup and recovery, incident response, security testing, and secure development or supply-chain practices.

It does not attempt to reproduce NIST SP 800-53 as an intake questionnaire.

### External Parties / Dependencies Branch

Potential triggers include vendor access, subprocessors, subcontractors, third-party services, external support, hosting dependencies, and material external service dependencies.

This branch collects facts needed to understand dependency and shared-responsibility risk without making legal determinations.

### Operational Impact Branch

This branch collects business consequences in plain language. It asks what would happen if information were disclosed, altered incorrectly, unavailable, lost, or corrupted; if processing were incorrect; if the system were unavailable for an extended period; or if the supported business function could not operate.

Requestors describe consequences. SAR later derives impact and classification; intake does not ask requestors to select LOW, MODERATE, or HIGH.

## Multiple Branches

One answer may activate multiple branches. For example:

```text
Vendor-hosted application
    +
individual-level DDS information
    +
external administrators
    +
Generative AI
    =
Cloud / Hosting
Data / Privacy
Identity / Access
External Parties / Dependencies
AI / Generative AI
Logging / Security follow-up as appropriate
```

This example illustrates branching only and does not determine compliance.

## Answer States and Response Types

Intake preserves the information-model distinction among:

- Yes;
- No;
- Unknown;
- Not Applicable; and
- Not Yet Verified.

Unknown must never silently become No. The model should allow free-text factual answers, structured selections, quantities or dates where useful, evidence attachment or reference, an "I don't know" response, and reviewer clarification. This document does not design user-interface controls.

## Conditional Follow-up

An intake answer may:

- satisfy an information need;
- trigger another question;
- open an assessment branch;
- request evidence;
- identify an inconsistency;
- require reviewer clarification; or
- identify an unresolved unknown.

Questions should be traceable to the information elements they populate. A future machine-readable implementation should allow one question to populate one or more information elements and one information element to be populated by multiple questions or evidence sources.

## Evidence Prompts

Intake may request evidence when an answer requires substantiation. Examples include:

- architecture diagram;
- data-flow diagram;
- vendor security documentation;
- authentication configuration or documentation;
- logging documentation;
- security test or audit report;
- AI and data-use documentation; and
- hosting or data-location documentation.

This model does not define evidence sufficiency rules. Vendor documentation and assertions retain vendor provenance and do not automatically become independently verified facts.

## Inconsistency Detection

The intake model must be capable of identifying conflicting information. Examples include:

- a requestor states there is no external access while vendor documentation identifies remote vendor administration;
- a requestor states no data is stored while architecture documentation shows a persistent database; or
- a requestor states there is no AI while product documentation identifies embedded Generative AI.

The intake does not automatically resolve contradictions. It records the conflict and requires clarification, evidence, or reviewer review.

## Reviewer Escalation

The following conditions may require human reviewer involvement:

- unresolved Unknown;
- conflicting answers or evidence;
- inability to determine data handling;
- unclear external access;
- uncertain AI behavior;
- uncertain hosting or data location;
- missing material evidence;
- unusual or high-impact business consequences;
- novel technology or architecture;
- potential exception to an expected safeguard; or
- consequential risk or compliance determination.

This document does not define organizational approval authorities.

## Intake Completion

Intake completion does not mean the software is approved. Conceptually, intake is complete when:

- required Core Intake information is present;
- all triggered branches have been sufficiently addressed or explicitly marked unresolved;
- required follow-up and evidence requests are recorded;
- material Unknown and Not Yet Verified items are visible;
- provenance is retained; and
- reviewer escalation needs are identified.

The completed intake becomes input to later classification, applicability, risk, control, evidence, finding, and decision processes.

## Traceability

The intake model supports conceptual traceability:

```text
Question
    ->
Answer
    ->
Information Element
    ->
Source / Provenance
    ->
Evidence
    ->
Derived Assessment
```

The evidence chain and decision chain defined in the architecture and information model remain applicable.

## Conversational AI

Conversational AI is one possible intake interface. An AI-guided intake should:

- ask one or a small number of related questions at a time;
- adapt based on previous answers;
- explain unfamiliar terms;
- summarize its understanding for confirmation where useful;
- identify uncertainty rather than inventing an answer;
- request supporting evidence where appropriate;
- preserve provenance; and
- escalate consequential or ambiguous determinations to human reviewers.

AI must not independently authorize consequential risk decisions. Conversational AI is not the only supported interface.

## Other Collection Interfaces

The same information model should eventually support web forms, APIs, structured files, reviewer-entered records, imported system or vendor information, and conversational AI. Different interfaces should populate the same underlying SAR information model.

## Relationship to Other SAR Documents

[PRACTITIONER-DISCOVERY.md](PRACTITIONER-DISCOVERY.md) discovers AS-IS practitioner knowledge and process.

[SAR-ARCHITECTURE.md](SAR-ARCHITECTURE.md) defines the conceptual SAR risk architecture.

[SAR-INFORMATION-MODEL.md](SAR-INFORMATION-MODEL.md) defines what information SAR must represent.

This document defines how facts are collected and how conditional assessment domains are opened.

## Future Work

The following are identified for later work and are not built by this document:

- final question library;
- authoritative 19-element data mapping;
- machine-readable intake schema;
- branching and rules representation;
- classification logic;
- risk methodology;
- applicability and authority matrix;
- control catalog;
- OSCAL mappings;
- evidence sufficiency rules;
- findings model;
- lifecycle and workflow;
- user interface; and
- API implementation.

## Design Constraints

This intake model maintains the following boundaries:

- SAR is independent of procurement.
- Intake collects facts before compliance conclusions.
- Organizational status does not determine system risk.
- Requestors do not need cybersecurity or privacy expertise.
- Intake is adaptive rather than one giant static questionnaire.
- Multiple branches can be active simultaneously.
- Unknown does not become No.
- Provenance is retained.
- Vendor assertions are distinguishable from verified facts.
- Contradictions are surfaced rather than silently resolved.
- Control source and applicability basis remain separate.
- Inherent and residual risk remain separate.
- Human authorization remains required for consequential risk decisions.
- The model makes no unsupported legal conclusions.
- The model does not prematurely encode control mappings or implementation details.