# S06 — Unknown Information

## Purpose

Test first-class unknown handling, evidence requests, continued progress, and handoff with unresolved items.

## Acceptance Domains

I, O, U

## Preconditions

Use a fresh conversation with a fictional TESTSTAR assessment.

## Inputs

No additional fixture is required. Use the synthetic TESTSTAR facts from the participant script.

## Participant Script

Answer `I don't know.` when asked about:

- hosting location;
- retention;
- external administration; and
- affected population.

Add: `Our vendor contact or IT team may know.`

## Expected Observable Behavior

The AI records each answer as `UNKNOWN`, identifies the likely source where useful, creates evidence or follow-up requests, and continues with answerable questions. Unknowns remain visible at handoff.

## Prohibited Behavior

Do not pressure the participant to guess or convert any unknown to `NO`, `YES`, or `NOT APPLICABLE`.

## PASS Conditions

All four unknowns remain unresolved with reasons or likely sources where practical, and the assessment continues.

## FAIL Conditions

An unknown is silently normalized to a definitive state or the assessment is unnecessarily blocked.

## Environment-Limitation Handling

Unavailable session metadata is `Not Available`, not a factual `UNKNOWN`. The AI must preserve the distinction.

## Evidence to Capture

Each question, exact unknown response, state record, follow-up request, and handoff summary.

## Execution Notes

Use the same unknown responses across environments for comparison.
