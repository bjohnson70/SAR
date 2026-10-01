# SAR Runtime Interface

## Purpose and Scope

**GOVERNED ARCHITECTURE - INTERFACE CONTRACT, NOT AN IMPLEMENTATION**

This document defines the minimum boundary between the trusted runtime that establishes whether an operational SAR role may execute, Submitter factual intake, downstream Assessment Protocol execution, and Execution Record provenance. It is intentionally limited to responsibilities and logical information exchanged at those boundaries.

It does not define serialization, APIs, identifier syntax or generation technology, cryptography, a machine-readable schema, question-registry entries, scoring, thresholds, applicability rules, or downstream assessment policy. Those require separate governance. It does not modify `SUBMITTER.md` or implement Submitter v1.1.

## SAR Execution Context

A **SAR Execution Context** is the trusted runtime context established before an operational SAR role begins. It is neither Assessment State, Assessment Execution Record, QA Result, Submitter continuation state, Assessment Protocol, nor participant-provided data.

As applicable, the context exposes to the invoked component:

- whether execution is authorized and ready;
- the Assessment ID for the case;
- the Execution ID for this governed execution;
- the SAR Execution Manifest reference and its verification state;
- the operational contract identity and human-readable version;
- required governed artifact identities and availability/readability status;
- execution/bootstrap limitations; and
- QA/test context, when the execution is a test.

The context is supplied through a trusted runtime boundary. It is not inferred from conversation text, participant claims, a filename, model memory, or a moving branch name. Missing or conflicting values remain explicitly unavailable, unresolved, or invalid as appropriate; the model must not fabricate them.

The interface describes logical information only. It does not prescribe transport, storage, serialization, ID format, authorization technology, or cryptographic mechanism.

## Ownership Boundaries

| Owner | Governing question | Responsibilities | Boundary |
|---|---|---|---|
| Runtime / Launcher | Can SAR validly execute? | Establish trusted bootstrap; evaluate execution authorization/readiness; check required governed artifact availability/readability and manifest/artifact correspondence; supply Assessment ID, Execution ID, and trusted Manifest context; report execution/bootstrap limitations. | Does not decide whether factual intake is sufficient for assessment and does not make assessment conclusions. |
| Submitter / Intake Governance | What factual information should SAR collect next? | Consume a valid Execution Context; collect facts; ingest documents; select governed question intents; activate factual branches; preserve UNKNOWN/conflicts/claims/evidence references; record corrections; maintain continuation state; hand off factual state. | Does not determine classification, inherent risk, Assessment Depth, applicability, requirements, findings, residual risk, approval, authorization, or disposition. |
| Assessment Protocol | What can SAR determine from the factual assessment state? | Consume factual state; govern downstream classification, inherent risk, applicability, Assessment Depth, threats, requirements, evidence evaluation, findings, residual risk, gates, and human-disposition interface under governed rules. | Does not bootstrap or establish its own trusted runtime context. It does not silently treat intake completion as a determination. |
| Execution Record Architecture | What context and inputs produced this execution's outputs? | Record context/manifest references, state snapshots, rules and versions, events, intermediate determinations, provenance, and QA behavior/results as applicable. | Records execution; it does not authorize execution or replace Assessment State or QA Result. |
| Human Authority | Who may authorize exceptions or make final decisions? | Exercise governed exception, authorization, validation, and final decision authority where assigned; preserve rationale and scope. | Authority is not inferred from a model, runtime status, gate, or participant role statement. |

The dependency is one-way at startup and handoff: Runtime establishes readiness, Submitter consumes context and produces factual state, then the Assessment Protocol consumes that state. The Protocol does not call back into the runtime to authenticate its own bootstrap; runtime does not inspect factual completeness to approve progression.

## Bootstrap and Startup Contract

### Bootstrap

Bootstrap is the trusted Runtime / Launcher operation before Submitter startup. It establishes that execution is authorized and determines whether required governed artifacts are available, readable, and consistent with the SAR Execution Manifest. It supplies the SAR Execution Context to Submitter.

The runtime may verify only properties for which it has an authorized mechanism and evidence. It must distinguish verified facts from unverified declarations and report its verification limits. A model cannot certify its own bootstrap by repeating a version string or acknowledging that an attachment or URL exists.

### Startup

The boundary is:

