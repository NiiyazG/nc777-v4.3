# NC 777 v4.3 — Role Operating System

11-role operating system for AI agents with risk-driven routing, explicit artifact contracts, failure ownership, independent verification, adversarial second-lens testing, recovery, security and release gates.

## What v4.3 changes

- Adds explicit inter-role schemas, including mandatory `QA Report.primary_lens`.
- Adds failure taxonomy: `EXPECTED_RED`, `IMPLEMENTATION_GAP`, `REGRESSION`, `INCIDENT`, `ENV_BLOCKED`.
- Keeps intentional TDD RED with Developer; Pitbull is only regression/incident recovery.
- Makes QA verification-only and gives GREEN tasks a no-Architect fallback strategy.
- Gives Saboteur deterministic second-lens selection and a bounded attack catalog.
- Restores deep Pitbull triage, Reviewer smells, browser QA and LLM/agent security as optional playbooks.
- Documents only final verified behavior; Cleaner changes always invalidate PASS.
- Keeps a single canonical role tree (`references/`) to prevent drift.
- Uses Project Profile instead of hardcoded Node/npm/curl/browser/deploy assumptions.
- Keeps least-privilege execution and capability/policy-driven commit/deploy behavior.

## Structure

```text
nc777-ros/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── references/
│   ├── project-profile.md
│   ├── artifact-contracts.md
│   ├── <11 role files>.md
│   └── playbooks/
│       ├── research-mode.md
│       ├── review-smells.md
│       ├── browser-qa.md
│       ├── saboteur-attacks.md
│       ├── pitbull-triage.md
│       └── llm-agent-security.md
├── scripts/
│   ├── lint_skill.py
│   └── test_routes.py
└── tests/
    └── router-cases.yaml
```

## Use

1. Read `SKILL.md`.
2. Create/update a minimal Project Profile.
3. Classify explicit intent, existing failure state and risk tier.
4. Load only the needed role files/playbooks.
5. Pass explicit artifacts rather than narrative guesses.
6. Re-verify whenever production behavior changes after PASS.

## Self-check

```bash
python3 scripts/lint_skill.py
python3 scripts/test_routes.py
```

## Project source

https://github.com/NiiyazG/nc777-v4.3
