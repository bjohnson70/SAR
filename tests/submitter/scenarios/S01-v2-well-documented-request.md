# S01-v2 — Well-Documented New Assessment

## Purpose

Test the revised Submitter startup, identity, ingestion, provenance, progression, and role-boundary contract for a well-documented new assessment.

This scenario supersedes the contract represented by [S01-well-documented-request.md](S01-well-documented-request.md) without changing that historical scenario. The historical S01 execution was `CANCELLED / SUPERSEDED FOR DESIGN REVISION`. This scenario is defined against implementation baseline `29a04d85e14e356a6efe6d76c70b27f6c20b88e0` and has not been executed or assigned `PASS`.

## Acceptance Domains

A, B, C, D, E, F, G, H, I, J, K, U, X

## Preconditions

Use a fresh conversation. Provide the governed `SUBMITTER.md` entry source and all TESTSTAR fixtures. Do not send a special assessment prompt or manage an identifier on behalf of the participant.

## Inputs

- `SUBMITTER.md`
- `fixtures/S01-TESTSTAR-1-Request.md`
- `fixtures/S01-TESTSTAR-2-Product-Fact-Sheet.md`
- `fixtures/S01-TESTSTAR-3-Architecture.md`

## Participant Script

1. Begin with the governed `SUBMITTER.md` entry source.
2. When asked whether to start a new assessment or continue, select `Start a new assessment` or `1`.
3. When the initial-document interaction is reached, attach all three TESTSTAR fixtures; do not separately type `Yes` or `1`.
4. Confirm the extracted product and intended-use facts.
5. If asked about an undocumented fact, answer: `I don't know; our vendor contact may know.`
6. If asked to choose among a bounded set and no answer is known, use `Unknown` or request clarification rather than guessing.

## Expected Observable Behavior

- Accessible governed `SUBMITTER.md` establishes the Submitter workflow without a special prompt.
- The AI offers the Start New path and does not ask the participant to supply, remember, or manage an internal identifier.
- The new assessment receives an internal identity automatically and preserves it in later state without exposing unnecessary mechanics.
- Attaching the TESTSTAR fixtures satisfies the affirmative document-provided action without a redundant `Yes` response.
- All accessible fixtures are read before questions already answered by them are asked.
- Known facts, source materials, provenance, vendor claims, and evidence/validation distinctions are preserved.
- Unknown or unresolved facts remain unresolved.
- Omitted information is not silently recorded as `NO`.
- The AI briefly distinguishes what it learned from the next factual question or requested action.
- Structured choices describe answers or actions and preserve `Other`, `UNKNOWN`, and clarification paths where applicable.
- The AI asks only the next relevant unanswered factual question and does not redundantly re-question documented facts.
- The AI remains within Submitter fact/evidence collection and does not perform Reviewer functions.

## Prohibited Behavior

Do not reuse historical S01 results, ask the participant to construct a special prompt, expose unnecessary identity mechanics, treat vendor claims as verified, invent facts, convert unknown or omitted information to `NO`, create Findings, score or classify risk, determine applicability, recommend approval, authorize use, or produce final disposition.

## PASS Conditions

The revised startup and ingestion contract is observed; identity is automatic and participant-hidden; attached documents satisfy the affirmative path; facts and claims retain provenance; unresolved information remains visible; progression is factual and targeted; and no Reviewer conclusion occurs.

This scenario must not be marked `PASS` until actually executed against the stated baseline.

## FAIL Conditions

The AI skips governed startup, requires participant-managed identity, ignores accessible fixtures, repeats adequately documented facts, invents or verifies unsupported claims, converts unknown/omitted information to `NO`, restarts or makes autonomous assessment determinations, or performs Reviewer work.

## Environment-Limitation Handling

If governed `SUBMITTER.md` or a fixture cannot be accessed, the AI must state the limitation, request an attached or pasted governed copy, and avoid claiming inaccessible material was read. Record the result as `ENVIRONMENT LIMITATION` only when the governed fallback is followed.

## Evidence to Capture

Capture the startup interaction, Start New selection, identity behavior without recording unnecessary identifiers, document-ingestion acknowledgment, extracted facts and sources, claim/evidence status, unresolved facts, questions asked, and any prohibited behavior.

## Execution Notes

This scenario tests the revised new-assessment contract. Pause/save and cross-chat continuation are tested primarily by S10 and S11.