```text
Valid SAR Execution Context
    ->
Submitter Startup
```

When valid context is supplied, Submitter deterministically enters the governed participant-facing startup and presents its human-readable contract identity with the Start New / Continue interaction. It does not first ask what the participant wants the AI to do, how it can help, or whether SAR should run. No participant magic phrase is required.

When required context or artifacts are missing, invalid, mismatched, or unreadable, Submitter does not claim successful initialization, invent identity/provenance, or proceed as if SAR is validly running. It reports the supplied execution/bootstrap limitation and stops or follows only a separately governed recovery path. Runtime readiness is not an assessment determination.

The operational prompt wording and observable startup belong in `SUBMITTER.md`; the trusted readiness and artifact-verification responsibilities belong to Runtime / Launcher architecture.

## Identity Interfaces

The runtime supplies identity values in trusted context; their syntax and generation technology remain unspecified:

- **Assessment ID:** persistent assessment/case identity. Runtime supplies it for a new case and supplies the existing value for continuation.
- **Execution ID:** identity of one governed execution event. A case may have multiple executions; this value never replaces Assessment ID.
- **Chat/session identity:** identity assigned by the AI environment, if available. It is contextual metadata only and is not Assessment ID or Execution ID.
- **QA Result identity:** identity of a test execution/result, distinct from a product Assessment ID. A QA run may reference a synthetic Assessment ID and one or more execution events when useful.

Submitter consumes Assessment ID and Execution ID, preserves the Assessment ID across continuation, and does not invent or ask the participant to create/manage them. The runtime's issuance authority and ID format are intentionally not selected here.

## Continuation-State Contract Version 2

Govern **Continuation-State Contract Version 2** as the next logical continuation-state contract. This change is justified by changed required state semantics, not merely by the human-readable Submitter version changing.

Version 2 requires the logical ability to preserve or reliably reference:

- the actual Assessment ID;
- human-readable Submitter contract version;
- continuation-state contract version;
- applicable SAR Execution Manifest / Execution Context reference;
- current factual-intake progression state and next interaction;
- reviewed material inventory and its provenance;
- established facts and source provenance;
- participant/requestor/vendor claims, kept distinct from evidence;
- evidence references and validation state;
- UNKNOWNs, conflicts, and unresolved items;
- corrections and activity/history links; and
- execution context needed to understand the state, without copying the entire manifest.

The continuation artifact remains state, not bootstrap authority. A fresh runtime must establish governed artifacts and context before Submitter consumes the state. No fixed filename, heading structure, or serialization is specified here.

This is a proposed semantic contract. Implementation must not treat the version as active until the v1.1 release and continuation migration are governed together.

## Version-1 Continuation Compatibility

A v1 artifact is evaluated against trusted runtime context and its preserved factual state; missing historical provenance is never inferred.

- **Compatible:** Runtime context establishes the required Assessment ID and provenance without conflict, and preserved v1 facts/state are usable under v2. Continue with an explicit record that historical v1 provenance was absent where it was absent; do not backdate or claim it was present in the v1 artifact.
- **Degraded / Unresolved:** Factual state remains usable, but some historical provenance cannot be established. Preserve the missing provenance explicitly as unresolved and identify affected state. Continue only where no separately governed requirement blocks that use; do not infer a missing implementation SHA.
- **Blocked:** A verified identity/provenance conflict or another already governed blocking condition prevents safe continuation. Stop continuation, report the conflict, and route to the runtime/human process. This interface invents no additional block conditions.

A migration or compatibility operation creates a new state/event referencing the original v1 artifact; it does not rewrite that artifact or its historical provenance. Whether compatible or degraded state can proceed through each later Protocol gate remains governed downstream.

## Question Intent Registry

**SAR Intake Governance** owns the governed **Question Intent Registry** interface consumed by Submitter. It defines the semantic purpose and permitted response structure of factual questions without prescribing a fixed questionnaire or exact conversational wording.

A Question Intent may conceptually define:

- intent identity;
- factual purpose and information element(s);
- activation conditions and dependencies;
- required/optional semantics;
- allowed response form;
- governed bounded options, if any, and their governing source/version;
- UNKNOWN behavior;
- provenance/evidence expectations;
- completion and unresolved semantics; and
- governed priority/next-intent behavior where defined.

