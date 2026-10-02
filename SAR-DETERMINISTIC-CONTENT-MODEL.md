# SAR Deterministic Assessment Content Model

## 1. Purpose and Boundary

**ARCHITECTURE PROPOSAL - CONTENT MODEL; NOT AN APPROVED RULESET, COMPLETE CATALOG, OR ENGINE**

This document defines the minimum logical content structures SAR would need to make machine-determinable intermediate assessment results reproducible. It complements, rather than replaces, the Information Model, Intake Model, Decision Logic, Source Catalog, Applicability Model, Requirement Model, Assessment Protocol, Runtime Interface, Execution Record architecture, and Submitter contract.

It does not populate the SAR Requirement Catalog, establish legal or organizational applicability, set classification/risk/depth thresholds, create a full Threat Library, define evidence sufficiency policy, implement a rules engine, select a general serialization format, or authorize assessment decisions. Existing documents remain authoritative within their scope. Proposed structures and examples below are not operational rules unless separately reviewed and approved.

### Status Labels Used Here

- **EXISTING GOVERNED SEMANTICS** identifies a distinction or principle already stated by an existing SAR artifact.
- **PROPOSED STRUCTURE** identifies the logical data needed to express and trace that semantic; it is not an approved schema.
- **NON-NORMATIVE EXAMPLE** is illustrative only and creates no rule, requirement, threshold, applicability, or policy result.
- **UNRESOLVED GOVERNANCE** identifies content or authority not yet supplied by SAR.

## 2. Deterministic Assessment Relationship

**EXISTING GOVERNED SEMANTICS:** The Assessment Protocol states that identical normalized inputs and identical governed rule/source versions must yield identical machine-determinable intermediate results. Human judgment and final disposition remain distinct. The Information Model distinguishes facts, derived information, evidence, and decisions.

**PROPOSED STRUCTURE:** A result is reproducible only when the execution can identify the exact factual input state, the exact governed content/rules and their source versions, and the applicable evidence/validation state:

```text
Normalized Assessment Facts
+ Governed Content and Rule Versions
+ Source / Requirement Versions and Applicability Basis
+ Evidence / Validation State
    ->
Reproducible Machine-Determinable Intermediate Determinations
```

The relation does not mean every assessment stage is currently executable. Missing facts, conflicts, inaccessible evidence, unpopulated rules, or authority questions remain explicit and may produce an unresolved result or a human-review route. The LLM may extract candidate facts and explain a governed result; it may not invent semantic inputs or rules to make the equation appear complete.

Human judgment is recorded as judgment, with role, rationale, inputs, and provenance where required. Authorized final risk acceptance/authorization/disposition does not become a deterministic result merely because prior stages were reproducible.

## 3. Existing Deterministic-Content Capabilities and Gaps

### Existing Content and Tools

- `SAR-INFORMATION-MODEL.md`, `SAR-INTAKE-MODEL.md`, `SAR-DECISION-LOGIC.md`, `SAR-APPLICABILITY-MODEL.md`, and `SAR-REQUIREMENT-MODEL.md` define conceptual objects and distinctions, not complete executable rule sets.
- `SAR-SOURCE-CATALOG.md` defines source identity, provenance, versioning, and source/applicability separation. It lists candidate source families but does not create their requirement mappings.
- `SAR-CANDIDATE-REQUIREMENT-BOUNDARY-MODEL.md` defines a proposal layer between source extraction and SAR Requirements. It explicitly requires human validation before a candidate boundary creates a governed Requirement.
- `schemas/sar-candidate-requirement-boundary-set.schema.json` and `tools/validate_candidate_boundaries.py` are an existing narrow exception to the otherwise conceptual models: a JSON Schema and validator for Candidate Requirement Boundary set structure and mechanical consistency with a source slice. The validator checks source snapshot metadata, coverage counts, IDs, source-part ancestry/order, normative parameter references, and relationship references. It does not validate semantic boundary correctness, authorize a Requirement, determine applicability, or establish a control/evidence/finding rule. This proposal does not extend that schema or tool.
- `sources/nist-sp800-53-rev5.oscal-source.yaml` identifies a pinned NIST SP 800-53/800-53B OSCAL source snapshot: content release `5.2.0`, upstream repository commit `78650f02ad9321bb7b817846f8fbd4f2bcd620de`, and catalog/profile artifacts. It records LOW, MODERATE, HIGH, and PRIVACY source-profile membership. The source file also preserves an observed upstream title/version inconsistency for the HIGH profile rather than resolving it by guess.
- `sources/nist-sp800-53-rev5.ac-2-si-12.slice.yaml` contains source-object structure, part relationships, parameters, profile membership, and references for a limited AC-2/SI-12 slice. The accompanying candidate-boundary files contain 12 AC-2 and 4 SI-12 proposals, all with `validation_status: PROPOSED`. They are not validated SAR Requirements, applicability outcomes, control mappings, or assessment results.
- `HIPAA-IDENTIFIERS.md` preserves the federal Safe Harbor identifier set; `HIPAA-IDENTIFIERS-INTERPRETATION.md` defines interpretation states and explicitly records that participant-facing wording is not yet governed. These artifacts do not classify all information, determine PHI/HIPAA applicability, or map requirements to safeguards.
- `SUBMITTER.md` governs factual intake, UNKNOWN handling, and `Claim != Evidence != Validation`; it does not decide downstream classification, applicability, findings, or risk.

