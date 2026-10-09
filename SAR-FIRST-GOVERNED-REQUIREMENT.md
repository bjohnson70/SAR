# SAR First Governed Requirement

**SAR-CODEX-069 | GOVERNANCE DESIGN APPROVAL RECORD**

> **PROPOSED - NOT REQUIREMENT-APPROVED - NOT EXECUTABLE**

This document records DDS CISO approval of five Requirement-governance design recommendations. It is not a Requirement Catalog record, an implemented workflow, or an assessment instruction. It does not create or approve the SI-12(3) Requirement proposed below.

## 1. Purpose and Scope

Design the controlled transition from a human-validated Candidate Requirement Boundary to a separately governed SAR Requirement, using NIST SP 800-53 Rev. 5 SI-12(3) as the first example.

This proposal preserves:

```text
Authority / Source Content != SAR Executable Content
Source != Candidate Boundary != Requirement != Applicability Basis != Control / Safeguard
```

It does not modify a governed model, establish a production identifier convention, populate a Requirement Catalog, assign a parameter, determine applicability, define safeguards or evidence, create executable rules, or make an assessment finding or risk decision.

The five governance principles identified below are approved design. Lifecycle mechanics, schemas, ownership assignments, workflows, and executable policy remain unimplemented unless explicitly identified as existing semantics.

## 2. Verified Baseline and Approved Source Boundary

**Repository baseline:** `main`, `HEAD == origin/main == dfe1400fa6dbcc7c996ed002578d39f0c03c1fa6`; worktree and index were clean before this design task.

**Validated Candidate Requirement Boundary:** `cbr-nist-sp800-53-rev5-si-12-3-smt`

| Boundary element | Verified value |
|---|---|
| Status | `VALIDATED` |
| Source object | `si-12.3` - Information Disposal |
| Root and included normative part | `si-12.3_smt` |
| Normative parameter reference | `si-12.3_prm_1` |
| Parent source relationship | `si-12.3 --required--> #si-12` |
| Boundary rationale | Distinct enhancement statement under parent SI-12; source relationship retained. |
| Source release / pinned upstream revision | NIST SP 800-53 Rev. 5 OSCAL release `5.2.0`, commit `78650f02ad9321bb7b817846f8fbd4f2bcd620de` |

The [CISO validation package](SAR-SI-12-3-BOUNDARY-VALIDATION.md) records approval by the DDS CISO, dated 2026-10-08, with no additional conditions. Its scope is **source-boundary fidelity only**. It does not approve creation of this proposed Requirement, applicability, a parameter value, or assessment content. The existing candidate and pinned source references are inputs to this design, not objects modified by it.

## 3. Existing Governance Constraints

### Existing governed semantics

- The Candidate Requirement Boundary model distinguishes Source, Candidate Boundary, Requirement, applicability, evidence, finding, and risk decision. Only a `VALIDATED` boundary may produce a governed Requirement.
- The Requirement Model says a Requirement is source-bound, distinct from a safeguard/control, version-aware, and traceable to exact source provision. It calls for a stable internal Requirement ID but does not define identifier syntax, a final schema, or an approval workflow.
- The Requirement Model gives conceptual validation states (`unverified`, `source-matched`, `reviewed`, `approved`, `superseded`, `requires review`) and separately gives conceptual Requirement/currentness statuses (`candidate`, `verified`, `current`, `superseded`, `withdrawn`, `expired` where applicable, `currentness unknown`, `requires review`). Neither list is an operational lifecycle implementation.
- The Source Catalog distinguishes current source from the immutable source version used by an assessment and requires historical source provenance to be preserved.
- Applicability is distinct from source registration and Requirement validation. A source or profile's membership does not establish that it applies to an assessment.
- The Assessment Protocol and Deterministic Content Model are proposals, not an operational engine or approved rule set. They prohibit model-invented requirements, authority, applicability rules, thresholds, or approval logic.

### Current repository content boundary

The repository has a Candidate Requirement Boundary schema and narrow structural validator. They check candidate structure and correspondence to the source slice; they do not create Requirements or establish assessment outcomes. No populated Requirement Catalog entry for SI-12(3), Requirement-specific schema, production Requirement ID convention, or Requirement promotion workflow was found. The catalog described in [SAR-REQUIREMENT-MODEL.md](SAR-REQUIREMENT-MODEL.md) is future content.

