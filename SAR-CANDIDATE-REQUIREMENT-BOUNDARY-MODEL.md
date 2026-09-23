# SAR Candidate Requirement Boundary Model

## Purpose

This document defines the conceptual model for a persisted, reviewable Candidate Requirement Boundary. It is the semantic bridge between authoritative extracted source content and a governed SAR Requirement.

A Candidate Requirement Boundary records which authoritative normative source content is proposed to form one complete, independently traceable obligation. It preserves the semantic-boundary decision without treating the proposal as an authoritative source statement or as a SAR Requirement.

This document does not create Candidate Requirement Boundary records, SAR Requirement records, control mappings, applicability determinations, parameter assignments, evidence requirements, findings, or risk decisions.

## Core Distinctions

```text
Source
    !=
Candidate Requirement Boundary
    !=
Requirement
    !=
Applicability Determination
    !=
Evidence
    !=
Finding
    !=
Risk Decision
```

- **Source** answers: "What authoritative or reference material was obtained and preserved?"
- **Candidate Requirement Boundary** answers: "Which source content is proposed to form one complete, independently traceable obligation?"
- **Requirement** answers: "What governed obligation representation does SAR establish from a validated boundary?"
- **Applicability Determination** answers: "Why is a source, requirement, or expectation relevant to a particular assessment?"
- **Evidence** answers: "What supports whether an expected condition is satisfied?"
- **Finding** answers: "What conclusion follows from comparing an expected and observed condition?"
- **Risk Decision** answers: "What authorized disposition applies to residual risk?"

A Candidate Requirement Boundary is not an applicability conclusion, evidence, a finding, a safeguard or control expectation, or a risk decision.

## Lifecycle

```text
Authoritative Source
    ->
Deterministic Source Extraction
    ->
Source Object / Normative Structure
    ->
Candidate Requirement Boundary
    ->
Governed Validation
    ->
SAR Requirement
```

### Deterministic Extraction

Deterministic extraction obtains and preserves source identity, exact source version or revision, immutable retrieval identity where available, source objects or provisions, source parts, parameters, relationships, and other source metadata. It must not invent source text or silently discard provenance.

### Semantic Boundary Determination

Selecting a complete normative boundary is semantic. A source parser may identify normative-looking content and a deterministic rule may create proposals for known structural patterns, but a structure alone does not always establish whether a part is an independently complete obligation or must remain joined to its parent or descendants.

Automation or AI may propose boundaries, identify likely parameters, summarize source structure, or flag ambiguity. A proposal is not self-authorizing. Human validation is required before a Candidate Requirement Boundary may produce a governed SAR Requirement.

### Provenance Through Transition

Each transition preserves source family, exact version or revision, immutable retrieval identity where available, source object or provision reference, exact source-part references, extraction/derivation provenance, and later validation provenance. The authoritative source remains authoritative; a candidate does not replace it.

## Core Model

### Essential Identity and Provenance

Every Candidate Requirement Boundary should retain the following conceptual fields:

- **candidate_boundary_id** -- Stable SAR identity for this proposed boundary, distinct from a SAR Requirement ID.
- **source_reference** -- Registered source family plus the exact source version or revision and immutable retrieval identity used for the boundary.
- **source_object_reference** -- The source object or provision containing the normative structure, when the source has one.
- **root_source_part_reference** -- The source part or provision that supplies the boundary's root or inherited operative meaning.
- **included_source_part_references** -- Ordered references to the normative source parts comprising the boundary, including the root.
- **normative_parameter_references** -- References to source-defined parameters used by the included normative content.
- **related_source_relationship_references** -- References to source relationships relevant to understanding provenance or incorporation.
- **boundary_rationale** -- A concise explanation of why the referenced content is proposed as one complete semantic obligation.
- **derivation_method** -- How the proposal was produced, such as deterministic extraction rule, human analysis, or AI-assisted analysis.
- **validation_status** -- The boundary's current validation state.
- **resulting_requirement_reference** -- The SAR Requirement created from a validated boundary, if one exists.

The candidate stores references, not a replacement copy of authoritative prose. Cached or display representations may later be useful, but are not the authoritative record.

### Optional Audit and Review Metadata

