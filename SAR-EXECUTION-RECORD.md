# SAR Execution Record and QA Result Architecture

## Status and Authority

**ARCHITECTURE PROPOSAL - NOT AN APPROVED RECORD SCHEMA OR RESULT**

This document proposes how SAR distinguishes evolving assessment state, immutable assessment execution history, and QA/acceptance-test results. It also defines the architectural provenance interface needed to explain and reproduce governed machine-determinable outputs.

This is not a machine-readable schema, operational engine, result record, test result, assessment decision, evidence repository, or authorization. It does not alter the Assessment Protocol, Submitter contract, test definitions, or evidence-retention policy. Governance approval is required before implementing the proposed record types, manifest, result location, identifiers, storage, access controls, or retention.

## Architectural Context

The [SAR Assessment Protocol](ASSESSMENT-PROTOCOL.md) governs lifecycle orchestration and reserves a QA result interface. This document specifies the logical record concepts and their relationships without re-defining the Protocol, Information Model, Source Catalog, Requirement Model, Applicability Model, or Decision Logic.

The record architecture preserves:

```text
Assessment State != Assessment Execution Record != QA / Acceptance-Test Result
```

These records may reference shared identities and provenance, but have different purposes, lifecycle, authority, access, and retention requirements. They must not be collapsed into a single mutable compliance document.

## Record Types and Relationships

### Identity Separation

The following identities are distinct and must never substitute for one another:

- **Assessment ID** identifies the assessment/case. It persists across multiple executions, pauses and resumes, evidence updates, reevaluations, remediation, and retests when the same assessment remains in scope. It is not a chat, execution, or QA-result identity.
- **Execution ID** identifies one governed orchestration/evaluation event. One Assessment ID may have many Execution IDs. An Execution ID identifies that event only; it must never replace, redefine, or cause regeneration of the Assessment ID.
- **QA Execution ID / QA Result ID** identifies a QA behavior-evaluation run/result, distinct from the product Assessment ID. A QA execution may reference a synthetic Assessment ID when appropriate, one or more execution events, and the scenario/test-definition identity. It does not become the assessed product's Assessment ID or state.

These are conceptual identity roles only. No identifier syntax, generation method, namespace, or collision policy is selected here.

### Assessment State

Assessment State is the current, evolving, governed state of one assessment. It is the current projection of accepted facts, evidence references, validations, determinations, gates, findings, treatments, and any human disposition. It is not a transcript and is not itself an immutable execution event.

As applicable, it can contain or reference:

- Assessment ID and product/service/use scope;
- established facts, claims, sources, and provenance;
- evidence and its validation state;
- unresolved, unknown, conflicting, and inaccessible items;
- applicability determinations and rationales;
- requirements and source/version/citation references;
- threat selections and Assessment Depth determination where governed;
- safeguards, evaluation results, findings, treatment, and residual risk;
- current Protocol stage and gate state; and
- human dispositions and conditions where made by an authorized person.

A state update may change the current projection, but must not erase its provenance or make earlier state unrecoverable. Current values link to the events and records that established or changed them.

### Assessment Execution Record

An Assessment Execution Record is an immutable record of one governed orchestration or evaluation event against an identified assessment-state snapshot. It answers what inputs and governed versions were evaluated, what machine-determinable intermediate outputs and gate results were produced, what remained unresolved, and where professional judgment or human action entered.

One assessment has evolving state and may have many execution records. An execution record references the input snapshot and creates an output snapshot or state delta; it does not replace Assessment State or itself authorize software.

### QA / Acceptance-Test Result

A QA Result is an immutable record evaluating observable SAR behavior against one exact committed test definition, implementation-under-test, fixture set, and execution context. It answers whether specified criteria passed, failed, were not tested, were limited by the environment, inconclusive, or were cancelled/superseded under the governed vocabulary.

A QA Result is not Assessment State, not an Assessment Execution Record, not evidence that every future run will behave identically, and not an approval decision. It may reference one or more execution records and controlled evidence items, but its criterion outcomes remain specific to its scenario and run.

### Relationships

```text
Assessment State (evolving current projection)
    <- produced/updated by - Assessment Execution Records (immutable history)

QA Result (immutable behavior evaluation)
    -> references test definition, implementation, fixtures, environment
    -> may reference execution records and controlled evidence references
    != Assessment State
    != human risk disposition
```

A Submitter Continuation Artifact remains a portable state-transfer representation subordinate to `SUBMITTER.md`; it is not any of these record types unless a later governed format explicitly maps it to a state snapshot. A transcript is contextual evidence only and is not the system of record.

## Authoritative Execution Provenance

### SAR Execution Manifest

