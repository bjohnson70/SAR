# Submitter Interaction Revision Plan

## Status

**APPROVED IMPLEMENTATION SCOPE / NOT YET IMPLEMENTED**

This document records the approved planning scope following cancellation of the current S01 execution cycle. It does not implement the revision, change SUBMITTER.md, change acceptance scenarios or fixtures, or create a replacement S01.

## Current S01 Execution Status

```text
CANCELLED / SUPERSEDED FOR DESIGN REVISION
```

The active S01 execution was intentionally terminated because SAR's Submitter interaction design and implementation/test contract will be revised before acceptance testing continues.

This execution:

- is not `PASS`;
- is not `FAIL`;
- reached no current S01 acceptance disposition;
- cannot later be treated as testing the replacement implementation or contract; and
- must be followed by a completely fresh S01 execution against the future governed baseline.

The historical staff observations recorded in [S01-STAFF-TEST-OBSERVATIONS-2026-09-25.md](../tests/submitter/S01-STAFF-TEST-OBSERVATIONS-2026-09-25.md) remain historical evidence. They do not constitute a current-baseline S01 result.

## Approved Implementation Scope

### A. Participant-Facing Assessment Identity

Participants should not need to know, supply, construct, or manage GUIDs, UUIDs, internal assessment identifiers, or internal artifact filenames.

A new assessment should receive a unique internal assessment identity automatically. A resumed assessment should preserve that identity. Internal identity and state mechanics should normally remain hidden from participant-facing questions while remaining available for traceability and artifact management.

The exact identity implementation remains governed by the existing SAR identity architecture and any later approved implementation detail.

### B. Participant Language

Remove unnecessary participant-facing instructions telling a participant that they may answer in "plain language."

SAR should ask understandable questions, avoid unnecessary acronyms and technical terminology, and explain necessary terms when relevant. This is a design requirement for the tool's communication, not a requirement to display internal instruction text to participants.

### C. Question and Answer Construction

Where the answer space is bounded, SAR may use numbered or lettered structured choices. Choices should describe the participant's answer or action.

Avoid first-person scripted responses such as:

```text
I'll upload it.
```

Prefer action-oriented choices such as:

```text
Upload the documents.
```

Where appropriate, preserve:

- `Other`;
- `Unknown / I don't know`; and
- `Clarify / explain the question`.

Omission must never silently become `No`. Information/reporting must remain distinguishable from the next requested action.

### D. Document Ingestion

Attaching requested documentation should satisfy the document-provided action without requiring a redundant textual `Yes`.

SAR should inspect all accessible supplied material before asking questions already answered by it, preserve provenance, distinguish claims from validated evidence, preserve unresolved information, and never claim inaccessible material was reviewed.

### E. Capability-Aware Bootstrap

SAR must account for AI environments that cannot dereference the normal governed SAR entry-point URL. The governed URL mechanism is not eliminated solely because historical test environments experienced access limitations.

The invariant is:

> SAR must never claim that inaccessible governance material was read.

A later implementation should provide or evaluate a governed fallback mechanism without generalizing the NH/FP observations to every AI environment or selecting a preferred fallback in this planning document.

### F. Deterministic Conversational Progression

Document ingestion must not cause SAR to jump directly into an autonomous Reviewer-style assessment.

The interaction should distinguish conceptually between:

- what SAR has learned or understood; and
- what information or action is needed next.

Exact participant-facing headings are not mandated here. Submitter must remain within Submitter responsibilities and must not perform Reviewer scoring, approval, classification decisions, findings, or final disposition.

### G. Pause, Save, and Resume

Participants must be able to naturally express intent such as:

- take a break;
- stop for now;
- save this; and
- continue later.

SAR should create a portable continuation artifact containing enough governed state to resume without manually reconstructing the previous transcript. Subject to later design, state should preserve:

- assessment identity;
- process/version information;
- reviewed materials;
- extracted facts;
- provenance;
- participant answers;
- unknown/unresolved information;
- relevant corrections/history; and
- current interview/progression state.

Participants should not need to understand GUIDs or internal state mechanics.

### H. Resume Behavior

SUBMITTER.md remains the governed entry point. The continuation artifact represents assessment state and does not replace SAR governance.

Resume behavior should distinguish:

1. saved continuation state;
2. previously reviewed supporting documentation; and
3. new or additional supporting documentation.

A resumed assessment must preserve its existing identity and prior governed state.

## Governed Architecture Decisions

### A. Internal Assessment Identity

