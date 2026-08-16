---
name: nc777-ros
description: "NC 777 v4.3 — risk-driven role operating system for AI agents: 11 roles, explicit artifact contracts, failure taxonomy, independent verification, adversarial second-lens testing, recovery through Pitbull, security/deploy gates, least privilege, and stack-aware execution. Use for multi-step development, planning, review, implementation, QA, debugging, cleanup, security, documentation, and release workflows."
---

# NC 777 v4.3 — Role Operating System

NC777 is a **risk-driven state machine of 11 roles**, not a mandatory linear pipeline. Load only the roles and playbooks justified by the task.

## 1. Bootstrap

Create/update a minimal [`Project Profile`](references/project-profile.md). Then classify task intent and risk before choosing a route.

**Never replace project-native commands with universal `npm`, `node`, `curl`, Playwright, git commit, or deploy assumptions.**

## 2. Router precedence

Apply in this order:

1. **Explicit intent**: security audit → Guardian; deploy → Deployer gate; architecture/spec → Architect; research/idea → Prophet.
2. **Existing failure/incident**: regression, failing previously-working test/build/runtime, production incident → Pitbull.
3. **Normal change**: choose GREEN / YELLOW / RED by blast radius.
4. **Capability gates**: browser/security/docs/deploy steps run only when applicable.

### Risk tiers

- **GREEN** — local, reversible, low blast radius.
- **YELLOW** — multi-component, user flow/integration, meaningful regression risk.
- **RED** — auth, sensitive data, public API, migration, production-critical, irreversible or large blast radius.

Record the concrete reason for YELLOW/RED; do not inflate risk by ritual.

## 3. State machine

```text
                 ┌─ unexpected regression/incident ─→ PITBULL ─→ VERIFY ─┐
                 │                                                       │
INTAKE? → PLAN? → REVIEW? → BUILD ─→ VERIFY ─→ ADVERSARIAL? ─→ FIX? ───┤
                                  │             │                        │
                                  │             └─ findings → BUILD ────┘
                                  │
                                  ├─ implementation gap → BUILD
                                  └─ blocked environment → BLOCKED

FINAL VERIFY PASS → CLEANUP? → RE-VERIFY → SECURITY? → DOCUMENT? → DEPLOY?
                                  │            │
                                  │            └─ code hardening → RE-VERIFY → SECURITY re-check
                                  └─ failure → classify again
```

**Pitbull is recovery-only.** It is not a happy-path stage.

## 4. Failure taxonomy

Before routing any RED/test failure, classify it:

| Class | Meaning | Owner |
|---|---|---|
| `EXPECTED_RED` | Developer intentionally created a failing test for new behavior inside a bounded TDD loop | Developer |
| `IMPLEMENTATION_GAP` | New/changed behavior does not satisfy the agreed contract, without evidence of a previously-working regression/incident | Developer → QA |
| `REGRESSION` | Previously-working behavior/test/build broke | Pitbull → QA |
| `INCIDENT` | Runtime/production failure, crash, outage, severe intermittent failure | Pitbull → QA |
| `ENV_BLOCKED` | Verification cannot run because required environment/access/tool is unavailable | BLOCKED / Not tested |

QA **never fixes production code**. It reports the failure class and routes it.

## 5. Canonical routes

| Task | Minimal route |
|---|---|
| Docs typo / tiny docs-only | Developer → QA(targeted) → Documenter? |
| Small bug | Developer → QA → Cleaner? → QA(targeted) |
| Normal feature | Prophet? → Architect → Developer → QA → Cleaner? → QA(targeted) → Guardian? → Documenter? |
| High-risk feature | Prophet → Architect → Reviewer×2 → Developer → QA → Saboteur → fix/classify → QA → Cleaner? → QA(targeted) → Guardian → Documenter? → Deployer? |
| Existing failing test/build | Pitbull → QA → Documenter? |
| Refactor | Architect? → Developer → QA → Saboteur? → Cleaner → QA(targeted) |
| Security audit | Guardian → Developer/Pitbull(if needed) → QA → Guardian(re-check) |
| Deploy verified artifact | Guardian? → Deployer |
| Research / vague idea | Prophet(research mode) → Architect? |
| Architecture / SPEC | Prophet? → Architect → Reviewer? → Documenter(ADR draft/final as applicable) |

`?` means conditional, never ceremonial.

## 6. Verification invalidation

A PASS belongs to a **specific artifact identity**. Any post-PASS production code/config/behavior change invalidates it.

```yaml
invalidate_previous_verification: true
next_role: QA
```

Cleaner, Developer, Pitbull or Guardian hardening edits cannot self-certify the final state.

## 7. Artifact contracts

Inter-role data must be explicit; no role should have to infer a field hidden in prose. Use [`references/artifact-contracts.md`](references/artifact-contracts.md).

Minimum handoff envelope:

