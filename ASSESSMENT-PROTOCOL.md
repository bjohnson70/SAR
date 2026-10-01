# SAR Assessment Protocol

## Status and Authority

**ARCHITECTURE PROPOSAL - NOT AN OPERATIONAL ENGINE OR APPROVED RULESET**

This document proposes the canonical SAR assessment-execution protocol: the orchestration contract that defines how governed intake, source and requirement models, decision logic, evidence, reviewer work, and human authority participate in one assessment lifecycle.

It does not implement the protocol, establish assessment thresholds, populate source requirements, create a threat catalog, prescribe a scoring formula, or authorize a decision. Before implementation, this architecture and its referenced rule interfaces require explicit governance. Until then, the owning governed model or operational contract remains authoritative for its domain.

This protocol is not:

- the Submitter interview or a replacement for `SUBMITTER.md`;
- the Reviewer role or a grant of Reviewer authority to an AI;
- a source, requirement, control, or threat catalog;
- an assessment result, approval, rejection, or human risk decision; or
- a substitute for applicable legal, procurement, contractual, or organizational authorities.

## Architectural Position

The protocol orchestrates, but does not absorb, the existing SAR models:

```text
Information Model = what SAR represents
Intake Model      = how Submitter facts are collected
Source Catalog    = which source/version is registered and its provenance
Requirement Model = how source-bound requirements are represented
Applicability     = why a source/requirement applies to this assessment
Decision Logic    = how governed facts and rules produce derived conclusions
Assessment Protocol = when and how these components are invoked and gated
Assessment Record = facts, relationships, evidence, conclusions, and history
Human Authority  = who may make consequential risk/disposition decisions
```

The protocol is the deterministic orchestration contract connecting these components. It does not redefine their domain semantics.

## Governing Invariants

1. **Facts before conclusions:** `Facts -> Interpretation -> Determination`. Submitter captures facts and provenance. Classification, applicability, findings, residual risk, and disposition occur only in their authorized later stages.
2. **Keep assessment objects distinct:**

   ```text
   Source != Requirement != Applicability != Control / Safeguard
          != Evidence != Validation != Finding != Risk Decision
   ```

3. **No model-invented governance:** model output cannot create policy, source authority, requirements, applicability rules, threat triggers, numeric thresholds, scoring, gates, or approval logic.
4. **Unknown remains explicit:** `UNKNOWN`, `NOT_YET_VERIFIED`, conflicting, inaccessible, and not-applicable states remain distinct. Unknown is not converted to Yes, No, or Not Applicable by default.
5. **Provenance is carried:** each stage consumes versioned inputs and records relationships and rule/source versions used. Historical conclusions are not silently rewritten when an input changes.
6. **Deterministic where governed:** identical normalized inputs and identical governed rule/source versions produce the same machine-determinable intermediate results. Human judgment and LLM-assisted interpretation are marked as such and are not represented as deterministic rule output.
7. **A gate is not a disposition:** an unsatisfied or unresolved gate blocks or routes work; it does not itself approve or reject software.
8. **Human authority is explicit:** consequential acceptance of residual risk and final disposition remain with the authorized human decision-maker.

## Roles and Components

| Role / component | Permitted responsibility | Must not do |
|---|---|---|
| Submitter | Collect and correct factual statements, intended use, users, data, environment, dependencies, claims, evidence references, unknowns, and provenance; confirm factual summaries. | Determine final classification, applicability, controls, findings, residual risk, approval, authorization, or disposition. |
| Assessment orchestrator | Maintain assessment state, stage, inputs, rule/source version manifest, gate results, event history, and permitted transitions. Invoke governed services and report blockers. | Invent stage logic, skip required gates, or silently advance on missing inputs. |
| Deterministic rules service | Evaluate approved, versioned predicates and mappings over normalized facts and other authorized inputs; return reproducible intermediate results and reasons. | Supply unapproved thresholds, requirements, threat logic, scoring formulas, or legal interpretations. |
| Source / requirement services | Resolve registered source versions, validated requirement records, source relationships, citations, and approved mappings. | Infer applicability from catalog presence or source references alone; silently merge different authorities. |
| Threat Library service | Select governed threat patterns whose approved triggers match supported facts; retain pattern provenance and version. | Freely generate threat patterns or equate a threat with a vulnerability, finding, or risk decision. |
| LLM assistant | Facilitate natural-language intake, extract candidate facts, summarize, propose candidate links, explain governed results, and identify ambiguity for review. | Treat its extraction or interpretation as verified without an authorized validation path; create governing rules, decide gates by discretion, or authorize consequential outcomes. |
| Reviewer / qualified assessor | Review evidence and conflicts, make professional judgments where rules do not decide, validate material determinations, propose findings and treatment, and document rationale. | Override source authority or omit rationale/history; make a human risk decision unless separately authorized. |
| Evidence validator | Perform or record evidence checks within an explicitly granted role: authenticity, scope, currency, correspondence, and sufficiency against an expectation. | Treat a vendor assertion, certificate, or generic artifact as proof outside its scope. |
| Authorized human decision-maker | Decide residual-risk disposition and conditions under delegated authority; record identity/role, rationale, date, and the exact assessment state considered. | Delegate the final decision to an LLM or infer approval from a gate or status label. |

