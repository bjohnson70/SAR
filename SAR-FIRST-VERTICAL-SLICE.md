# SAR First Deterministic Vertical Slice

## 1. Purpose and Status

**SELECTION / DESIGN PROPOSAL - NOT POPULATED, VALIDATED, OR EXECUTABLE**

This document recommends one first vertical slice for future SAR content governance. It selects a bounded source area to govern and test end-to-end; it does not establish source applicability, validate a Candidate Requirement Boundary, create a SAR Requirement, map a control, define evidence sufficiency, create an executable rule, or make an assessment finding.

The selection objective is the smallest useful proof of:

```text
Assessment Fact(s)
    -> Applicability Determination
    -> Requirement
    -> Control / Safeguard Expectation
    -> Evidence Expectation
    -> Validation
    -> Finding / Gap
    -> Report Projection
```

The chosen area is a **candidate for governance work**, not an approved assessment rule or vertical slice ready for implementation. Existing source/candidate artifacts retain their current statuses.

### Status Terms

- **EXISTING GOVERNED CONTENT** means repository content explicitly has a governed status and authority for its stated purpose.
- **CANDIDATE SOURCE / BOUNDARY** means a source or proposed boundary is available for review but is not a validated SAR Requirement.
- **PROPOSED DESIGN** means a model or future structure described here for governance consideration.
- **UNRESOLVED / GOVERNED RULE NOT YET POPULATED** means the required semantic decision is not available and must not be inferred.
- **NON-NORMATIVE STRUCTURAL EXAMPLE** means placeholders only; it creates no SAR content or result.

## 2. Selection Criteria

Candidate slices were compared against these criteria:

- **A. Source clarity:** exact authoritative source, version, and citeable boundary.
- **B. Fact clarity:** relevant facts can come from documents or ordinary factual responses.
- **C. Applicability clarity:** a small supportable basis can be governed without resolving the whole legal/applicability architecture.
- **D. Requirement boundary:** the scope can become a small, human-validated requirement set.
- **E. Safeguard clarity:** a separate expectation can be governed without conflating Requirement and Control.
- **F. Evidence observability:** plausible evidence can be supplied/inspected, with limits stated.
- **G. Deterministic gap potential:** a useful comparison can be defined without invented severity or risk scores.
- **H. Practitioner value:** a result would inform actual review work.
- **I. Traceability:** the end-to-end fact/source/requirement/evidence chain is tractable.
- **J. Scope:** the set is small enough to govern and test.
- **UX fit:** available documents can establish much of the factual state before minimal clarification.

Qualitative ratings are only a development-selection aid: `STRONG`, `MODERATE`, and `WEAK` do not describe SAR risk, severity, evidence validation, Assessment Depth, approval, or disposition.

## 3. Candidate Inventory and Comparison

### Candidate 1: NIST SP 800-53 Rev. 5 SI-12.3 - Information Disposal

- **Authoritative source:** pinned NIST SP 800-53 OSCAL source snapshot, content release `5.2.0`, upstream repository commit `78650f02ad9321bb7b817846f8fbd4f2bcd620de`; source object `si-12.3`, statement part `si-12.3_smt`, candidate boundary `cbr-nist-sp800-53-rev5-si-12-3-smt`.
- **Current repository content:** `sources/nist-sp800-53-rev5.oscal-source.yaml`, `sources/nist-sp800-53-rev5.ac-2-si-12.slice.yaml`, and `sources/nist-sp800-53-rev5.si-12.candidate-boundaries.yaml`. The candidate boundary is `PROPOSED`, with a referenced organization-defined parameter. No source text is duplicated here.
- **Likely facts:** what information/data the system retains or disposes; relevant information categories and system scope; documented retention/disposal practices; responsible parties and external services; and what records or artifacts exist. These are potential facts, not mandatory policies or requirements.
- **Applicability complexity:** weak under current governance; bounded as a future governance question. The source object has PRIVACY profile membership in the pinned source representation, but profile membership does not establish profile selection or assessment applicability. SAR has no approved NIST profile-selection or SI-12 applicability rule. A case-specific applicability basis/rule would need governance.
- **Requirement-validation effort:** low-to-moderate in scope, but still requires human validation of exact source provision, normative meaning, parameter treatment, scope, and the proposed boundary before any SAR Requirement is created.
- **Evidence possibilities:** retention/disposal policy or procedure, system configuration/export, data lifecycle documentation, disposal service record, or scoped test/attestation if later approved as relevant. These are evidence candidates, not current SAR expectations or sufficiency criteria.
- **Gap potential:** useful comparison could be possible after an applicable Requirement, a separate safeguard expectation, evidence expectation, and validation rule are approved. Missing documentation alone would mean evidence missing/unresolved, not that disposal safeguards are absent.
- **Maturity / complexity / usefulness:** pinned source and a single proposed boundary make a tractable starting point; parameter and applicability work remain. Data retention/disposal is understandable and useful to privacy/security reviewers and can often be documented.

