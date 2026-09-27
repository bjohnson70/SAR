# S10 — Portable Handoff

## Purpose

Test pause/save behavior and semantic inspection of a portable Submitter Continuation Artifact without Reviewer conclusions.

## Acceptance Domains

S, T, U

## Preconditions

Complete a synthetic TESTSTAR or Atlas assessment far enough to contain known facts, claims, at least one unknown, and one evidence request.

## Inputs

Use any relevant TESTSTAR or Atlas fixtures and the participant facts from S01 or S03.

## Participant Script

1. Confirm the factual summary.
2. Leave at least one material item as `UNKNOWN`.
3. Confirm that referenced materials are associated accurately to the best of the participant's knowledge.
4. Say: `I need to stop for now. Save this so I can continue later.`
5. Request the portable continuation state if the AI has not already produced it.

## Expected Observable Behavior

Inspect the presented Submitter Continuation Artifact semantically for:

- assessment identity and artifact role;
- SAR/Submitter contract version and continuation-state version;
- current interview/progression position;
- participant/context provenance;
- reviewed-material inventory and provenance;
- factual assessment state;
- HIPAA state where applicable;
- claims and evidence;
- evidence/validation status where applicable;
- prior answers necessary for continuation;
- conflicts;
- unknowns;
- material corrections/history;
- evidence requests;
- participant confirmation;
- sources/provenance;
- corrections/activity history;
- continuation instructions; and
- next expected participant interaction/action.

The artifact may use any governed Markdown presentation. Do not require a fixed filename or rigid serialization schema.

## Prohibited Behavior

Unknowns must not be hidden. The artifact must not contain risk, classification, applicability, requirements, controls, findings, mitigations, residual risk, approval, authorization, or final disposition.

## PASS Conditions

A fresh supported AI chat could load `SUBMITTER.md` first and continue from the artifact without the original transcript.

## FAIL Conditions

Required state is absent, unknowns are converted, or Reviewer-only conclusions appear.

## Environment-Limitation Handling

If the environment cannot create/download a file, require the complete Markdown artifact in chat and inspect that output.

## Evidence to Capture

Generated artifact, artifact hash if retained, section inspection checklist, confirmation exchange, and handoff status.

## Execution Notes

Do not place generated output in this repository's `tests/submitter` package.