An individual may hold more than one organizational role only where governance permits; each action must retain the acting role and authority. The protocol does not define named DDS approval authorities.

## Lifecycle

The lifecycle is a governed dependency sequence with controlled return paths, not a one-way checklist. New material facts, changed sources, revised rules, evidence conflicts, or remediation can invalidate dependent derived state and trigger re-evaluation. Each transition records its inputs, outputs, rule versions, actor/component, time, gate result, and trace links.

```text
Characterize
    -> Classify / Inherent Risk
    -> Applicability
    -> Assessment Depth
    -> Threat resolution
    -> Requirement resolution
    -> Evidence plan and collection
    -> Evaluate
    -> Findings / gaps
    -> Risk treatment and residual risk
    -> Human disposition
    -> Publish / maintain Assessment
```

The existing models describe concepts for many of these stages. The sequence below makes their orchestration explicit without claiming that executable rules or complete catalogs already exist.

| Stage | Purpose and required inputs | Allowed operation / owner | Output and trace links | Unknowns, human point, and transition gate |
|---|---|---|---|---|
| **Characterize** | Establish assessment identity/context; Submitter facts, claims, source materials, deployment/use, data, users, environment, connectivity, dependencies, AI, population, consequences, unknowns, provenance. | Submitter collects; orchestrator checks required record structure and material completeness; LLM may extract candidate facts from readable inputs and cite their locations. | Versioned factual snapshot; source/evidence inventory; claims separated from facts; unresolved/conflicting items; links from question/material to information elements and originating actor. | Unknown is allowed and retained. Inaccessible material is recorded. Gate: identity and provenance of the assessment record are sufficient to continue, or the assessment is explicitly held for clarification. No classification is made here. |
| **Classify / Inherent Risk** | Established facts and provenance; applicable governed classification rules and versions; supported context and evidence where required. | Deterministic rules derive only classifications for which approved criteria exist. Reviewer handles ambiguous classification. Inherent-risk analysis considers the characterized system, data, use, environment, and dependencies before credit for safeguards/controls. | Distinct information/system classification determinations and inherent-risk characterization, each with rationale and links to supporting facts, evidence, and rule versions. | Classification is a determination based on established facts and governed classification rules; it is not synonymous with risk. Inherent risk is risk before safeguards/controls; it is not residual risk. Unknowns remain unresolved and may prevent a specific determination. No ungoverned impact or risk scale is inferred. Gate: required determinations are supported or explicitly routed for review. |
| **Applicability** | Supported facts/derived characteristics, registered source and version candidates, source relationships, contracts/relationships, and approved applicability rules. | Resolver identifies candidates and evaluates only approved rules. Reviewer handles ambiguity, exceptions, competing paths, or legal interpretation. | Per-target determination/status and rationale, including source/version, requirement/provision, basis facts, relationship context, rule version, and authority/reference role. | Outcomes use the Applicability Model's conceptual statuses: Applicable, Not Applicable, Potentially Applicable / Requires Review, or Insufficient Information. Gate: each requirement candidate needed for the selected depth has a determination or an explicit unresolved route. A source reference alone never satisfies this gate. |
| **Assessment Depth** | Characterized facts, supported classifications, applicability candidates, consequence/dependency characteristics, and an approved depth rule set. | Deterministic depth rules select the required breadth and rigor; Reviewer may document an authorized exception or explain a rule input. | Depth decision, rule/version, contributing facts, branches, expected evidence/review activities, exclusions, and rationale. | No depth labels or thresholds are approved by this proposal. Until governed, represent the result as `UNRESOLVED / HUMAN REVIEW REQUIRED` rather than inventing a level. Unknown may cause a governed rule to require more evidence/review or hold a branch; never silently treat unknown as Yes or choose a level by model intuition. Gate: a governed depth rule and reproducible rationale exist, or assessment remains explicitly unresolved. |
| **Threat resolution** | Supported facts, derived characteristics, selected depth, and a versioned governed Threat Library. | Library rules select candidate patterns by explicit trigger matches. Reviewer confirms relevance, scope, and context; LLM may explain but not invent patterns. | Threat-pattern identity/version; matched trigger facts; affected assets/data/processes; linked requirements, safeguards, evidence expectations, applicability rationale, source/provenance, and disposition as relevant. | No governed Threat Library or threat patterns are currently populated. If none is approved, record threat analysis as not yet governed/unresolved; do not synthesize a library during execution. Gate: relevant patterns are considered at selected depth or the gap is routed for human review. |
| **Requirement resolution** | Candidate authorities, assessment source versions, provision citations, applicability determinations, approved Requirement Catalog and mappings. | Resolver loads validated requirements and mappings. Reviewer resolves interpretation, conflicts, scope, and source-role ambiguity. Multiple sources may support one expectation while retaining independent provenance. | Requirement instances/versions and source citations; applicability state and rationale; relationship to shared or separate control/safeguard expectations. | A source may be relevant without all its provisions applying. Missing/uncertain source ingestion is not fabricated. Gate: requirements required by the selected depth are resolved or each unresolved item is recorded and routed. |
| **Evidence plan and collection** | Applicable requirements/expectations, threat patterns, assessment facts, evidence already supplied, depth decision, and approved evidence rules. | Engine derives requests only from governed mappings/evidence criteria; Submitter or other responsible party supplies material; validator/reviewer evaluates provenance and scope. | Evidence requests and evidence records linked bidirectionally to assertion/requirement/expectation/threat; origin, version, date, scope, validation status, and limitation. | Missing evidence remains missing; inaccessible evidence remains inaccessible. A claim or certificate is not automatically validated. Gate: evidence is available, explicitly unresolved, or an authorized exception/review route is recorded; no silent completion. |
| **Evaluate** | Validated or explicitly unverified evidence; requirements/expectations; facts; rule and source versions; conflicts; gate state. | Deterministic comparison applies only approved criteria. Reviewer evaluates context, sufficiency, conflicts, and professional judgment. LLM can organize and explain evidence but cannot silently determine sufficiency. | Evaluation per expectation: supported status, rationale, evidence links, rule version, uncertainty, reviewer/validator identity where applicable. | Missing/conflicting evidence yields unresolved or review-required output under governed semantics, not assumed satisfaction. Gate: every in-scope expectation is evaluated or explicitly left unresolved with disposition path. |
| **Findings / gaps** | Evaluation results and authorized finding rules/criteria, unresolved items, and evidence links. | Rules may create findings only where approved predicates and severity rules exist; Reviewer validates finding substance and treatment. | Finding or no-finding/unresolved result linked to expected and observed conditions, facts, applicability, source/version/citation, safeguard, evidence, validation, and rationale. | No finding is invented from an unknown alone unless an approved rule says so. Severity is not assigned without governed criteria. Gate: findings are reviewed or clearly marked candidate/unresolved; each material gap has a treatment or escalation path. |
| **Risk treatment / residual risk** | Inherent-risk characterization, applicable expectations, validated evidence, findings, treatments, compensating safeguards, and approved risk methodology if any. | Deterministic calculation only under an approved methodology. Reviewer assesses treatment and residual risk; unresolved methodology means no numeric score. | Separate inherent and residual risk records, treatment links, rationale, limitations, methodology/version, and trace links to findings/evidence. | Unknowns and unsupported safeguards remain visible. No numeric or categorical result is invented. Gate: residual-risk conclusion is supported under an approved method or marked unresolved for human decision. |
| **Human disposition** | Assessment snapshot, residual-risk state, findings, treatment, unresolved gates, authority/delegation, and decision evidence. | Authorized human decision-maker accepts, rejects, defers, conditions, remediates, escalates, or records another governed disposition. | Decision record identifies authority, scope, exact assessment/version snapshot, date, rationale, conditions, and links to residual risk/findings. | AIs and automated rules cannot make the final consequential decision. Unresolved gates are presented; an authorized person may choose an allowed exception path only if such authority is governed. Gate: decision authority and required record fields are satisfied. |
| **Publish / maintain Assessment** | Versioned assessment state, stage/gate history, trace links, decision if any, source/rule manifest, and approved output contract. | Orchestrator renders a concise human report and detailed linked record; Reviewer validates content; human disposition remains separate. | Assessment artifact with status clearly distinguishing in-progress, unresolved, ready for disposition, and disposed states as later governed; revision history and trace links. | Publication does not mean approval. No approval state is inferred from completion or absence of findings. Gate: artifact integrity/provenance and required links validate; human disposition is displayed only if recorded. |