### Candidate 2: NIST SP 800-53 Rev. 5 AC-2 - Account Management

- **Authoritative source:** same pinned NIST OSCAL source snapshot and source slice, source object `ac-2`.
- **Current repository content:** `sources/nist-sp800-53-rev5.ac-2.candidate-boundaries.yaml` contains 12 proposed AC-2 boundaries; AC-2.10 has zero independent candidates and is recorded as incorporated into AC-2 item k. Multiple organization-defined parameters and source-part relationships are represented.
- **Likely facts:** user/account categories, administrators, account provisioning/deactivation processes, shared/service accounts, reviews, and available account records; exact intents and scope need governance.
- **Applicability complexity:** moderate-to-high. AC-2 profile membership spans LOW/MODERATE/HIGH in the source metadata, but the applicable profile is not selected by SAR rules. Relationship to organizational identity policy and assessment scope also requires decisions.
- **Requirement-validation effort:** higher than the selected candidate because 12 proposed boundaries, parameter assignments, hierarchy, and incorporation relationships need review.
- **Evidence possibilities:** account inventory, provisioning/deprovisioning procedures, review records, configuration/report output, or tests, all subject to later scope and validation rules.
- **Gap potential:** multiple narrow comparisons may be possible after governance; breadth and parameterized obligations raise complexity and judgment needs.
- **Maturity / complexity / usefulness:** strongest structural candidate-boundary material but broad, multi-part, and parameterized. Useful to practitioners, though less suitable as the smallest first end-to-end slice.

### Candidate 3: HIPAA Safe Harbor Identifier Discovery (HIPAA-ID-01 through HIPAA-ID-18)

- **Authoritative source:** `HIPAA-IDENTIFIERS.md` preserves the federal identifier set and cites 45 CFR § 164.514(b)(2) plus HHS/OCR explanatory guidance. `HIPAA-IDENTIFIERS-INTERPRETATION.md` separates authority from conversational interpretation and marks several wording/example questions as requiring governance.
- **Current repository content:** identifier content is available and the 18-member set is explicit; no new identifiers are permitted. This is an actual narrow data-discovery content area, not a populated Requirement/Control catalog.
- **Likely facts:** documents and participant statements may identify data elements or state that they are unknown. Submitter already preserves `YES`, `NO`, `UNKNOWN`, and omission distinctions for governed identifier discovery.
- **Applicability complexity:** high for a full compliance chain. Identifier presence does not establish PHI status, HIPAA applicability, or de-identification; the source itself preserves those boundaries.
- **Requirement-validation effort:** it is source/interpretation content, not a set of independently validated SAR Requirements or safeguard expectations. Building a requirement/control chain would require additional source and policy governance.
- **Evidence possibilities:** source documents and data inventories can support discovery, but sufficiency/validation for any downstream HIPAA determination is not governed here.
- **Gap potential:** strong for deterministic discovery-state checks; weak for the requested end-to-end applicability-to-finding slice without broadening scope into HIPAA interpretation and legal applicability.
- **Maturity / complexity / usefulness:** high for one discovery function, but it cannot by itself prove the requested Requirement → Safeguard → Evidence → Finding chain. It is not selected for the first full vertical slice.

### Qualitative Comparison

| Criterion | SI-12.3 Information Disposal | AC-2 Account Management | HIPAA Identifier Discovery |
|---|---|---|---|
| A. Authoritative source clarity | STRONG | STRONG | STRONG for identifier text |
| B. Factual input clarity | STRONG | MODERATE | STRONG for discovery facts |
| C. Applicability clarity | WEAK under current governance | WEAK | WEAK for full chain |
| D. Requirement boundary clarity | MODERATE | WEAK | WEAK for Requirement conversion |
| E. Safeguard clarity | MODERATE | MODERATE | WEAK for full chain |
| F. Evidence observability | STRONG | STRONG | MODERATE |
| G. Deterministic gap potential | MODERATE | MODERATE | MODERATE for discovery only |
| H. Practitioner value | STRONG | STRONG | MODERATE |
| I. Traceability | STRONG | STRONG | MODERATE |
| J. Scope | STRONG | WEAK | STRONG for discovery; WEAK for end-to-end |
| UX fit | STRONG | MODERATE | STRONG for discovery |

