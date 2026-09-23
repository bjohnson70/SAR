# SAR Information Model

## Purpose

This document defines the conceptual information model needed to support a Software Assessment and Review (SAR) assessment. It defines information that the future SAR process must be capable of representing; it does not define a questionnaire, user interface, risk-scoring model, control catalog, OSCAL implementation, workflow implementation, database schema, or storage design.

The model separates four kinds of information:

1. **Facts:** information supplied or evidenced about the software, service, environment, data, users, business use, and implementation.
2. **Derived assessment information:** information determined by SAR reviewers and/or approved decision logic from facts and evidence.
3. **Evidence:** artifacts or authoritative information used to substantiate facts, controls, findings, and decisions.
4. **Decisions:** authorized conclusions concerning findings, conditions, remediation, residual risk, and final disposition.

The guiding principle is:

> The requestor tells SAR what is true. SAR determines what those facts mean.

This principle does not make requestor statements conclusive. Independent verification, reviewer-developed facts, and supporting evidence may be needed to validate, refine, or contradict a statement.

## Core SAR Record

Every SAR assessment must be capable of representation as one logical SAR record identified by its SAR GUID. The record correlates the assessment's information over its lifecycle without prescribing a database or implementation structure.

```text
SAR Identity
    ->
Request / Assessment Context
    ->
Software / Function
    ->
Data
    ->
Users & Identity
    ->
Environment / Hosting
    ->
Connectivity & Integrations
    ->
External Parties / Dependencies
    ->
AI Capabilities
    ->
Logging / Auditability
    ->
Security Capabilities
    ->
Operational Impact
    ->
Evidence
    ->
Derived Classification
    ->
Inherent Risk
    ->
Applicable Controls
    ->
Findings / Gaps
    ->
Risk Treatment
    ->
Residual Risk
    ->
Risk Decision
    ->
Lifecycle History
```

The sequence expresses conceptual dependency and traceability. It does not prescribe a linear workflow: information may be updated, verified, or reconsidered as evidence becomes available.

## Facts

Facts are assertions about an assessment subject or its context. They may be supplied by requestors, practitioners, vendors, systems, reviewers, or evidence. Facts should be recorded separately from compliance conclusions so a reasonable business requestor can provide useful information without cybersecurity, privacy, legal, or compliance expertise.

### SAR Identity

This domain identifies and situates the assessment. It includes concepts such as:

- SAR GUID;
- assessment title;
- assessment status;
- creation date;
- relevant organizational and business context; and
- responsible and requesting parties.

This model does not define GUID generation or lifecycle states.

### Request / Assessment Context

This domain records why an assessment exists without making procurement the center of SAR. Potential triggers include:

- proposed new software;
- cloud or SaaS service;
- software renewal;
- major version or other material change;
- new integration;
- new use of existing software;
- AI capability;
- discovery of software already in use;
- material data-use change;
- security or privacy concern; or
- another trigger.

Procurement or acquisition may be a trigger, but it does not determine the technology's risk.

### Software / Function

This domain describes the technology and its use. Facts may include:

- product or service identity;
- vendor or provider;
- business purpose;
- capabilities;
- intended use;
- user population;
- administrative functions;
- deployment or use scope; and
- whether the software is commercial, custom, open source, internally developed, hosted, managed, or another form.

This information supports assessment of the technology's function and context; it is not a procurement inventory.

### Data

Data is a major information domain. The record must represent factual information about data that the solution collects, receives, stores, processes, generates, displays, transmits, exports, shares, deletes, or retains.

Relevant facts include:

- whose information it is;
- source and destination;
- approximate volume or scope where relevant;
- retention;
- data flow; and
- whether the data is production, test, or synthetic data.

The existing 19 data and identifier elements concept is a known design input that requires later authoritative definition and mapping. This document does not invent or enumerate those elements.

The model must allow later SAR logic to determine whether information may constitute PHI/ePHI, PII or personal information, confidential or non-public information, State or DDS information, or other regulated or sensitive information. Such classifications are derived unless already established by an authoritative source.

### Users & Identity

This domain represents facts about access and identity, including:

- user populations;
- internal and external users;
- administrators and other privileged users;
- authentication method;
- MFA capability and use;
- SSO capability;
- SAML, OIDC, or other federation capability;
- Microsoft Entra ID integration where relevant;
- service and other non-human accounts; and
- authorization and role model.

