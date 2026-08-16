# Artifact Contracts — explicit inter-role interfaces

**Rule:** if role B requires data from role A, the field must exist explicitly in A's output. Do not rely on narrative inference.

## Common handoff

```yaml
status: PASS | FAIL | BLOCKED | NEEDS_CHANGES
risk: GREEN | YELLOW | RED
artifact_id: "stable identity if available"
artifact: "scope"
evidence: []
findings: []
not_verified: []
failure_class: N/A | EXPECTED_RED | IMPLEMENTATION_GAP | REGRESSION | INCIDENT | ENV_BLOCKED
next_role: "Role | DONE"
invalidate_previous_verification: false
```

## Architect Plan

```yaml
objective: "..."
constraints: []
assumptions: []
existing_patterns: []
dependency_graph: []
vertical_slices: []
boundaries:
  always_do: []
  ask_first: []
  never_do: []
testing_strategy:
  mission: "risk and beneficiary"
  oracle_sources: []
  budget: "targeted | moderate | broad"
  pulse: [smoke, changed_behavior, risk_zones, broader_if_justified, report_gaps]
  not_planned: []
verification_commands: []
rollback_or_migration: []
not_doing: []
```

## Review Report

```yaml
verdict: APPROVED | NEEDS_CHANGES
independence: STRONG | WEAK | N/A
axes:
  correctness: []
  simplicity: []
  architecture: []
  security: []
  performance: []
blocking_findings: []
suggestions: []
```

## QA Report

`primary_lens` is mandatory because Saboteur consumes it.

```yaml
mission: "what risk matters and to whom"
primary_lens: actor | what | risk | action | oracle | sequence_state | boundary_failure_mode
oracle:
  source: spec | contract | invariant | product | history | justified_common_sense
  expectation: "..."
result: PASS | FAIL | BLOCKED
tested: []
not_tested: []
evidence: []
regressions_or_findings: []
failure_class: N/A | IMPLEMENTATION_GAP | REGRESSION | INCIDENT | ENV_BLOCKED
artifact_id: "..."
next_role: "..."
```

## Sabotage Report

```yaml
primary_lens: "different from QA primary_lens"
attack_budget: "bounded scope/time/check count"
findings:
  - summary: "one issue"
    status: CONFIRMED | UNCONFIRMED
    severity: CRITICAL | HIGH | MEDIUM | LOW
    priority: NOW | NEXT | LATER
    reproduction: "..."
    expected: "oracle/contract"
    actual: "..."
    evidence: "..."
not_attacked: []
next_role: "..."
```

## Pitbull Recovery Report

```yaml
failure_class: REGRESSION | INCIDENT
reproduction: "..."
root_cause: "..."
attempts: []
recovery_change: "..."
regression_guard: "test/invariant or rationale"
residual_uncertainty: []
next_role: QA
invalidate_previous_verification: true
```

## Security Report

```yaml
verdict: PASS | FAIL | BLOCKED
trust_boundaries: []
threats_checked: []
findings: []
dependency_or_scanner_evidence: []
not_assessed: []
accepted_risks: []
artifact_id: "..."
next_role: "..."
```

## Deployment Report

```yaml
artifact_id: "must match final verified artifact"
release_strategy: "..."
gates: []
observed_signals: []
rollback_or_forward_fix: "..."
result: PASS | FAIL | BLOCKED
```
