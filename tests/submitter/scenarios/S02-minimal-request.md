# S02 — Minimal Request

## Purpose

Test Start New selection and direct no-document factual discovery without a giant questionnaire.

## Acceptance Domains

A, C, E, F, G

## Preconditions

Use a fresh conversation with only `SUBMITTER.md` and no additional source material.

## Inputs

Participant statement: `We are considering TESTSTAR Scheduling for appointment coordination.`

## Participant Script

1. When Start/Continue is presented, answer `Start a new assessment` or `1`.
2. When the initial-document question is presented, answer `No` or `2`.
3. Answer the next factual question in ordinary language.
4. When asked about an unknown fact, answer: `I don't know.`

## Expected Observable Behavior

The AI establishes the Submitter workflow without a special prompt, offers Start New, creates identity automatically without participant management, asks the initial-document question, accepts `No` or `2`, moves directly into factual discovery, and does not treat absent documentation as a negative fact.

## Prohibited Behavior

Do not ask for documents again after `No`, dump the complete assessment, request security terminology, or ask for risk or compliance classifications.

## PASS Conditions

The interaction begins naturally, the no-document path moves directly into fact discovery without creating negative findings, adapts to answers, and opens only relevant discovery branches.

## FAIL Conditions

The AI presents a giant static questionnaire, asks for hidden classifications, or treats missing facts as `NO`.

## Environment-Limitation Handling

If UUID generation is unavailable, the AI records its fallback identity limitation and preserves the selected identifier.

## Evidence to Capture

Opening response, first three question/answer exchanges, identity behavior, and branch triggers.

## Execution Notes

This scenario tests usability and sequencing, not completion of every assessment domain.
