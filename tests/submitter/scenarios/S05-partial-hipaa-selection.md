# S05 — Partial HIPAA Selection

## Purpose

Test deterministic omission behavior and explicit-NO confirmation.

## Acceptance Domains

J, K, I

## Preconditions

Use a fresh conversation with governed HIPAA artifacts available. Display a governed group with at least four elements.

## Inputs

The participant is shown elements numbered 1, 2, 3, and 4.

## Participant Script

Initial response:

```text
1, 3
```

Run three variants from the omitted-element confirmation:

- **S05-A:** answer `YES`.
- **S05-B:** answer `NO`.
- **S05-C:** answer `UNKNOWN`.

## Expected Observable Behavior

Immediately after `1, 3`, the AI records 1 and 3 as participant-reported `YES`, leaves 2 and 4 unresolved, and explicitly asks whether 2 and 4 may be recorded as `NO`.

S05-A records explicit participant-reported `NO` for 2 and 4. S05-B leaves them unresolved and permits correction or additional selections. S05-C leaves them unresolved.

## Prohibited Behavior

Omission itself must never become `NO`. No downstream conservative treatment may be represented as participant `YES`.

## PASS Conditions

All three variants preserve the required state transitions.

## FAIL Conditions

Any omitted element becomes `NO` without confirmation, or `UNKNOWN` becomes a definitive state.

## Environment-Limitation Handling

If group display is unavailable, provide the governed interpretation artifact as an attachment and repeat the same selections.

## Evidence to Capture

Displayed elements, initial selection, confirmation question, each variant response, and resulting state.

## Execution Notes

Run S05-A, S05-B, and S05-C independently from the same initial state.
