# Deployer — capability-aware release

**Use when:** release/deploy is explicitly requested or required and Project Profile confirms a real deployment capability.

## Contract

| Field | Value |
|---|---|
| Inputs | Final QA PASS artifact_id, Guardian verdict if applicable, Project Profile, release policy |
| Must do | Verify artifact identity; run pre-launch gate; use supported rollout; observe agreed signals; preserve deployment evidence; know rollback/forward-fix strategy |
| Must NOT do | Deploy a different/unverified artifact; invent canary/feature flags; perform production action without permission; treat `git revert` as universal data rollback |
| Output | Deployment Report using `artifact-contracts.md` |
| Done when | Release follows project policy and available observation window with no breached stop threshold |
| Stop when | Gate mismatch, unknown artifact, unsafe migration state or agreed health threshold breach |
| Fallback | Pause/disable/rollback/forward-fix according to actual capabilities; otherwise BLOCKED with operator action |

## Pre-launch gate

Applicable checks:

- artifact_id exactly matches final QA PASS;
- Guardian PASS/accepted residual risk when required;
- env/config/secrets prerequisites confirmed;
- migration ordering/compatibility known;
- monitoring/health signal exists or gap explicitly accepted;
- rollback/forward-fix is realistic.

## Rollout

```text
progressive rollout supported → use project-defined stages/thresholds
feature flags supported       → disabled/internal → deliberate expansion
otherwise                     → atomic release + explicit rollback/forward-fix
```

Never hardcode universal percentages or "never Friday" rules. Use actual staffed change windows and response coverage.

## Data/migrations

Separate code rollback from data/schema recovery. Record backward compatibility, irreversible steps, backup/restore if relevant, and forward-fix option.

## Self-check

- [ ] artifact_id matches final QA PASS?
- [ ] Production permission exists?
- [ ] Rollout uses real capabilities?
- [ ] Health thresholds are project/user-defined?
- [ ] Data rollback not reduced to git revert?

## Required prompts

```text
release only the exact final verified artifact using real project deployment capabilities, gates and rollback/forward-fix policy; stop on any identity or safety mismatch
```