### Missing Executable Governance

The reviewed repository does not contain a populated Question Intent Registry; validated SAR Requirements and complete source-to-requirement extraction; approved applicability rules; data/system classification rules; inherent-risk methodology; Assessment Depth labels/rules; a populated Threat Library and trigger rules; requirement-to-safeguard mappings; evidence expectation/sufficiency rules; finding rules/severity; executable gate rules; or an approved report contract/schema. Privacy and evidence are represented conceptually and by limited HIPAA source/interpretation artifacts, not by a complete privacy rule corpus or evidence engine.

NIST OSCAL catalog/profile membership is real source metadata, but it is not by itself SAR Requirement validation, baseline selection for a particular assessment, legal applicability, or evidence evaluation. No end-to-end deterministic SAR assessment can be claimed until the necessary governed content is populated and validated.

## 4. Question Intent Model

**EXISTING GOVERNED SEMANTICS:** The Runtime Interface assigns the Question Intent Registry to SAR Intake Governance. Submitter uses governed intents; wording may vary but purpose and answer semantics may not. Intake is adaptive, not a giant questionnaire.

**PROPOSED STRUCTURE:** A Question Intent describes an information need and the conditions for asking it. It is not a script or rule that interprets its answer as a risk or compliance conclusion.

A governed intent should be able to reference:

- stable `intent_id` and immutable content version;
- lifecycle/approval status and governing owner;
- one or more Information Element references;
- concise factual purpose and scope;
- activation condition, expressed through references to approved rules/conditions rather than free-text model discretion;
- prerequisite/dependency intent references;
- required/optional semantics and the consequence of not obtaining an answer;
- permitted response form, including free text or bounded response where specifically governed;
- each bounded option and its source/rule reference when options exist;
- explicit handling of `UNKNOWN`, `NO`, `NOT APPLICABLE`, and `NOT_YET_VERIFIED` where meaningful;
- provenance and evidence expectations for resulting facts;
- completion condition and unresolved condition;
- conflict behavior and relevant reviewer route; and
- next-intent/priority reference where sequencing is governed.

No fixed wording is required. If no approved intent applies, the LLM may not invent a semantic branch or choice set; it may capture a clearly attributed free-text statement or identify an unresolved information need according to the governing intake contract.

**NON-NORMATIVE EXAMPLE:** An intent about hosting model could reference a hosting Information Element, activate when the system deployment is not yet characterized, permit factual free text, allow `UNKNOWN`, and point to any option definitions only if separately governed. This example defines no required hosting categories and no trigger policy.

## 5. Assessment Fact Model

**EXISTING GOVERNED SEMANTICS:** A participant/vendor assertion is not independently verified merely because it was stated or extracted. `UNKNOWN != NO`. Omitted information is not a negative response. Provenance and correction history must be retained.

**PROPOSED STRUCTURE:** Each fact record should reference its assessment subject and Information Element, record a value or explicit answer state, and retain its origin and transformation history. A fact record should be able to carry a stable fact reference, source actor, source/artifact and location, observed time when available, extraction/derivation method, validation state where applicable, and links to prior/superseding records. Identifier syntax is not selected here.

