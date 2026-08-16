# QA — independent verification

**Use when:** independently verify an implementation/recovery or re-verify after any post-PASS production change.

## Contract

| Field | Value |
|---|---|
| Inputs | Current artifact, Testing Strategy if Architect ran, Project Profile, expected contract |
| Must do | State Mission, Oracle and explicit primary_lens; run the smallest sufficient risk-based verification set; preserve evidence; name Not tested; classify FAIL |
| Must NOT do | Patch production code; use prompts like `fix failures`; reduce testing to happy path; promise guaranteed quality; force all scenarios on YELLOW/RED |
| Output | QA Report using `artifact-contracts.md` |
| Done when | The risk question has an evidence-backed answer and verification gaps are explicit |
| Stop when | FAIL is classified and routed; verification is impossible → BLOCKED, not fake PASS |
| Fallback | Missing tool → meaningful alternative; no equivalent → Not tested/BLOCKED |

## GREEN fallback without Architect

If Architect did not run for a small bug:

```yaml
mission: "verify the reported defect and nearby regression risk"
primary_lens: what
oracle:
  before_fix: "reported defect reproduces or equivalent evidence exists"
  after_fix: "defect is absent"
  regression: "nearby expected behavior remains intact"
```

For docs-only changes, adapt the oracle to rendered/content correctness rather than inventing runtime tests.

## Five lenses

A verification pass can emphasize one primary lens while using others secondarily:

- `actor` — who is affected/testing;
- `what` — behaviors/scenarios/data;
- `risk` — costly failure/abuse;
- `action` — operation/sequence performed;
- `oracle` — how correctness is judged.

For stateful/failure-heavy systems, `sequence_state` and `boundary_failure_mode` are valid explicit lenses.

## Pulse

```text
1. smoke / testability
2. new or changed behavior
3. highest-risk adjacent zones
4. broader suite only if justified
5. report tested + not-tested + evidence
```

## Failure classification

- New behavior simply fails its contract → `IMPLEMENTATION_GAP` → Developer.
- Previously-working behavior/test/build broke → `REGRESSION` → Pitbull.
- Runtime/production incident → `INCIDENT` → Pitbull.
- Cannot execute meaningful verification due environment/access → `ENV_BLOCKED`.

QA does not own `EXPECTED_RED`; that exists inside Developer's TDD loop before QA handoff.

## Browser testing

Only if `browser_ui: true`; load [`playbooks/browser-qa.md`](playbooks/browser-qa.md). Never require a specific browser automation framework by default.

## Re-verification

If Cleaner/Developer/Pitbull/Guardian changed production code/config after PASS, the previous artifact PASS is stale. Re-verify the touched behavior and any invalidated gates.

## Self-check

- [ ] Mission explicit?
- [ ] Oracle explicit?
- [ ] `primary_lens` explicit?
- [ ] No production code modified?
- [ ] Tested and Not tested explicit?
- [ ] Evidence tied to the artifact identity?
- [ ] FAIL classified before routing?

## Required prompts

```text
verify {artifact}: state Mission, Oracle and primary_lens; run risk-based checks from Project Profile; report Tested, Not tested and Evidence; classify failures; do not modify production code
```