The source manifest is [sources/nist-sp800-53-rev5.oscal-source.yaml](sources/nist-sp800-53-rev5.oscal-source.yaml). It pins the upstream NIST OSCAL repository commit and identifies the catalog artifact; the candidate/source slice is a limited extraction, not the complete raw catalog. The pinned source relationship and parameter remain provenance, not executable SAR content.

## 4. Proposed Requirement Representation Contract

The following is the **CISO-approved minimum conceptual representation contract for future governance**. It is not a JSON/YAML schema or a production record. Any eventual Requirement record should preserve typed references to these elements rather than flattening them into a single prose field.

| Concern | Minimum proposed content |
|---|---|
| Logical identity | Stable SAR-internal logical identity, distinct from NIST's control ID and the Candidate Boundary ID. No production syntax assigned here. |
| Version | Immutable Requirement representation version; distinguish the logical identity from each source-bound/versioned representation. Record predecessor/successor or supersession links. |
| Lifecycle | CISO-approved design requires governed lifecycle/status transitions, kept distinct from source currentness and assessment applicability. Exact state vocabulary and transition mechanics remain to be specified and implemented. |
| Ownership | Named SAR Requirement content owner role responsible for source monitoring, review coordination, change proposal, and provenance. No specific role/person is designated here. |
| Approval authority | Human authority and delegation for Requirement approval, separate from Candidate Boundary validation and risk acceptance. The CISO-approved design requires recorded human authorization; the specific approver role and delegation remain unassigned. |
| Source identity | Source family/source identifier, publisher, source title, release/version, immutable revision/commit, source artifact path, and retrieval/integrity references where available. The manifest's `source_family_id` is `nist-sp800-53-rev5`; do not imply a settled SAR Source ID syntax. |
| Source provision | Source object `si-12.3`, part `si-12.3_smt`, exact authoritative citation/reference, and source relationship `required` to `#si-12`. Preserve source text/reference separately from SAR's normalized representation. |
| Boundary provenance | Exact Candidate Boundary identity `cbr-nist-sp800-53-rev5-si-12-3-smt`, status `VALIDATED`, its revision/snapshot, and its CISO source-fidelity decision record. Boundary identity does not become Requirement identity. |
| Normative representation | Controlled SAR statement that preserves the source's obligation, scope, conditions, qualifiers, and normative strength. Keep exact source text/reference available; do not turn guidance or assessment objectives into additional obligations. |
| Scope/dependencies | Source object/part scope, parent relationship, dependencies, qualifications, exclusions and their source references. Do not imply that SI-12.3 applies to every system or information set. |
| Parameters | Source-defined parameter reference and unresolved/bound state. Keep the authoritative parameter definition distinct from any organization-specific assignment and its authority, scope, effective time, and provenance. |
| Validation/approval evidence | Separate records for source-boundary validation and Requirement content review/approval: decision maker/authority, date, scope, exact version considered, rationale, conditions, and decision provenance. Structural validator output is not human approval. |
| Change control | Change reason/type, affected source/boundary/Requirement versions, review and approval history, effective/supersession decision where governed, downstream dependency analysis, and links to prior records. Never overwrite history. |

### Approved identity principle and remaining implementation detail

1. **Embed source identifiers in the SAR ID.** Human-readable, but couples identity to source numbering and can be awkward after split/merge or source changes.
2. **Use a stable opaque SAR logical ID with a separate version and source keys.** Keeps SAR identity stable while source object, boundary, and immutable source version remain explicit provenance; IDs need not expose sensitive governance semantics.
3. **Use source key as the only identity.** Simple initially, but does not satisfy the Requirement Model's direction toward a stable SAR-internal identity independent of source title/location and complicates succession.

**CISO decision: APPROVED - alternative 2.** Use a stable opaque SAR Requirement logical identity with a separate immutable version and explicit source/candidate keys. The other alternatives were considered but not selected. Exact production syntax is not authorized; use only a placeholder such as `[SAR Requirement ID: to be assigned under approved convention]`. Do not derive a production ID from `SI-12(3)` or the candidate ID.

## 5. Approved Lifecycle Design and Promotion Gates

The CISO approved the lifecycle and gate principles in this section as governance design. The states, actors, evidence records, and transitions remain conceptual until a workflow is separately specified and implemented. Requirement governance state must not be conflated with source currentness, applicability, or assessment status.