These ratings reflect the visible repository/source structure and expected governance effort only. They are not assessment outputs or substantive policy judgments.

## 4. Recommended First Slice

Recommend exactly one first slice to govern:

> **NIST SP 800-53 Rev. 5 SI-12.3 Information Disposal, limited to one assessed system/service and one human-validated Candidate Requirement Boundary rooted at source part `si-12.3_smt`.**

This is preferable to the alternatives based on the selection criteria, not simply because its artifacts happen to be present: it has an identifiable pinned source and one proposed source boundary, a factual domain that can often be characterized from documents, observable evidence candidates, and a plausible nonnumeric comparison path. Its current applicability clarity is weak and explicitly requires governance; selection means only that its bounded source boundary is a reasonable first candidate for that work. AC-2 has more proposed boundaries and parameter/relationship complexity. HIPAA identifier discovery is more mature as an isolated discovery content set but does not reach the required requirement/safeguard/applicability/finding chain without adding substantial HIPAA governance.

The SI-12.3 candidate references an organization-defined parameter (`si-12.3_prm_1`). The parameter's value and meaning for a SAR assessment are not supplied by this design. No retention period, disposal technique, scope rule, or expected outcome is selected here.

### Scope Boundary

In scope for future governance:

- one pinned SI-12.3 source object/version and its validated semantic boundary;
- facts about information/data in the assessed system and documented retention/disposal practice;
- one approved applicability path, if governance supplies it;
- one or more validated SAR Requirement representations only after human review;
- separately governed safeguard/control expectation(s), evidence expectations, validation method/authority, and a deterministic gap condition; and
- a narrow report projection of this chain.

Out of scope:

- selecting LOW/MODERATE/HIGH/PRIVACY profile for an assessment;
- deciding legal/privacy applicability from source membership or organizational labels;
- populating all SI-12 or NIST requirements;
- assigning organization-defined parameter values without authorized policy;
- inventing retention periods, destruction techniques, or control mappings;
- calculating risk/severity or deciding residual risk; and
- final risk acceptance, authorization, or disposition.

If governance cannot identify an approved applicability basis for this source use, the path stops at `UNRESOLVED / GOVERNED RULE NOT YET POPULATED`; that is an acceptable design outcome, not a failed control conclusion.

## 5. Minimum Fact Set

These are proposed information needs for future governance, not a questionnaire or assertions that every fact is always required.

### Facts Likely Extractable from Documents

- system/service identity, purpose, scope, and relevant environment;
- what information/data is handled and where it is stored or processed, if described;
- documented retention, archival, deletion, or disposal processes and named responsible components/parties;
- published policy/procedure or vendor statements, with author/source and exact document location; and
- available configuration exports, lifecycle diagrams, or records describing the process.

Extraction produces candidate facts tied to source locations. A vendor statement remains a vendor claim; a policy describing expected practice does not prove that a deployed system follows it.

### Facts That May Require Clarification

- which information/data sets are in scope for the assessed product/service and use;
- whether documented practices apply to the specific tenant, configuration, environment, and data path;
- which systems, parties, or media are involved in the described disposal process; and
- whether the available documents describe current deployed practice, intended policy, or future design.

The operator/participant supplies factual context, not the applicable NIST profile, legal applicability, required disposal technique, or evidence sufficiency determination.

### Facts Not to Ask the Submitter as SAR Determinations

Do not ask the Submitter/requestor to decide whether SI-12.3 or a NIST profile legally applies, whether an organization-defined parameter is satisfied, whether evidence is sufficient, whether a control is effective, whether there is a finding, or what risk/disposition follows. Those require separately governed rules and/or authorized review.

## 6. Minimum Question Intents

Future intents should be activated only when the fact is material and absent from readable documents. No fixed wording is proposed.

