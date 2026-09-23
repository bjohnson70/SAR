# SAR Requirement Model

## Purpose

This document defines the conceptual model for representing authoritative or reference requirements extracted from registered SAR sources. It defines what a requirement is and how SAR preserves its identity, meaning, provenance, version relationship, scope, applicability relationship, and connection to safeguards or control expectations.

It does not populate the Requirement Catalog, create actual HIPAA, HITECH, NIST, California State, DDS, cloud, AI, contractual, BAA, or other requirements, create control mappings, or create executable applicability rules.

## Core Distinctions

```text
Source
    !=
Requirement
    !=
Applicability Determination
    !=
Safeguard / Control Expectation
    !=
Evidence
    !=
Finding
```

- **Source** answers: "Where did this authoritative or reference material come from?"
- **Requirement** answers: "What does the source require, prohibit, permit, condition, define, direct, or otherwise establish?"
- **Applicability Determination** answers: "Why is this requirement relevant or not relevant to this assessment?"
- **Safeguard / Control Expectation** answers: "What outcome, protection, behavior, or condition does SAR expect?"
- **Evidence** answers: "What supports whether the expectation is satisfied?"
- **Finding** answers: "What gap, issue, unresolved condition, or other assessment conclusion results from evaluating the expectation?"

SAR must not collapse these concepts.

## Requirement Is Not Synonymous With Control

```text
Requirement
    !=
Control
```

A requirement may concern security safeguards, privacy protections, data handling, permitted or prohibited use, disclosure, retention, deletion, data location, access, authentication, encryption, logging, incident notification, breach handling, vulnerability management, continuity or recovery, documentation, reporting, approval, contractual duties, flow-down obligations, AI disclosure or use restrictions, training-data restrictions, governance, procedural obligations, technical obligations, administrative obligations, physical protections, or other conditions and duties.

These are conceptual examples only. This document creates no actual requirements.

## Requirement Identity

SAR should use a stable internal SAR Requirement ID. It should eventually allow SAR to refer to the same conceptual requirement without depending solely on source title, URL, page number, section number, source wording, or an external control number.

```text
SAR Requirement Identity
    ->
Source Family
    ->
Source Version
    ->
Source Location / Provision
    ->
Requirement Representation
```

A requirement's wording or location may change across source versions. External section and control identifiers are not assumed globally unique. This document does not define identifier syntax.

## Source-Bound Requirements

Every authoritative requirement must remain traceable to its source:

```text
SAR Source ID
    ->
Assessment / Registered Source Version
    ->
Source Provision / Location
    ->
Requirement
```

Normalization for SAR use must not remove source provenance. Where appropriate, SAR should preserve source identity, source version, source provision or location, authoritative text reference, extraction or interpretation provenance, date extracted or verified, and relationship to superseding versions.

This document does not invent citations or requirement text.

## Requirement Representation

SAR distinguishes four representations:

### Source Text / Authoritative Text

Source text is the authoritative wording or authoritative source reference.

### SAR Requirement Statement

A SAR requirement statement is SAR's controlled representation of what the source establishes.

### Interpretation / Guidance

Interpretation or guidance explains meaning, context, implementation considerations, or reviewer guidance where authorized.

### Safeguard / Control Expectation

A safeguard or control expectation describes the expected outcome or protection evaluated by SAR.

These representations remain distinguishable. Paraphrased SAR text must not silently replace authoritative source text. SAR need not store verbatim copyrighted text where an authoritative source reference is sufficient. This document does not implement extraction.

## Requirement Granularity

A source provision may contain one requirement, multiple requirements, a definition, exception, condition, permission, prohibition, applicability statement, implementation instruction, or combinations of these.

SAR must eventually support decomposition into assessable requirement units while retaining traceability to the original provision:

```text
Source Provision
    ->
Requirement A
Requirement B
Condition C
Exception D
```

This document does not define automated parsing rules.

## Requirement Type / Semantic Role

The model should distinguish conceptual semantic roles including obligation, prohibition, permission, condition, exception, definition, disclosure requirement, reporting requirement, documentation requirement, approval requirement, technical safeguard requirement, administrative safeguard requirement, physical safeguard requirement, procedural requirement, contractual requirement, flow-down requirement, and other governed requirement types.

These are conceptual examples, not a final enumeration. A definition or exception may materially affect assessment reasoning even when it is not itself a safeguard.

## Normative Strength

Requirements may express different normative strength or meaning. Authoritative text may use concepts equivalent to must, shall, required, prohibited, may, should, recommended, conditional, or informational.

SAR must preserve source meaning and authority. It must not blindly normalize those meanings or convert guidance into a mandatory requirement merely because it is used as a benchmark. This document does not define a final normative-strength enumeration.

## Authority Versus Reference / Benchmark

A requirement may originate from an applicable authoritative source or from a source used as a reference or benchmark:

```text
Requirement
    +-- Source Role: Applicable Authority

or

Requirement
    +-- Source Role: Reference / Benchmark
```