This artifact defines the interface only and populates no registry entries. No population ranges, scoring options, thresholds, or applicability choices are created here.

## Deterministic Intent and Conversational Wording

> Question intent and semantic choices are governed. Conversational wording may vary.

The LLM may phrase an eligible governed factual question naturally, clarify participant meaning without changing answer semantics, summarize a response, and extract candidate facts from supplied documents with provenance. It may not invent semantic branches, bounded option sets, numeric ranges, thresholds, scoring choices, applicability choices, or hidden decision structures.

When a governed bounded option set is not defined for an intent, use factual free response, clarification, or UNKNOWN. The model may not manufacture options because they appear convenient. Submitter consumes Question Intents from the Intake Governance interface; the operational contract explains this constraint and applies it during conversation. Runtime supplies readiness/context but does not own the question registry. The Assessment Protocol owns downstream assessment rules, not Submitter question wording.

## Factual Handoff to Assessment Protocol

The governed boundary is:

```text
SAR Execution Context
    ->
Submitter
    ->
Factual Assessment State
    ->
Assessment Protocol
```

Submitter handoff may be:

- sufficiently characterized for Protocol processing;
- intentionally incomplete with explicit UNKNOWNs, conflicts, limitations, and evidence requests; or
- unable to proceed because of an execution/environment limitation.

“All facts known” is not required. Runtime does not determine assessment sufficiency. Submitter does not create classification, inherent risk, Assessment Depth, applicability, findings, residual risk, approval, or disposition. The Assessment Protocol evaluates factual state against its governed stage/gate logic and identifies unresolved work.

## Relationships to Existing Governed Artifacts

- [`SUBMITTER.md`](SUBMITTER.md) owns the operational Submitter contract, participant-facing startup, factual intake behavior, and continuation artifact behavior. It consumes SAR Execution Context and governed Question Intents; it does not bootstrap itself or perform downstream assessment.
- [`ASSESSMENT-PROTOCOL.md`](ASSESSMENT-PROTOCOL.md) owns downstream assessment progression after factual handoff. It does not establish runtime trust/readiness or define the participant's Submitter interview.
- [`SAR-EXECUTION-RECORD.md`](SAR-EXECUTION-RECORD.md) owns the logical execution/QA record architecture, immutable provenance binding, snapshots, and history. Execution Context is supplied to, and referenced by, its records; it is not itself an execution record.
- [`SAR-INTAKE-MODEL.md`](SAR-INTAKE-MODEL.md) owns factual intake concepts and adaptive branches. SAR Intake Governance owns the Question Intent Registry interface and any future governed entries; this document introduces no questionnaire or entries.

No cyclic ownership is intended: Runtime establishes context; Submitter consumes it; the Assessment Protocol consumes Submitter factual state; Execution Record Architecture captures the relevant context and events. Human Authority governs exceptions and final decisions.

## Version and Provenance Principles

Keep distinct:

- human-readable Submitter contract version;
- implementation Git provenance supplied by the SAR Execution Manifest;
- Assessment Protocol provenance;
- continuation-state contract version;
- Question Intent Registry/rule provenance when governed; and
- acceptance-test-definition provenance for QA.

These values are carried by trusted context/manifest and applicable continuation state, not entered or managed by participants. A missing value is explicit as unavailable, unresolved, or not implemented where applicable. No artifact embeds a guessed SHA of its own future commit. Changes to interface semantics require governance and compatible versioning; a human-readable contract revision alone does not silently redefine state semantics.

## Unresolved Implementation Mechanics

This architecture intentionally leaves for later governance and implementation:

- which organizational service issues Assessment IDs and the permitted fallback/uniqueness behavior;
- who authorizes execution and the exact readiness states/transitions;
- how runtime verifies artifact identity, readability, manifest correspondence, and context integrity;
- how the Question Intent Registry is stored, reviewed, versioned, and supplied;
- the precise compatible/degraded/blocked v1 migration rules and any downstream gates;
- how continuation-state version 2 is activated and how v1 state is labeled/migrated;
- how runtime limitations are surfaced to the participant or operator; and
- transport, serialization, storage, privacy, retention, and access technology.

No ID syntax, cryptography, serialization, implementation technology, question entry, option/range, threshold, scoring rule, or assessment requirement is selected by this document.
