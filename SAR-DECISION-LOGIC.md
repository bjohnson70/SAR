# SAR Decision Logic

## Purpose

This document defines the conceptual decision-logic model for Software Assessment and Review (SAR). Decision logic explains how SAR moves from collected facts to derived assessment conclusions while preserving traceability, uncertainty, applicability, evidence, and human authorization.

The intended separation is:

```text
Information Model = what SAR needs to know
Intake Model      = how SAR obtains facts
Decision Logic    = how SAR interprets facts and derives assessment conclusions
Control Mapping   = future authoritative mapping of requirements and safeguards
                    to specific control sources
```

This document is not a final rules engine, risk-scoring methodology, control catalog, OSCAL implementation, complete HIPAA analysis, California State requirements matrix, legal opinion, final approval workflow, or replacement for human risk authorization. It does not encode NIST control mappings or regulatory applicability rules.

## Core Reasoning Model

SAR uses the following conceptual reasoning dependency model:

```text
Collected Facts
    ->
Validation / Unresolved Facts
    ->
Derived Characteristics
    ->
Classification
    ->
Inherent Risk
    ->
Applicability Determination
    ->
Applicable Control Expectations
    ->
Evidence Evaluation
    ->
Findings / Gaps
    ->
Risk Treatment
    ->
Residual Risk
    ->
Authorized Risk Decision
```

This is a reasoning dependency model, not necessarily a strictly linear workflow. New facts, evidence, or applicability information may require prior conclusions to be reconsidered.

## Facts Before Conclusions

Decision logic begins with facts represented by the [SAR Information Model](SAR-INFORMATION-MODEL.md) and collected through the [SAR Intake Model](SAR-INTAKE-MODEL.md).

> The requestor tells SAR what is true. SAR determines what those facts mean.

Requestor statements and vendor assertions may be unverified. Evidence may support or contradict those statements; reviewers and system-generated information may establish additional facts; and uncertainty must remain visible. An unsupported assertion must not silently become an established fact.

## Validation State

Decision logic preserves the factual-information distinctions of:

- Yes;
- No;
- Unknown;
- Not Applicable; and
- Not Yet Verified.

Unknown must never silently become No. Not Yet Verified remains distinguishable from a validated fact.

Where material information remains unresolved, decision logic may request additional evidence or clarification, escalate to a reviewer, identify an assessment limitation, or prevent a conclusion that cannot yet be supported. This document does not define detailed workflow states.

## Derived Characteristics

A derived characteristic is a reviewer- or logic-derived description based on one or more facts. Examples include externally hosted, individual-level information involved, external privileged access, Internet exposed, production information involved, third-party dependency, AI processes organizational information, persistent data storage, and high operational dependency.

These are examples only, not a complete taxonomy. Each derived characteristic must remain traceable to the facts and evidence from which it was derived.

## Classification

Classification is a derived assessment activity. Potential future classifications may include data classification, information sensitivity, system or impact classification, and regulatory or contractual characterization where appropriate.

This model does not define LOW, MODERATE, or HIGH calculation rules, require requestors to select NIST impact levels, or encode HIPAA or other legal determinations as simplistic single-answer rules.

Classification conclusions must retain supporting facts, provenance, evidence, reasoning or rationale, and uncertainty where applicable.

## Inherent Risk

Inherent risk is risk before considering the effectiveness of safeguards or mitigating controls. Decision logic may consider factual and derived characteristics involving data, business function, users, identity, hosting, connectivity, external dependencies, AI, operational impact, and other relevant characteristics.

This document does not create numeric risk scoring.

## Applicability Determination

Applicability determination establishes why a requirement, safeguard, or control expectation is relevant to a specific SAR.

### Control Source

A control source is the framework, law, regulation, policy, contractual provision, standard, guidance, or other authoritative or reference source from which a safeguard or requirement originates.

### Applicability Basis

An applicability basis is the reason that a source, requirement, safeguard, or control is relevant to a specific system, data type, relationship, environment, or use.

A control source does not automatically imply applicability. An applicability basis must be traceable to facts, derived characteristics, relationships, classification, or other supported assessment information.

### Applicability Status

Conceptual outcomes for applicability reasoning include:

- Applicable;
- Not Applicable;
- Potentially Applicable / Requires Review; and
- Insufficient Information.

These statuses are distinct from the Yes, No, Unknown, Not Applicable, and Not Yet Verified states used for factual information. A Not Applicable determination should eventually require rationale rather than merely the absence of evidence. This document does not define a rules engine or final enumeration schema.

