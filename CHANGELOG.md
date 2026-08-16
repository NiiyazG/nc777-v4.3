# Changelog

## v4.3

- Added explicit Artifact Contracts for Architect, Review, QA, Saboteur, Pitbull, Security and Deployment outputs.
- Added mandatory `QA Report.primary_lens` and deterministic QA→Saboteur second-lens mapping.
- Added failure taxonomy separating intentional TDD RED from implementation gaps, regressions, incidents and environment blocks.
- Restricted Pitbull to regression/incident recovery; restored Reproduce→Isolate→Root Cause→Fix→Guard playbook.
- Added GREEN QA fallback for routes without Architect.
- Added bounded Saboteur attack catalog and one-finding-one-bug advocacy.
- Added Reviewer design-smell heuristics, contextual Prophet research mode, browser QA and LLM/agent security playbooks.
- Clarified Developer.Done vs QA verification vs release readiness.
- Moved normal behavior documentation after final verification; ADR draft remains possible during architecture.
- Enforced a single canonical role tree and expanded self-lint/regression checks.

## v4.2

- Replaced mandatory linear pipeline with a risk-driven state machine.
- Moved Pitbull to failure/incident recovery only.
- Made QA verification-only; removed production-fix responsibility.
- Added mandatory re-verification after Cleaner or any post-PASS production change.
- Added Project Profile for stack-aware commands and capabilities.
- Removed hardcoded Node/npm/curl/browser assumptions from role contracts.
- Changed dirty worktree from STOP condition to ownership-preservation rule.
- Made commit, cache busting, feature flags, progressive rollout and deploy conditional on project policy/capability.
- Replaced full-access default with least-privilege permission policy.
- Split Codebase-Driven and Source-Driven Development.
- Made Guardian security gate capability-aware and evidence-based.
- Added structured role handoff state, package lint and router regression cases.