Distinguish these fact-record states and history relationships; they are not a risk scale or a single quality score:

- **Asserted:** a person/system stated the fact. Retain who asserted it. A vendor claim remains vendor-attributed.
- **Extracted candidate:** content was read from a source and mapped to a candidate fact. Retain source location and extraction provenance; extraction alone is not independent confirmation.
- **Inferred candidate:** a possible fact proposed from other inputs. Preserve the derivation and mark it as a candidate; it must not silently become an asserted, confirmed, or validated fact.
- **Confirmed:** a responsible source/person confirmed that the record reflects their current understanding. Confirmation is not independent technical validation.
- **UNKNOWN:** an explicit answer that the value is not currently known, or an unresolved known information need as separately represented by the owning model.
- **Conflicting:** incompatible factual records or evidence exist. Preserve each source and the conflict; do not select one silently.
- **Corrected / superseded:** a later record corrects an earlier fact. Preserve the earlier record and link the correction, actor/source, reason, and applicable time.

An omitted answer or absent source statement is **NOT STATED / NO ASSERTION**, not `NO` and not automatically explicit `UNKNOWN`. `NO` is a substantive answer only when an actor explicitly denies the proposition or an authorized source/rule establishes it. `UNKNOWN != NO`; absence of a record cannot satisfy a negative condition.

**NON-NORMATIVE EXAMPLE:** A vendor document says “hosted in a region selected by the customer.” That can yield an extracted candidate with a source location and vendor attribution; it does not yield a specific region. A participant saying “I do not know” is an explicit `UNKNOWN`. A missing region in both sources is not a `NO` answer and does not prove a region is absent.

## 6. Determination Rule Model

**EXISTING GOVERNED SEMANTICS:** The Assessment Protocol requires approved, versioned deterministic predicates, traceable inputs, explicit unresolved behavior, and no model-invented governance.

**PROPOSED STRUCTURE:** One generic Determination Rule content shape can serve specialized rule purposes without creating an unrelated schema for every domain. A rule should identify:

- stable `rule_id`, immutable version, rule kind, title/purpose, owner, and approval/effective status;
- authority/source references and the exact source/version/provision supporting the rule;
- required input fact, determination, evidence, and version references;
- activation/preconditions and dependencies on other rules/content;
- a deterministic condition over normalized, typed inputs;
- typed resulting intermediate determination and its permitted values/meaning;
- behavior for missing input, `UNKNOWN`, conflicting inputs, and non-conclusive conditions;
- downstream dependencies, gates, or permitted routing;
- rationale/trace requirements sufficient to show matched inputs and rule path; and
- supersession, change rationale, effective interval, and validation/approval provenance.

A deterministic rule returns its specified result for the same normalized inputs and same governed content versions. It does not convert free-form LLM reasoning into a rule result. If the condition cannot be evaluated, the rule returns its governed unresolved behavior rather than a guessed default.

**NON-NORMATIVE STRUCTURAL EXAMPLE:** `EXAMPLE-RULE` references `EXAMPLE-FACT-A` and a hypothetical approved condition token; if that condition is established, it emits `EXAMPLE-DETERMINATION-A`, otherwise it invokes the rule's declared unresolved behavior. The tokens demonstrate references only; this document supplies no condition, substantive output, threshold, or policy result.

## 7. Applicability Rules

**EXISTING GOVERNED SEMANTICS:** The Applicability Model distinguishes source, applicability basis, target, and status. Source registration/profile membership alone does not establish applicability. Conceptual statuses are `Applicable`, `Not Applicable`, `Potentially Applicable / Requires Review`, and `Insufficient Information`.

**PROPOSED STRUCTURE:** Applicability uses a specialized Determination Rule whose target may be a source version, individual Requirement, Requirement family, or safeguard/control expectation, and whose inputs include supported facts, derived characteristics, relationship context, relevant source scope, and the applicable rule version. Its output retains status, basis fact references, relationship/source/requirement references, rationale, unresolved/conflict details, and reevaluation history.

`Applicable` or `Not Applicable` is produced only when an approved rule and supported facts establish that result. `Not Applicable` requires an affirmative reason; failure to find a positive applicability fact is insufficient. Missing facts use `Insufficient Information`; plausible but interpretive or competing paths use `Potentially Applicable / Requires Review` where the governing rule directs that route. These are applicability conclusions, not factual answer states.