These roles remain distinct. A benchmark-derived expectation must not silently become a legal, regulatory, or contractual requirement.

## Requirement Scope

Requirements may apply to different subjects or scopes. Conceptual scope dimensions include assessment; software or product; system; service; environment; information or data; user; privileged user; administrator; organization; external party; service provider; subprocessor or subcontractor; integration; business process; contractual relationship; AI capability; lifecycle phase; and other governed subjects.

SAR must not assume every requirement applies to an entire system. This document does not finalize scope enumerations.

## Conditions and Exceptions

Requirements may be conditional:

```text
Requirement
    +
Applicability Condition(s)
    +
Exception(s)
    ->
Requirement Applicability
```

Conditions and exceptions must be preserved as authoritative requirement content and later evaluated through the [SAR Applicability Model](SAR-APPLICABILITY-MODEL.md). Absence of a condition must not be interpreted casually, and an exception must not be inferred without supporting authority. This document does not implement applicability logic.

## Requirement Dependencies

Requirements may depend on or relate to other requirements. Potential conceptual relationships include depends on, prerequisite for, exception to, modifies, supplements, supersedes, superseded by, implements, clarifies, references, incorporates, conflicts with, and related to.

This document does not finalize relationship enumerations or infer legal hierarchy solely from these relationships.

## Requirement and Expectation Relationships

### One Requirement to Many Expectations

A single requirement may result in multiple safeguard or control expectations:

```text
Requirement A
    ->
Safeguard Expectation 1
Safeguard Expectation 2
Safeguard Expectation 3
```

A broad obligation may eventually require technical, administrative, and evidentiary expectations. This document creates no actual mappings.

### Many Requirements to One Expectation

Multiple requirements may support the same safeguard or control expectation:

```text
Requirement A ----\
                   \
Requirement B ------> Safeguard / Control Expectation
                   /
Requirement C ----/
```

Each requirement, source, and applicability path must remain independently traceable. SAR must not collapse multiple authorities into one generic justification.

## Requirement to NIST Control Relationship

SAR must not assume every requirement maps one-to-one to a NIST SP 800-53 control. Future mappings may include one requirement to one control, one requirement to many controls, many requirements to one control, a requirement to a safeguard not represented by a specific NIST control, a NIST control to an expectation supported by risk rather than a separate external requirement, or a requirement to a procedural or contractual obligation outside the control catalog.

NIST SP 800-53 is an important control framework, but this Requirement Model remains framework-neutral. This document does not populate NIST controls or create OSCAL mappings.

## Requirement Versioning

Requirements integrate with [SAR-SOURCE-CATALOG.md](SAR-SOURCE-CATALOG.md) and must be version-aware. A source revision may leave a requirement unchanged; modify wording without changing meaning; materially modify a requirement; split or merge requirements; add, remove, replace, or withdraw a requirement; or change a condition, exception, scope, or normative strength.

SAR must preserve historical requirement provenance and distinguish:

```text
Current Requirement Representation
    !=
Requirement Representation Used by Assessment
```

A new source version must not silently rewrite the requirement basis of a completed assessment.

## Requirement Change / Succession

Requirement succession may be represented conceptually as:

```text
Requirement Version A
    -> unchanged in Version B

Requirement Version A
    -> modified by Requirement Version B

Requirement A
    -> split into Requirements B + C

Requirements A + B
    -> merged into Requirement C

Requirement A
    -> withdrawn / removed / replaced
```

This document does not define executable change detection. Requirement changes should eventually integrate with Source Catalog materiality and affected-assessment analysis.

## Temporal Requirements

A requirement may have temporal characteristics including publication date, effective date, expiration date, transition period, compliance deadline, reporting deadline, notification period, retention period, review interval, or contractual term.

These are different concepts and must not be collapsed into a single generic date. This document invents no date values and defines no date-calculation logic.

## Requirement Provenance

Every material requirement representation should eventually answer:

- What is the SAR Requirement ID?
- What source did it come from and which source version?
- Where in the source is it located?
- What authoritative wording or reference supports it?
- Who or what extracted it, and was extraction automated, human, or assisted?
- Who or what verified it, and when?
- Is the SAR requirement statement authoritative text, normalization, interpretation, or guidance?
- Has the source or requirement changed, and what replaced it if anything?
- Which assessments used this requirement or version?

This document does not create a final schema.

## Requirement Validation

A requirement extracted or normalized into SAR must not automatically be treated as verified merely because it was generated by AI, OCR, a parser, automated extraction, an imported mapping, a third-party reference, or a prior SAR record.

Future implementation should preserve conceptual validation states such as unverified, source-matched, reviewed, approved, superseded, and requires review. These are examples, not an executable enumeration. Human review must remain possible where interpretation or authority is consequential.

## AI and Automated Extraction

Future SAR implementation may use AI or deterministic tooling to locate candidate provisions, extract candidate requirements, decompose compound provisions, normalize language, identify conditions or exceptions, propose semantic roles or relationships, propose control or safeguard mappings, and identify source changes.