Each new SAR assessment receives an internally generated UUID v4. The identifier represents the assessment or case. It does not represent a participant, chat, AI session, or individual artifact.

Participants are not required to provide, remember, enter, select, or manage the identifier. Participant-facing interaction normally hides the internal identifier.

The assessment identity persists across continuation and related assessment artifacts. Resuming an assessment preserves the existing identity; resume must not generate a new assessment identity.

If UUID v4 generation is unavailable in the execution environment, a documented unique fallback identifier may be generated. A fallback identifier must be recorded as a fallback and must not be falsely represented as UUID v4.

This decision does not define a new identifier format beyond the UUID v4 preference and documented fallback.

### B. Minimum Continuation State

SAR governs a logical minimum-state contract rather than a rigid serialization schema.

Portable continuation state must preserve at least:

- assessment identity;
- SAR/Submitter contract version;
- continuation-state version;
- current interview/progression position;
- reviewed-material inventory;
- provenance for reviewed material;
- established facts;
- participant-reported claims;
- evidence/validation status where applicable;
- prior answers necessary for continuation;
- unresolved or unknown information;
- material corrections/history necessary to interpret current state accurately; and
- next expected participant interaction or action.

The original chat transcript is **NOT** required for continuation. The continuation state must contain enough governed state for a supported fresh AI chat to resume the assessment without reconstructing the prior conversation.

### C. Submitter Continuation Artifact

SAR establishes the governed concept:

```text
Submitter Continuation Artifact
```

Its purpose is **portable assessment-state transfer**.

For the current SAR implementation:

- Markdown is the minimum governed portable format;
- the artifact contains continuation state;
- the artifact remains subordinate to `SUBMITTER.md`;
- it does not replace SAR governance;
- it may be produced when the participant requests to pause, save, stop, continue later, or when a handoff is required;
- it remains associated with the internal assessment identity;
- participants do not need to understand or manage that identifier;
- no exact filename is finalized unless an existing repository convention governs one; and
- PDF, DOCX, JSON, XML, CSV, XLSX, and other formats are not required by this decision.

Artifact purpose remains distinct from file format.

### D. Capability-Aware Bootstrap

The governed bootstrap precedence is:

1. accessible governed `SUBMITTER.md` entry source;
2. attached governed copy of `SUBMITTER.md`; and
3. governed copied or pasted `SUBMITTER.md` content when provenance and version can be established.

If none of these governed sources is accessible:

- do not claim `SUBMITTER.md` was read;
- do not pretend a governed SAR assessment has started; and
- explain what governed material is needed before proceeding.

This decision does not state or imply that external URLs generally fail and is not specific to Copilot, ChatGPT, or another AI vendor.

The governing invariant is:

> SAR must never claim it read governance it could not access.

### E. Resume Entry Contract

The SAR-specific Submitter startup contract distinguishes:

1. starting a new assessment; and
2. continuing a previously started assessment.

For a new assessment, create the internal assessment identity automatically and do not require the participant to supply or manage it.

For continuation:

- request or consume the saved Submitter Continuation Artifact;
- preserve its assessment identity;
- restore prior governed state;
- preserve prior facts, provenance, unknowns, and material history;
- distinguish previously reviewed supporting material from newly supplied supporting material; and
- allow new supporting material to be ingested without restarting the assessment.

`SUBMITTER.md` remains the governed entry point. The Submitter Continuation Artifact supplies assessment state; it does not replace or supersede `SUBMITTER.md`.

This contract does not add vendor-specific resume behavior.

### F. Replacement S01

The existing S01 scenario remains unchanged for historical traceability. The cancelled/superseded S01 must not be retrofitted to the revised contract.

After implementation, a new explicitly versioned or otherwise clearly superseding S01 artifact will test the revised contract. The replacement must trace to:

- the historical S01;
- the cancelled/superseded design-revision cycle; and
- the implementation baseline being tested.

The repository naming conventions must be inspected before selecting the exact successor filename. This documentation step does not create the replacement S01 and does not select its filename.

## Architecture Separation

These artifacts have different responsibilities and must not silently substitute for one another:

- `SUBMITTER.md` = governance and interaction contract;
- `Submitter Continuation Artifact` = portable assessment state;
- supporting documents = assessment inputs/evidence; and
- chat transcript = execution context and is not required as the system of record.

## Deferred Design Candidates

The following remain candidates in [QNA-INTERACTION-ENHANCEMENTS.md](QNA-INTERACTION-ENHANCEMENTS.md) and are not promoted or implemented by this plan:

- a global COG QnA standard;
- a universal output-format taxonomy;
- mandatory PDF, DOCX, JSON, XML, CSV, or XLSX support;
- broad management-report redesign;
- Reviewer workflow redesign;
- a generalized application framework beyond SAR; and
- other remaining QnA candidates not listed in the approved implementation scope.

## Explicitly Out of Scope

This revision plan does not authorize changes to:

- SUBMITTER.md;
- the current S01 scenario;
- S02-S12;
- acceptance fixtures;
- current HIPAA or source-authority artifacts;
- Reviewer behavior;
- current S01 grading or release disposition;
- a COG artifact or formal QnA standard; or
- the historical staff-test evidence record beyond its existing status.

## Replacement S01 Requirements

A future replacement S01 must verify at minimum:

1. Governed startup occurs correctly.
2. The participant does not manage GUID, UUID, or internal identity.
3. Supporting documents are handled naturally.
4. Attaching documents does not require redundant confirmation that documents were supplied.
5. Accessible documents are reviewed before redundant factual questions.
6. Inaccessible governance or source material is disclosed honestly.
7. Claims remain distinguishable from validated evidence.
8. Unresolved facts remain unknown.
9. Submitter remains within Submitter scope.
10. Structured choices work where appropriate.
11. Interview progression is deterministic.
12. The participant can pause and save.
13. Continuation state contains sufficient information to resume.
14. A fresh supported AI conversation can consume that continuation state.
15. A resumed assessment preserves identity and prior facts.
16. Saved state is distinguishable from new supporting material.
17. No prohibited Reviewer conclusions are produced.

The replacement S01 does not exist yet. No current S01 result is inferred from this requirements list.

## S01 Versioning and Supersession Recommendation

The current stable S01 filename should remain unchanged for the historical record. The current scenario is tied to its tested commit through the acceptance README and Git history.

After implementation, create a new explicitly versioned or otherwise clearly superseding S01 scenario only under an approved repository convention. The replacement must preserve a reference to:

- this cancelled execution status;
- the historical S01 evidence record;
- the exact implementation commit tested; and
- the prior S01 contract it supersedes.

Do not rename or replace the current S01 during this planning task. A future implementation task should select the final scenario naming convention before creating the replacement scenario.

## Change-Impact Matrix

| Artifact or area | Expected classification | Expected future change | Reason |
|---|---|---|---|
| `SUBMITTER.md` | Operational behavior | Change expected | Implement startup, identity hiding, ingestion, progression, pause/save/resume, bootstrap fallback, and resume distinctions. |
| `tests/submitter/README.md` | Acceptance test | Change expected | Record `CANCELLED / SUPERSEDED`, replacement-baseline rules, and revised execution guidance. |
| Current S01 scenario | Acceptance test | Supersession expected | Preserve historical traceability; do not mutate the cancelled contract in place. |
| Future replacement S01 scenario | Acceptance test | New artifact expected | Verify the replacement implementation and all replacement requirements. |
| S02 | Acceptance test | Review/change expected | Exercise revised no-document startup and absence-of-documents semantics. |
| S10/S11 | Acceptance test | Review/change expected | Exercise portable continuation state, resume identity, and cross-model continuation. |
| S12 | Acceptance test | Review/change expected | Exercise governed bootstrap and inaccessible-entry-point fallback. |
| Existing fixtures | Fixture | Review/change expected | Add only synthetic material needed for revised startup, continuation, and capability paths. |
| Continuation artifact specification | Continuation/state artifact specification | New or expanded specification expected | Define minimum resumable state, process/version identity, and supporting-material distinctions. |
| `roadmap/QNA-INTERACTION-ENHANCEMENTS.md` | Governance/documentation | Reference or refine later | Preserve deferred candidates and traceability without promoting them here. |
| `roadmap/ROADMAP.md` | Governance/documentation | Status pointer expected | Track cancellation and approved revision planning. |
| Historical S01 evidence | Governance/documentation | No change expected | Preserve the external observations as historical evidence tied to the old baseline. |
| HIPAA/source artifacts | No change expected | No change expected | The revision concerns interaction and state handling, not source authority. |
| `ASSESSMENT.md` | No change expected | No change expected | Historical untracked prototype remains outside this work. |

## Implementation Boundary

This document defines the approved planning scope only. It does not implement any change, restart S01, assign a current S01 result, or authorize staging, commitment, or publication of operational changes.