## Multiple Independent Applicability Bases

A single safeguard or control expectation may have many independent bases:

```text
Safeguard / Control Expectation
        |
        +-- Risk Basis
        |      -> why the system needs the safeguard
        |
        +-- Control Source A
        |      -> source of requirement / safeguard
        |
        +-- Applicability Basis A
        |      -> why Source A applies
        |
        +-- Control Source B
        |      -> another source
        |
        +-- Applicability Basis B
        |      -> independent reason Source B applies
        |
        +-- Control Source C
               -> another source
               |
               +-- Applicability Basis C
```

SAR must not assume a safeguard has only one authority or source, or flatten multiple bases into a generic label such as "State requirement." It should eventually be capable of explaining what safeguard is expected, what risk it addresses, where the expectation comes from, why each source applies, what evidence demonstrates implementation, and what gap exists when the expectation is not demonstrated.

## HIPAA CE / BA Relationship

Within SAR, **CE** means HIPAA Covered Entity and **BA** means HIPAA Business Associate where those terms are used in this context. BA does not mean State contractor. The HIPAA CE-to-BA relationship is a separate applicability dimension from State-contractor classification or State procurement terminology.

DDS's status as a State Department is another fact. DDS and Regional Center contractual or agreement relationships are another factual and applicability dimension. State or DDS contractual, procurement, cloud, IT, security, privacy, or other requirements each require their own applicability basis.

Where applicable, these dimensions may coexist. This model does not assert that every Regional Center activity is necessarily a HIPAA BA activity, that Regional Centers are State contractors, or that State requirements cannot apply. The decision model keeps these relationships independently traceable.

```text
HIPAA Relationship
    ->
HIPAA / HITECH / BAA applicability where supported

Contractual / Agreement Relationship
    ->
Applicable contractual obligations where supported

State / DDS Requirement
    ->
Applicability independently established

System / Data / Environment Risk
    ->
Safeguard / control expectations
```

These paths may converge on the same safeguard without becoming the same applicability basis.

## Risk Basis and Authority / Applicability Basis

### Risk Basis

A risk basis explains why a safeguard is appropriate because of the risk presented by the system, information, environment, use, or dependency.

### Authority / Applicability Basis

An authority or applicability basis explains why a particular external or internal requirement applies.

For example, external privileged administration can indicate elevated access risk and support an expectation for strong privileged-access safeguards. Separately, an applicable framework, agreement, or requirement may provide an independent source for some or all of those safeguards.

Risk may justify a safeguard even when a specific legal or contractual source is not yet established. Conversely, an authoritative requirement may establish a safeguard even where qualitative risk reasoning alone would not have selected it. This document does not create actual control mappings.

## Applicable Control Expectations

After risk and applicability analysis, SAR may derive control or safeguard expectations. An expectation should eventually be capable of retaining:

- safeguard or control identity;
- risk basis;
- one or more control sources;
- one or more applicability bases;
- applicability rationale;
- expected outcome;
- evidence needed to evaluate implementation; and
- evaluation status.

This model does not enumerate NIST controls, establish the final control catalog, or state that all systems receive the same baseline.

## Evidence Evaluation

Evidence is evaluated against the specific assertion, safeguard, or control expectation it is intended to support. Provenance must be preserved.

Evidence may support an assertion, partially support it, contradict it, be insufficient, be outdated, be inapplicable to the assessed environment, or require reviewer interpretation. Vendor documentation does not automatically become an independently verified fact. Certification or audit evidence does not automatically demonstrate every SAR control expectation.

This model does not define final evidence-sufficiency scoring.

## Findings / Gaps

A finding or gap arises from a traceable difference between an expected condition and the supported assessed condition:

```text
Expected Condition
    +
Evidence / Observed Condition
    ->
Evaluation
    ->
Finding / No Finding / Unresolved
```

A finding should eventually be able to identify the expectation, observed condition, supporting evidence, affected risk, source and applicability relationship, rationale, and remediation or treatment relationship. This document does not create severity scoring.

## Risk Treatment

Conceptual risk treatments include remediation, compensating safeguard, avoidance, transfer where appropriate, and documented acceptance by authorized authority.

Risk treatment does not erase the original finding or evidence history. This document does not define approval authorities.

## Residual Risk

Residual risk is the risk remaining after applicable controls, implemented safeguards, evidence, findings, remediation, compensating controls, and other risk treatments are evaluated. It must remain distinguishable from inherent risk.