Preserve:

```text
Source != Requirement != Applicability Basis != Control / Safeguard
```

An organizational label by itself does not establish legal or regulatory applicability. HIPAA relationship, agreement relationship, State/DDS scope, risk basis, and benchmark/reference roles remain independently represented. Profile/baseline membership is source/profile provenance, not legal applicability.

**UNRESOLVED GOVERNANCE:** No populated general applicability rule matrix or complete source-to-requirement mapping exists. No concrete applicability example in this document should be read as a policy outcome.

## 8. Classification and Inherent Risk

**EXISTING GOVERNED SEMANTICS:** Classification and inherent risk are separate derived determinations. Inherent risk concerns the system, data, use, environment, connectivity, and dependencies before credit for safeguards. Neither should be selected by a requestor or model intuition.

**PROPOSED STRUCTURE:** A Classification Rule uses identified subject/scope, supported normalized facts, source/authority where relevant, a governed classification vocabulary, deterministic conditions, explicit unknown/conflict handling, and traceable rationale. An Inherent Risk Rule separately identifies the evaluated risk subject and contributing fact/derived-characteristic references, the governing method and version, whether safeguards are excluded as inherent-risk inputs, and unresolved behavior. If a method defines no result for the available inputs, the determination remains unresolved. Their versions/results must not be collapsed into one label.

**Current support:** The repository includes HIPAA Safe Harbor identifier sources and interpretation guidance, but that content does not provide a complete data-classification rule or establish PHI/HIPAA applicability. NIST SP 800-53 OSCAL profiles provide source-profile membership, not SAR classification or risk thresholds. `SAR-INFORMATION-MODEL.md` explicitly says it does not define LOW/MODERATE/HIGH rules; `SAR-DECISION-LOGIC.md` leaves classification and inherent-risk methodology future work. No current source reviewed supplies sufficient SAR rules for a general deterministic data/system classification or inherent-risk result.

**UNRESOLVED GOVERNANCE:** No classification vocabulary/rule set or inherent-risk method is approved. Do not invent HIGH/MODERATE/LOW or numerical scoring.

## 9. Assessment Depth

**EXISTING GOVERNED SEMANTICS:** Assessment Depth is separate from classification, inherent risk, residual risk, and disposition. The Assessment Protocol proposes it as a revisitable scope/rigor decision but explicitly supplies no labels, thresholds, or rules.

**PROPOSED STRUCTURE:** An Assessment Depth Rule should reference normalized facts, supported determinations, applicable profile/content versions, and approved inputs; define a deterministic condition and resulting depth/work scope; state evidence/review expectations and exclusions; define unresolved and conflict routes; and preserve rule version, matched facts, rationale, actor, time, and prior result. A change must link to the triggering correction, evidence, applicable rule change, or authorized human direction and preserve prior depth and dependent outputs.

Assessment Depth describes scope, rigor, evidence expectations, and effort. It is not a risk rating, inherent/residual risk, approval, or rejection. No depth names, scoring, or thresholds are introduced here.

**UNRESOLVED GOVERNANCE:** No executable Assessment Depth rule set or approved result labels exist.

## 10. Threat Resolution

**EXISTING GOVERNED SEMANTICS:** The Assessment Protocol proposes a versioned Threat Library selected by explicit triggers and states that no governed Threat Library or patterns are currently populated. A threat is not a vulnerability, finding, risk score, or disposition.

**PROPOSED STRUCTURE:** A Threat content entry should be able to identify stable threat reference/version, description and scope, originating source/reference and provenance, activation facts/conditions, related assets/processes, governed relationships to applicable requirements and safeguards where established, relevant evidence implications where governed, and unresolved/ambiguity behavior. A Threat Selection Rule uses supported facts and derived characteristics to select or decline a specific versioned entry with a traceable trigger match and rule version. Fuzzy LLM suggestions remain candidates for review and do not create Threat entries or determinations.

MITRE ATT&CK or another corpus may later be registered as a source or reference where governed; importing a corpus does not automatically establish threat selection, applicability, requirement mapping, or risk. No external threat content is imported or proposed as active here.

**UNRESOLVED GOVERNANCE:** No Threat entries or selection rules are populated.

