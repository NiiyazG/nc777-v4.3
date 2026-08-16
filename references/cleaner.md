# Cleaner — behavior-preserving cleanup

**Use when:** current artifact is QA PASS and simplification has concrete value. Skip when cleanup would add more risk than benefit.

## Contract

| Field | Value |
|---|---|
| Inputs | Verified artifact, diff, Project Profile |
| Must do | Preserve behavior; reduce accidental complexity; follow project conventions; remove only task-created temporary artifacts; minimize diff |
| Must NOT do | Use clean worktree as success criterion; remove product behavior; touch unrelated/pre-existing work; hide a functional change inside cleanup |
| Output | Cleaner Summary + behavior-sensitive changed areas |
| Done when | Cleanup scope is complete and understandable; any production change explicitly invalidates prior verification |
| Stop when | Behavior preservation cannot be justified or file ownership is unclear |
| Fallback | Leave doubtful code unchanged and record recommendation instead |

## Principles

1. Preserve inputs, outputs, errors, side effects and timing-sensitive contracts.
2. Follow local conventions; do not impose style for style's sake.
3. Reduce nesting/duplication only when complexity actually drops.
4. Avoid premature abstraction before multiple real use cases justify it.
5. Treat public API rename/removal as migration, not cleanup.

## Mandatory re-verification

Any production code/config/test edit that can affect behavior:

```yaml
invalidate_previous_verification: true
next_role: QA
```

Final PASS belongs to QA, never Cleaner.

## Self-check

- [ ] Cleanup has concrete value?
- [ ] Behavior-sensitive changes listed?
- [ ] Unrelated work preserved?
- [ ] Previous PASS invalidated after production edits?
- [ ] Migration semantics not disguised as cleanup?

## Required prompts

```text
simplify only the verified scope without changing behavior; preserve unrelated work; invalidate verification and route to QA if production code/config changes
```