## Facts, Interpretation, and Stage Boundaries

`Characterize` is the factual boundary. It consumes the Submitter record and accessible evidence, preserves actor/source and uncertainty, and does not decide what facts mean. It may identify missing factual elements needed to route later work, but must not label an assessment compliant, high risk, applicable, or approved.

`Classify / Inherent Risk` begins only after the required factual inputs and evidence references are available. **Classification** assigns a governed information or system category from established facts under applicable governed classification rules. **Inherent risk** characterizes risk before consideration of safeguards/controls. They may consume overlapping facts and be coordinated in one lifecycle stage, but they are different determinations with separate outputs, rationales, and trace links. Neither is a final applicability or residual-risk determination. Preserve both `Facts before classification` and `Inherent risk before safeguards.`

`Applicability` evaluates a governed target against supported facts and authority, not against a requestor's chosen label. `Assessment Depth` selects the scope and rigor of the remaining work; it is not a risk classification, inherent-risk score, residual-risk score, or approval status. Re-evaluation may return a changed conclusion to earlier stages while preserving the prior conclusion and its basis.

No stage transition is justified solely because an LLM says it is complete. Transitions require a defined output contract and evaluated gate.

## Assessment Depth Architecture

Assessment Depth is recommended as an orchestration decision distinct from risk. It answers: **what breadth, evidence rigor, and review effort are required to assess this case adequately under approved SAR rules?** It does not answer whether the product is acceptable or how much risk remains.