| Intent purpose | Trigger | Information element | Response form | UNKNOWN handling |
|---|---|---|---|---|
| Identify in-scope information handled by the system/service | Source material indicates the service stores/processes information, or the data scope remains unclear | Data/information type and system scope | Factual free response; source/document reference where available | Preserve `UNKNOWN`; do not infer no data is retained |
| Characterize documented retention/disposal practice | Documents identify or leave unclear retention, archival, deletion, or disposal activities | Data lifecycle practice and responsible component/party | Factual description; distinguish policy, configured behavior, and observed practice | Preserve unknown duration/technique as unknown; do not supply a default |
| Establish applicability facts and relationships, if needed by an approved rule | The approved slice's applicability rule names missing subject, source scope, relationship, or risk-basis facts | Relevant system/data/service/relationship facts | Factual free response and supporting reference | Keep applicability `Insufficient Information` or unresolved as dictated by the approved model; do not ask the participant to choose Applicable/Not Applicable |
| Locate evidence for a governed expectation | A validated Requirement and Evidence Expectation exist and no suitable evidence has been supplied | Evidence artifact/reference and tested scope | Attach/reference available policy, configuration, record, or test evidence | Record missing/inaccessible evidence distinctly; absence does not prove safeguard absence |

These intents are proposals only. They create no registry entry or bounded choice.

## 7. Applicability Path

The smallest possible path for this slice is a source/requirement-level applicability determination for the assessed system/data scope:

1. Identify the source object/version and its source role from the pinned source record.
2. Collect supported facts about the assessment subject, data, use, environment, and any relationship/scope required by a future rule.
3. Identify an applicability basis (for example, a governed risk basis or an approved profile/policy selection), but do not assume one from NIST profile membership.
4. Apply only an approved versioned rule to its defined target and facts.
5. Record `Applicable`, `Not Applicable` with affirmative rationale, `Potentially Applicable / Requires Review`, or `Insufficient Information` as the approved rule permits; otherwise report `UNRESOLVED / GOVERNED RULE NOT YET POPULATED`.

No current SAR rule supports making the SI-12.3 applicability determination. Profile membership is source provenance and does not establish assessment applicability. This design makes no legal/regulatory applicability finding.

## 8. Requirement Validation Path

The source snapshot identifies NIST SP 800-53 Rev. 5 content release `5.2.0`, repository commit `78650f02ad9321bb7b817846f8fbd4f2bcd620de`, and source object `si-12.3`. The proposed boundary is `cbr-nist-sp800-53-rev5-si-12-3-smt`, with root/included part `si-12.3_smt` and normative parameter reference `si-12.3_prm_1`.

Before a SAR Requirement could be created, human validation must:

- retrieve/inspect the exact pinned authoritative source object and provision;
- confirm that the candidate boundary represents one complete normative obligation with all operative context;
- confirm source role and normative strength and preserve any conditions/exceptions;
- resolve the source-defined organization parameter's meaning and identify what authorized governance, if any, assigns its assessment value;
- decide whether the source's intended use is authority or reference/benchmark and document the basis; and
- approve the SAR Requirement representation, identity, scope, version, provenance, and status.

Until that work is approved, `Candidate Requirement Boundary != SAR Requirement`. The existing schema/validator can check structure and correspondence to the source slice; it cannot perform these semantic validation decisions. No candidate is promoted in this task.

## 9. Safeguard / Control Path

A validated Requirement may later map to zero, one, or multiple safeguard/control expectations; an expectation may also relate to multiple Requirements. The model must retain those relationships independently.

For this slice, the only permitted design statement is that a future safeguard/control expectation would describe the outcome SAR evaluates for an approved disposal obligation, within the requirement's validated scope and any approved organization parameter. This document does not assert a particular technical technique, retention period, sanitization method, or NIST-control mapping. If the expected outcome cannot be governed from the validated Requirement and an authorized SAR risk/authority basis, report the mapping as unresolved.

## 10. Evidence Path

Potential evidence candidates, subject to a future validated expectation and scope, include:

- policy/procedure describing information lifecycle or disposition;
- configuration or system-generated settings/report that identifies configured retention/disposal behavior;
- operational records or a scoped test result showing a particular disposition event; and
- vendor documentation describing service behavior, retained as a vendor claim until its scope and evidence status are reviewed.

Machine-observable properties may include that an artifact exists, is readable, identifies a version/date, or contains a stated configuration value. Such checks establish only those mechanical properties. They do not prove a deployed practice is effective, complete, in scope, or compliant. A reviewer/authorized validator must assess authenticity, currency, scope, relevance, and sufficiency when those judgments are required and authorized.

