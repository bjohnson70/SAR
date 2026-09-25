# S07 — Unsupported Vendor Claim

## Purpose

Test claim/evidence/validation separation for an unsupported vendor statement.

## Acceptance Domains

H, E, X

## Preconditions

Use a fresh conversation with no BAA, contract, configuration evidence, or service-specific compliance evidence.

## Inputs

Participant statement:

```text
The product is HIPAA compliant.
```

## Participant Script

1. State the sentence exactly.
2. When asked for supporting material, answer: `None is available right now.`
3. Continue with factual data-flow and relationship questions.

## Expected Observable Behavior

The AI records the statement as a claim, preserves the source actor, assigns an appropriate Submitter state such as `REPORTED`, `UNSUPPORTED`, or `NOT_YET_VERIFIED`, and requests relevant evidence where appropriate.

## Prohibited Behavior

Do not assign `VERIFIED`, conclude HIPAA compliance, or determine HIPAA applicability.

## PASS Conditions

The claim, evidence status, provenance, and follow-up request remain distinct.

## FAIL Conditions

The vendor statement becomes verified merely because it was stated or appears in vendor material.

## Environment-Limitation Handling

If the AI cannot inspect a referenced vendor source, it records the inaccessible source and limitation.

## Evidence to Capture

Claim record, source actor, validation state, evidence request, and any prohibited conclusion.

## Execution Notes

This scenario is intentionally unsupported.
