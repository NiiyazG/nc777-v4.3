# Prophet / Intake

**Use when:** requirements, environment or blast radius are unclear; normally YELLOW/RED. May be skipped for a fully-defined GREEN task.

## Contract

| Field | Value |
|---|---|
| Inputs | User goal, Project Profile, available context |
| Must do | Surface material assumptions; inspect only context that can falsify the current understanding; classify risk; identify likely failure points; separate verified from assumed |
| Must NOT do | Run stack-specific checks without evidence; expand repository reading without a search hypothesis; block on safe reversible ambiguity |
| Output | Intake/Risk Map + assumption classes + context inventory |
| Done when | Material requirements are sufficiently determined for planning/execution |
| Stop when | An unresolved A3 or material A2 assumption can make the next action unsafe/wrong |
| Fallback | Continue only with safe reversible assumptions; mark unresolved material items BLOCKED |

## Assumptions

- **A0 Verified** — confirmed by code/config/spec/tool.
- **A1 Safe/Reversible** — can proceed explicitly; easy rollback, small blast radius.
- **A2 Material** — changes behavior/architecture/cost; resolve if repository cannot answer.
- **A3 Irreversible/Security/Data** — deletion, migration, auth boundary, production action; requires explicit contract/permission.

## Contextual pre-flight

Check **what this task can lie about**, not a universal checklist. Examples: syntax/build only if relevant, server health only if a server exists, repository ownership only if editing files, credentials only if the task requires them.

Dirty worktree is not a STOP by itself.

## Interview mode

Ask only questions that can materially change the answer:

1. user/consumer;
2. success condition;
3. constraints;
4. existing attempts/system;
5. risk/time trade-offs.

Do not ask what the repository already answers.

## Research mode

For vague design/idea exploration load [`playbooks/research-mode.md`](playbooks/research-mode.md).

## Self-check

- [ ] Risk tier has a concrete blast-radius reason?
- [ ] A0/A1/A2/A3 separated?
- [ ] No unnecessary question or repository crawl?
- [ ] Pre-flight matches actual project capabilities?
- [ ] Dirty worktree handled by ownership, not panic?

## Required prompts

```text
surface only assumptions that can materially change the implementation; classify A0-A3 and inspect the smallest context that can verify them
```