This document does not create numeric scoring.

## Authorized Risk Decision

The final risk decision concerns residual risk. Consequential risk decisions require appropriate human authorization.

AI or automated logic may organize facts, derive supported intermediate characteristics, identify possible applicability paths, identify missing information or conflicts, and assist reviewers. Where later authorized logic permits, it may propose or calculate results. AI must not independently authorize consequential risk acceptance or final risk disposition.

This document does not define specific DDS approval authorities.

## Explainability and Rationale

Every material derived conclusion should eventually be capable of answering:

- What did SAR conclude?
- What facts support that conclusion?
- What evidence supports or contradicts those facts?
- What reasoning produced the conclusion?
- What uncertainty remains?
- If a requirement applies, where does it come from?
- Why does that source apply here?
- What risk does the safeguard address?
- Who authorized the consequential decision?

SAR should avoid opaque conclusions such as "NIST AC-2 applies" without an associated rationale chain.

## Decision Trace

SAR maintains a conceptual decision trace:

```text
Fact(s)
    ->
Validation / Provenance
    ->
Derived Characteristic(s)
    ->
Classification / Risk
    ->
Applicability Analysis
    ->
Control Expectation
    ->
Evidence Evaluation
    ->
Finding
    ->
Risk Treatment
    ->
Residual Risk
    ->
Authorized Decision
```

This trace complements, rather than replaces, the existing evidence and decision chains.

## Re-evaluation

Decision logic must support reassessment when material information changes. Potential triggers include new evidence, corrected facts, changed data use, changed hosting, a new integration or AI capability, vendor or subprocessor change, material software change, changed contractual or regulatory basis, remediation, or a newly discovered vulnerability or condition.

Material changes can invalidate or alter prior derived conclusions and therefore require traceable re-evaluation. This document does not build lifecycle workflow.

## Machine-Readable Future

The decision model should eventually be representable through structured rules and relationships suitable for JSON or YAML, OSCAL-related mappings, APIs, databases, deterministic rule evaluation, reviewer tools, and conversational AI.

Human-readable Markdown remains the design source at this stage. This document does not create schemas or executable rules.

## Relationship to Existing Documents

[PRACTITIONER-DISCOVERY.md](PRACTITIONER-DISCOVERY.md) discovers AS-IS practitioner knowledge and process.

[SAR-ARCHITECTURE.md](SAR-ARCHITECTURE.md) defines the conceptual risk architecture and governing principles.

[SAR-INFORMATION-MODEL.md](SAR-INFORMATION-MODEL.md) defines what information SAR must represent.

[SAR-INTAKE-MODEL.md](SAR-INTAKE-MODEL.md) defines how facts are collected through adaptive intake.

This document defines how supported facts are interpreted into traceable derived assessment conclusions. Future control mappings and rules will provide authoritative implementation detail beneath this conceptual model.

## Future Work

The following are identified for later work and are not built by this document:

- authoritative 19-element data mapping;
- data-classification logic;
- impact-classification methodology;
- inherent-risk methodology;
- applicability and authority matrix;
- control catalog;
- NIST SP 800-53 Rev. 5 mappings;
- OSCAL mappings;
- HIPAA and HITECH mappings;
- BAA requirement mappings;
- State and DDS requirement mappings;
- cloud requirement mappings;
- AI requirement mappings;
- evidence-sufficiency rules;
- finding and severity model;
- residual-risk methodology;
- authorization matrix;
- executable decision rules;
- lifecycle and workflow; and
- reporting.

## Design Constraints

This decision-logic model maintains the following boundaries:

- Facts remain separate from derived conclusions.
- Unverified assertions do not silently become facts.
- Unknown does not silently become No.
- Derived characteristics are traceable to supporting facts.
- Classification remains derived.
- Inherent and residual risk remain separate.
- Risk basis is distinct from authority and applicability basis.
- Control source is distinct from applicability basis.
- Multiple independent sources and applicability bases are supported.
- HIPAA BA is not treated as synonymous with State contractor.
- Contractual relationships are not collapsed into HIPAA relationships.
- State applicability is independently established.
- A branch opening does not itself establish control applicability.
- Evidence does not automatically prove an assertion.
- Findings are traceable to expected and observed conditions.
- Human authorization remains required for consequential risk decisions.
- No actual NIST or control mappings are created.
- No unsupported legal conclusions are introduced.
- No premature executable rules or implementation schema are created.