## 11. Requirement Resolution

**EXISTING GOVERNED SEMANTICS:** Requirements are source-bound obligations distinct from controls/safeguards. One Requirement may map to many expectations and many Requirements may map to one expectation. Applicability is determined per appropriate target; candidate boundaries require human validation before a SAR Requirement is created.

**PROPOSED STRUCTURE:** Requirement resolution consumes validated SAR Requirement versions, exact Source and source-object/provision references, relevant applicability determinations, and any applicable approved Profile/Baseline membership. A resolution rule identifies selection scope and conditions, records selected/not-selected/unresolved Requirement references with the exact inputs and rationale, and preserves source-role and version provenance. Requirement-to-Control/Safeguard mapping is a separate many-to-many governed relationship; selecting a Requirement must not create a Control.

NIST OSCAL profile membership records which source objects belong to a pinned profile. It does not choose a profile for an assessment, establish legal applicability, or by itself make every profile member an applicable SAR Requirement. Any SAR use of a baseline/profile needs a separately approved selection policy and applicable authority/risk relationship. A source relationship such as `required` must be interpreted only according to its governed source semantics and must not replace assessment-specific applicability.

**Current content boundary:** the NIST 5.2.0 source snapshot and profile membership are present; the AC-2/SI-12 source slice and proposed candidate boundaries are limited source extraction artifacts. There is no populated validated SAR Requirement Catalog or NIST control/safeguard mapping. The HIPAA identifier artifacts are not a general requirement catalog.

**UNRESOLVED GOVERNANCE:** Requirement extraction, validation, applicability, profile selection, and Requirement-to-expectation mappings remain unpopulated. NIST baseline membership remains provenance/profile membership, not legal applicability.

## 12. Evidence Expectation Model

**EXISTING GOVERNED SEMANTICS:** `Claim != Evidence != Validation != Finding`. Vendor claims do not become verified evidence by being read. Evidence is evaluated against a particular fact/assertion/expectation and scope. The Assessment Protocol leaves evidence sufficiency rules unpopulated.

**PROPOSED STRUCTURE:** An Evidence Expectation is linked to a governed Requirement or safeguard/control expectation, the scope/subject tested, the assertion or condition it addresses, applicable source/rule versions, what evidence can address it if governed, and any human validator/role requirements. It records provenance and expected relationship, not a conclusion that evidence exists or is sufficient.

Track evidence properties independently rather than as one implied ladder:

- requested and request context;
- supplied reference/artifact and source actor;
- accessible/readability result;
- relevance to the asserted subject/scope;
- evaluation or sufficiency result under an approved rule or human validator;
- validation state and validating actor/method where applicable;
- conflict, limitation, or missing status; and
- version/date/scope and links to supported or contradicted facts.

Possible evidence observations include requested, supplied, inaccessible, relevant, irrelevant, sufficient under an identified criterion, insufficient, validated, conflicting, and missing. They are dimensions/observations, not universal exclusive lifecycle states. `VALIDATED` is not a claim the LLM may make absent an authorized validation process. Missing evidence means evidence was not supplied/available; it does not prove a safeguard is absent.

**UNRESOLVED GOVERNANCE:** No general evidence expectation catalog or sufficiency criteria exist.

## 13. Finding Rule Model

**EXISTING GOVERNED SEMANTICS:** A finding/gap relates an expected condition to a supported observed condition and evidence evaluation. Severity, finding rules, and machine/human responsibilities remain unpopulated.

**PROPOSED STRUCTURE:** A Finding Rule references a validated applicable Requirement, a governed expected condition or safeguard relationship, its Evidence Expectation, evidence/validation inputs, scope, source/rule versions, and a deterministic comparison condition. It declares whether its result can be a machine-determinable gap, an unresolved evidence/condition gap, or a candidate needing human review, and records matched inputs and rationale.

Distinguish:

- **Machine-determinable gap condition:** a rule's required inputs are present and the explicit predicate establishes a difference between an applicable expected condition and the supported observed condition.
- **Human judgment:** requirement interpretation, applicability ambiguity, evidence sufficiency outside a deterministic criterion, competing evidence, exception handling, or other matters reserved to an authorized reviewer/validator.