| Approved conceptual stage/transition | Prerequisites and validation | Permitted actor / approval | Evidence and provenance | Return/reject/change behavior |
|---|---|---|---|---|
| **1. Validated source boundary** -> **2. Proposed SAR Requirement** | Candidate is human-validated; pin resolves; source part, relationships, parameter references, and boundary approval scope are intact. Draft a representation from the validated boundary only. | Content owner or authorized drafter may prepare a proposal; drafting does not authorize it. | Candidate ID/version, pinned source identity/part, parameter and relationship refs, source text/reference, draft provenance. | Return to source review if references or content do not resolve. A boundary change follows Candidate Boundary succession/revalidation; do not silently edit the validated source decision. |
| **2. Proposed SAR Requirement** -> **3. Human-reviewed Requirement** | Review exact source fidelity, normalized wording, semantic role/normative strength, granularity, parent/dependency context, parameter semantics, scope, identity strategy, version, authority/reference role treatment, and unresolved fields. | Qualified human reviewer(s) designated by future governance; reviewer is not automatically the author or automated validator. | Review checklist/notes, reviewer identity/authority, exact version reviewed, discrepancies, disposition, date, provenance. | Return for correction or reject with rationale. Any changed boundary returns to boundary validation; any content interpretation change creates a new proposed Requirement revision. |
| **3. Human-reviewed Requirement** -> **4. Approved governed Requirement** | All blocking review items resolved or explicitly accepted within the approval scope; approval record names the exact Requirement version and any parameterized/unresolved limitations. No applicability or executable rule is implied. | Explicit authorized human Requirement approver under a separately approved delegation. Candidate validation approval alone is insufficient. | Approval authority, version, scope, rationale, conditions, effective state if governed, source/boundary references, parameter-state declaration, date, and immutable decision provenance. | Return/defer/reject with rationale. No default approval from validator pass, silence, a “ready” label, or CISO source-boundary approval. |
| **4. Approved governed Requirement** -> **5. Superseded or retired Requirement** | Approved change-control review identifies source/interpretation change, replacement, withdrawal, expiry, or retirement basis; assess linked requirements, rules, mappings, and assessments. | Authorized Requirement owner proposes; designated human approval authority approves the change/retirement under future governance. | New/old versions, reason, source comparison, impact analysis, effective/supersession or retirement record, retained history. | Keep previous version immutable. Where transition is disputed or effects unclear, mark for review/unresolved according to future vocabulary; do not silently remove it. |

`Superseded` and `retired/withdrawn` should be distinct outcomes if their operational consequences differ; the precise vocabulary remains open. No candidate-boundary status such as `VALIDATED` should be reused to mean Requirement approval.

**Gate distinction:** Boundary fidelity approval answers “does this candidate faithfully select the cited source obligation?” Requirement governance approval answers “does SAR approve this source-bound representation, identity, semantics, dependencies, and lifecycle record?” Applicability answers a different question for a particular assessment target. None implies the others.

The approved design requires a human-validated source boundary, explicit provenance and parameter treatment, human Requirement review, recorded approval authority/decision, and change/supersession handling before promotion. Approval of that design does not mean those gates are implemented or that this example has passed them.

## 6. SI-12(3) Proposed Requirement

> **PROPOSED — NOT REQUIREMENT-APPROVED — NOT EXECUTABLE**

This example is a human-review proposal, not an operational Requirement Catalog entry.

