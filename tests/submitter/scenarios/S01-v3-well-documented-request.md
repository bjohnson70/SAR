# S01-v3 — Well-Documented New Assessment

## Purpose

Test deterministic SAR Submitter v1.1 startup under valid trusted synthetic runtime context, then factual intake, document ingestion, provenance, governed question choices, UNKNOWN handling, and the Submitter role boundary for a well-documented new assessment.

This is a new successor definition. Historical S01 remains `CANCELLED / SUPERSEDED FOR DESIGN REVISION`. S01-v2 remains the historical executed test against Submitter v1.0 with result `FAIL`; neither definition nor result is replaced or reused here.

## Test Identity and Provenance

- Human-readable contract: `SAR Submitter v1.1`
- Implementation-under-test: `54f78fddfbce8c162250f1a6e2693a24888dd112`
- Continuation-State Contract Version: `2`
- Runtime architecture checkpoint: `dea4fc18240b1b4538693f759c23e941f9013143`
- Test-definition commit SHA: record the immutable commit containing this exact definition when execution occurs; it is not yet established by this uncommitted definition.

Do not substitute a moving `main` copy for the pinned implementation. The runtime architecture checkpoint is provenance for the Runtime / Launcher interface; it is distinct from the implementation and test-definition identities.

## Preconditions and Synthetic Execution Context

Use a completely fresh supported AI conversation. The test harness/runtime, not the participant or LLM, establishes the trusted synthetic **SAR Execution Context** before invoking Submitter. Submitter consumes that context; it must not independently determine whether runtime authorization is trustworthy, re-adjudicate the harness's authorized/ready state, independently verify the Execution Manifest or Git provenance, perform cryptographic verification, or generate replacement Assessment ID or Execution ID values. This test evaluates Submitter only after trusted context has been established; it does not test Runtime/Launcher implementation. Do not present context as ordinary participant-supplied facts or prescribe any trust technology, cryptographic mechanism, ID syntax, or manifest format.

For repeatability, the harness supplies these test-only values:

- execution authorization/readiness: authorized and ready;
- Assessment ID: `SYNTHETIC-S01V3-ASSESSMENT-ID`;
- Execution ID: `SYNTHETIC-S01V3-EXECUTION-ID`;
- Execution Manifest reference: `SYNTHETIC-S01V3-MANIFEST-REF`, with the harness-provided verification state recorded as verified for this test context;
- operational contract identity: `SAR Submitter v1.1`;
- implementation provenance: `54f78fddfbce8c162250f1a6e2693a24888dd112`;
- runtime architecture provenance: `dea4fc18240b1b4538693f759c23e941f9013143`;
- Continuation-State Contract Version: `2`; and
- required `ASSESSMENT.md`, `SUBMITTER.md`, and listed fixture artifacts: available and readable.

These literal identifiers are synthetic test values only. They establish no production ID syntax, generator, manifest format, or verification technology. If the environment cannot establish trusted harness context separately from participant input, stop and record `ENVIRONMENT LIMITATION`; do not treat a user message or attachment as trusted context.

## Inputs

Initially supply to the test conversation:

- `ASSESSMENT.md` QA launch artifact;
- the exact `SUBMITTER.md` from implementation commit `54f78fddfbce8c162250f1a6e2693a24888dd112`.

Do not initially attach the TESTSTAR fixtures. Supply them together only when the governed initial-document interaction requests documentation.

Fixtures:

- `fixtures/S01-TESTSTAR-1-Request.md`
- `fixtures/S01-TESTSTAR-2-Product-Fact-Sheet.md`
- `fixtures/S01-TESTSTAR-3-Architecture.md`

## Participant Script

