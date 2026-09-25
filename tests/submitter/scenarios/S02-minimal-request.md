# S02 — Minimal Request

## Purpose

Test natural minimum-context discovery without a giant questionnaire.

## Acceptance Domains

A, C, E, F, G

## Preconditions

Use a fresh conversation with only `SUBMITTER.md` and no additional source material.

## Inputs

Participant statement: `We are considering Northstar Scheduling for appointment coordination.`

## Participant Script

1. Provide the statement.
2. Answer the next factual question in ordinary language.
3. When asked about an unknown fact, answer: `I don't know.`

## Expected Observable Behavior

The AI creates or explains assessment identity, establishes participant and organization context, identifies the product and intended use, and asks one useful question or small related group at a time.

## Prohibited Behavior

Do not dump the complete assessment, request security terminology, or ask for risk or compliance classifications.

## PASS Conditions

The interaction begins naturally, adapts to answers, and opens only relevant discovery branches.

## FAIL Conditions

The AI presents a giant static questionnaire, asks for hidden classifications, or treats missing facts as `NO`.

## Environment-Limitation Handling

If UUID generation is unavailable, the AI records its fallback identity limitation and preserves the selected identifier.

## Evidence to Capture

Opening response, first three question/answer exchanges, identity behavior, and branch triggers.

## Execution Notes

This scenario tests usability and sequencing, not completion of every assessment domain.
