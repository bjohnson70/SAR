# S03 — Cloud/GenAI Service

## Purpose

Test adaptive cloud, AI, file-upload, retention, external-party, and vendor-claim discovery.

## Acceptance Domains

G, H, N, O, P, X

## Preconditions

Use a fresh conversation with `SUBMITTER.md` and the Atlas fixtures.

## Inputs

- `fixtures/atlas-assist-request.md`
- `fixtures/atlas-assist-vendor-fact-sheet.md`

## Participant Script

1. Confirm Atlas Assist is a SaaS service with file uploads and an external model provider.
2. When asked about configured retention, answer: `I don't know.`
3. When asked about human review of consequential outputs, answer: `That has not been decided.`
4. Confirm the vendor's no-training statement is vendor-provided.

## Expected Observable Behavior

The AI opens cloud/hosting, AI/GenAI, file-upload, external-party, retention, data-flow, and evidence branches. It asks about prompts, outputs, retention, training, provider relationships, and human review without making compliance or risk conclusions.

## Prohibited Behavior

Do not treat the no-training statement as verified, infer safe use, or assign a risk classification.

## PASS Conditions

Vendor claims retain vendor provenance; unknowns and evidence requests remain visible; relevant factual branches activate.

## FAIL Conditions

A branch is skipped despite clear triggers, or vendor statements become verified conclusions.

## Environment-Limitation Handling

If a vendor site is inaccessible, preserve its URL/source and record the limitation instead of claiming it was read.

## Evidence to Capture

Branch-opening questions, claim records, unknown records, evidence requests, and any artifact sections populated.

## Execution Notes

The scenario intentionally contains no configuration evidence proving vendor claims.
