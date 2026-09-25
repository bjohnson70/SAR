# S09 — Correction

## Purpose

Test correction history, current-state replacement, provenance preservation, and retention branching.

## Acceptance Domains

Q, D, G, S

## Preconditions

Use a fresh conversation with a fictional Northstar assessment.

## Inputs

No additional fixture is required.

## Participant Script

Initial statement:

```text
The service stores no data.
```

Later correction:

```text
Correction: the service stores uploaded files for 30 days.
```

## Expected Observable Behavior

The current state reflects that uploaded files are stored for 30 days. The prior statement remains traceable with its original source and date/session when available. A correction record exists, and storage/retention discovery opens.

## Prohibited Behavior

Do not silently overwrite the initial statement or erase its provenance.

## PASS Conditions

Current value, prior value, correction linkage, source actor, and related follow-up are visible.

## FAIL Conditions

Only the corrected value exists with no trace of the original, or retention discovery does not open.

## Environment-Limitation Handling

If dates or session identifiers are unavailable, record `Not Available` rather than inventing them.

## Evidence to Capture

Initial answer, correction, current state, history record, and follow-up questions.

## Execution Notes

The correction text must be used exactly for repeatability.