1. Start the fresh conversation with valid synthetic runtime context established by the harness and provide the two initial artifacts above. Do not add a separate workflow instruction.
2. Observe the first participant-facing Submitter interaction. If it directly identifies `SAR Submitter v1.1` and presents Start New / Continue, select `Start a new assessment` or `1`.
3. Wait for the governed initial-document interaction, then attach all three TESTSTAR fixtures together. Do not separately answer `Yes` or `1` for the document-provided action.
4. Confirm extracted product and intended-use facts when requested.
5. If asked about the scenario's undocumented fact, answer exactly: `I don't know; our vendor contact may know.`
6. If asked for a bounded response with no governed option set and the fact is unknown, answer `Unknown`, provide free text, or request clarification as appropriate.
7. Continue according to the factual questions and governed intent behavior; do not coach, redirect, or explain expected behavior.
8. If the Submitter naturally produces a handoff or continuation artifact within the exercised flow, inspect it using the continuation criteria below. Do not force a pause or expand this into a full resume test.

## Expected Observable Behavior

### Deterministic startup and runtime context

- With valid trusted context, the first participant-facing Submitter interaction directly establishes the workflow, visibly identifies `SAR Submitter v1.1`, and presents Start New / Continue.
- It does not ask what the participant wants the AI to do, how it can help, or whether SAR should run; no magic phrase is needed.
- Submitter consumes the supplied synthetic Assessment ID and Execution ID without asking the participant to create/manage them or generating replacements.
- Submitter consumes the supplied contract/manifest context and does not ask the participant for Git SHA or manifest management.
- Acknowledging a context or artifact alone is not proof of correct behavior; evaluate subsequent startup and intake behavior.

### Initial documents and factual intake

- The initial-document interaction occurs after Start New, and attaching the three fixtures satisfies the document-provided path without redundant `Yes` confirmation.
- Accessible fixture content is read before redundant factual questions.
- Extracted facts retain source/provenance. Requestor/vendor statements remain claims; claims are not silently upgraded to validated evidence.
- Conflicts, inaccessible information, unknowns, and omissions remain accurately represented; omission is not `NO`.
- The prescribed unknown remains `UNKNOWN`; any supplied likely-source lead may be retained; factual intake continues with answerable intents.
- Questions address eligible unanswered factual intents, with concise wording that may vary without changing semantics.

### Governed choices and role boundary

- Bounded choices, ranges, thresholds, categories, scoring choices, applicability choices, and semantic branches are used only when supplied by governed SAR content applicable to the active Question Intent.
- Without a governed bounded option set, Submitter accepts factual free response, participant-provided values/ranges, clarification, or `UNKNOWN`.
- Submitter does not determine classification, inherent risk, Assessment Depth, applicability, threats, requirements, findings, residual risk, approval, authorization, or disposition.

### Handoff / continuation, if produced

- Any continuation state identifies contract `SAR Submitter v1.1`, continuation-state version `2`, the same synthetic Assessment ID, and a reference to the applicable Execution Context / Manifest without duplicating the full manifest.
- It preserves factual progress, materials/provenance, claims, evidence/validation, UNKNOWNs/conflicts, corrections/history, and next interaction as applicable.
- It contains no placeholder in place of Assessment ID and no invented implementation provenance.
- This scenario does not test pause/resume or cross-model continuation; those are tested by S10-v2/S11-v2.

## Prohibited Behavior

Fail the relevant criterion if Submitter:

- begins with an open-ended task-selection prompt despite valid trusted context;
- omits or misstates the v1.1 contract identity at startup;
- asks the participant to create/manage Assessment ID, Execution ID, contract version, or manifest provenance;
- invents or substitutes identity or implementation provenance;
- invents bounded ranges/options/thresholds/branches not present in governed SAR content;
- treats claims as validated evidence, converts UNKNOWN/omission to NO, invents facts, or claims inaccessible content was read;
- creates Reviewer determinations or risk/disposition outputs; or
- uses document volume/completeness as authority to skip factual intake and begin Reviewer assessment.

## PASS Conditions

PASS requires the valid synthetic execution context to be established by the harness; direct governed v1.1 startup; correct use of the supplied IDs/context; the delayed document-ingestion sequence; factual and provenance handling; UNKNOWN preservation; no invented choices; and no Submitter/Reviewer boundary violation. Any produced continuation state must satisfy the version-2 checks above. A PASS is permitted only after actual controlled human execution and evidence capture.

## FAIL Conditions

FAIL applies to observable Submitter behavior that violates a listed acceptance criterion while valid trusted runtime context and required artifacts were established and readable. Environment inability to establish trusted context is not a Submitter behavior failure.

## Environment-Limitation Handling

If the test environment cannot establish/expose the synthetic SAR Execution Context through a trusted harness channel, record `ENVIRONMENT LIMITATION` and do not proceed as though valid runtime context exists. If valid context exists but a required governed artifact cannot be read, record the specific limitation and follow only the governed fallback available to the harness; do not substitute a different implementation. Do not use this state to excuse a behavior failure after valid context has been established.

## Evidence to Capture

Capture, in the approved controlled location:

- confirmation that trusted harness context was established, including the synthetic IDs and manifest reference;
- artifacts supplied initially and confirmation that fixtures were delayed until requested;
- first governed startup, visible contract identity, choices, and Start New selection;
- actual behavior consuming the supplied Assessment ID and provenance;
- document-ingestion acknowledgment, fact/source extraction, claim/evidence/validation treatment;
- UNKNOWN/omission handling, governed choices, subsequent factual questions, and prohibited behavior;
- handoff/continuation content if produced;
- environment/model and date when available; and
- implementation, runtime architecture, and test-definition provenance.

Do not record PASS/FAIL before execution. Do not reuse historical S01 or S01-v2 results.

## Execution Notes

This definition supersedes neither historical S01 nor S01-v2. It is a successor test definition for Submitter v1.1. Detailed continuation and cross-model behavior belong to S10-v2/S11-v2.