Missing evidence alone yields missing/unresolved evidence status, not proof that the safeguard is absent. A finding of safeguard absence requires an applicable expected condition and an explicit rule/evidence basis that supports that conclusion. No severity formula or finding status enumeration is invented here.

**UNRESOLVED GOVERNANCE:** No Finding Rules, severity method, or complete expectation mappings exist.

## 14. Gate Model

**EXISTING GOVERNED SEMANTICS:** A gate controls progression, not final disposition. The Protocol offers proposed outcomes `SATISFIED`, `UNSATISFIED`, `UNRESOLVED`, and `HUMAN DISPOSITION REQUIRED`, subject to governance; no actual gate rules are established.

**PROPOSED STRUCTURE:** A reusable Gate definition should reference stable gate identity/version, owner/status, purpose, stage/transition scope, required input objects and versions, deterministic PASS/satisfaction predicate or required human action, explicit unknown/conflict behavior, blocking behavior, allowed downstream routing, exception authority where defined, and trace/provenance requirements. A Gate Evaluation records the exact rule/content and assessment snapshot, inputs, result, explanation, actor/tool and time, and permitted next action.

Use existing proposed gate vocabulary only if approved. An unsatisfied or unresolved gate may block/reroute work; it is not rejection or approval. No gate may be cleared by model confidence or by silently changing an input. Human exception and risk-acceptance authority remain human.

**UNRESOLVED GOVERNANCE:** Gate vocabulary and actual gate rules remain proposals.

## 15. Report Projection Inputs

The report is a projection of governed assessment state and its trace, not a second decision engine. The renderer may organize and present stored facts and determinations; it must not invent missing conclusions to complete a template.

A reliable report projection requires references to the following objects where available:

- assessment identity and execution/provenance assurance, with unavailable states explicit;
- characterization and participant/source provenance;
- facts about data/information, environment, hosting, and connectivity;
- classification and inherent-risk determinations with rule/version/rationale, or explicit unresolved states;
- Assessment Depth with rule/version/work scope, or explicit unresolved state;
- applicability targets, bases, statuses, and rationales;
- selected Requirements and source/profile versions, distinct from Safeguards/Controls;
- governed threat selections and trigger traces;
- Evidence Expectations, supplied/accessibility/scope information, Validation records, and gaps;
- Findings or candidate/unresolved conditions and their rules/authority;
- residual-risk inputs/result only where a method is governed;
- open questions, conflicts, unknowns, and gate results;
- human judgments/decisions with actor, authority, scope, and rationale where recorded; and
- Assessment Trace links and source/rule/content versions.

The full visual report, publication format, and status terms remain outside this content-model task.

## 16. Assessment Trace

**EXISTING GOVERNED SEMANTICS:** The Information Model defines a bidirectional Assessment Trace; the Protocol links facts through applicability, requirements, sources, controls, evidence, validation, findings, residual risk, and human decision. The Execution Record architecture preserves snapshot/event/version provenance.

**PROPOSED STRUCTURE:** Each object and relationship must have a stable logical reference and immutable content version where it is governed. No identifier syntax is selected here. A trace should link, where applicable:

```text
Assessment Fact(s)
    -> Applicability Determination + Rationale
    -> Requirement + Requirement Version
    -> Authority / Source + Version + Provision/Citation
    -> Control / Safeguard Expectation
    -> Evidence + Scope
    -> Validation + Method/Actor
    -> Finding / Gap + Rule
    -> Residual-Risk Evaluation + Method (if governed)
    -> Human Risk Decision + Authority
```

Minimum references include assessment/state snapshot; Information Element and Question Intent; Fact and provenance/source location; derived-characteristic or Determination Rule/version; source-family/source-version/source-object/provision; Candidate Requirement Boundary where relevant; Requirement/version; applicability target/basis/determination/rule; Control/Safeguard expectation and mapping version; Evidence/Evidence Expectation/Validation; Threat/Threat Selection Rule; Finding/Finding Rule; Gate/Gate Evaluation; residual-risk evaluation/method; and human decision. These are logical references, not new required production identifiers or a schema.

Forward traversal from a fact should show dependent determinations and report statements. Reverse traversal from a finding or decision should reach the supporting evidence/validation, expectation, requirement/source/applicability basis, originating facts, and exact rule/content versions. A source or rule change creates a new versioned relationship/evaluation; it must not mutate historical trace edges.