Establish one provenance mechanism: an externally supplied, immutable **SAR Execution Manifest** bound to the governed package/runtime before an assessment or test begins. This manifest, rather than a Git SHA embedded in `SUBMITTER.md`, is authoritative for identifying which exact artifacts and versions the execution is expected to use.

The manifest is created or approved by a governed release/distribution process, is made available to the execution host/orchestrator, and is bound to the package contents through immutable references and integrity checks. The participant does not enter, choose, remember, confirm, or manage any manifest fields. The specific signing, distribution, and verification mechanism requires future security and release-governance approval; this proposal does not invent one.

Each Assessment Execution Record must bind to the exact manifest instance used through the combined reference:

```text
Manifest Identity
+ Manifest Version
+ Manifest Content Integrity Reference
    ->
Assessment Execution Record
```

The record preserves all three reference components as observed/verified for that execution and records the integrity-verification outcome. A later manifest revision receives a new immutable manifest identity/version or an equivalent immutable representation. It must not change, replace, or rewrite the manifest provenance attached to historical executions. No hash algorithm, signing technology, serialization format, or PKI mechanism is selected here.

If a file contains a conflicting embedded SHA, the manifest does not silently rewrite that file. The conflict is recorded as a provenance mismatch, an execution gate is evaluated under an approved rule, and the exact artifact actually consumed is retained by immutable reference/hash. Never claim that a mismatched artifact is the expected build.

### Manifest Identity Fields

The future manifest should identify, using a value or an explicit state such as `NOT IMPLEMENTED`, `NOT APPLICABLE`, or `UNRESOLVED` where appropriate:

- manifest ID, manifest format/version, issuer/approver, creation time, and integrity reference;
- human-readable contract version, for example `SAR Submitter v1.0`;
- implementation provenance: repository identity, immutable Git commit where applicable, artifact path, and content digest;
- Assessment Protocol version/provenance;
- deterministic rule-set, mapping, gate, and classification versions actually available;
- source-family and assessment source-version references where bound to a package;
- Requirement Catalog/version or explicit not-yet-implemented state;
- Threat Library/version or explicit not-yet-implemented state;
- continuation-state contract version where relevant;
- scenario/test-definition commit SHA and scenario ID when this is a QA package;
- fixture identities and content digests for QA; and
- supported runtime/dependency identifiers when governed and material to reproducibility.

These are separate identities. Human-readable contract version is not implementation commit; protocol version is not rule-set version; source version is not requirement version; continuation-state version is not a file schema; and test-definition SHA is not implementation provenance. Unavailable items must not be fabricated or inferred from a moving branch name.

### Self-Referential Git Provenance

A Git artifact cannot reliably contain the final commit SHA of the commit that contains the artifact itself. Therefore:

- source documents describe provenance requirements and semantic version identities, not their own future commit SHA;
- the manifest supplies the immutable implementation SHA and exact artifact digest externally;
- an execution record copies the verified manifest identity and records the exact artifact actually loaded; and
- an embedded SHA mismatch is preserved as a provenance defect, not silently corrected or accepted.

This mechanism addresses the known stale SHA in the historical Submitter implementation without modifying that implementation here. Until the manifest mechanism is implemented and governed, affected provenance is explicitly unresolved; it must not be represented as verified.

## Assessment Execution Record Content

A future Assessment Execution Record should be append-only and identify at minimum:

### Identity and execution context

- Assessment ID;
- Execution ID/Event ID, unique within the governed namespace;
- QA Execution ID and QA Result ID when the event is a QA run, distinct from Assessment ID;
- execution timestamp and time basis;
- exact input state snapshot identity/integrity reference and resulting state snapshot identity/integrity reference or state-delta reference;
- acting component/role and authority context;
- SAR Execution Manifest identity, version, content-integrity reference, and verification state; and
- controlled evidence references where applicable.

### Governed versions and inputs

- SAR Execution Manifest and manifest-integrity result;
- human-readable contract and implementation provenance actually consumed;
- Assessment Protocol version/provenance;
- rule-set, mapping, gate, classification, and depth-rule versions used, each explicitly stateful if unavailable;
- exact source and requirement versions/citations evaluated;
- Threat Library version/patterns where applicable;
- continuation-state version where applicable;
- relevant fact/state snapshot or stable references, including fact provenance and states;
- evidence references, scope, integrity references, and validation states; and
- applicable test definition, scenario, and fixture identities if the event is QA-related.

### Stage execution and outputs