Keep `Claim != Evidence != Validation`. Record `REQUESTED`, `SUPPLIED`, `INACCESSIBLE`, `MISSING`, `CONFLICTING`, or other observations only under an approved evidence model. Do not equate missing evidence with absence of a disposal safeguard.

## 11. Deterministic-Rule Opportunity

No substantive rule is approved here. The future rule to govern would compare a validated applicable Requirement and its defined scope/parameters with supported facts and evidence/validation state, then return only a typed intermediate result permitted by that rule.

A future rule specification must define its exact inputs, source/requirement/rule versions, preconditions, affirmative and negative conditions, UNKNOWN/conflict behavior, and result. Possible structural outcomes include satisfied under the stated criterion, rule-supported gap, or unresolved because required facts/evidence/validation are unavailable. These terms are illustrative pending governance; they do not assert that the source currently establishes any particular SAR criterion.

No severity, risk score, default retention duration, or disposal technique is supplied. Until the requirement, applicable scope, expectation, evidence criterion, and rule are all governed, result is `UNRESOLVED / GOVERNED RULE NOT YET POPULATED`.

## 12. Finding / Gap Path

A future machine-determinable gap could arise only if:

1. a validated SAR Requirement is applicable to the assessed scope;
2. its separately approved safeguard/control expectation is defined;
3. the evidence expectation and validation rule are available; and
4. an approved deterministic condition establishes a difference between the expected and supported observed conditions.

Otherwise, represent the state as missing evidence, unresolved applicability, conflicting evidence, or human-review candidate as appropriate. Missing evidence alone is not proof that the safeguard is absent. Human judgment remains necessary for ambiguous normative meaning, scope, evidence sufficiency outside mechanical criteria, exceptions, and any severity or treatment judgment not otherwise governed. Final risk acceptance/disposition remains human.

## 13. Small Report Projection

A future report projection for this slice should contain only populated objects and explicit unresolved states:

- **Facts:** in-scope system/data and documented lifecycle practice, each linked to source and epistemic status.
- **Applicability:** target, supported basis, rule/version and rationale, or `UNRESOLVED / GOVERNED RULE NOT YET POPULATED`.
- **Requirement:** validated SAR Requirement reference/version and exact source provision, or “candidate boundary only; not a validated Requirement.”
- **Expectation:** separate safeguard/control expectation and mapping reference, or unresolved.
- **Evidence:** artifact/reference, provenance, scope, mechanical accessibility observations, and validation state.
- **Finding/gap:** only if an approved rule supports it; otherwise missing/unresolved/candidate status, not an assumed failure.
- **Open items:** parameters, applicability, evidence, validation, or rule gaps and the responsible governance/review route.
- **Trace:** links through fact, source version/provision, applicability, Requirement, expectation, evidence/validation, rule, and resulting status.

The projection does not infer risk or disposition and does not complete empty sections with model assumptions.

## 14. Non-Normative Assessment Trace Example

This is a relationship-shape example only. Bracketed placeholders are intentionally unresolved; none creates an approved policy result.

```text
[Fact: system retains/disposes identified information; source and epistemic state recorded]
  -> [Applicability determination: UNRESOLVED / GOVERNED RULE NOT YET POPULATED]
  -> [Authority: NIST SP 800-53 Rev. 5, content release 5.2.0, pinned source commit;
      source object si-12.3 / part si-12.3_smt]
  -> [Candidate Requirement Boundary: cbr-nist-sp800-53-rev5-si-12-3-smt; PROPOSED]
  -> [SAR Requirement: NOT CREATED; awaits human validation]
  -> [Safeguard / Control Expectation: NOT POPULATED]
  -> [Evidence / Evidence Expectation: candidate artifact references only; criteria NOT POPULATED]
  -> [Validation: NOT PERFORMED / AUTHORIZED VALIDATOR NOT DEFINED]
  -> [Finding: NOT DETERMINED]
  -> [Report projection: facts, provenance, and unresolved governance only]
```

A future approved instance must be navigable in reverse from report/finding to evidence, expectation, Requirement, applicability basis/rule, authoritative source provision/version, and originating facts. This example is not a requirement, applicability decision, finding, or assessment result.

## 15. Future Deterministic Test Strategy

After the content is separately approved and implemented, test with fixed normalized facts, exact governed content and source versions, evidence inputs, and validation states. Compare machine-determinable intermediate outputs and traces across repeated runs and, where possible, different AI models/conversational phrasings that normalize to the same fact state.