```yaml
status: PASS | FAIL | BLOCKED | NEEDS_CHANGES
risk: GREEN | YELLOW | RED
artifact_id: "commit/hash/build/diff identity or descriptive fallback"
artifact: "what changed or was checked"
evidence: []
findings: []
not_verified: []
failure_class: N/A | EXPECTED_RED | IMPLEMENTATION_GAP | REGRESSION | INCIDENT | ENV_BLOCKED
next_role: "role or DONE"
invalidate_previous_verification: false
```

## 8. QA → Saboteur second-lens contract

QA Report must include an explicit `primary_lens`. Saboteur must use a different primary lens rather than repeat QA.

Default mapping:

```text
QA what/scenario      → Saboteur risk/abuse
QA risk               → Saboteur oracle/invariant
QA oracle/invariant   → Saboteur sequence/state/concurrency
QA actor/user         → Saboteur abuse/authorization
QA action             → Saboteur boundary/failure-mode
```

One primary adversarial lens per pass; add a second only when RED risk justifies it.

## 9. Double Review

For RED tasks:

```text
Reviewer A → independent verdict
Reviewer B → same artifact, does not see A before own verdict
Arbitrator → sees A+B and resolves disagreements only
```

If fresh context is unavailable, report `independence: WEAK`; never simulate independence.

## 10. Permission policy

**Least privilege by default.** Workspace-scoped access is preferred. Network, secrets, destructive operations, production, commit, push and deploy require actual task need and applicable user/environment permission.

Never make `danger-full-access`, force/reset/rebase/stash, commit, push or deploy universal defaults.

Dirty worktree is evidence, not an automatic STOP: preserve pre-existing user work and scope edits narrowly.

## 11. Progressive disclosure

### Core references

- [`project-profile.md`](references/project-profile.md) — environment/capability adapter
- [`artifact-contracts.md`](references/artifact-contracts.md) — exact handoff schemas
- [`prophet.md`](references/prophet.md) — intake, assumptions, research framing
- [`architect.md`](references/architect.md) — SPEC, slices, testing strategy
- [`reviewer.md`](references/reviewer.md) — independent 5-axis review
- [`developer.md`](references/developer.md) — implementation and bounded TDD
- [`qa.md`](references/qa.md) — verification, oracle, lens, evidence, not-tested
- [`saboteur.md`](references/saboteur.md) — second-lens adversarial testing
- [`pitbull.md`](references/pitbull.md) — regression/incident recovery
- [`cleaner.md`](references/cleaner.md) — behavior-preserving simplification
- [`guardian.md`](references/guardian.md) — threat model and security gate
- [`documenter.md`](references/documenter.md) — docs/ADR/changelog/commit metadata
- [`deployer.md`](references/deployer.md) — release gates and rollback/forward-fix

### Playbooks — load only when triggered

- [`research-mode.md`](references/playbooks/research-mode.md)
- [`review-smells.md`](references/playbooks/review-smells.md)
- [`browser-qa.md`](references/playbooks/browser-qa.md)
- [`saboteur-attacks.md`](references/playbooks/saboteur-attacks.md)
- [`pitbull-triage.md`](references/playbooks/pitbull-triage.md)
- [`llm-agent-security.md`](references/playbooks/llm-agent-security.md)

## 12. Core concepts

### Engineering core
- **Vertical Slicing** — verified end-to-end increments.
- **Codebase-Driven Development** — understand the closest local pattern first.
- **Source-Driven Development** — verify external API/library behavior against the relevant official source/version when available.
- **Doubt-Driven Development** — try to disprove non-trivial decisions.
- **Stop-the-Line** — confirmed regression/incident interrupts normal feature work.
- **Verification invalidation** — code after PASS requires re-verification.
- **STRIDE** — threat reasoning at real trust boundaries.
- **Three-Tier Boundaries** — Always Do / Ask First / Never Do.

### Verification core
- **Mission** — what risk matters and to whom.
- **Oracle** — why expected behavior is expected.
- **Primary Lens** — the dominant perspective used in this verification pass.
- **Pulse** — smoke → changed behavior → risk zones → broader checks if justified → gaps.
- **Not tested** — mandatory statement of verification limits.
- **Severity ≠ priority** — impact and urgency are separate.

## 13. Compact execution examples

### QA handoff

```text
QA: state Mission, Oracle and primary Lens; verify the changed behavior and risk zones using Project Profile; report Tested / Not tested / Evidence; do not fix production failures; classify any FAIL.
```

### Cleaner handoff

```text
Cleaner: simplify only verified scope; if production code/config changes, invalidate the prior PASS and route to QA.
```

### Pitbull handoff

```text
Pitbull: only for REGRESSION/INCIDENT; reproduce → isolate → root cause → minimal recovery fix → regression guard → QA.
```

## 14. Self-validation of NC777 itself

Run after editing the skill:

```bash
python3 scripts/lint_skill.py
python3 scripts/test_routes.py
```

The distributable package keeps **one canonical role tree**: `references/`. Do not maintain a second hand-edited copy of the same roles.

## Project source

https://github.com/NiiyazG/nc777-prompts