- stage entered and stage completed, or explicit interruption/failure;
- transition reason and inputs consumed;
- rule IDs/versions and predicates evaluated;
- machine-determinable intermediate determinations and rationale/trace output;
- gate IDs/versions, outcomes, and permitted next actions;
- unresolved, unknown, conflicting, inaccessible, or not-applicable state;
- professional-judgment points, including the responsible role, inputs considered, rationale, and result;
- human overrides or dispositions, authority and rationale, when they occur; and
- links created or superseded in the Assessment Trace.

The record must distinguish a calculated/rule-derived output from a model-proposed candidate and from a Reviewer judgment. A result with missing provenance is marked unresolved rather than given an assumed version. It must not require transcript replay to reconstruct machine-determinable outcomes: the governed state snapshot, manifest, input versions, rule versions, evaluation trace, and outputs are the reproducibility basis.

## Event, History, and Snapshot Model

Use an append-only execution/event history plus immutable state snapshots or content-addressed snapshot references. The current Assessment State is a projection of accepted facts and determinations from that history.

The conceptual relationship for each state-affecting execution is:

```text
Assessment ID
    -> Input State Snapshot Identity / Integrity Reference
    -> Execution Event (Execution ID + bound Manifest reference)
    -> Resulting Determinations and Gate Outcomes
    -> Next State Snapshot Identity / Integrity Reference or State Delta
```

The execution record must establish which exact assessment state was evaluated and which state/delta resulted. An implementation need not duplicate the entire assessment state in every event: it may reference immutable snapshots or governed state deltas, provided the references resolve to the exact input state and resulting state for that execution. Snapshot identity and integrity-reference semantics are conceptual here; their syntax and technical integrity mechanism remain for future governance.

- Events record facts or evidence added/corrected, validation changes, source/requirement/rule changes, stage transitions, gate evaluations, depth reevaluations, reviewer judgments, overrides, and human dispositions.
- Snapshots capture the exact normalized assessment state and version manifest used at important execution boundaries, including each reproducible evaluation and human decision.
- State projections can be recomputed from the event history and snapshot inputs under a specified projection/version, subject to future implementation and retention approval.
- Corrections append a superseding state event and preserve the prior value, provenance, reason, and link; they do not mutate historical execution inputs or overwrite history. A corrected fact is present in a later snapshot/state delta and triggers a new execution where required.
- Re-evaluation appends a new determination linked to the prior determination and states whether it supersedes, supplements, or leaves it unchanged.

Every change record should identify a change cause, when known: new fact; corrected fact; new evidence; validation change; source update; requirement update; rule update; Assessment Depth reevaluation; professional judgment; human disposition; or another governed cause. If the cause is not established, record it as unknown. A changed source or rule version does not itself rewrite prior outputs; affected evaluations are identified and rerun through governed impact/reassessment logic.

This is an architectural preference, not an approved storage or database design. Hash chaining, event-log technology, retention periods, and transaction guarantees require later implementation/security governance.

## Deterministic Evaluation Record

The reproducibility relation is:

```text
Assessment Facts / State Snapshot
+ SAR Execution Manifest
+ Governed Rule Versions
+ Source / Requirement Versions
+ Evidence / Validation State
    ->
Machine-Determinable Intermediate Determinations
```

An evaluation record captures:

1. exact input snapshot and relevant fact IDs/states/provenance;
2. manifest and verified artifact identities;
3. source and requirement versions/citations actually evaluated;
4. rule/mapping/gate/protocol versions used;
5. evidence identity/scope and validation state at evaluation time;
6. deterministic predicates/clauses and inputs matched;
7. output and result state, including unresolved where rules are absent or inputs insufficient;
8. rationale that explains the rule path without substituting freeform LLM reasoning for rule provenance; and
9. any separate professional judgment or human action required afterward.

Candidate applicability, conclusive governed applicability, required Assessment Depth where rules are conclusive, applicable requirement set, required evidence, gate state, and unresolved state may be machine-determinable. Whether to accept residual risk or issue final disposition is not. If professional judgment is necessary, the record marks it as required/provided and records who exercised it and why; it must not claim that identical inputs alone determined that judgment.

Identical governed inputs and versions must produce identical machine-determinable outputs regardless of AI model, participant, Reviewer, or chat session. Chat history is not the system of record. If an LLM contributes an extracted candidate fact or proposed mapping, that candidate and model/tool provenance are recorded; until authorized validation, it is not silently promoted to a deterministic input.

## QA / Acceptance-Test Result Architecture

### Purpose and relation

A QA Result is a test-run record against one immutable test definition and implementation package. It evaluates behavior observed in the test, not the assessed product's risk or approval. It is separate from Assessment State and Assessment Execution Record, even if all three refer to the same Assessment ID or implementation.