Compare at least: selected intent references/activation; normalized fact states and provenance; applicability result/rationale; selected Requirement/version; expectation references; evidence observations/validation inputs; rule inputs/version/output; unresolved/gate routes; finding/gap status where governed; and report projection references. Human judgments and final decisions are not compared as deterministic outputs unless the same authorized decision record is simply being reproduced.

A test fails determinism if identical governed normalized inputs and versions produce different machine-determinable results, or if an output cannot be traced to those inputs/content versions. A wording difference alone is not semantic divergence. This proposes test properties; it creates no acceptance criteria or test run.

## 16. Reference-Tool Comparison

The reference Risk Assessment Tool illustrates minimal user effort through a preconfigured agent, canonical instructions, supporting knowledge assets, a predictable workflow, and a stable output template. For the selected slice, documents should supply most factual context; the agent should extract facts first and ask only material unresolved questions.

SAR adds explicit pinned authority and source roles, applicability bases, human validation between candidate and Requirement, distinct Requirement and safeguard expectation, scoped evidence and validation, rule-linked findings, bidirectional trace, explicit unresolved states, and a human disposition boundary. Consistency comes from approved content and rules rather than expecting model reasoning to repeat itself. The reference tool's risk tiers, formulas, checklists, or approval semantics are not imported.

## 17. Ordered Governance / Implementation Sequence

No step below is performed in this task. A future sequence for the chosen slice is:

1. Confirm the intended SI-12.3 source use and exact canonical source content at the pinned revision.
2. Human-review the candidate boundary, source scope, normative meaning, parameter reference, and authority-versus-benchmark role.
3. If approved, create/version the SAR Requirement representation with provenance; otherwise reject or revise the candidate without loss of history.
4. Identify the fact Information Elements and approve the minimal Question Intents and UNKNOWN/conflict behavior.
5. Govern whether/how the requirement applies to the selected assessment scope; explicitly preserve unresolved applicability if no rule is approved.
6. Define separate safeguard/control expectation relationships, if supported by the Requirement and authorized risk/authority basis.
7. Define evidence expectations, scope, validator authority, and validation behavior.
8. Approve a deterministic comparison rule, including required inputs and missing/conflict routes, without inventing numeric severity or risk formulas.
9. Define any gate/routing condition and report projection inputs.
10. Create synthetic facts/evidence fixtures and deterministic acceptance tests only after the semantics are approved.
11. Execute QA only after a supported host mode, test definition, and result/evidence governance are in place.

## 18. Decision Gate

### READY FOR VERTICAL-SLICE GOVERNANCE

A narrowly bounded candidate source boundary is sufficiently identifiable to begin governance: the repository pins a NIST OSCAL source snapshot and identifies SI-12.3's source object, statement-part reference, source profile membership, and one proposed Candidate Requirement Boundary. The source material can be reviewed at its exact pinned upstream revision, and the fact domain has support in the existing Information and Intake Models.

This decision means only that work may begin to validate source meaning, scope, applicability basis, and candidate requirement content. It does **not** mean that the Requirement is validated, applicable, mapped to a safeguard, supported by an evidence criterion, executable, or ready for assessment. The first governance gate is human validation of the exact source boundary and parameter semantics. If that review cannot establish a complete obligation or a permissible source role, stop or select another slice through a new governed decision.

`READY FOR VERTICAL-SLICE GOVERNANCE` does not mean applicability, safeguard expectations, evidence criteria, deterministic or finding rules are approved; the slice is implemented; or QA has passed.

## 19. Unresolved Governance

- Human approver and process for validating the SI-12.3 Candidate Requirement Boundary and assigning/handling its organization-defined parameter.
- Whether the source is used as applicable authority or a reference/benchmark, and the independent applicability basis for the selected assessment scope.
- Which system/data scope is appropriate and how it is represented without assuming all system data is subject to the same practice.
- Whether the proposed evidence candidates are relevant, sufficient, current, and in scope; which actor may validate each.
- Whether a deterministic gap can be defined from a validated requirement and evidence criterion without making absence-of-evidence claims.
- Any Requirement-to-Safeguard/Control expectation mapping and its independent source/risk basis.
- Gate, finding, status, and report projection vocabulary and their approval owners.
- Test/record schema, supported execution mode, provenance, and controlled evidence/result handling.

Until these questions are governed, do not populate this slice. Missing semantic content remains `UNRESOLVED / GOVERNED RULE NOT YET POPULATED`.