The architecture should support a future governed depth rule set that consumes versioned, traceable facts and derived characteristics involving:

- information/data characteristics and uncertainty;
- population and scope;
- hosting, service boundary, and location;
- external parties, subprocessors, and administrative access;
- connectivity and integrations;
- AI/GenAI capabilities and data use;
- operational consequences and system impact;
- independently established authority/applicability triggers; and
- conflicts, evidence quality, or material unknowns.

This proposal does not adopt `streamlined`, `standard`, `enhanced`, numeric cutoffs, weights, or a scoring algorithm. A future decision must approve the names, criteria, rule version, overrides, and required work for each outcome. Until then, implementations must not invent levels or silently select one.

Unknown handling is explicit: a missing value is represented as unknown, not as a positive trigger. A governed rule may specify that an unknown on a material factor requires a different evidence/review path or prevents depth resolution. That is a conservative process response, not an assertion that the factor is present. If no approved rule handles that unknown, the depth result is unresolved and routed for human review; the LLM must not decide.

Every future depth decision should retain the assessment snapshot, input fact IDs/states, rule set/version, matched clauses, selected work plan, unresolved inputs, rationale, reviewer/override authority if applicable, and transition gate result.

### Re-evaluation and Change History

Assessment Depth is a revisitable, governed assessment-scope determination, not an irreversible one-time branch. Later-established facts, new applicability determinations, selected threats, evidence conflicts, findings, material `UNKNOWN` items, or changed source/rule versions may be candidate triggers for reassessment of depth.

A depth change is permitted only when a versioned governed rule evaluates the trigger or an authorized human explicitly directs the change under approved authority. An LLM may identify and explain a candidate trigger, but may not invent an escalation rule or independently change depth. Each change must preserve the prior determination and record the triggering fact/event or rule, prior and new depth state, rule/version or human authority, rationale, actor, time, and affected assessment branches/work plan. Link the change and dependent re-evaluations through the Assessment Trace. Re-evaluate dependent stage outputs and gates without overwriting their prior history.

## Threat Library Architecture

SAR should govern a versioned Threat Library as a separate future catalog, not generate threats freely during each assessment. No threat patterns or trigger rules are created by this protocol proposal.

A future threat-pattern record should be capable of expressing:

- stable threat-pattern identity and version/status;
- threat family/category and concise scenario description;
- explicit triggering fact/derived-characteristic predicates and their rule version;
- affected asset, data, service, process, actor, and boundary scope;
- relationships to candidate requirements, safeguards/controls, and evidence expectations, each with provenance and applicability kept separate;
- rationale for selection, rejection, or human review;
- publisher/source, version, citation, and extraction/validation provenance;
- evidence or validation requirements where governed; and
- relationships to findings and risk records without equating these objects.

