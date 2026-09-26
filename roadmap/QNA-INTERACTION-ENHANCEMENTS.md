# QnA Interaction Enhancements

## Status

**DESIGN CANDIDATES / NOT YET GOVERNED**

This document captures interaction, continuation, portability, and output-design candidates identified through SAR Submitter acceptance testing and related design discussion. Inclusion here does not mean a behavior is approved, implemented, or an acceptance requirement.

Each candidate requires later review, design, governance, and testing before it may affect SUBMITTER.md, acceptance tests, or another operational artifact. SAR is currently a proving ground for some of these ideas. Reusable interaction patterns may later be evaluated for promotion into a COG-governed QnA standard.

This document does not change current SAR behavior.

## A. SAR and Reusable Q&A Governance

SAR contains domain-specific software-assessment behavior, including facts, provenance, evidence, HIPAA discovery, risk boundaries, Reviewer boundaries, and Submitter handoff.

COG is intended to provide reusable and global governance patterns. Lessons learned through SAR may expose interaction standards that should not permanently belong only to SAR.

A future subordinate COG QnA standard should be evaluated. It could support:

- compliance assessments;
- process-driven questionnaires;
- surveys;
- practitioner interviews;
- intake workflows; and
- other conversational Q&A tools.

A reusable QnA standard must not automatically import SAR-specific HIPAA, security-risk, evidence, Reviewer, or software-assessment semantics. Application-specific governance would remain separate.

## B. Entry and Startup Model

Candidate opening interaction for every Submitter session, including resumed work:

> Are you starting a new assessment or continuing a previously started assessment?
>
> 1. Start a new assessment
> 2. Continue a previous assessment

`Start a new assessment` remains option 1. `Continue a previous assessment` remains option 2.

SUBMITTER.md remains the governed entry point. A saved assessment artifact does not replace SUBMITTER.md.

This candidate is distinct from the currently implemented initial-document question. The relationship between the two startup interactions requires later design.

## C. Continuing an Existing Assessment

If the participant selects continuation, candidate interaction:

> Do you have a previously saved assessment file?
>
> 1. Yes — upload the file
> 2. No — start a new assessment instead

The selectable responses describe the participant's choice or action. Avoid first-person scripted answer text such as `I'll upload it.` The tool asks the question; selectable responses describe choices or actions.

If a saved assessment is supplied, the tool should eventually:

- recognize it as continuation state;
- preserve the existing assessment identity internally;
- avoid requiring the participant to understand or manage the GUID;
- restore established facts, provenance, prior answers, unresolved information, and interview position as supported by the artifact;
- avoid unnecessarily re-asking answered questions;
- ask about new or additional documentation before continuing where appropriate; and
- resume at the next relevant unresolved point.

These are candidates only. They are not implemented by this document.

## D. New Assessment and Document Ingestion

Candidate interaction for a new assessment:

> Do you have any documents for SAR to review before beginning?
>
> 1. Yes — upload the documents
> 2. No — continue without documents

For resumed work, the equivalent interaction should distinguish new or additional documents from materials already represented in the saved assessment.

Participant attachment behavior may satisfy an upload/Yes path without requiring a redundant textual answer.

This candidate is related to the current Submitter startup and ingestion contract, but it does not amend that contract.

## E. Hide Internal Assessment Mechanics

Participants should not need to understand:

- GUID;
- UUID;
- UUID-v4 syntax;
- internal artifact naming;
- assessment/session identifiers; or
- state-management mechanics.

Candidate behavior:

- a new assessment receives an internal unique assessment identifier automatically;
- resumed assessments preserve their existing identity; and
- internal identifiers remain available for traceability and artifact management without becoming participant-facing questionnaire concepts.

The exact governed identifier implementation remains unresolved here.

## F. Language and Participant Experience

Candidate UX findings:

- use understandable participant-facing language;
- avoid unnecessary acronyms;
- do not tell participants that they may "answer in plain language";
- communicate clearly without implying that participants normally communicate poorly; and
- expose technical or internal terminology only when needed for the participant's task.

`Use plain language` is a design instruction to the Q&A tool, not necessarily text to display to the participant.

## G. Question and Answer Construction

Candidate interaction principles:

- prefer one question or a small related question set at a time;
- use structured choices where the answer domain is reasonably bounded;
- use a/b/c/d or numbered choices where they reduce cognitive load;
- preserve `Other`, `Unknown / I don't know`, and `Clarify / explain` paths where relevant;
- never silently derive a negative answer from an omitted selection; and
- distinguish information/reporting from the next requested action.

An emerging presentation pattern is:

```text
What has been understood / learned
Next question / requested action
```

These are conceptual labels, not mandated headings. Avoid large responses that mix summaries, caveats, instructions, multiple questions, and technical details into one overwhelming participant response.

## H. Conversational Pacing

Longer interviews may become cognitively burdensome or may be interrupted by normal work priorities. Future design should evaluate:

- manageable question size;
- progressive disclosure;
- meaningful checkpoints;
- opportunities to correct or clarify;
- an unobtrusive ability to pause; and
- avoidance of unnecessary `Are you ready to continue?` prompts after every question.

No mandatory cadence is established here.