The presence of these fields does not state that every solution must use Entra ID, SSO, or any particular identity approach.

### Environment / Hosting

This domain captures the operating and hosting context, including:

- on-premises, cloud, hybrid, vendor-hosted, or other deployment model;
- SaaS, PaaS, or IaaS where relevant;
- hosting provider;
- regions and data locations;
- administrative access locations;
- production and non-production separation;
- endpoints or infrastructure involved; and
- tenancy model where relevant.

These facts support later determination of cloud, hosting, and data-location requirements.

### Connectivity & Integrations

This domain describes how the technology connects and exchanges information. It includes:

- network connectivity;
- Internet exposure;
- APIs;
- system-to-system integrations;
- inbound and outbound data exchanges;
- identity integrations;
- DDS or organizational systems touched;
- external connections; and
- protocols or interfaces where relevant.

### External Parties & Dependencies

This domain represents material relationships and dependencies, including:

- vendor or service provider;
- subcontractors and subprocessors where known;
- third-party services;
- hosting dependencies;
- support and administrative access;
- shared-responsibility relationships; and
- material software or service dependencies.

These facts do not themselves make legal determinations about a party or relationship.

### AI / Generative AI

This domain captures factual AI capabilities, including:

- whether AI, machine learning, or Generative AI is present;
- whether AI is integral, optional, embedded, or externally connected;
- data submitted to AI functionality;
- whether prompts or outputs are retained;
- whether organizational data may be used for training, tuning, improvement, or model development;
- external model or service providers;
- autonomous or agentic actions where applicable; and
- human review of consequential outputs or actions.

This domain captures facts and does not determine compliance.

### Logging / Auditability

This domain captures available auditability capabilities, including:

- security and audit logs available;
- events recorded;
- administrator activity;
- user activity where relevant;
- retention;
- access to logs;
- export or API capability;
- SIEM integration capability;
- immutability or tamper resistance where relevant; and
- time synchronization where relevant.

Immutable audit records and SIEM integration are known SAR design inputs, not universal requirements merely because they appear in this model.

### Security Capabilities

This domain captures factual capabilities for later control determination, including where relevant:

- encryption in transit;
- encryption at rest;
- key management;
- vulnerability management;
- patching;
- malware or endpoint protection;
- secure configuration;
- backup and recovery;
- incident response capability;
- security testing; and
- secure development and supply-chain information.

This is not a complete security questionnaire.

### Operational / Business Impact

This domain records business consequences that may result from:

- loss of confidentiality;
- loss of integrity;
- loss of availability;
- extended outage;
- incorrect processing;
- loss or corruption of information;
- unauthorized disclosure; or
- inability to perform the supported business function.

Requestors should describe consequences in business terms rather than selecting a NIST impact level themselves.

## Evidence

Evidence is separately identifiable information or an artifact that can support or contradict assessment facts and control assertions. Examples may include:

- architecture or data-flow documentation;
- security documentation;
- configurations;
- screenshots or exports;
- attestations or certifications;
- audit reports;
- test results;
- policies and procedures;
- contracts or agreements where relevant to applicability;
- vendor documentation; and
- reviewer observations.

Each evidence item should eventually be capable of correlation to the SAR GUID and to the fact, control, finding, or decision it supports. This document does not define evidence storage, retention, or access implementation.

## Derived SAR Information

Derived assessment information is determined by SAR reviewers and/or approved decision logic from facts and evidence. It must remain distinguishable from the underlying factual record and its provenance.

### Data Classification

Data classification is the derived characterization of data and applicable sensitivity or regulatory categories.

### Impact / System Classification

Impact or system classification is the derived classification appropriate to the assessment. This model does not define LOW, MODERATE, or HIGH calculation rules.

### Inherent Risk

Inherent risk is the risk presented by the software, its function, data, environment, connectivity, dependencies, and use before considering the effectiveness of safeguards or mitigating controls.

### Applicability / Authority

For each applicable requirement or control, the record must preserve both concepts below:

- **Control source:** the framework, law, regulation, policy, contractual provision, standard, guidance, or other source from which a control or safeguard is derived.
- **Applicability basis:** why that control applies to the particular system, data, relationship, or environment.

Control source and applicability basis are separate information elements. A source alone does not explain why a control applies to a specific assessment, and an applicability basis does not replace the authority or source from which a safeguard is derived.

### Applicable Controls