| Proposal field | Proposed content |
|---|---|
| Requirement identity strategy | Stable opaque SAR logical ID plus explicit version, pending approval of an ID convention. Placeholder only: `[SAR Requirement ID: to be assigned under approved convention]`. |
| Proposed lifecycle state | Proposed SAR Requirement; not reviewed or approved as a Requirement. The source boundary alone is `VALIDATED`. |
| Candidate reference | `cbr-nist-sp800-53-rev5-si-12-3-smt`, `VALIDATED` for source-boundary fidelity only. |
| Source | NIST SP 800-53 Rev. 5 OSCAL content, release `5.2.0`, upstream commit `78650f02ad9321bb7b817846f8fbd4f2bcd620de`; source artifact `nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json`. |
| Exact provision | Source object `si-12.3`, normative part `si-12.3_smt`; parent source relationship `required` to `#si-12`. |
| Normative statement reference | Exact source text is recorded in [the boundary validation package](SAR-SI-12-3-BOUNDARY-VALIDATION.md). Preserve source reference `si-12.3_smt`; any SAR statement must preserve its normative meaning and parameter insertion, not replace the source text. |
| Proposed controlled representation | “Use the organization-defined techniques to dispose of, destroy, or erase information following the retention period.” This is a non-executable summary. It neither supplies a technique nor establishes the retention period. |
| Source parameter | `si-12.3_prm_1`, source label `organization-defined techniques`; assignment remains unresolved. |
| Owner and approval authority | Requirement content owner and specific approval authority/delegation are not assigned; define them under the approved human-authorization design before any Requirement approval. |
| Applicability | `UNRESOLVED / GOVERNED RULE NOT YET POPULATED`. No assessment target/basis or profile selection is supplied by this proposal. |
| Traceability | Preserve links to source family/revision/artifact/object/part, parent `required` relationship, candidate boundary and approval, Requirement revision, parameter assignment when governed, and subsequent applicability/expectation/evidence records if separately authorized. |
| Remaining human questions for any future Requirement approval | Is the controlled representation faithful and appropriately scoped for Requirement governance? Which owner and delegated approver roles apply? What authorized policy/decision assigns the parameter, at what scope and effective version? What authority-versus-benchmark role and applicability basis, if any, apply to a particular assessment? |

The source says to use “the following techniques” but does not itself identify their assigned values here. The proposed summary retains that dependency rather than replacing it with a disposal method. No evidence threshold, implementation expectation, assessment criterion, or universal applicability is inferred.

## 7. Parameter Governance

Keep these layers separate:

1. **Authoritative source parameter:** `si-12.3_prm_1`, defined by the pinned NIST OSCAL source as `organization-defined techniques` and referenced by `si-12.3_smt`.
2. **Organization-defined value:** a future authorized assignment, not present in this repository and not set by this proposal.
3. **Assignment authority and record:** owner/role authorized under applicable organizational governance; supporting policy/decision; system, information, or organizational scope; effective date/version; rationale; approver; and change history. None is currently identified here.
4. **Unresolved state:** until an authorized assignment exists, retain `UNRESOLVED`/unassigned as the explicit parameter binding state. Do not treat empty, omitted, or unknown as a value.

### Proposed gate placement

| Activity | Must the parameter value exist first? | Proposed handling |
|---|---|---|
| Requirement governance approval | **Not necessarily. CISO-approved design:** a Requirement may be approved with an unresolved organization-defined parameter when the dependency and unassigned state are explicit and approval cannot be mistaken for assessment readiness. | Separate Requirement approval from assessment-usable/configured readiness. The approved principle does not assign a value or define the operational readiness state. |
| System-specific applicability determination | The parameter value is **not inherently a prerequisite** to decide whether the source/Requirement is relevant, because applicability has its own facts and basis. A future approved applicability rule may identify a dependency. | Applicability can be evaluated only under an approved rule; if that rule requires the parameter or its assignment context, leave the determination unresolved until supplied. |
| Safeguard expectation/evaluation | **Yes, before evaluating conformance to a parameter-dependent expectation.** | First govern the separate expectation and authorized assignment; otherwise stop as unresolved/not evaluable, not as a failure. |
| Deterministic assessment comparison | **Yes, before a rule that compares implementation against the assigned techniques.** | Rule must consume a versioned, scoped assignment. No value or comparison logic exists in this task. |

These gate placements follow the approved design principle; operational policy and rule behavior remain unimplemented. No specific technique, scope, owner, date, or retention duration is supplied.

## 8. Applicability Separation

```text
Source != Candidate Boundary != Requirement != Applicability Basis != Control/Safeguard
```

An approved Requirement could exist in SAR without applying to every assessment. Approval would establish a governed source-bound content object; applicability is a separate determination for a defined target (for example, a system, service, data scope, or relationship) using supported facts and an approved basis/rule.

For any future assessment use, preserve independently:

- whether the NIST source is treated as applicable authority or reference/benchmark for that assessment, and the basis for that role;
- the assessment target and scope;
- system/data/use/relationship facts relevant to an approved applicability rule;
- the rule/version and each supporting basis, result, rationale, and provenance;
- conflicts, missing facts, or interpretation questions.