A threat is a possible adverse scenario; it is not a vulnerability, a finding, a control failure, a risk score, or a decision. A vulnerability or observed weakness may contribute to a threat/risk analysis but remains separately represented. MITRE ATT&CK may be a future source or mapping where suitable; SAR must support other sources and non-ATT&CK threat patterns. No ATT&CK relationship is presumed.

Threat selection is deterministic only where a validated pattern's explicit trigger rules match supported inputs. Fuzzy matches proposed by an LLM remain candidates for Reviewer confirmation. Changes to facts, pattern versions, or trigger-rule versions create a new selection evaluation and preserve prior history.

## Source, Requirement, Applicability, and Safeguard Resolution

The protocol consumes the Source Catalog and Requirement Model; it must not repeatedly ask an LLM to reinterpret raw source documents as the authority for each assessment.

1. **Discover candidates:** use governed source-family metadata and approved routing rules against characterized facts. The output is a candidate set, not an applicability conclusion.
2. **Pin assessment sources:** identify the exact registered source versions and immutable references used. Missing or stale metadata is surfaced for ingestion/review, not guessed.
3. **Resolve requirement records:** retrieve validated requirement representations and source provisions/citations for the candidates. Preserve source text/reference, SAR-normalized representation, semantic role, scope, conditions, exceptions, version, and validation provenance.
4. **Evaluate applicability:** apply only approved, versioned applicability rules to supported facts and relationship context. Record each independent basis and rationale. `Source references Source B` does not apply every requirement from B.
5. **Associate safeguards:** resolve approved requirement-to-safeguard/control mappings. Preserve multiple-source convergence and distinct risk bases. Do not duplicate a semantic requirement solely because multiple authorities reference a common framework; retain each authority path and provision.
6. **Plan evidence:** resolve approved expectation-to-evidence mappings for the selected depth. Evidence requirements must identify the assertion/expectation they test and applicable scope.
7. **Record provenance:** every candidate, resolution, rule execution, and relationship carries source/version/citation or an explicit unknown/unregistered state.

If a source family is registered but requirements have not yet been extracted and validated, the protocol records source presence and the requirement-coverage limitation. It must not fabricate requirement instances or mark source coverage complete. Candidate-source, applicable-authority, and reference/benchmark roles remain distinct.

## Claim, Evidence, and Validation Flow

The protocol preserves `Claim != Evidence != Validation != Finding`. A record may progress through these conceptual transitions only through a permitted actor/action and with provenance retained:

```text
REPORTED claim or fact
    -> evidence referenced/collected
    -> evidence checked against assertion and scope
    -> validation state recorded
    -> governed expectation evaluated
    -> candidate or reviewed finding / no-finding / unresolved
```

- Submitter may record a participant or vendor statement as `REPORTED`, link evidence, preserve `UNKNOWN`, `NOT_YET_VERIFIED`, and `CONFLICTING`, and correct a statement without erasing history. Submitter must not mark a claim independently `VERIFIED`.
- Automated checks may report mechanical results (for example, file presence, hash match, required metadata, or deterministic rule match) under an identified rule and tool version. Such checks validate only the property they actually tested; they do not establish truth or broad compliance.
- A reviewer/authorized validator may set a validation state such as `SUPPORTED`, `CONFLICTING`, `UNSUPPORTED`, or `VERIFIED` only when the evidence scope, method, authority, and role permit it. `VERIFIED` is a controlled assertion with actor, method, date, scope, and evidence linkage, not a synonym for “AI read a document.”
- Conflicting evidence remains conflicting until an authorized resolution is recorded. Do not overwrite superseded claims, evidence, or validation events.
- Missing, inaccessible, stale, or out-of-scope evidence remains explicitly unresolved and may block a dependent gate or require an evidence request/review; it is never presumed to satisfy an expectation.

Every transition links evidence and validation bidirectionally into the Assessment Trace. Validation is attached to the particular assertion/evidence/expectation and scope evaluated, not generalized across a product or vendor.

## Hard-Gate Architecture

A hard gate is a governed condition on a stage transition. Gates constrain progression and make blocked/unresolved work visible; they do not make the final software decision. No actual gate rules, severity thresholds, or approval logic are established here.