A QA Result must identify the exact scenario/test-definition SHA, implementation-under-test provenance from the manifest, contract version, Protocol/rule versions where applicable, fixture identities/hashes, execution ID/date, environment/model where known, and result for each governed criterion. It should record:

- criteria evaluated and criteria not tested/insufficiently evidenced;
- passed behaviors and failed behaviors;
- prohibited behavior observed;
- environment limitations and `INCONCLUSIVE` observations;
- overall result under the currently governed result vocabulary;
- finding IDs and severity basis where governed;
- remediation linkage and retest linkage; and
- controlled-evidence references without embedding protected evidence.

Result values remain those already governed in [tests/submitter/README.md](tests/submitter/README.md): `PASS`, `FAIL`, `NOT TESTED`, `ENVIRONMENT LIMITATION`, `INCONCLUSIVE`, and `CANCELLED / SUPERSEDED`. A later approved common test architecture may generalize them, but this proposal does not redefine them.

A QA Result does not become Assessment State, a finding about an assessed product, an Assessment Execution Record, or a human risk decision. A QA finding concerns SAR implementation/test behavior and has separate identity/linkage from assessment findings.

### Domain crosswalk

S01-v2 currently declares domains `A, B, C, D, E, F, G, H, I, J, K, U, X`. No authoritative mapping from those letters to domain names was found in the reviewed repository. The crosswalk must not be inferred from criteria wording or invented in a result record.

Before a result relies on domain-letter outcomes, acceptance-test governance should define one canonical Domain Registry/crosswalk at the shared test-framework level, with stable domain ID, display name, definition, criteria mapped to it, version, owner, and change history. Each scenario should reference those stable IDs; historical test definitions/results preserve the mapping version used. If this governance is not approved, results record criterion-level outcomes and quote the scenario's declared domain codes unchanged, with domain names marked `UNMAPPED` rather than guessed.

## Public Repository and Controlled Evidence Boundary

The SAR repository is public. A public QA Result may contain only generalized, synthetic, non-identifying information such as:

- scenario/test and implementation/protocol/rule/source provenance;
- criterion-level outcomes and generalized findings;
- synthetic TESTSTAR facts or fixture hashes;
- remediation/retest IDs or public commit references; and
- a logical reference indicating that supporting evidence is retained in an approved controlled location.

Do not put raw staff emails, names, contact details, signatures, screenshots, raw transcripts containing organizational details, DDS-sensitive information, non-public assessment artifacts, private filesystem paths, or other protected information in public records. Do not require private paths to resolve a public reference.

Use a logical controlled-evidence reference (for example, an opaque evidence-record ID issued by the controlled evidence custodian) plus an access/retention classification governed outside the public artifact. The public record may state evidence category, custodian role, date range, retention/access restriction, and opaque reference if approved; it must not disclose the secret location or protected contents. Encryption, access control, retention, redaction, custodian workflow, and public-reference policy require separate governance.

## S01-v2 Design Exemplar

The first governed S01-v2 execution is an architecture exemplar with these supplied identities:

- scenario: `S01-v2`;
- human-readable contract: `SAR Submitter v1.0`;
- implementation-under-test: `22eb88f7eb78a1c07bd68eec1424e1341d0eae73`;
- test definition: `d28e6cceccdae8b5d7605ca7ee2e6a807ddf816f`;
- continuation-state contract version: `1`; and
- overall S01-v2 result: `FAIL`.

Do not create or modify its historical result record in this task. The reviewed generalized findings map as follows:

| Finding | Record relationship | S01-v2 disposition relationship |
|---|---|---|
| `S01-F01` - governed startup did not directly establish Submitter workflow | QA behavior finding, linked to startup/version criterion and controlled execution evidence reference. | Directly supports S01-v2 `FAIL`: governed startup and visible initialized contract are explicit acceptance/failure criteria. |
| `S01-F02` - model introduced non-governed numeric population ranges | QA behavior finding, linked to facts-before-classification and population/scope criterion, relevant `SUBMITTER.md` rule, and evidence reference. | Directly supports S01-v2 `FAIL`: model-invented bounded population ranges violate the operational contract and scenario's no-invented-facts/no-unapproved behavior criteria. |
| `CONT-F01` - continuation artifact used placeholder rather than actual persistent Assessment ID | Continuation behavior finding linked to continuation-state identity requirements and S10/S11 evidence. | Not independently a reason S01-v2 fails: S01-v2 explicitly does not test persistence through later continuation state. Keep as a separate continuation defect for its owning acceptance scope. |
| `CONT-F02` - continuation omitted exact implementation provenance | Continuation/provenance finding linked to minimum continuation-state provenance and S10/S11 evidence. | Not independently within S01-v2's later-persistence scope. It is nevertheless a provenance defect in the reported continuation artifact and may have separate execution-package significance. |
| `PROV-F01` - operational contract embeds obsolete/self-referential SHA | Implementation/provenance defect linked to the exact contract blob and external manifest identity. | Not an observed model behavior and not by itself a participant behavior criterion. It is a serious execution-provenance defect: the artifact bytes are identified by the supplied IUT commit, while the embedded value conflicts. Preserve and report the mismatch; do not silently rewrite the historical run identity. |

