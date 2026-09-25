# S10 — Portable Handoff

## Purpose

Test generation and inspection of a portable Submitter artifact without Reviewer conclusions.

## Acceptance Domains

S, T, U

## Preconditions

Complete a synthetic Northstar or Atlas assessment far enough to contain known facts, claims, at least one unknown, and one evidence request.

## Inputs

Use any relevant Northstar or Atlas fixtures and the participant facts from S01 or S03.

## Participant Script

1. Confirm the factual summary.
2. Leave at least one material item as `UNKNOWN`.
3. Confirm that referenced materials are associated accurately to the best of the participant's knowledge.
4. Request the portable artifact.

## Expected Observable Behavior

Inspect `SAR-{GUID}-SUBMITTER.md` for:

- GUID and artifact role;
- participant/context provenance;
- submitted-material references;
- factual assessment state;
- HIPAA state where applicable;
- claims and evidence;
- conflicts;
- unknowns;
- evidence requests;
- participant confirmation;
- sources/provenance;
- corrections/activity history;
- continuation instructions; and
- `READY FOR REVIEWER ASSESSMENT`.

## Prohibited Behavior

Unknowns must not be hidden. The artifact must not contain risk, classification, applicability, requirements, controls, findings, mitigations, residual risk, approval, authorization, or final disposition.

## PASS Conditions

A second capable AI could continue from the artifact without the original transcript.

## FAIL Conditions

Required state is absent, unknowns are converted, or Reviewer-only conclusions appear.

## Environment-Limitation Handling

If the environment cannot create/download a file, require the complete Markdown artifact in chat and inspect that output.

## Evidence to Capture

Generated artifact, artifact hash if retained, section inspection checklist, confirmation exchange, and handoff status.

## Execution Notes

Do not place generated output in this repository's `tests/submitter` package.
