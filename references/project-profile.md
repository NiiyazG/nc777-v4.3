# Project Profile — Environment & Capability Adapter

Determine the project's real stack, commands, capabilities and permissions once, then let all roles reuse the profile.

## Discovery order

1. Repository instructions (`AGENTS.md`, `CLAUDE.md`, README, CONTRIBUTING, CI).
2. Manifest/lock/build/config files.
3. Existing scripts/tasks/Makefile/workflows.
4. Only then cautious command probes.

Do not invent a command or install a dependency only to satisfy NC777.

## Template

```yaml
project_profile:
  language: unknown
  framework: unknown
  package_manager: unknown
  vcs: git | other | none
  repository_state: clean | dirty | unknown

  commands:
    test: N/A
    lint: N/A
    typecheck: N/A
    build: N/A
    smoke: N/A
    security_audit: N/A

  capabilities:
    server: false
    api: false
    cli: false
    browser_ui: false
    database: false
    migrations: false
    external_services: false
    llm_or_agent: false
    feature_flags: false
    progressive_rollout: false
    monitoring: false
    ci: false
    deploy: false

  artifact_identity:
    strategy: commit | build_id | package_version | digest | descriptive

  permissions:
    workspace_write: allowed | ask | denied
    network: allowed | ask | denied
    secrets: allowed | ask | denied
    destructive_ops: ask
    production: ask
    commit: allowed | ask | denied
    push: ask
    deploy: ask

  constraints: []
```

## Command rules

- Prefer commands already used by CI/project scripts.
- Prefer targeted checks in inner loops; broaden only at gates when risk justifies it.
- Missing tooling is a verification gap, not automatically a product failure.
- If the project exposes multiple test modes, record the cheapest targeted mode and the broader gate mode.

## Dirty repository rule

Dirty worktree is evidence, not automatic failure:

1. inspect status/diff;
2. distinguish pre-existing changes from current-task changes;
3. never reset/stash/discard unrelated user work without explicit permission;
4. scope edits narrowly.

Default to least privilege when policy is unknown.
