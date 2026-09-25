# S01 — Well-Documented Software Request

## Purpose

Test that the AI reads supplied material first, extracts known facts, preserves vendor claims, and asks only remaining factual questions.

## Acceptance Domains

A, B, D, E, H, S

## Preconditions

Use a fresh conversation and provide the committed `SUBMITTER.md` URL. Do not send a special assessment prompt.

## Inputs

- `fixtures/S01-TESTSTAR-1-Request.md`
- `fixtures/S01-TESTSTAR-2-Product-Fact-Sheet.md`
- `fixtures/S01-TESTSTAR-3-Architecture.md`

## Participant Script

1. Attach all three TESTSTAR fixtures immediately when the startup question is presented; do not separately type `Yes` or `1`.
2. Confirm extracted product and intended-use facts.
3. If asked about an undocumented fact, answer: `I don't know; our vendor contact may know.`

## Expected Observable Behavior

- Reads the supplied material before substantive questioning.
- Treats attaching the fixtures as an affirmative startup response without requiring a special prompt or separate `Yes` answer.
- Extracts known product, SaaS, data, and vendor-administration facts.
- Attributes encryption and other assertions to the vendor.
- Does not ask the participant to repeat adequately documented facts.
- Asks only remaining factual questions.
- Preserves provenance and unresolved items.

## Prohibited Behavior

Do not skip the startup contract, require a special assessment prompt, ask whether HIPAA applies, request a NIST baseline, assign risk, or treat vendor claims as verified.

## PASS Conditions

The first new-assessment question is the initial-document question; attached fixtures satisfy the affirmative path; known facts are summarized with sources; claims and evidence remain distinct; the interview continues with a relevant unresolved factual question; and no Reviewer determination is made.

## FAIL Conditions

The AI ignores supplied material, repeats documented questions, invents facts, or produces a Reviewer conclusion.

## Environment-Limitation Handling

If an attachment cannot be read, the AI identifies it and requests a readable copy or only the necessary facts.

## Evidence to Capture

First substantive AI response, extracted-fact summary, source attribution, questions asked, and generated state if available.

## Execution Notes

Record wording differences as non-blocking unless they change state or authority behavior.