The source's presence, the candidate's `VALIDATED` status, Requirement approval, and PRIVACY profile membership do not establish system applicability or select a baseline. No applicability rule is populated. Retain **`UNRESOLVED / GOVERNED RULE NOT YET POPULATED`** until separate governance supplies one. Conflicting or insufficient facts must not be defaulted to Applicable or Not Applicable.

## 9. Execution Boundary

If separately approved, a Requirement approval could establish only SAR's governed normative content, version, source/candidate trace, semantic representation, owner/approval provenance, and declared dependencies/limitations.

It would not automatically establish:

- applicability to a system or selection of a NIST baseline/profile;
- source role as applicable authority rather than benchmark for a particular assessment;
- a required safeguard implementation or control mapping;
- evidence expectations, evidence sufficiency, or validation criteria;
- compliance, a deterministic result, a finding, or severity;
- inherent or residual risk, risk acceptance, or deployment authorization.

Before SAR could deterministically evaluate SI-12(3), future governance would need, at minimum: a governed Requirement representation and version; approved applicability basis/rule; authorized, scoped parameter assignment; distinct safeguard/control expectation and mapping if used; evidence expectation and validation authority/criteria; deterministic comparison rule with unknown/conflict behavior; controlled trace/output contract and any gates. None is authorized or created here. Missing any required governed input leaves that evaluation path unresolved, not silently executable.

## 10. Versioning and Change Control

Preserve immutable revisions and decision provenance; never rewrite what an earlier assessment or approver considered. A change triggers review and impact analysis, not automatic propagation into approved or executable content.

| Change event | Proposed required response |
|---|---|
| Corrected source transcription or source-slice error | Verify against the exact pinned source; record correction and integrity/provenance. If the validated boundary or its meaning changes, create a revised Candidate Boundary and obtain boundary revalidation. Review every dependent Requirement draft/version. |
| New NIST source revision | Pin and verify the new revision; compare affected source objects/parts/parameters/relationships; decide materiality through human review. Do not replace the source revision used by an existing Requirement or assessment. Create a source-bound Requirement revision and approval if meaning/scope changes or governance requires re-attestation. |
| Changed Candidate Boundary | Preserve the prior boundary and approval. Create a separately identified/revisioned candidate under future succession rules; human boundary validation is required before any Requirement derives from it. Reassess any linked Requirement proposal. |
| Changed Requirement interpretation, scope, or normative representation | Record a new Requirement revision, rationale, source/boundary links, impact review, review/approval decisions, and effective/supersession handling where governed. Material semantic changes require new Requirement approval. |
| Newly assigned or changed parameter | Record authorized source/policy, owner/approver, value, scope, effective version/date, and prior assignment history. Determine affected assessments and parameter-dependent expectations/rules. Do not mutate the source parameter or imply old assessments used the new value. |
| Changed applicability rule | Version and approve the rule separately; preserve prior rule/determinations. Analyze affected Requirements and assessments, then reevaluate only through separately authorized workflow. |
| Superseded, withdrawn, or retired Requirement | Preserve prior versions and links; record authority, reason, decision date, effective semantics if established, replacement if any, and impacted rules/assessments. Do not delete historical records. |

Whether a change requires revalidation, Requirement approval, or downstream reassessment depends on which source-bound content or interpretation changed and on future approved materiality/impact rules. Until those rules exist, require documented human triage and preserve the prior state. Never automatically turn an upstream source update into SAR executable content.

## 11. CISO Decisions and Approval Effects

The five decisions below were explicitly approved by the DDS CISO on 2026-10-08. Approval consequences refer only to adopting these governance design principles; none approves the example Requirement itself or authorizes implementation.

### Decision A - Requirement identity and lifecycle

- **Approved decision:** stable opaque SAR logical ID plus explicit immutable Requirement version; keep Candidate Boundary ID, NIST source/control IDs, source version, lifecycle state, currentness, and applicability as separate references/axes. Exact production ID syntax remains unauthorized.
- **Alternatives considered, not selected:** source-derived readable ID; source key as sole identity; defer identity design.
- **Rationale:** supports continuity across source edits and split/merge while preserving traceability; no production syntax is currently defined.
- **Unresolved dependencies:** ID authority/namespace, versioning rules, ownership, workflow tooling.
- **Approval effect:** authorizes future definition of an identity convention; it does not create an operational record or approve SI-12(3) content.