AI-generated or machine-generated requirement content must preserve provenance and must not silently become authoritative. AI must not invent requirement text, citations, authority, applicability, legal interpretation, or source metadata. Consequential interpretations must support appropriate human review.

## Requirement Status

Requirement lifecycle or currentness status is distinct from applicability status. Conceptual statuses may include candidate, verified, current, superseded, withdrawn, expired where applicable, currentness unknown, and requires review.

```text
Requirement Status
    !=
Applicability Status
```

A requirement can be current but Not Applicable to a particular assessment. A superseded requirement may remain historically relevant to an older assessment.

## Requirement Catalog

The future Requirement Catalog is the governed collection of SAR requirement records:

```text
Source Catalog
    ->
Requirement Catalog
    ->
Applicability Determinations
    ->
Safeguard / Control Expectations
```

This model defines structure and meaning. The future Requirement Catalog will contain verified requirement instances. This task does not populate it.

## Requirement Trace

SAR supports the following conceptual requirement trace:

```text
Authoritative Publisher
    ->
SAR Source
    ->
Source Version
    ->
Source Provision / Location
    ->
Requirement
    ->
Requirement Version / Representation
    ->
Applicability Basis
    ->
Applicability Determination
    ->
Safeguard / Control Expectation
    ->
Evidence
    ->
Finding
    ->
Risk Treatment / Decision
```

Not every requirement path uses every layer. This trace complements the Evidence Chain, Decision Trace, Source Trace, and Applicability Trace; it does not replace them.

## Conflicts and Overlap

Requirements may overlap, partially overlap, establish different thresholds, use different terminology, impose different obligations, conflict or appear to conflict, or operate at different scopes.

SAR must preserve each source and requirement independently rather than silently merging them. Future authorized analysis may determine how overlapping or conflicting requirements are reconciled. This document creates no legal precedence rules.

## Relationship to Existing SAR Documents

[PRACTITIONER-DISCOVERY.md](PRACTITIONER-DISCOVERY.md) discovers AS-IS practitioner knowledge and process.

[SAR-ARCHITECTURE.md](SAR-ARCHITECTURE.md) defines conceptual SAR risk architecture.

[SAR-INFORMATION-MODEL.md](SAR-INFORMATION-MODEL.md) defines what information SAR represents.

[SAR-INTAKE-MODEL.md](SAR-INTAKE-MODEL.md) defines how facts are collected.

[SAR-DECISION-LOGIC.md](SAR-DECISION-LOGIC.md) defines how supported facts become assessment conclusions.

[SAR-SOURCE-CATALOG.md](SAR-SOURCE-CATALOG.md) defines source identity, provenance, versioning, currentness, and historical preservation.

[SAR-APPLICABILITY-MODEL.md](SAR-APPLICABILITY-MODEL.md) defines how SAR establishes and explains applicability.

This document defines how requirements extracted from registered sources are represented, governed, versioned, and connected to applicability and future safeguard or control expectations.

## Future Work

The following are identified for later work and are not built by this document:

- machine-readable Requirement Catalog schema;
- SAR Requirement ID convention;
- source-to-requirement extraction;
- authoritative requirement population;
- requirement validation workflow;
- requirement change detection and diffing;
- requirement succession and relationship-model implementation;
- applicability rules and matrix;
- safeguard and control catalog;
- requirement-to-safeguard and requirement-to-control mappings;
- NIST SP 800-53 mappings and OSCAL integration;
- HIPAA, HITECH, BAA, and contractual mappings;
- California State, DDS, cloud, AI, and DDS 19-data-element mappings;
- evidence requirements and finding logic;
- automated affected-assessment analysis;
- lifecycle and reassessment automation; and
- authorization and governance roles.

## Design Constraints

This requirement model maintains the following boundaries:

- Source is distinct from Requirement.
- Requirement is distinct from Applicability Determination.
- Requirement is distinct from Safeguard / Control Expectation, Evidence, and Finding.
- Requirement is not synonymous with Control.
- Every authoritative requirement remains source-traceable and version-aware.
- Source text or reference is distinguishable from SAR normalization, interpretation, and guidance.
- Requirement granularity can represent compound source provisions, conditions, and exceptions.
- Normative strength is not silently changed.
- Guidance or benchmark material does not silently become mandatory.
- Requirement scope can be narrower than the entire system.
- One requirement may map to many expectations, and many requirements may map to one expectation.
- NIST is not assumed to be a one-to-one mapping target; the model is framework-neutral.
- Requirement versioning does not rewrite historical assessments.
- Requirement status is distinct from applicability status, and Currentness Unknown does not silently become Current.
- Automated or AI extraction does not silently become verified authority.
- Conflicting or overlapping requirements remain independently traceable.
- No legal precedence rules, actual requirement content, mappings, citations, URLs, section numbers, dates, or legal conclusions are invented.
- No executable schema or rules engine is created.