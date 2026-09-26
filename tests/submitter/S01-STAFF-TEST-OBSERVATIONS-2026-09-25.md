# S01 Staff-Test Observations — 2026-09-25

## Historical Status

**HISTORICAL TEST EVIDENCE**

**NOT A CURRENT-BASELINE S01 RESULT**

This document summarizes three external DDS staff-test evidence packages reviewed for SAR. The tests were conducted against the historical controlled baseline `d979db8b09063ecb06e8b968e024362ab80dae11`, not the current repository baseline.

The current repository baseline when this record was created is `4aee0c1c0a6d96ab2d9d695a90e26a12bc6be98a`. The historical observations must not be silently reinterpreted as testing that current baseline.

- Test date: 2026-09-25
- Scenario: S01 — Well-Documented Software Request
- Synthetic test identity: TESTSTAR
- Testers: IM, NH, FP

This is a governed summary of external evidence. Source PDFs, email chains, screenshots, raw transcripts, and staff contact information remain outside the public repository.

## Interpretation Boundary

This record documents observations, environment limitations, and design implications. It does not declare the current S01 test `PASS` or `FAIL`, change current acceptance criteria, or identify a proven root cause for any observed behavior.

The historical procedure included a new chat, three TESTSTAR fixture attachments, an Initial Information Block, confirmation of known product/intended-use facts, preservation of unknowns, and continuation toward Submitter handoff. It also anticipated recording environment limitations involving URL access, attachments, session/browser metadata, and Markdown creation/download.

## Tester IM

### Observed Tester Report

- Tester reported reaching step 6.
- Tester reported: "But I am not being asked to 'confirm' anything."

### Observed AI Behavior

- The AI stated that it had pulled in all three uploaded documents.
- The AI stated that it would conduct a SAR-style software assessment.
- It proceeded into a structured presentation titled approximately `SAR Assessment: TESTSTAR Scheduling`.

### Design Implication

The expected extracted-facts confirmation interaction described by the historical S01 procedure was not observed by the tester. This is documented as a historical S01 behavioral finding and a possible interview-state or confirmation-flow design issue.

### Interpretation Limitation

This observation does not independently establish that current S01 fails. No root cause is concluded from this evidence.

## Tester NH

### Observed Environment Behavior

- Copilot reported that it could not open external URLs, including GitHub raw links.
- SUBMITTER.md was therefore inaccessible through the supplied URL.
- Copilot explicitly stated that it should not pretend to have accessed instructions it could not retrieve.
- Copilot requested that SUBMITTER.md be supplied as an attachment.
- The tester asked whether the SAR Submitter instructions could be supplied as a file rather than referenced through the URL.

### Classification

This is an environment limitation and deployment/bootstrap design finding for the observed run.

### Positive Boundary Behavior

The AI disclosed that the source was inaccessible, did not claim to have read inaccessible instructions, and requested a usable copy rather than fabricating the source.

## Tester FP

### Observed Environment Behavior

- Tester reported becoming stuck at step 5.
- The AI stated that it could not view SAR SUBMITTER.md.
- It requested that the SAR Submitter template/instructions be pasted into the chat.
- It indicated that it could use the three supplied TESTSTAR files after receiving the missing Submitter instructions.

### Classification

This is an environment limitation and deployment/bootstrap design finding for the observed run.

### Positive Boundary Behavior

The AI did not claim to have accessed SUBMITTER.md and requested the missing governed information rather than inventing it.

## Cross-Test Observations

### URL and Bootstrap Portability

Two independent staff tests, NH and FP, encountered substantially the same inability to rely on the supplied GitHub raw SUBMITTER.md URL in their tested Copilot environments.

This record does not generalize that all Microsoft Copilot environments cannot access GitHub, that DDS Copilot will always behave this way, or that GitHub URLs are universally unusable. The evidence supports only the observed environments and runs.

The resulting design concern is that a public GitHub URL by itself may not be a sufficient bootstrap or distribution mechanism for every intended SAR AI environment. Future SAR/QnA design should evaluate, without selecting or implementing a preferred mechanism here:

- governed URL access;
- an attached SUBMITTER.md; and
- governed copied content or another governed distribution mechanism.

### Capability Disclosure

NH and FP provide positive evidence that the tested AI sessions disclosed source inaccessibility rather than pretending the governance material had been read. They requested an accessible representation.

### Interview-State Determinism

IM's experience provides evidence that supplying the materials and instructions did not always produce the expected confirmation/interview progression in the historical run. This remains a design concern. The evidence does not establish a root cause.

## Relationship to QnA Design Candidates

The observations may inform the design candidates in [QNA-INTERACTION-ENHANCEMENTS.md](../../roadmap/QNA-INTERACTION-ENHANCEMENTS.md), particularly:

- governed entry-point fallback and alternate distribution;
- capability-aware bootstrap behavior;
- deterministic conversational state progression;
- distinguishing source accessibility from source content; and
- never claiming inaccessible governance material was read.

The roadmap remains a design-candidate document. This historical record does not promote any candidate to an approved or implemented requirement.

## Current-Test Boundary

The historical observations do not alter:

- SUBMITTER.md;
- S01 or any other acceptance scenario;
- acceptance fixtures;
- current S01 grading;
- the current release gate; or
- operational SAR behavior.

Final S01 disposition for the active test must be performed separately after testing the intended current baseline.