### Decision B - Requirement approval boundary

- **Approved decision:** Requirement governance approval establishes an approved normative representation, verified source provenance, controlled Requirement identity/version, and recorded human authorization. It does not establish assessment applicability, safeguard implementation, evidence sufficiency, compliance, findings, severity, risk acceptance, or deployment authorization.
- **Alternatives considered, not selected:** merge Requirement and applicability approval; treat boundary validation as Requirement approval; delegate human approval to automated validation.
- **Rationale:** preserves separation between source-bound content, assessment applicability, safeguards, evaluation, and human risk decision. Combining these would exceed this task's authority and existing model distinctions.
- **Unresolved dependencies:** approver/delegation, approval standard, effective-state meanings, whether parameterized Requirements may be approved before assignment.
- **Approval effect:** approves this design boundary only. Future approval of an actual Requirement remains a separate human decision; no applicability, executable rule, or risk decision follows.

### Decision C - Parameter governance

- **Approved decision:** store the source parameter reference separately from any organization-defined assignment. A governed Requirement may be approved with unresolved parameters, but parameter-dependent evaluation remains blocked until the assignment is authorized, scoped, versioned, and traceable to its governing decision or source.
- **Alternatives considered, not selected:** require assignment before any Requirement approval; treat the parameter as optional/irrelevant. Assessment-level assignment remains possible only if future authority establishes it.
- **Rationale:** preserves the source's open parameter without inventing a value and makes readiness dependencies explicit. Assessment-level assignment is only an option if authorized policy says values vary by assessment; it is not established here.
- **Unresolved dependencies:** authorized assigning role, governing policy, value format, scope, effective date, and treatment of missing/conflicting assignments.
- **Approval effect:** authorizes design of an assignment process only; no technique or retention period is assigned now.

### Decision D - Promotion prerequisites

- **Approved decision:** promotion into an approved governed Requirement requires a human-validated boundary; complete source/candidate provenance; controlled identity/version; normative fidelity checks; explicit parameter dependencies; human Requirement review; recorded approval authority/decision; and change/supersession handling.
- **Alternatives considered, not selected:** promote directly from candidate validation; rely on structural validator pass. Applicability and safeguard mapping remain distinct from Requirement promotion.
- **Rationale:** the boundary approval is limited to source fidelity; schema validation is mechanical only. Applicability and safeguard mapping are separate relationships and should not be prerequisites to accurately representing a source-bound Requirement unless CISO chooses otherwise.
- **Unresolved dependencies:** formal review checklist, approver role, validation evidence format, parameterized-state policy, version/return/reject rules.
- **Approval effect:** establishes design prerequisites only. It is not evidence that the SI-12(3) Requirement has passed them.

### Decision E - Future implementation scope

- **Approved decision:** the next proposed implementation increment is limited to a minimum governed Requirement representation/schema, non-executable promotion validation, human approval recording, and version/provenance controls. No such capability is implemented by this approval checkpoint.
- **Alternatives considered, not selected:** add SI-12(3) directly as a production Requirement; implement applicability or assessment rules in the same increment.
- **Rationale:** the smallest next step can test representation and traceability without activating unsupported assessment behavior. Do not create it until separately authorized.
- **Unresolved dependencies:** approved data format/storage, exact identity convention, owner, approval workflow, parameter governance, and change control.
- **Approval effect:** establishes a future implementation scope only. It does not authorize SAR-CODEX-070 or execution of that increment.

## 12. Future Implementation Prerequisites

The five design principles are approved; implementation still requires separate authorization. Future work may define:

1. Requirement identity and version convention, owner, state axes, approval authority, and decision record.
2. Requirement representation contract and machine-readable form if approved, including exact source/candidate references and immutable history.
3. Parameter assignment authority, source/policy, scope, effective dating/version, unresolved/conflict handling, and change-impact behavior.
4. Applicable source role and an assessment-specific applicability basis/rule with rationale and provenance.
5. Separate safeguard/control expectation, applicability relationship, and source/risk rationale if SAR will evaluate an expectation.
6. Evidence expectations, validation authority, evidence sufficiency rules, and evidence provenance.
7. Deterministic comparison rules, inputs, versioning, outputs, unknown/conflict behavior, gates, and test fixtures only after each policy is governed.
8. Trace from facts to source version/part, Candidate Boundary, Requirement/version, parameter binding, applicability determination, expectation, evidence/validation, rule/result, and any later human decision.