The following may be retained where useful, but are not required to establish the boundary itself:

- derivation actor or actor type;
- derivation timestamp;
- validator;
- validation timestamp;
- review notes; and
- succession or replacement references.

This model does not prescribe workflow queues, assignments, service levels, or approval hierarchies.

## Boundary Representation

The model uses a root source-part reference plus ordered included source-part references. A single-part boundary uses the same part as both root and sole included reference. A multi-part boundary uses the root to preserve inherited operative meaning and an ordered included collection to preserve the complete source-defined content.

An unordered collection is insufficient. It loses source order and makes it impossible to distinguish a parent action qualified by descendants from a group of unrelated parts. The references must resolve to the authoritative source structure so hierarchy remains available without copying a source tree.

For example, a source part that says "Specify" followed by required subparts must retain both the root and its ordered descendants. The descendants alone omit the operative directive; the root alone omits what must be specified.

## Source Object Cardinality

One source object or provision may yield zero, one, or many Candidate Requirement Boundaries:

```text
Source Object / Provision
    -> 0..n Candidate Requirement Boundaries
```

This supports a single provision with many independently complete obligations and avoids assuming that every source object has a corresponding requirement. It also avoids treating all source objects as indivisible requirements.

## Zero-Candidate Source Objects

An authoritative source object may exist without independent normative content. It remains registered and traceable even when it produces zero Candidate Requirement Boundaries.

For example, NIST AC-2.10 has no independent normative statement and has an `incorporated-into` relationship to AC-2 item `k`. It produces zero boundaries. Its source identity and incorporation relationship remain preserved and may be referenced from the boundary containing AC-2 item `k`. SAR must not invent normative text or create a placeholder Requirement merely to give every source object an output.

## Parameters

Parameters remain separated by role:

| Information | Layer | Treatment |
|---|---|---|
| Authoritative parameter definition | Source | Retained once with the authoritative source; not copied into the candidate. |
| Normative parameter reference | Candidate Boundary | Referenced when used by included normative source content. |
| Assessment or evaluation parameter reference | Source / assessment provenance | Not Candidate Boundary membership solely because it appears in assessment content. |
| Organization or DDS-assigned parameter value | Assessment, application, or configuration | Assigned later; never changes the authoritative definition. |

A parameter is not itself a Requirement. One parameter may be referenced by multiple boundaries, and one boundary may reference multiple parameters.

## Source Relationships

Candidate Boundaries may reference source relationships relevant to provenance, incorporation, context, or later review. Relationships remain source provenance:

- they do not independently create normative text;
- they do not automatically create Candidate Requirement Boundaries; and
- they do not automatically create Requirements.

The AC-2.10 incorporation relationship is the primary example: it preserves why the AC-2 item `k` boundary has related source-object context without creating an AC-2.10 boundary.

## Profile and Baseline Membership

Profile or baseline membership remains source provenance. A Candidate Requirement Boundary normally resolves this context through its source-object reference rather than copying membership into every boundary.

For NIST, LOW, MODERATE, HIGH, and PRIVACY membership remain facts about the pinned source profiles and source objects. They do not establish applicability to an assessment:

```text
Profile / Baseline Membership
    !=
Applicability Determination
```

## Validation and Succession

The minimum initial validation states are:

- **PROPOSED** -- A boundary has been derived or suggested but not validated.
- **VALIDATED** -- A human has confirmed that the boundary accurately represents one complete, independently traceable source obligation.
- **REJECTED** -- A human has determined that the proposal is not an appropriate boundary.

Only a VALIDATED boundary may produce a governed SAR Requirement.

**SUPERSEDED** becomes appropriate when SAR implements explicit succession or replacement behavior. It should not be added merely to indicate that a proposal changed during review. If a reviewer changes a proposed boundary, SAR preserves the original candidate and creates a revised candidate with review or succession provenance. The eventual Requirement must trace to the actual validated boundary, not only to an earlier proposal.

## Identity and Change

Candidate Boundary identity remains distinct from SAR Requirement identity. The boundary represents a particular semantic selection from a particular source version; the Requirement represents SAR's governed obligation representation.