## 17. Minimum Governed Content Types

Avoid a separate schema for every rule domain. The minimum logical content categories are:

1. **Information Element and Question Intent** — what fact is needed and under what governed conditions it may be asked.
2. **Fact and provenance** — asserted/extracted/confirmed/unknown/conflicting/corrected information and source history.
3. **Source and versioned source object** — authority/reference, exact version, structure, profiles, and immutable references.
4. **Candidate Requirement Boundary and Requirement** — candidate semantic boundary and reviewed source-bound obligation, kept distinct.
5. **Control/Safeguard Expectation and mapping** — outcome expectation and many-to-many relationships to Requirements.
6. **Evidence Expectation, Evidence, and Validation** — what evidence addresses an expectation, what was supplied, and what an authorized check established.
7. **Determination Rule and Determination** — one reusable rule shape with a `rule_kind` and typed result for applicability, classification, inherent risk, depth, requirement selection, threat selection, finding conditions, or residual-risk evaluation where an approved method exists.
8. **Threat entry** — governed scenario and provenance; selected only by a linked rule.
9. **Gate and Gate Evaluation** — permitted transition conditions and recorded outcomes.
10. **Finding, Residual-Risk Evaluation, Human Decision** — distinct conclusions and authorized judgment, not collapsed into one result.
11. **Trace Link and Report Projection** — relationships between objects and a report view over them.

This is a logical inventory, not a requirement to implement eleven separate databases or schemas. Reuse the generic Determination Rule structure for specialized rule kinds; preserve the distinct domain objects and authorities.

## 18. Authority / Source Content vs SAR Executable Content

**Authority / Source Content** is what the external publisher or governing instrument says, at its exact version and location. SAR preserves source identity, source text/reference, structure, source relationships, publication/version provenance, and authority/reference role without silently normalizing away meaning.

**SAR Executable Content** is the governed SAR representation used in execution: validated Requirements, Question Intents, typed mappings, applicability/classification/risk/depth/selection rules, evidence expectations, finding rules, gates, and report projections. Every executable item references its source authority/version where applicable, SAR owner/approval status, version, rationale, and effective/supersession history. Some SAR rules may derive from organizational risk policy rather than an external source; that authority must also be explicit.

The path from authority to executable content is governed transformation:

```text
Authoritative Source + Exact Version
    -> extraction / candidate boundary
    -> authorized validation (human validation for Candidate Requirement Boundaries)
    -> approved SAR Requirement / Rule / Mapping
    -> versioned execution
```

The existing Candidate Requirement Boundary model and tool support structural extraction checks, not semantic approval. The LLM may locate, quote, summarize, or propose candidate content during development/review, but may not translate source prose into new executable rules during an assessment. A source revision triggers review/impact analysis; it does not silently rewrite executable SAR content or past outcomes.

## 19. Versioning and Change Impact

**PROPOSED STRUCTURE:** Each governed content object has a stable logical ID and immutable versioned revisions. This model defines no ID syntax or release mechanism. Each revision should state, as applicable:

- status such as proposed, under review, approved/effective, superseded, withdrawn, or not yet governed;
- owner/approver and rationale for change;
- source identity, exact source version/provision, and derivation/validation provenance;
- effective interval or applicability date where governance defines one;
- dependencies on other content/rule versions; and
- supersession/replacement links without overwriting historical versions.

Keep these changes distinct:

- **Source change:** an upstream publisher changes source content/version.
- **Requirement change:** SAR validates a changed, split, merged, or withdrawn interpretation of source obligations.
- **Rule change:** SAR changes how governed normalized inputs produce a determination.
- **Assessment input change:** facts, evidence, or validation changes for one case.

Each can have different effects. A new source version does not automatically change a rule; a rule change does not rewrite the source; a profile membership change does not by itself change applicability. Change impact identifies dependencies and assessments using earlier versions. Re-evaluation, when required, creates a new determination/event linked to the prior one and exact input snapshot. Historical assessments remain as evaluated; no retroactive silent mutation.

**UNRESOLVED GOVERNANCE:** Release states, approval authority, effective-date semantics, impact-review triggers, and backward-compatibility policy are not fully defined.

## 20. Machine-Readable Future