## I. Pause, Save, and Resume

Participants should eventually be able to express naturally:

- take a break;
- stop for now;
- save this; and
- continue later.

The tool should eventually be capable of producing a portable continuation artifact or checkpoint. The motivation includes interruption, distraction, missing information, and higher-priority work, not only fatigue.

Subject to later governance, saved state should be sufficient for a new AI chat to understand:

- which governed Q&A process applies;
- assessment identity;
- material already reviewed;
- established facts;
- source and provenance where applicable;
- prior answers;
- unresolved information;
- corrections and history where applicable;
- interview progress/state; and
- enough continuation information to determine what should happen next.

A returning participant still starts with SUBMITTER.md. The saved artifact is state, not the application entry point. The new chat loads the governed entry point first and then consumes the saved state.

## J. Cross-Chat and Cross-Model Portability

Continuation should not depend on the original transcript or a specific AI vendor or model.

A participant should eventually be able to:

1. Start a new supported AI chat.
2. Provide or open SUBMITTER.md.
3. Choose Continue.
4. Supply the saved assessment artifact.
5. Resume without reconstructing the prior interview manually.

This should later be evaluated against the existing S10 and S11 concepts. Those scenarios are not modified by this document.

## K. Artifact Purpose and File Format

Artifact purpose is not the same thing as serialization or file format.

Candidate artifact-purpose classes:

1. **Continuation / State Artifact** — sufficient state to resume the Q&A process.
2. **Human Report** — designed for reading, review, management, approval, or normal business distribution.
3. **Machine Exchange** — structured for applications, APIs, validators, automation, or other machine processing.
4. **Data Export** — structured/tabular representation for analytics, spreadsheets, reporting, or downstream processing.
5. **Evidence / Record Copy** — stable representation of information or process state at a point in time.

This is a candidate taxonomy, not a finalized classification.

## L. Output and Export Types

Formats for future QnA or application capability declarations may include:

- Markdown (`.md`);
- Text (`.txt`);
- PDF (`.pdf`);
- Microsoft Word (`.docx`);
- JSON (`.json`);
- XML (`.xml`);
- CSV (`.csv`); and
- Microsoft Excel (`.xlsx`).

Not every implementation must support every format.

Candidate output principles:

- an application declares which formats it supports;
- one or more formats may be preferred for a particular artifact purpose;
- format choice follows intended use;
- normal participants should not need to understand serialization mechanics merely to save or continue; and
- advanced/export workflows may expose explicit supported-format selection.

For SAR, Markdown is currently useful for human readability, AI portability, Git/version control, and continuation state. This document does not make Markdown permanently mandatory for all future COG QnA implementations.

## M. Output Intent and User Experience

Users may express an intent rather than a file extension. Candidate intents include:

- save this so work can continue later;
- create something suitable for management;
- export the collected data;
- preserve a record copy; and
- provide machine-readable output.

A governed QnA implementation may map intent to its preferred supported output representation. Advanced users may still request an explicit supported format.

This is a candidate interaction principle, not implemented behavior.

## N. Traceability to S01 Learning

These candidates were informed in part by observations and design discussion during SAR Submitter acceptance testing, including S01.

The following remain distinct:

- acceptance criterion;
- observed usability issue;
- design enhancement candidate; and
- reusable COG/QnA candidate.

Not every UX observation is an S01 acceptance failure. Final S01 disposition must be performed separately after the active test is complete.

This document records possible improvements without changing S01 or other acceptance scenarios.

Historical staff-test observations are summarized in [S01-STAFF-TEST-OBSERVATIONS-2026-09-25.md](../tests/submitter/S01-STAFF-TEST-OBSERVATIONS-2026-09-25.md). That record is historical evidence, not a current-baseline S01 result.

The current S01 cycle was subsequently documented as `CANCELLED / SUPERSEDED FOR DESIGN REVISION`. The approved revision scope is recorded in [SUBMITTER-INTERACTION-REVISION.md](SUBMITTER-INTERACTION-REVISION.md); this does not promote the remaining candidates or implement them.

## O. Future Governance Questions

The following questions remain unresolved:

- Which interaction rules belong in SAR versus COG?
- Should COG contain a subordinate QnA standard?
- What is the formal conformance relationship between COG, QnA, and applications such as SAR?
- Which QnA rules are mandatory versus recommended?
- What output-purpose taxonomy should be governed?
- Which serialization formats should be core, optional, or application-specific?
- What minimum state is necessary for portable continuation?
- How should schema/version compatibility work across QnA revisions?
- How should resumed assessment behave when SUBMITTER.md has changed since checkpoint creation?
- How should the system distinguish a saved assessment artifact from ordinary supporting documentation?
- What participant-visible language should be standardized versus left to individual applications?
- What accessibility requirements should govern conversational Q&A?
- What should happen when the AI environment cannot create or download a requested artifact type?
- How should integrity and provenance of resumed state be represented and validated?

No question is resolved here unless already governed elsewhere in the repository.

## Implementation Boundary

This document does not implement any candidate behavior. It does not modify SUBMITTER.md, acceptance tests, fixtures, source-authority artifacts, or operational SAR behavior. It does not create a COG artifact or a formal QnA standard.
