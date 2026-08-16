# Pitbull Triage — Reproduce → Isolate → Root Cause → Fix & Guard

## 1. Preserve
Capture the original failure: command/request/input, logs, stack trace, artifact identity, relevant environment and recent changes. Do not destroy the scene with broad cleanup/reset.

## 2. Reproduce
Find the smallest reliable reproducer. If intermittent, record frequency/conditions rather than pretending certainty.

## 3. Isolate
Reduce dimensions one at a time:
- which component/path/data/state;
- before/after which change;
- minimal input;
- dependency/environment difference;
- concurrency/timing condition.

## 4. Root cause
Build a causal chain. Use 5 Whys only while each answer has evidence; stop when the chain reaches an actionable mechanism, not a slogan.

Example:
```text
symptom → immediate mechanism → enabling condition → violated invariant → missing guard
```

## 5. Minimal recovery fix
Fix the mechanism, not only the visible symptom. Avoid unrelated refactor during incident recovery.

## 6. Guard
Add the smallest regression test/invariant/monitoring check that catches recurrence early. If impossible, record the reason and detection plan.

## 7. Independent verification
Pitbull hands off to QA. Recovery evidence is not final QA PASS.
