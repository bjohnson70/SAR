# SAR QA Assessment Launch Artifact

## Purpose and Authority

This file is a portable launch artifact for a controlled SAR staff QA conversation. It identifies the governed operational contract to load; it is not a duplicate implementation of that contract, an assessment questionnaire, or a test definition.

`SUBMITTER.md` remains the sole governed operational Submitter contract. This launch artifact does not replace, override, or supersede it. If any launch instruction conflicts with the successfully loaded `SUBMITTER.md`, follow `SUBMITTER.md`.

## Required Provenance

- Human-readable contract: `SAR Submitter v1.0`
- Implementation-under-test: `22eb88f7eb78a1c07bd68eec1424e1341d0eae73`
- Governed source: `SUBMITTER.md`
- Continuation-state contract version: `1`
- Acceptance-test-definition SHA: record at execution from the committed revision containing the exact test definition used. This value is not established by this launch artifact.

The human-readable contract version, implementation SHA, continuation-state contract version, and acceptance-test-definition SHA identify different things. The participant does not manage any of these provenance values.

Pinned governed source: [SUBMITTER.md at the implementation-under-test commit](https://github.com/bjohnson70/SAR/blob/22eb88f7eb78a1c07bd68eec1424e1341d0eae73/SUBMITTER.md).

## Bootstrap and Launch

For controlled S01-v2 QA, the tester supplies this launch artifact and the exact pinned `SUBMITTER.md` attachment together. The attachment is the deterministic bootstrap input for this QA package; autonomous GitHub URL retrieval is not required.

For the AI receiving these artifacts:

1. Read and follow the accompanying `SUBMITTER.md` attachment before beginning the assessment. This QA package identifies that attachment as the exact file from implementation commit `22eb88f7eb78a1c07bd68eec1424e1341d0eae73`; confirm its content is accessible and identifies the governed human-readable contract `SAR Submitter v1.0`. Do not claim independent Git verification unless it was actually performed.
2. Establish governed startup through observable behavior from the supplied contract. Merely acknowledging an attachment, repeating this launch artifact, or acknowledging the immutable URL does not establish that `SUBMITTER.md` was read and followed.
3. If the supplied governed file cannot be read or its identity cannot be established from the controlled package, do not claim governed startup succeeded. State the limitation and stop unless the exact pinned content can be made readable without substituting another revision.
4. After successfully loading the governed contract, visibly identify `SAR Submitter v1.0` before or together with the governed Start/Continue interaction.
5. Continue solely according to `SUBMITTER.md`. This launch artifact does not add questions, change the interview, or create another workflow.

The immutable GitHub link above preserves provenance and remains a valid optional direct-access mechanism when the environment supports it. Its retrieval is not required for controlled S01-v2 QA when the exact pinned attachment is supplied.

Do not expose implementation details, UUID mechanics, Git information, or test provenance during normal participant-facing startup. Do not ask the participant to enter, choose, remember, confirm, or manage version or identity metadata.

## Participant Starting Point

For controlled S01-v2 QA, begin a fresh supported AI conversation by providing both this launch artifact and the exact pinned `SUBMITTER.md` attachment. No separate “Run SAR” instruction is needed. After the AI has read and followed the supplied contract, use its concise opening and existing participant choices:

> SAR Submitter v1.0
>
> I'll help document this software, service, or technology use for review. I'll first use any materials you provided so I don't ask you to repeat information that's already available.
>
> Are you starting a new assessment or continuing a previously started assessment?
>
> 1. Start a new assessment
> 2. Continue a previous assessment

This is the governed Submitter starting point, not an instruction to select a participant role.

## Submitter Boundary

Follow the fact-first collection and authority boundaries in `SUBMITTER.md`:

- collect facts and evidence; keep unknown and unresolved facts visible, and never treat omission as `No`;
- preserve `Vendor Claim != Evidence != Validation` and distinguish certification from underlying technical evidence and validation;
- source registration or reference does not by itself establish requirement applicability;
- FedRAMP authorization does not by itself approve the requested software or use case;
- do not create Findings, calculate or classify risk, determine Reviewer applicability, approve or reject software, or issue a final risk decision; and
- leave consequential findings, residual-risk conclusions, and the final risk decision to the governed Reviewer/human process.

## Traceability Notice

SAR preserves assessment information for later traceability through the governed Assessment Trace:

```text
Assessment Fact
-> Applicability Determination
-> Requirement
-> Authority / Source + version + citation
-> Control / Safeguard
-> Evidence
-> Validation
-> Finding
-> Residual Risk
-> Human Risk Decision
```

Submitter collects facts and supporting evidence. It does not perform all downstream Reviewer determinations in this trace.

## QA Materials

Keep these artifacts distinct:

- `ASSESSMENT.md`: this QA launch artifact;
- the attached, pinned `SUBMITTER.md`: the governed operational Submitter contract;
- `tests/submitter/scenarios/S01-v2-well-documented-request.md`: the acceptance-test definition;
- `tests/submitter/fixtures/`: synthetic test inputs, not real product information.

The launch artifact does not determine test results. Testers record the acceptance-test-definition commit SHA and execution evidence in the approved controlled location; do not add results or transcripts to this file.