These are future prerequisites, not populated objects or permission to implement them in this task.

## 13. Unresolved Issues and Limitations

- No Requirement Catalog entry, production Requirement schema, stable ID syntax, or operational promotion workflow is present.
- The source-boundary CISO approval remains limited to boundary fidelity. The later governance approval covers design principles only and does not approve a Requirement representation or any downstream use.
- Detailed Requirement owner assignment, approver delegation, state mapping, currentness/retirement mechanics, and approval-record implementation remain unresolved implementation details under the approved governance principles.
- `si-12.3_prm_1` has no assigned technique value. Assignment authority, policy, scope, effective date, and conflict behavior are unknown. SI-12.3 does not supply a retention duration.
- `UNRESOLVED / GOVERNED RULE NOT YET POPULATED` remains the applicability status; no system facts, basis, source role for a particular assessment, or applicability rule is established.
- No safeguard expectation, evidence criterion, validation rule, deterministic comparison, finding, severity, risk formula, or report rule is approved or populated.
- The repository's upstream source pin is available in a manifest and limited source slice; the raw catalog is not bundled. The prior source validation package documents retrieval/integrity review limitations.

No Requirement is created or approved by this artifact. No assessment or executable content is authorized.

## 14. CISO Governance Approval Record

| Decision field | Record |
|---|---|
| Decision authority | DDS CISO |
| Decision date | 2026-10-08 |
| Workflow | SAR-CODEX-069 |
| Disposition | **APPROVE ALL FIVE GOVERNANCE RECOMMENDATIONS** |
| Additional conditions | None |
| Approval scope | Requirement governance design only |

SAR-CODEX-069 is workflow tracking metadata. It is not a production Requirement ID or schema identifier.

| Decision | Approved design principle |
|---|---|
| A - Identity and lifecycle | Stable opaque SAR Requirement logical identity; separate immutable Requirement version; explicit source identity/provenance; governed lifecycle/status transitions; preserve historical versions and approval decisions. Exact production ID syntax is not authorized. |
| B - Requirement approval scope | Approval establishes the approved normative representation, verified source provenance, controlled identity/version, and recorded human authorization only. Applicability, safeguards, evidence sufficiency, compliance, findings, severity, risk acceptance, and deployment authorization remain separate and unapproved. |
| C - Parameter governance | A Requirement may be approved with unresolved organization-defined parameters if dependencies/state remain explicit. Parameter-dependent evaluation is blocked until assignment is authorized, scoped, versioned, and traceable to its governing decision/source. No value is assigned here. |
| D - Promotion prerequisites | Require a human-validated boundary; complete source/candidate provenance; controlled identity/version; normative fidelity checks; explicit parameter dependencies; human Requirement review; recorded approval authority/decision; and change/supersession handling. These design requirements do not mean this SI-12(3) proposal passed them. |
| E - Next implementation scope | Limit the next proposed increment to minimum Requirement representation/schema, non-executable promotion validation, human approval recording, and version/provenance controls. These capabilities are not implemented here; this decision does not authorize SAR-CODEX-070. |

### Three Separate Decisions

1. **SI-12(3) boundary validation:** DDS CISO approval on 2026-10-08, limited to fidelity of the corrected Candidate Requirement Boundary to the pinned source; candidate remains `VALIDATED`.
2. **Requirement governance design:** the five design recommendations above are approved by DDS CISO on 2026-10-08 under SAR-CODEX-069.
3. **Actual SI-12(3) SAR Requirement approval:** **NOT APPROVED / NOT DECIDED.** The example remains `PROPOSED - NOT REQUIREMENT-APPROVED - NOT EXECUTABLE`; a future authorized human decision would be required.

The applicability state remains `UNRESOLVED / GOVERNED RULE NOT YET POPULATED`. The source parameter `si-12.3_prm_1` remains unassigned. No Requirement Catalog entry, schema, executable rule, safeguard, evidence expectation, finding, or assessment is created or authorized by this design approval.

**Record scope:** Requirement governance design approval only; the SI-12(3) Requirement itself remains unapproved and unimplemented.