A future Gate Rule should carry a stable identifier, version, owner/approver, scope/stage transition, deterministic predicate or required human action, required inputs, outcome semantics, evidence/rationale requirements, and exception/escalation authority. A Gate Evaluation should capture the rule version, assessment snapshot, matched inputs, result, explanation, actor/tool, time, and permitted next actions.

Proposed gate-result vocabulary, subject to governance approval, is:

- `SATISFIED` - the specified transition condition is met;
- `UNSATISFIED` - evaluated criteria are not met;
- `UNRESOLVED` - required facts/evidence/rule interpretation are missing or conflicting; and
- `HUMAN DISPOSITION REQUIRED` - an authorized human must decide or approve a documented exception before the transition.

Possible gate families for later governed rule design include:

- assessment identity and execution/source provenance;
- required source or evidence inaccessible, unregistered, or unpinned;
- material data handling, population, hosting, or service boundary unknown;
- unsupported material vendor claim or evidence outside assessed product/tier/scope;
- required authority applicability unresolved;
- required safeguard not demonstrated or conflicting evidence;
- prohibited configuration established by an approved rule;
- material threat, finding, or high-impact condition unresolved under an approved rule; and
- human decision authority or record requirements absent.

The examples are gate-design candidates, not present-day policy. A failed gate may route to further characterization, evidence request, remediation, compensating safeguard, exception review, escalation, or human disposition as separately governed. It must not automatically label the software rejected, non-compliant, or unsafe. A gate cannot be cleared by LLM confidence or by changing an input without preserving the change event and re-evaluating dependent outputs.

## Deterministic Rules and Judgment Boundary

The conceptual deterministic evaluation relationship is:

```text
Assessment Facts
+ Governed Rule Versions
+ Source / Requirement Versions
+ Evidence / Validation State
    ->
Machine-Determinable Intermediate Determinations
```

Examples of intermediate determinations, only where the governing rules are complete and conclusive, include candidate applicability, governed applicability, required assessment depth, applicable requirement set, required evidence, gate state, and unresolved state. Human risk acceptance and final disposition are never machine-determinable results.

For a machine-determinable result, the protocol requires a reproducible evaluation context containing:

- normalized assessment facts and their state/provenance;
- applicable evidence and validation states;
- exact source and requirement versions;
- exact mapping, trigger, gate, classification, depth, or evaluation rule versions;
- protocol version and implementation/rules-engine provenance; and
- explicit rule inputs, outputs, and evaluation traces.

Under identical governed assessment facts, rule versions, source/requirement versions, and evidence/validation state, a deterministic rule must return identical machine-determinable intermediate results regardless of AI model, participant, Reviewer, or chat session. The evaluation must be reproducible from the governed assessment state and provenance; it must not depend on the original transcript or hidden conversational context. Rule changes or changed inputs create new evaluations; they do not silently mutate prior assessment history. The system records both the rule result and the exact facts, versions, and clauses producing it.

The deterministic boundary ends where a governed rule is absent, facts are ambiguous/conflicting, source meaning needs interpretation, evidence sufficiency depends on context, risk treatment involves professional judgment, or an exception/disposition requires authority. Record such outcomes explicitly as candidate, unresolved, or professional/human judgment, including the responsible role, inputs considered, rationale, and provenance. Do not present a judgment-dependent outcome as if it were a deterministic rule result. Final human risk acceptance and disposition remain separate authorized human decisions.

The LLM may facilitate intake, extract candidate facts with source locations, summarize, map candidate relationships, draft evidence questions, explain an already governed result, or flag mismatch/uncertainty. It may not silently create facts, thresholds, choices that encode thresholds, source obligations, requirements, applicability, threat patterns, findings, scores, gate rules, or approval logic. All LLM-derived candidates retain model/tool provenance and require the authorized validation path before they become governed determinations.

## Assessment Trace Integration

Each stage creates or updates versioned relationships in the existing bidirectional Assessment Trace; it does not create a parallel compliance record. At minimum the protocol must preserve:

```text
Assessment Fact(s)
    -> Applicability Determination + Rationale
    -> Requirement
    -> Authority / Source + Assessment Version + Citation
    -> Control / Safeguard
    -> Evidence
    -> Validation
    -> Finding
    -> Residual Risk
    -> Human Risk Decision
```

Characterize links questions/materials to facts and evidence. Classify links derived characteristics to supporting facts/rules. Applicability links each target to its independent basis and source version. Requirement resolution links requirement representations to provisions/citations. Threat selection links patterns to triggering facts. Evidence planning and evaluation link evidence/validation to the expectation and scope tested. Findings link expected and observed conditions, the supporting chain, and unresolved state. Residual risk links applicable safeguards, findings, treatments, evidence, and method. Human disposition links the exact assessment snapshot, residual risk, conditions, authority, and rationale.