Applicable controls are the safeguards determined necessary based on risk, classification, environment, data, and applicable authorities.

### Findings / Gaps

Findings or gaps describe differences between expected controls or evidence and assessed conditions. They can identify missing evidence, incomplete safeguards, exceptions, or conditions requiring remediation.

### Risk Treatment

Risk treatment records conceptually how findings or risk are addressed, such as remediation, a compensating safeguard, avoidance, transfer where appropriate, or documented acceptance by authorized authority. This document does not define approval authorities.

### Residual Risk

Residual risk is the risk remaining after applicable controls, implemented safeguards, available evidence, findings, remediation, compensating controls, and other risk treatments have been evaluated.

### Risk Decision

The risk decision is the authorized disposition of residual risk. This model does not define approval thresholds or scoring rules.

## Decisions

Decisions are authorized conclusions, not merely observations or recommendations. The record must be able to associate an authorized decision with the relevant residual risk, findings, conditions, remediation commitments, and final disposition. Consequential risk decisions remain subject to appropriate human authorization.

## Provenance and Validation

The information model anticipates multiple sources for any fact, evidence item, or assessment conclusion. Conceptual provenance includes:

- requestor supplied;
- practitioner supplied;
- vendor supplied;
- system generated;
- reviewer observed;
- evidence derived; and
- SAR derived.

The model should preserve, where appropriate:

- source;
- date and time;
- evidence or reference relationship; and
- reviewer or validation status.

Provenance and validation allow SAR to distinguish an unverified statement from an evidence-supported fact, and to explain how a conclusion was reached.

## Unknown, Not Applicable, and Not Yet Verified

For information that may not be immediately known, the model must distinguish conceptually between:

- **Yes:** the assertion is affirmed;
- **No:** the assertion is denied;
- **Unknown:** the answer is not currently known;
- **Not Applicable:** the question or concept does not apply to this assessment; and
- **Not Yet Verified:** an answer has been provided or observed but has not yet been adequately validated.

Unknown information must not silently become No. These distinctions affect risk analysis, evidence quality, follow-up needs, and the ability to determine whether a gap reflects a missing capability, unavailable information, or an inapplicable condition.

## Evidence Chain

The model supports a traceable evidence chain:

```text
Fact
    ->
Source / Provenance
    ->
Evidence
    ->
Derived Classification / Applicability
    ->
Control Expectation
    ->
Finding
```

This chain supports review of the basis for facts and the path from those facts to control expectations and findings.

## Decision Chain

The model supports a traceable decision chain:

```text
Inherent Risk
    ->
Applicable Controls
    ->
Evidence
    ->
Findings
    ->
Risk Treatment
    ->
Residual Risk
    ->
Authorized Risk Decision
```

This chain preserves the distinction between risk before safeguards are evaluated and the remaining risk after controls and treatments are considered.

## Machine Readability

The information model should eventually support structured, machine-readable representations. Potential future representations include JSON, YAML, OSCAL-compatible artifacts, APIs, databases, forms, and conversational AI interfaces.

Markdown remains the human-readable design source at this stage. This document does not create schemas.

## Relationship to Other SAR Documents

[PRACTITIONER-DISCOVERY.md](PRACTITIONER-DISCOVERY.md) discovers AS-IS practitioner knowledge and process.

[SAR-ARCHITECTURE.md](SAR-ARCHITECTURE.md) defines the conceptual SAR risk architecture.

This document defines the information the future SAR process must be capable of representing. It must remain consistent with the architecture document and does not overwrite or reinterpret practitioner statements as established fact.

## Future Work

The following are identified for later work and are not built by this document:

- machine-readable schema;
- intake and question model;
- authoritative definition of the 19 data elements;
- classification logic;
- risk methodology;
- applicability and authority matrix;
- control catalog;
- OSCAL mapping;
- evidence sufficiency rules;
- findings model;
- lifecycle and workflow model; and
- reporting model.

## Design Constraints

This information model maintains the following boundaries:

- SAR is independent of procurement.
- Organizational status does not determine system risk.
- Facts should precede compliance conclusions.
- Control source and applicability basis are separate.
- Inherent and residual risk are separate.
- Requestors should not need cybersecurity or privacy expertise.
- Unknown must not silently become No.
- Evidence and provenance must be traceable.
- Consequential risk decisions remain subject to human authorization.
- The model does not make unsupported legal conclusions.
- The model does not prematurely encode implementation details.