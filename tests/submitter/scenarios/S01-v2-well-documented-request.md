# S01-v2 — Well-Documented New Assessment

## Purpose

Test the revised Submitter startup, identity, ingestion, provenance, progression, and role-boundary contract for a well-documented new assessment.

This scenario supersedes the contract represented by [S01-well-documented-request.md](S01-well-documented-request.md) without changing that historical scenario. The historical S01 execution was `CANCELLED / SUPERSEDED FOR DESIGN REVISION`. This revision supersedes the prior S01-v2 implementation pin `29a04d85e14e356a6efe6d76c70b27f6c20b88e0` and tests `SAR Submitter v1.0` at implementation baseline `22eb88f7eb78a1c07bd68eec1424e1341d0eae73`. It has not been executed or assigned `PASS`.

## Acceptance Domains

A, B, C, D, E, F, G, H, I, J, K, U, X

## Preconditions

Use a completely fresh conversation. Provide both the root `ASSESSMENT.md` QA launch artifact and the exact pinned `SUBMITTER.md` corresponding to implementation SHA `22eb88f7eb78a1c07bd68eec1424e1341d0eae73`. The immutable [`SUBMITTER.md` URL](https://github.com/bjohnson70/SAR/blob/22eb88f7eb78a1c07bd68eec1424e1341d0eae73/SUBMITTER.md) is provenance and an optional direct-access mechanism, not a prerequisite for this controlled test. Do not substitute a current moving `main` copy. Do not initially attach the TESTSTAR fixtures. Do not send an extra `Run SAR` instruction or ask the participant to manage an identifier or version.

## Inputs

- Exact pinned `SUBMITTER.md` attachment from implementation SHA `22eb88f7eb78a1c07bd68eec1424e1341d0eae73`
- `ASSESSMENT.md` QA launch artifact (not the operational contract)
- `fixtures/S01-TESTSTAR-1-Request.md`
- `fixtures/S01-TESTSTAR-2-Product-Fact-Sheet.md`
- `fixtures/S01-TESTSTAR-3-Architecture.md`

## Participant Script

1. Start with a fresh conversation and provide both `ASSESSMENT.md` and the exact pinned `SUBMITTER.md` attachment. Do not add a separate workflow command or initially attach TESTSTAR fixtures.
2. Observe whether the AI reads and follows the supplied governed contract. Do not treat a simple acknowledgment of the attachment or GitHub URL as proof.
3. After governed startup visibly identifies `SAR Submitter v1.0` and presents Start/Continue, select `Start a new assessment` or `1`.
4. Wait for the governed initial-document interaction. Then attach all three TESTSTAR fixtures; do not separately type `Yes` or `1`.
5. Confirm the extracted product and intended-use facts.
6. If asked about an undocumented fact, answer: `I don't know; our vendor contact may know.`
7. If asked to choose among a bounded set and no answer is known, use `Unknown` or request clarification rather than guessing.

## Expected Observable Behavior

- The AI reads and follows the exact pinned `SUBMITTER.md` attachment supplied with the launch artifact; autonomous GitHub retrieval is not required for this scenario.
- The AI demonstrates use of the governed contract through the required startup and subsequent behavior; merely acknowledging the attachment, URL, or launch-artifact text is not proof.
- After successful governed initialization, the AI visibly displays `SAR Submitter v1.0` before or together with the Start/Continue interaction.
- The participant is not asked to enter, choose, remember, confirm, or manage the human-readable contract version.
- The AI treats `ASSESSMENT.md` as a launch artifact, not as the operational contract or a replacement for `SUBMITTER.md`.
- SAR automatically establishes the internal assessment identity for the new assessment.
- The participant is not asked to create, type, remember, select, or manage that identity, and unnecessary identity mechanics are not exposed to the participant.
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

Do not reuse historical S01 results, ask the participant to construct a special prompt, treat a URL acknowledgment as proof of reading `SUBMITTER.md`, accept the launch artifact as the governing contract, expose unnecessary identity or version mechanics, treat vendor claims as verified, invent facts, convert unknown or omitted information to `NO`, create Findings, score or classify risk, determine applicability, recommend approval, authorize use, or produce final disposition.

## PASS Conditions

The supplied exact pinned governed contract is successfully read and followed; successful startup visibly identifies `SAR Submitter v1.0` with the Start/Continue interaction; identity establishment is automatic and participant-hidden; fixtures attached at the initial-document interaction satisfy the affirmative path; facts and claims retain provenance; unresolved information remains visible; progression is factual and targeted; and no Reviewer conclusion occurs. This scenario does not test autonomous URL retrieval or identity persistence through later continuation state.

This scenario must not be marked `PASS` until actually executed against the stated baseline.

## FAIL Conditions

When the exact pinned attachment is supplied and readable, the AI fails to establish or follow it, fails to visibly identify `SAR Submitter v1.0` with the startup interaction, asks the participant to manage the version or identity, treats acknowledgment as proof of source access, ignores accessible fixtures, repeats adequately documented facts, invents or verifies unsupported claims, converts unknown/omitted information to `NO`, restarts or makes autonomous assessment determinations, or performs Reviewer work. If the environment cannot consume/read the supplied exact governed artifacts sufficiently to establish the contract, record an `ENVIRONMENT LIMITATION` instead of assigning `FAIL`.

## Environment-Limitation Handling

The exact pinned `SUBMITTER.md` attachment is the required controlled-QA bootstrap input. If the environment cannot consume/read it sufficiently, record `ENVIRONMENT LIMITATION` and stop; do not require GitHub retrieval or substitute another revision. Whether autonomous access to the immutable URL works may be recorded as a separate environment capability observation, but is not required for S01-v2 `PASS`. Apply the governed inaccessible-material rule to any fixture.

## Evidence to Capture

Capture that both launch and exact pinned contract artifacts were supplied, evidence that the pinned contract was actually followed, the visible `SAR Submitter v1.0` startup and Start New selection, identity behavior without recording unnecessary identifiers, document-ingestion acknowledgment, extracted facts and sources, claim/evidence/validation treatment, unresolved facts, questions asked, any prohibited behavior, and optional URL retrieval capability observations. Record the implementation-under-test SHA. At execution, record the SHA of the committed revision containing this exact S01-v2 definition; that test-definition SHA is not established until this revision is committed.

## Execution Notes

This scenario tests the revised new-assessment contract. Pause/save and cross-chat continuation are tested primarily by S10 and S11.
