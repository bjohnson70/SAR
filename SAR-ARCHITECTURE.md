# SAR Architecture

## Purpose

Software Assessment and Review (SAR) is an independent, risk-based assessment process for software, cloud services, technology services, and related solutions that may be introduced into or used in an organizational environment.

SAR evaluates the risk introduced by a technology and determines the security, privacy, and compliance controls necessary to manage that risk.

SAR is not a procurement process. Procurement, acquisition, renewal, contracting, deployment, discovery of existing software, and other organizational activities may trigger a SAR. The purchasing or acquisition mechanism does not determine the risk assessment.

## Governing Principles

The core SAR design principle is:

> Risk determines the controls. Authority and applicability determine why a control is required or enforceable.

Organizational status does not determine system risk. A Business Associate or Regional Center does not need to be classified as a State entity for software handling regulated or organizational data to require appropriate safeguards.

SAR must distinguish the assessment of system and data risk from determination of the legal, contractual, policy, or regulatory authority that makes a particular safeguard applicable. This architecture does not make legal conclusions about whether Regional Centers are State entities or State contractors.

## Conceptual SAR Decision Chain

SAR follows this conceptual decision chain:

```text
Software / Function
    ->
Data
    ->
Environment & Connectivity
    ->
Inherent Risk
    ->
Impact / Classification
    ->
Applicable Controls
    ->
Evidence
    ->
Findings / Gaps
    ->
Residual Risk
    ->
Risk Decision
```

### Software / Function

Identify what the solution does, the business purpose it serves, its intended users, and the capabilities it introduces. The assessment concerns the actual function and use of the technology, rather than its procurement category.

### Data

Identify the information the solution collects, receives, stores, processes, generates, displays, or transmits; whose information it is; and where it originates and goes. These facts support later data classification and applicability analysis.

### Environment & Connectivity

Identify where and how the solution is hosted, deployed, administered, accessed, and connected. This includes integrations, networks, remote access, identity systems, external parties, and service dependencies.

### Inherent Risk

Assess the security, privacy, operational, compliance, third-party, and other relevant risks presented by the combination of function, data, environment, connectivity, dependencies, and use before considering the effectiveness of safeguards or mitigating controls.

### Impact / Classification

Derive the system's impact and relevant classifications from the assessment facts and identified risk. Classification is an analytical outcome, not a question requestors must answer using compliance terminology.

### Applicable Controls

Identify the safeguards needed to manage the assessed risk and document the applicable authority or basis for each control. Not every control source or assessment domain applies to every solution.

### Evidence

Collect and evaluate the artifacts, attestations, configurations, records, and other support necessary to determine whether applicable controls are present and effective.

### Findings / Gaps

Document differences between applicable control expectations and available evidence or the assessed implementation. Findings may identify missing evidence, incomplete safeguards, exceptions, or conditions requiring remediation.

### Residual Risk

Assess the risk remaining after applicable controls, implemented safeguards, available evidence, findings, remediation, compensating controls, and other risk treatments have been evaluated.

### Risk Decision

Record the authorized disposition of residual risk after controls, evidence, findings, and applicable risk treatments have been considered, including any required conditions, remediation, acceptance, escalation, or other follow-up. Consequential risk decisions require appropriate human review and authorization.

## Facts Before Compliance Conclusions

SAR intake should primarily collect factual information that a reasonable business requestor can answer. Requestors should not be required to determine whether HIPAA applies, whether information is legally classified as PHI, whether a NIST baseline or specific NIST control applies, whether State cloud requirements apply, or whether a particular security architecture is compliant.

Intake should instead establish facts about:

- what the software does;
- information it collects, receives, stores, processes, generates, displays, or transmits;
- whose information it is;
- where information comes from and where it goes;
- users and administrators;
- authentication;
- integrations;
- connectivity;
- hosting and deployment;
- external parties;
- AI capabilities;
- logging and auditing; and
- operational and business impact.

SAR reviewers and/or decision logic derive classifications, risk, applicability, controls, and evidence requirements from those facts.

## Control Sources and Applicability Basis

### Control Source

A control source is the framework, law, regulation, policy, contractual provision, standard, guidance, or other source from which a control or safeguard is derived.

### Applicability Basis

An applicability basis explains why a control applies to a particular system, data type, relationship, or environment.

Potential control and authority sources may include, without asserting that every source applies to every assessment:

