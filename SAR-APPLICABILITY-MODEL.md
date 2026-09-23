# SAR Applicability Model

## Purpose

This document defines the conceptual model SAR uses to determine and explain why a source, requirement, safeguard, or control expectation is relevant or not relevant to a specific assessment.

It bridges:

```text
Assessment Facts
    ->
Derived Characteristics
    ->
Applicability Basis
    ->
Source / Requirement
    ->
Applicable Requirement
    ->
Safeguard / Control Expectation
```

This document does not create regulatory mappings, NIST control mappings, final applicability rules, legal conclusions, or an executable rules engine.

## Governing Principles

> Risk determines the controls. Authority and applicability determine why a control is required or enforceable.

```text
Control Source
    !=
Applicability Basis

Source Registration
    !=
Source Applicability
```

The [SAR Source Catalog](SAR-SOURCE-CATALOG.md) answers, "What is this source?" This model answers, "Why is this source or requirement relevant to this assessment?" Future requirement and control mappings will answer, "What specific requirement or safeguard follows?"

## Facts Before Applicability

Applicability reasoning begins with supported assessment information, not labels selected by a requestor. Requestors generally provide observable facts. SAR derives applicability from supported facts, relationships, derived characteristics, classifications, environment, use, agreements, and other relevant assessment information.

Requestors should not be asked derived assessment questions such as whether HIPAA applies, whether State cloud requirements are applicable, which NIST baseline applies, or whether they are subject to a regulation. Uncertainty must remain visible when supporting information is incomplete.

## Applicability Basis

An applicability basis is the supported reason that a source, requirement, safeguard, or control expectation is relevant to a specific assessment.

Conceptual basis categories may include:

- information or data characteristics;
- system or impact classification;
- organizational relationship;
- contractual or agreement relationship;
- hosting or environment characteristics;
- connectivity or integration characteristics;
- identity or access characteristics;
- external-party dependency;
- business or operational dependency;
- AI capability or use;
- jurisdictional or organizational scope;
- policy scope;
- risk characteristics; and
- other supported facts or derived characteristics.

These are conceptual categories only. They do not create final rules or establish that every category creates legal applicability.

## Applicability Subject

An applicability subject is the part of an assessment to which applicability may attach. Potential subjects include:

- the assessment as a whole;
- software or product;
- system;
- service;
- environment;
- data or information type;
- business process;
- integration;
- external party;
- contractual or agreement relationship;
- specific requirement; and
- safeguard or control expectation.

Applicability is not always system-wide. A source or requirement may apply only to part of an assessed solution.

## Applicability Target

The facts that create an applicability basis are distinct from the thing to which applicability is evaluated:

```text
Supporting Fact(s)
    ->
Applicability Basis
    ->
Applicability Target
```

An applicability target may be a source, source version, requirement, requirement family, safeguard, control expectation, or another future governed SAR object. This document does not finalize a schema.

## Source-Level and Requirement-Level Applicability

A source may be generally relevant to an assessment while individual requirements within that source differ in applicability.

```text
Source Relevance
    !=
Automatic Applicability of Every Requirement in the Source

One Applicable Requirement
    !=
Every Requirement in the Source Is Applicable
```

Future mappings must support applicability at an appropriate level of granularity. This document does not populate actual requirements.

## Multiple Independent Applicability Bases

A requirement or safeguard may have multiple independent applicability bases, each preserved separately:

```text
Requirement / Safeguard
        |
        +-- Applicability Basis A
        |       -> supported by Fact(s) A
        |
        +-- Applicability Basis B
        |       -> supported by Fact(s) B
        |
        +-- Applicability Basis C
                -> supported by Fact(s) C
```

SAR must not flatten these into a generic rationale such as "State requirement" or "HIPAA." It must be capable of explaining each independent path. If one basis later disappears, another basis may remain.

## Multiple Sources for the Same Safeguard

A safeguard may be supported by multiple independent sources:

```text
Safeguard / Control Expectation
        |
        +-- Risk Basis
        |
        +-- Source A
        |      +-- Applicability Basis A
        |
        +-- Source B
        |      +-- Applicability Basis B
        |
        +-- Source C
               +-- Applicability Basis C
```

Sources and bases must remain independently traceable and must not be collapsed into one authority.

## Risk Basis and Authority / Applicability Basis

### Risk Basis

A risk basis explains why a safeguard is appropriate because of risk presented by the system, information, environment, use, dependency, or other condition.

### Authority / Applicability Basis

An authority or applicability basis explains why a particular external or internal requirement applies.

These may converge on the same safeguard but are not interchangeable. A safeguard may be appropriate because of risk even where a specific legal or contractual authority has not been established. Conversely, an authoritative requirement may establish an expectation even where qualitative risk reasoning alone would not have selected it.

## Applicability Status

Conceptual applicability outcomes are:

- Applicable;
- Not Applicable;
- Potentially Applicable / Requires Review; and
- Insufficient Information.

These statuses are distinct from factual answer states: Yes, No, Unknown, Not Applicable, and Not Yet Verified. Factual states describe information quality or response; applicability status describes the conclusion about relevance of an applicability target.

