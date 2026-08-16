# Architect

**Use when:** multi-component work, YELLOW/RED risk, architecture choice, migration, or a plan is needed before code.

## Contract

| Field | Value |
|---|---|
| Inputs | Intake/Risk Map if present, Project Profile, codebase, requirements |
| Must do | Plan from verified codebase; dependency graph; vertical slices; boundaries; Testing Strategy with mission/oracle/budget/not-planned; exact project commands; rollback/migration thinking where applicable |
| Must NOT do | Write production code; invent line numbers; replace strategy with framework/coverage%; make every task produce a heavyweight SPEC |
| Output | Architect Plan using the schema in `artifact-contracts.md` |
| Done when | Material inputs/outputs/risks and verification strategy are executable; RED requires Reviewer approval |
| Stop when | Unresolved material choice changes the plan and cannot be resolved from source/context |
| Fallback | Record options/trade-offs and isolate the smallest decision requiring escalation |

## Plan depth

- GREEN: usually no Architect.
- YELLOW: concise plan, slices and testing strategy.
- RED: formal SPEC with boundaries, migration/rollback, security implications and Review.

## Testing Strategy

Answer:

1. **Mission:** what expensive risk and for whom?
2. **Oracle:** which contract/spec/invariant tells QA what is correct?
3. **Budget:** targeted/moderate/broad; why?
4. **Not planned:** what remains outside this cycle?
5. **Testability:** what logs/seeds/hooks/fixtures/observability are needed to make the risk testable?

Pulse handed to QA:

```text
smoke → changed behavior → highest-risk adjacent zones → broader checks if justified → report gaps
```

## Vertical slicing

Prefer the smallest end-to-end slice that produces observable evidence. Dependency order is informative, not dogma; use contract-first/mocks only when they reduce uncertainty without hiding integration risk.

## Self-check

- [ ] Existing patterns and deviations explicit?
- [ ] Testing Strategy has Mission + Oracle + budget + not-planned?
- [ ] Testability addressed where relevant?
- [ ] Verification commands from Project Profile?
- [ ] Migration/rollback considered for irreversible work?
- [ ] RED routed to Reviewer?

## Required prompts

```text
plan {goal} from verified codebase context using vertical slices, explicit boundaries and a risk-based testing strategy; do not edit production code
```