The supplied overall `FAIL` is consistent with S01-F01/F02. QA findings about SAR's behavior are not product assessment Findings and do not determine product risk or disposition. The raw source evidence remains controlled and is not copied into this proposal.

## Recommended Repository Structure and Naming

No general execution/result schema or result directory currently exists. The README explicitly says there is no `tests/submitter/results/` directory and that generated evidence remains in an approved controlled location until governance is approved. This architecture does not create a result record or directory.

The minimum recommendation is one reusable public architecture/template location for future records and no public operational execution log by default:

- `SAR-EXECUTION-RECORD.md` - this logical record/QA-result/provenance architecture;
- `tests/results/<scenario-id>/<execution-id>.md` - proposed public-safe QA result location, only after a separate governance decision and README update;
- controlled evidence store - raw execution evidence, referenced only through approved opaque evidence IDs; and
- controlled assessment record store - non-public Assessment State and Assessment Execution Records, unless a later publication policy authorizes synthetic/public records.

Use stable scenario IDs such as `S01-v2` and an execution ID independent of model/session identity. An execution ID must be unique in its governed namespace; its syntax, generation authority, and collision policy require implementation governance. A public result filename should be deterministic from scenario and execution IDs, not a person's name or a private path. Remediation and retest use stable finding/remediation/retest identifiers cross-linked to the QA Result, not overwritten result files. Repeated runs create new result records that link back to the superseded/current test or remediation chain; they do not replace earlier evidence.

This is a proposed structure, not permission to create `tests/results/`, expose a result, or store sensitive evidence publicly. A general `tests/results/` is preferred over Submitter-only results if approved, because future protocol, Reviewer, and other acceptance suites need the same separation. Do not create multiple template/schema directories before the record model and access policy are approved.

## Future Machine-Readable Representation

Markdown remains the design/governance source. Future machine-readable forms may map the stable logical concepts to JSON/YAML or appropriate OSCAL-linked structures without changing their distinctions. Candidate top-level objects are `AssessmentStateReference`, `ExecutionRecord`, `ExecutionEvent`, `StateSnapshotReference`, `SARExecutionManifestReference`, `RuleEvaluation`, `GateEvaluation`, `ProfessionalJudgment`, `HumanDispositionReference`, `QAResult`, `CriterionOutcome`, and `ControlledEvidenceReference`.

Stable logical identifiers should be defined for Assessment ID, Execution/Event ID, Snapshot ID, Manifest ID, Fact ID, Evidence ID, Validation ID, Rule ID/version, source and requirement version references, gate ID/version, finding ID, test/scenario ID, criterion ID, QA Result ID, remediation ID, retest ID, and opaque controlled-evidence reference. These are conceptual identifiers, not a finalized naming syntax or schema.

A future schema must express absent/unavailable values with explicit states rather than fabricated strings, preserve versioned relationships, support append-only history and snapshots, and validate that human disposition is never emitted as a machine-determinable rule output. Schema versioning must remain distinct from continuation-state version, protocol version, implementation provenance, and acceptance-test-definition commit.

## Unresolved Governance Decisions

Human approval is required for:

- authoritative issuer, verification, integrity, and distribution process for the SAR Execution Manifest;
- what constitutes a reproducible assessment snapshot and the runtime's input-capture boundary;
- event immutability, append-only guarantees, snapshot cadence, integrity protection, retention, and access;
- assessment, execution, snapshot, result, criterion, finding, remediation, retest, and evidence ID syntax and authority;
- Domain Registry ownership and migration/crosswalk policy for existing S01 letter codes;
- whether public-safe QA results are permitted, their exact directory/template, review/redaction gate, and publication authority;
- controlled evidence custodian, opaque reference format, access workflow, privacy classification, and retention;
- relationship between public QA Result, controlled Assessment Execution Record, and any Assessment State snapshot;
- result revision/supersession policy, test failure remediation linkage, and retest linkage; and
- future machine-readable schema format/version and validation rules.

Until those decisions are made, do not create a QA result record, result directory, execution manifest instance, or machine-readable schema. Use only the existing authorized controlled-evidence handling instructions.