### Not Applicable

A Not Applicable conclusion must eventually have affirmative rationale. Absence of evidence is not sufficient:

```text
Applicability Target
    +
Relevant Supported Facts
    +
Applicability Rule / Reasoning
    ->
Not Applicable
    +
Rationale
```

This document does not implement exclusion rules.

### Insufficient Information

Insufficient Information is a legitimate outcome. If SAR lacks facts needed to determine applicability, it must not silently convert uncertainty into Applicable, Not Applicable, No, or a default legal conclusion.

Future responses may include follow-up intake, an evidence request, practitioner review, privacy, security, or legal review where appropriate, an assessment limitation, or an unresolved applicability state. This document does not implement workflow.

### Potentially Applicable / Requires Review

Potentially Applicable / Requires Review is distinct from both Applicable and Insufficient Information. It may be appropriate where facts indicate a plausible applicability path but interpretation is required, authority or scope is ambiguous, contractual language requires review, competing evidence exists, or human judgment is needed.

This status must not become a generic substitute for uncertainty.

## Positive and Negative Applicability Conditions

The future model should represent both positive applicability conditions, which are facts supporting applicability, and negative or exclusion conditions, which are facts supporting a reasoned Not Applicable conclusion.

Absence of a positive condition does not automatically prove a negative condition. This document does not implement actual conditions.

## Relationship Context

Applicability may depend on relationships between entities rather than only software properties. Conceptual relationship contexts include:

- CE or BA relationship where applicable;
- contractual or agreement relationship;
- service-provider relationship;
- hosting relationship;
- administrative relationship;
- data-sharing relationship;
- integration relationship;
- organizational policy relationship; and
- other supported relationships.

Relationship facts must remain traceable. SAR must not infer a legal relationship solely from product type or organizational label.

## HIPAA CE / BA

Within SAR, **CE** means HIPAA Covered Entity where used in this context and **BA** means HIPAA Business Associate. BA does not mean State contractor.

The following remain separate dimensions:

1. HIPAA CE or BA relationship.
2. DDS or Regional Center contractual or agreement relationship.
3. California State-contractor classification or State-requirement applicability.
4. System, data, and environment risk.
5. Source and requirement applicability.

Where applicable, these dimensions may coexist. This model does not state that every Regional Center activity is necessarily a HIPAA BA activity, that Regional Centers are State contractors, or that State requirements cannot apply. Each applicability path requires its own supported basis.

## Contractual / Agreement Applicability

Applicability may arise through contracts, BAAs, agreements, incorporated terms, or other governing instruments. However:

```text
Existence of an Agreement
    !=
Every Provision Applies to Every Component or Activity
```

Future mapping must preserve the governing instrument, version, relevant provision, parties or relationship, scope, and applicability rationale. This document does not create contractual interpretations.

## State / DDS Applicability

State or DDS contractual, procurement, cloud, IT, security, privacy, AI, and other requirements each require their own applicability basis.

SAR must not infer applicability solely because DDS is a State Department, a Regional Center interacts with DDS, a product is cloud-hosted, a vendor sells to government, or a source appears in the Source Catalog.

A State or DDS source may be used as a benchmark or control-equivalency source where it is not independently applicable. That role remains distinct from authoritative applicability.

## Benchmark / Reference Use

SAR distinguishes:

```text
Applicable Authority
    !=
Reference / Benchmark
```

A source may inform a safeguard expectation without being an independently applicable authority. The future system must preserve which role the source serves. Benchmark use must not silently become legal or contractual applicability.

## Version-Aware Applicability

Applicability integrates with the Source Catalog and must eventually point to the relevant source version used for the assessment:

```text
Assessment
    ->
Applicability Determination
    ->
Source Family
    ->
Assessment Source Version
    ->
Requirement / Provision
    ->
Applicability Basis
```

A newer source version must not silently rewrite the applicability basis of an existing assessment. If a source changes materially, SAR may later perform impact analysis and re-evaluation according to the Source Catalog model.

## Temporal Applicability

Applicability may change over time. Conceptual examples include an agreement beginning or expiring, a source becoming effective or being superseded, changed hosting, a newly introduced data type, changed relationship, a new integration, AI capability activation, or a requirement change.

SAR should eventually preserve when an applicability determination was made and the facts and source versions on which it depended. This document does not build lifecycle workflow.

## Provenance

Every material applicability determination should eventually retain:

- applicability target;
- applicability status;
- supporting facts;
- derived characteristics where relevant;
- relationship context;
- source;
- source version;
- requirement or provision reference where applicable;
- applicability basis;
- rationale;
- evidence;
- reviewer or system provenance;
- determination date;
- uncertainty; and
- supersession or re-evaluation history.

This is conceptual information, not a final schema.

## Explainability

SAR must eventually be able to answer:

- What is being evaluated for applicability?
- What is the applicability conclusion?
- What facts support it?
- What evidence supports those facts?
- What relationship or context matters?
- What source is involved?
- Which version of the source was used?
- What specific requirement or provision is involved?
- Why does it apply or not apply?
- What uncertainty remains?
- Was the source used as authority or merely as a benchmark or reference?
- Who or what produced the determination?
- Has the determination subsequently been superseded or re-evaluated?

