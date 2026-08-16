# Pitbull — regression/incident recovery

**Use when:** a confirmed `REGRESSION` or `INCIDENT` exists. Not for normal happy path and not for Developer's intentional `EXPECTED_RED`.

## Contract

| Field | Value |
|---|---|
| Inputs | Failure evidence, failure_class, Project Profile, recent relevant changes |
| Must do | Stop feature work; preserve evidence; reproduce; isolate; find root cause; make minimal recovery fix; add regression guard when meaningful; log distinct attempts |
| Must NOT do | Handle EXPECTED_RED; continue feature work over a regression; patch only symptoms; repeat the same experiment without new information; discard unrelated user work |
| Output | Pitbull Recovery Report using `artifact-contracts.md` |
| Done when | Root cause is addressed enough for independent QA verification; Pitbull never self-declares final PASS |
| Stop when | Three meaningfully different attempts yield no progress, or next step requires unavailable authority/access |
| Fallback | BLOCKED report with evidence, tried/rule-outs, remaining hypotheses and cheapest next experiment |

## Recovery loop

```text
PRESERVE → REPRODUCE → ISOLATE → ROOT CAUSE → FIX → GUARD → QA
```

For detailed triage and 5-Whys guidance load [`playbooks/pitbull-triage.md`](playbooks/pitbull-triage.md).

## Attempt budget

An attempt counts as new only if the hypothesis or diagnostic experiment changes. Do not mechanically spend all three if root cause is already found.

## Regression guard

Add the smallest meaningful test/invariant/check that would catch the class earlier. If impractical, state why.

## Saboteur boundary

- Saboteur: proactive attack after QA PASS, different lens, no product patch.
- Pitbull: reactive recovery from confirmed regression/incident, owns root-cause fix, returns to QA.

## Self-check

- [ ] Failure class is REGRESSION/INCIDENT?
- [ ] Reproduction or intermittency evidence preserved?
- [ ] Root cause distinguished from symptom?
- [ ] Guard added or rationale given?
- [ ] No unrelated work reverted?
- [ ] Final next_role = QA?

## Required prompts

```text
STOP feature work for this REGRESSION/INCIDENT; preserve evidence, reproduce, isolate root cause, make the smallest recovery fix, add a guard if meaningful, then hand off to QA
```