Markdown remains the governance/design source. Existing SAR has a JSON Schema and validator only for Candidate Requirement Boundary artifacts. This task does not extend those or select JSON, YAML, OSCAL, a database, API, expression language, or rule engine as the general representation.

The logical model should be serializable later while preserving typed references, exact versions, explicit missing/unknown/conflicting states, source and rule provenance, immutable history, and non-self-authorizing proposals. A future machine-readable design must distinguish schema version from source version, requirement version, rule version, protocol version, implementation provenance, and continuation-state version.

## 21. Reference-Tool Consistency Lesson

The reference Risk Assessment Tool's useful consistency lesson is to constrain workflow and output semantics with canonical instructions, separate knowledge assets, a repeatable stage sequence, and a stable output template. SAR needs the same discipline across more independently governed domains.

SAR should achieve consistency through populated and versioned content objects, explicit ownership and precedence, deterministic rules where authority and inputs are conclusive, traceable source/requirement/applicability relationships, stable unresolved/conflict behavior, and a report projection of stored assessment state. Model reasoning may help interpret language and surface candidates; it must not replace a governed source-to-rule transformation or supply absent policy. More source breadth increases the need for provenance and independent applicability paths; it does not justify one omnibus prompt or inference from catalog membership.

## 22. Vertical-Slice Population Strategy

Populate one small end-to-end slice rather than an entire source catalog. Select a slice only after governance confirms it has:

- a pinned, authoritative, versioned source artifact and clear source role;
- low semantic ambiguity for the initial source boundary, or a human-validated Candidate Requirement Boundary;
- a small observable fact set and governed Question Intents that collect it without user classifications;
- an explicit applicability basis/rule or an approved statement that applicability is not determined in that slice;
- a small set of validated Requirements and separate safeguard/control expectations;
- evidence that can be scoped and assessed under explicit validation authority/criteria;
- a deterministic, nonnumeric gap rule with known unknown/conflict behavior;
- a gate outcome and report projection; and
- traceability from input fact to the output and a way to test identical-input repeatability.

The current AC-2/SI-12 NIST slice and Candidate Requirement Boundary proposals may be evaluated as a **candidate source-ingestion substrate** because the source snapshot is pinned and structural checks exist. They are all `PROPOSED` boundaries, and the candidate model requires human validation before creating Requirements. They do not yet supply applicable requirements, policy decisions, safeguard mappings, evidence criteria, or finding rules. Therefore they are not yet an executable vertical slice and this recommendation selects no substantive control outcome.

A first slice should prove the content-to-result path with approved material, not maximize source coverage. If any required authority, applicability, or evidence judgment is absent, stop that branch at `UNRESOLVED / GOVERNED RULE NOT YET POPULATED`; do not choose an easier-looking outcome to finish the demo.

## 23. Unresolved Governance Decisions

- Who owns, approves, versions, and retires each executable content type and its transformation from source material.
- Which Question Intent registry structure and activation/priority conventions become authoritative.
- Whether the proposed reusable Determination Rule record has one shared approval lifecycle or specialized domain approval roles.
- Which source families and exact versions are first in scope, and how current source and assessment source versions are managed.
- What validation steps convert `PROPOSED` Candidate Requirement Boundaries into SAR Requirements.
- Which applicability bases and rules can be machine-determined versus requiring legal, contractual, privacy, security, or human interpretation.
- Which classification and inherent-risk methods are authorized, and what unresolved outcomes apply when inputs are incomplete.
- What Assessment Depth result vocabulary and rules, if any, are approved.
- Who governs Threat entries/triggers and permissible external threat-source relationships.
- What constitutes evidence relevance, sufficiency, and validation for each expectation, and which roles may assert `VERIFIED`.
- Which finding conditions can be deterministic, which require reviewer confirmation, and what finding/severity rules are authorized.
- Which gate vocabulary/outcomes are approved and what block/routing authority they carry.
- How residual-risk methods, report projections, Assessment Trace IDs, and machine-readable representations are governed.
- How source, requirement, rule, and assessment-input changes trigger impact review without rewriting history.

Until these decisions are made, existing models remain conceptual except for their explicitly governed narrow content. Missing semantics must be reported as `UNRESOLVED / GOVERNED RULE NOT YET POPULATED` or the applicable existing owner-defined unresolved state.