SAR should avoid opaque conclusions such as "HIPAA applies," "State requirements apply," or "NIST applies" without a traceable applicability path.

## Applicability Trace

SAR supports the following conceptual applicability trace:

```text
Assessment Fact(s)
    ->
Validation / Provenance
    ->
Derived Characteristic / Relationship
    ->
Applicability Basis
    ->
Applicability Target
    ->
Source + Assessment Source Version
    ->
Requirement / Provision
    ->
Applicability Status + Rationale
    ->
Safeguard / Control Expectation
```

Not every applicability path uses every layer. This trace complements the Evidence Chain, Decision Trace, and Source Trace; it does not replace them.

## Conflicting Applicability Paths

Different evidence or interpretations may produce conflicting applicability paths. SAR must preserve the conflict rather than silently choosing one.

Potential future handling includes additional evidence, practitioner review, privacy, security, or legal review where appropriate, documented interpretation, and authorized resolution. This document does not define final escalation authorities or workflow.

## Re-evaluation

Applicability determinations may need re-evaluation when supporting facts or sources materially change. Potential triggers include corrected facts, changed data use, changed hosting, changed integrations, changed external parties, changed organizational or contractual relationship, agreement amendment or expiration, source revision, policy change, changed AI capability, or changed system scope.

Re-evaluation must preserve prior history; it must not overwrite a prior determination as though it never existed.

## Human Review and Automation

Future SAR implementation may automate deterministic applicability rules where underlying authority, facts, and logic have been authorized and validated.

AI may assist by organizing facts, identifying possible applicability paths, locating relevant registered sources, identifying missing information, explaining supported reasoning, and flagging conflicts. AI must not invent authority or applicability. Ambiguous or consequential applicability determinations must support appropriate human review.

This document does not define final authorization roles.

## Relationship to Existing SAR Documents

[PRACTITIONER-DISCOVERY.md](PRACTITIONER-DISCOVERY.md) discovers AS-IS practitioner knowledge and process.

[SAR-ARCHITECTURE.md](SAR-ARCHITECTURE.md) defines conceptual SAR risk architecture.

[SAR-INFORMATION-MODEL.md](SAR-INFORMATION-MODEL.md) defines what information SAR represents.

[SAR-INTAKE-MODEL.md](SAR-INTAKE-MODEL.md) defines how facts are collected.

[SAR-DECISION-LOGIC.md](SAR-DECISION-LOGIC.md) defines how supported facts become assessment conclusions.

[SAR-SOURCE-CATALOG.md](SAR-SOURCE-CATALOG.md) defines source identity, provenance, versioning, currentness, and historical preservation.

This document defines how SAR establishes and explains why a source, requirement, safeguard, or control expectation is relevant or not relevant to a particular assessment. Future requirement and control artifacts will provide the authoritative content to which this model is applied.

## Future Work

The following are identified for later work and are not built by this document:

- machine-readable applicability schema;
- applicability rule syntax;
- applicability rules engine;
- authoritative requirement catalog;
- requirement identifiers;
- source-to-requirement extraction;
- source-to-requirement mappings;
- applicability and authority matrix;
- classification-to-applicability rules;
- contractual applicability mappings;
- HIPAA, HITECH, and BAA applicability mappings;
- California State and DDS applicability mappings;
- cloud applicability mappings;
- AI applicability mappings;
- NIST SP 800-53 applicability mappings;
- OSCAL integration;
- safeguard and control catalog;
- control mappings;
- evidence sufficiency rules;
- applicability review workflow;
- authorization matrix; and
- lifecycle and reassessment automation.

## Design Constraints

This applicability model maintains the following boundaries:

- Applicability is derived from supported facts and context.
- Requestors are not expected to make compliance determinations.
- Source registration does not establish applicability.
- Control source remains separate from applicability basis.
- Risk basis remains separate from authority and applicability basis.
- Source-level relevance does not automatically apply every requirement.
- Applicability can attach to a specific subject or component rather than automatically to the whole system.
- Multiple independent applicability bases are preserved.
- Multiple independent sources can support the same safeguard.
- Applicable, Not Applicable, Potentially Applicable / Requires Review, and Insufficient Information remain distinct.
- Not Applicable requires rationale.
- Absence of evidence does not establish Not Applicable.
- Unknown does not silently become No.
- Benchmark or reference use does not become authoritative applicability.
- HIPAA BA is not treated as State contractor.
- HIPAA, contractual, State or DDS, and risk dimensions remain separate.
- No source is made applicable merely because it appears in the Source Catalog.
- Applicability is version-aware.
- Historical applicability determinations are preserved.
- Conflicting applicability paths remain visible.
- AI does not invent authority or applicability.
- No actual regulatory, contractual, NIST, OSCAL, State, DDS, cloud, or AI mappings are created.
- No executable rules or final schema are created.
- No unsupported legal conclusions are introduced.