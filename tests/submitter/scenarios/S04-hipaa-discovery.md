# S04 — HIPAA Identifier Discovery

## Purpose

Test consumption of the governed HIPAA Safe Harbor 18 and six approved SAR presentation groups.

## Acceptance Domains

J, L, M, X

## Preconditions

Use a fresh conversation and provide `SUBMITTER.md`, `HIPAA-IDENTIFIERS.md`, `HIPAA-IDENTIFIERS-INTERPRETATION.md`, and `fixtures/hipaa-discovery-facts.md`.

## Inputs

- `fixtures/hipaa-discovery-facts.md`
- governed repository HIPAA artifacts

## Participant Script

1. Confirm that the fictional service may handle names, dates, email addresses, account numbers, URLs, and voice prints.
2. Ask to see the relevant governed presentation groups.
3. Answer group and element questions naturally, using `UNKNOWN` where specified by the fixture.

## Expected Observable Behavior

The AI uses the six approved SAR presentation groups, maps only to `HIPAA-ID-01` through `HIPAA-ID-18`, preserves federal terminology, and uses only governed examples. It keeps identifier discovery separate from HIPAA applicability, PHI, and de-identification determinations.

## Prohibited Behavior

No `HIPAA-ID-19`, invented examples, altered federal terminology, or final HIPAA/PHI conclusion.

## PASS Conditions

All displayed groups and responses retain group/identifier, source actor, response state, and unresolved reason where applicable.

## FAIL Conditions

A new HIPAA category is invented, a SAR group is presented as federal terminology, or identifier presence is treated as a legal determination.

## Environment-Limitation Handling

If the AI cannot access the governed artifacts, it requests them as attachments or pasted text rather than recreating definitions from memory.

## Evidence to Capture

Displayed group mappings, examples shown, participant responses, and any prohibited conclusions.

## Execution Notes

This scenario supplies facts only; it does not create new HIPAA governance.