- NIST SP 800-53 Rev. 5;
- OSCAL representations of NIST controls and baselines;
- HIPAA;
- HITECH;
- FIPS;
- California security and privacy requirements;
- California cloud provisions;
- California IT General Provisions;
- State AI requirements;
- DDS policies and standards;
- Business Associate Agreements;
- contracts and agreements; and
- other applicable laws, regulations, policies, and standards.

California contractor and cloud provisions may also be evaluated as control-equivalency benchmarks where appropriate. Their use as benchmarks does not assert that a Business Associate is legally a State contractor.

## Business Associate and Regulated Data Principle

Organizational classification and regulatory applicability are separate questions. Where software creates, receives, maintains, transmits, or otherwise handles information associated with a regulated business relationship, SAR must evaluate applicable security and privacy obligations regardless of whether the operating organization is itself a State entity.

HIPAA, HITECH, and Business Associate obligations are examples of federal or contractual authority paths that SAR may need to evaluate. This principle defines an architectural requirement for assessment; it does not make a legal determination about any particular organization or relationship.

## Terminology: Covered Entity, Business Associate, and State Contractor

In this context, **CE** means a HIPAA Covered Entity and **BA** means a HIPAA Business Associate. Business Associate is a HIPAA relationship or designation and must not be treated as synonymous with State contractor. Where applicable, a Regional Center may operate as a BA within a HIPAA relationship in which DDS is the CE; HIPAA, HITECH, and the applicable Business Associate Agreement or other governing arrangement may provide obligations associated with that relationship.

DDS is a California State Department, and its contractual or agreement relationships with Regional Centers are separate facts from the HIPAA CE-to-BA relationship. A HIPAA BA designation does not by itself establish that an organization is a State contractor or that any State contractual, procurement, cloud, IT, security, privacy, or other requirement applies. Each such requirement requires its own applicability basis.

Multiple applicability bases may coexist for the same safeguard. SAR must preserve those bases independently so it can explain why a requirement or control applies. System, data, and environment risk determine safeguard and control expectations; the HIPAA relationship, contractual or organizational relationship, and State or DDS requirement applicability remain separately evaluated dimensions.

## Initial Known Assessment Domains

The following are known design inputs that require later detailed definition. They are not universal controls and do not automatically apply to every product:

- data and identifier review, including the existing 19-element concept;
- authentication and SSO/SAML/Microsoft Entra ID;
- audit logging and potential immutable audit records and SIEM integration;
- cloud hosting and cloud security;
- AI and Generative AI;
- NIST SP 800-53 Rev. 5 controls and baselines;
- OSCAL consumption;
- encryption;
- data location and remote access;
- incident and breach response;
- vulnerability and patch management;
- continuity, backup, and recovery; and
- third-party and shared-responsibility considerations.

Applicability for these domains will be derived from assessment facts and risk.

## Evidence and Decision Chains

### Evidence Chain

The evidence chain is the traceable path from requestor and practitioner facts and supporting artifacts through inherent-risk and classification analysis, control applicability, and the evidence evaluated by reviewers. It should make the basis for an assessment reproducible and auditable.

### Decision Chain

The decision chain is the traceable path from inherent risk and applicable requirements through findings or gaps and residual-risk evaluation to the final risk decision and any imposed conditions. It should make consequential decisions explainable, reviewable, and reproducible.

## SAR Identifier

Every SAR assessment will receive a globally unique identifier (GUID). The implementation is intentionally not defined here.

The GUID must allow intake information, evidence, findings, decisions, remediation, and lifecycle events associated with an assessment to be correlated.

## Relationship to Practitioner Discovery

[PRACTITIONER-DISCOVERY.md](PRACTITIONER-DISCOVERY.md) is used to discover and document the current AS-IS SAR process and practitioner knowledge.

This document defines the emerging conceptual architecture for the future operating SAR process. Practitioner discovery remains evidence for design. This architecture must not overwrite or reinterpret practitioner statements as established fact.

## Future Components

The following artifacts are likely future components of the operating process and are not defined by this document:

- SAR intake schema and question set;
- data classification logic;
- risk model;
- applicability and authority matrix;
- control catalog and OSCAL mappings;
- evidence requirements;
- findings register;
- risk decision record;
- lifecycle and workflow model;
- reporting; and
- implementation architecture.

## Design Goals

The SAR architecture should support:

- plain-language intake;
- reproducible assessments;
- explainable control applicability;
- evidence-based decisions;
- separation of risk from procurement;
- separation of organizational status from data and system risk;
- portability across approved AI and automation environments;
- machine-readable implementation where practical; and
- human review and authorization for consequential risk decisions.

The architecture remains technology-neutral except where a technology is an explicit known SAR requirement or control source.