Reverse traversal must start from a finding or human decision and reach originating facts, evidence, validation, safeguard, requirement, applicability basis, source/version/citation, and stage/rule versions. Forward traversal from a requirement must identify all assessments where it was evaluated and downstream evidence, findings, residual risk, and decisions. Supersession or re-evaluation appends history; it does not erase prior edges.

## Final Assessment Artifact

SAR should eventually publish a governed human-readable **Assessment** report for each assessment. It is the concise presentation of the assessment record, not a replacement for the detailed record, source catalog, trace, evidence, or human decision record. It should be capable of a concise opening summary that links to detailed traceability and presents, as applicable:

- assessment identity and status;
- product/service and intended use;
- assessment depth and its rule/version/rationale;
- key supported data, environment, and scope facts;
- applicable authority/source summary with versions and citations;
- key threats considered and their governed provenance;
- key findings and their evidence/validation links;
- unresolved items and open gates;
- residual-risk conclusion and method, if governed and established; and
- human disposition, conditions, decision-maker authority, and date, only if one exists.

No conclusion is fabricated to fill a missing field. Status must distinguish in-progress, blocked/unresolved, ready for human disposition, and disposed states once those terms are governed. “Complete” or “ready” never implies approved.

### `ASSESSMENT.md` Naming Collision and Migration

The repository-root `ASSESSMENT.md` currently serves as the S01-v2 QA launch/bootstrap artifact. It must not be overwritten, repurposed, or renamed by this architecture task.

The eventual canonical artifact should be the Assessment report concept, but a single shared repository-root `ASSESSMENT.md` is not a safe per-case result filename. Recommended migration, requiring separate approval:

1. Preserve the current QA launcher byte-for-byte with its commit provenance and move/copy it into a clearly governed test-launch location (for example, `tests/submitter/launch/ASSESSMENT.md`); update distribution and test references and verify its hash before removing any old path.
2. Define the per-assessment output identity and filename, preferably `SAR-{GUID}-ASSESSMENT.md`, with a governed template/schema and a deterministic report renderer. Keep a stable `ASSESSMENT.md` name only for a template or process entry if separately defined, not for multiple assessment results at repository root.
3. Preserve the launcher commit and QA-package history; do not make the old launch artifact appear to have been an assessment result.
4. Keep generated staff results and source evidence in approved controlled storage, not the public repository by default.

This proposal chooses no retention, publication, access, or schema policy for generated assessments.

## QA Result Interface (Reserved Hook)

No result-record schema or `tests/submitter/results/` location is currently governed. This protocol creates no result record and does not define that schema. It must expose a future execution interface sufficient to record:

- protocol human-readable/version identity and immutable protocol implementation provenance;
- Submitter/implementation provenance supplied by the governed execution package, not a SHA self-embedded in the same commit;
- assessment-depth, decision-rule, mapping, Threat Library, and gate-rule versions actually used;
- each assessment source/version/citation used;
- scenario/test-definition SHA and fixture identities/hashes;
- observable stage entry/exit events and transition reasons;
- Gate Rule IDs/versions, outcomes, unresolved conditions, overrides, and authority;
- evidence/validation transitions and provenance;
- final acceptance result or assessment disposition as a distinct field; and
- links to controlled evidence, remediation, and retest records.

The later QA-governance task must decide the record schema, permitted result states, storage location, privacy/redaction controls, retention, access, and how the controlled execution manifest supplies immutable identities. Until approved, testers use only the existing instruction to retain evidence in an approved controlled location.

## Existing Architecture Coverage and Remaining Gaps

The protocol relies on, and does not duplicate, these existing governed concepts:

| Existing artifact | Existing responsibility | Protocol gap this document addresses |
|---|---|---|
| [SAR-ARCHITECTURE.md](SAR-ARCHITECTURE.md) | Risk/authority principle, high-level decision/evidence chains, human risk authority. | No stage contracts, transition gates, or deterministic orchestration. |
| [SAR-INFORMATION-MODEL.md](SAR-INFORMATION-MODEL.md) | Facts, derived state, evidence, decisions, Assessment Trace. | Trace edges are defined, but no stage owns creating/updating them. |
| [SAR-INTAKE-MODEL.md](SAR-INTAKE-MODEL.md) | Adaptive fact collection, branches, unresolved facts, intake completion. | Intake completion is not a controlled handoff with explicit downstream gates. |
| [SAR-DECISION-LOGIC.md](SAR-DECISION-LOGIC.md) | Conceptual classification, inherent risk, applicability, controls, evidence, findings, residual risk, decision. | Rules are future work; sequencing, evaluation context, gate behavior, and human handoff are unspecified. |
| [SAR-APPLICABILITY-MODEL.md](SAR-APPLICABILITY-MODEL.md) | Applicability targets/bases/status, versioning, trace. | No executable resolver or stage-gate contract exists. |
| [SAR-REQUIREMENT-MODEL.md](SAR-REQUIREMENT-MODEL.md) | Source-bound requirement identity, version, semantics, scope, applicability and control relationships. | Requirement instances, validation, mappings, and resolution rules are unpopulated. |
| [SAR-SOURCE-CATALOG.md](SAR-SOURCE-CATALOG.md) | Source identity, versions, provenance, relationships, applicability separation. | No orchestration rules bind candidates to assessment-specific requirements. |
| [SUBMITTER.md](SUBMITTER.md) | Operational fact/evidence intake and Submitter boundary. | Human-directed LLM interaction is not a deterministic assessment engine; observed startup/threshold/state defects show a need for constrained execution. |
| [tests/submitter/README.md](tests/submitter/README.md) and scenario files | Manual behavior-based acceptance test method, vocabulary, and S01-v2 criteria. | No governed result-record schema/location or reusable stage/gate telemetry. |
| [roadmap/SUBMITTER-INTERACTION-REVISION.md](roadmap/SUBMITTER-INTERACTION-REVISION.md) and [roadmap/QNA-INTERACTION-ENHANCEMENTS.md](roadmap/QNA-INTERACTION-ENHANCEMENTS.md) | Submitter revision decisions and explicitly non-governed interaction candidates. | Neither is an approved assessment-execution protocol. |

No separate Reviewer architecture, deterministic rule catalog, Assessment Depth rules, Threat Library, gate-rule catalog, or executable assessment engine is present in the reviewed repository baseline. No source requirement extraction or rule population is created by this document.

## QA Findings as Architecture Inputs

The first governed S01-v2 result is recorded as `FAIL` at the governed test-definition baseline. The following generalized findings are architecture inputs; they do not rewrite the S01-v2 evidence or implement fixes:

- **S01-F01 - Startup determinism:** an open-ended “How would you like me to help?” response displaced direct governed startup. A protocol runner must own entry, initialization, and Start/Continue state; the LLM cannot decide whether to launch the governed workflow.
- **S01-F02 - Invented population ranges:** the model introduced numeric bins not provided by a governed rule. All bounded choices/ranges/thresholds must come from versioned governed rules or fact structures; unsupported bins are prohibited.
- **CONT-F01 - Missing actual assessment identity:** continuation output used a placeholder rather than a persistent case identifier. Machine-required state must be represented and validated as an actual identifier; narrative claims that one exists are insufficient.
- **CONT-F02 - Missing implementation provenance:** continuation omitted the exact implementation identity. Runtime/package provenance must be supplied externally and carried into state; it must not be guessed by the model.
- **PROV-F01 - Self-referential SHA:** `SUBMITTER.md` contains an obsolete SHA for the implementation. A commit cannot reliably embed its own final commit SHA. The runtime must obtain the SHA from an external governed execution/distribution manifest and must record mismatches as provenance errors; this task does not correct the operational artifact.

These generalized findings are based on the reviewed QA report and artifacts. The source staff files remain in controlled storage and are not copied here.

## Future Implementation Dependencies

This architecture does not authorize implementation. Before building an engine, SAR governance must separately approve:

- lifecycle terminology, stage states, transition contracts, and gate vocabulary;
- identity/provenance manifest and self-reference resolution;
- classification, inherent-risk, Assessment Depth, applicability, threat, requirement, evidence, evaluation, finding, severity, and residual-risk rules;
- source/requirement/control/threat catalog schemas and content validation;
- reviewer/validator/decision-maker roles and delegated authority;
- exception/remediation/escalation paths;
- assessment output and `ASSESSMENT.md` migration;
- QA result schema, protected storage, privacy, retention, and audit requirements; and
- machine-readable representation, rule engine, validation, and change-control process.

No numerical thresholds, assessment-depth labels, threat scenarios, source requirements, control mappings, finding severities, risk formulas, or approval criteria are established here.