- A new source version may produce new candidate boundaries, even where the semantic obligation appears unchanged.
- A candidate change produces a revised candidate rather than silently rewriting the prior candidate.
- One candidate may be split into multiple revised candidates, or multiple candidates may be combined into a revised candidate, with explicit provenance.
- A Requirement statement may be normalized or otherwise transformed for SAR use while preserving traceability to the validated boundary and source content.
- A Requirement may survive source-version review as the same conceptual requirement while gaining a new source-bound representation or succession relationship.

This document does not prescribe identifier syntax.

## Relationship to the SAR Requirement Model

A validated Candidate Requirement Boundary establishes the authoritative semantic source boundary from which [SAR-REQUIREMENT-MODEL.md](SAR-REQUIREMENT-MODEL.md) may create a SAR Requirement.

The SAR Requirement remains the governed representation of what the source establishes. Its wording may be transformed for usability or controlled normalization, but it must remain traceable to the validated boundary and authoritative source content. The Candidate Requirement Boundary does not itself determine applicability, select safeguards or controls, prescribe evidence, generate findings, calculate residual risk, or authorize risk acceptance.

## Cross-Source Design

This model is source-neutral. A source object, provision, part, and normative content may be represented by:

- a standards clause and subclauses;
- a statutory or regulatory provision and conditions or exceptions;
- a contractual clause and incorporated terms;
- a policy section and ordered directives;
- a procedural step and mandatory criteria; or
- another authoritative requirement source.

The source's native identifiers and hierarchy remain in the source layer. Candidate Boundary references preserve that structure without requiring OSCAL controls, OSCAL parts, or any other specific source format.

## NIST Examples

These examples are conceptual demonstrations, not production Candidate Requirement Boundary records and not Requirement records.

| Source object | Root | Included normative parts | Normative parameter references | Candidate result |
|---|---|---|---|---|
| AC-2 | `ac-2_smt.a` | `ac-2_smt.a` | None | One single-part candidate. |
| AC-2 | `ac-2_smt.d` | `d`, `d.1`, `d.2`, `d.3` | `ac-02_odp.02` | One multi-part candidate; root supplies the directive and descendants supply its required content. |
| AC-2 | `ac-2_smt.h` | `h`, `h.1`, `h.2`, `h.3` | `ac-02_odp.05`, `.06`, `.07`, `.08` | One multi-part candidate; shared action and recipients remain joined to triggers and periods. |
| AC-2.7 | `ac-2.7_smt.a` through `.d` | Each item separately | `ac-02.07_odp` on `a` | Four candidates; each item has a distinct operative action. |
| AC-2.10 | None | None | None | Zero candidates; preserve incorporation into `#ac-2_smt.k`. |
| AC-2.12 | `ac-2.12_smt.a`; `ac-2.12_smt.b` | Each item separately | `ac-02.12_odp.01`; `ac-02.12_odp.02` | Two candidates for distinct monitor and report actions. |
| SI-12 | `si-12_smt` | `si-12_smt` | None | One single-part candidate. |
| SI-12.2 | `si-12.2_smt` | `si-12.2_smt` | `si-12.2_prm_1` | One single-part candidate; assessment-objective-only parameters are excluded from boundary membership. |

## Design Principles

- Preserve authoritative source meaning.
- Never invent missing normative content.
- Extract and preserve source content before interpreting a semantic boundary.
- Keep semantic-boundary decisions reviewable.
- Treat AI and automated proposals as non-self-authorizing.
- Preserve source provenance through every transformation.
- Accept zero candidates as valid.
- Support one source object producing many candidates.
- Treat one candidate as one proposed semantic obligation, without assuming every source part is one obligation.
- Keep source, Candidate Boundary, Requirement, applicability, evidence, findings, and risk decisions distinct.
- Do not collapse identity across source, candidate, and Requirement lifecycle layers.

## Future Work

This model does not create:

- a machine-readable Candidate Requirement Boundary schema;
- Candidate Requirement Boundary records;
- SAR Requirement records or identifier syntax;
- automated semantic-boundary selection;
- source-to-requirement transformations;
- applicability rules or determinations;
- parameter assignments;
- safeguard or control mappings;
- evidence requirements, findings, or risk decisions; or
- validation workflow or authorization roles.