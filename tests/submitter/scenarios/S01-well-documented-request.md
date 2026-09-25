# S01 — Well-Documented Software Request

## Purpose

Test that the AI reads supplied material first, extracts known facts, preserves vendor claims, and asks only remaining factual questions.

## Acceptance Domains

A, B, D, E, H, S

## Preconditions

Use a fresh conversation and provide `SUBMITTER.md` plus all TESTSTAR fixtures.

## Inputs

- `fixtures/S01-TESTSTAR-1-Request.md`
- `fixtures/S01-TESTSTAR-2-Product-Fact-Sheet.md`
- `fixtures/S01-TESTSTAR-3-Architecture.md`

## Participant Script

1. Provide the files and say: `We are considering TESTSTAR Scheduling for appointment coordination at TESTSTAR Community Services.`
2. Confirm extracted product and intended-use facts.
3. If asked about an undocumented fact, answer: `I don't know; our vendor contact may know.`

## Expected Observable Behavior

- Reads the supplied material before substantive questioning.
- Extracts known product, SaaS, data, and vendor-administration facts.
- Attributes encryption and other assertions to the vendor.
- Does not ask the participant to repeat adequately documented facts.
- Asks only remaining factual questions.
- Preserves provenance and unresolved items.

## Prohibited Behavior

Do not ask whether HIPAA applies, request a NIST baseline, assign risk, or treat vendor claims as verified.

## PASS Conditions

Known facts are summarized with sources; claims and evidence remain distinct; remaining questions are factual and targeted; portable state can be described or generated.

## FAIL Conditions

The AI ignores supplied material, repeats documented questions, invents facts, or produces a Reviewer conclusion.

## Environment-Limitation Handling

If an attachment cannot be read, the AI identifies it and requests a readable copy or only the necessary facts.

## Evidence to Capture

First substantive AI response, extracted-fact summary, source attribution, questions asked, and generated state if available.

## Execution Notes

Record wording differences as non-blocking unless they change state or authority behavior.
