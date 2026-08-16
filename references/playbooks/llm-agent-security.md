# LLM / Agent Security Playbook

Use when `llm_or_agent: true` or untrusted natural-language/model output can influence tools, data or privileged actions.

Treat **model output and retrieved content as untrusted input**. A system prompt is guidance, not a security boundary.

## Threats
- direct and indirect prompt injection;
- tool poisoning / malicious tool descriptions or retrieved instructions;
- excessive agency and overbroad tool permissions;
- credential/secret leakage into prompts, logs, model-visible context or outputs;
- cross-user/tenant data leakage;
- unsafe model output consumed as code/query/path/command/HTML;
- destructive actions without confirmation/authorization;
- permission escalation across tools/accounts;
- infinite tool loops / retry storms;
- cost/resource exhaustion;
- untrusted external content overriding higher-priority policy.

## Controls
- least-privilege tool scopes and data access;
- separate trusted instructions from untrusted content;
- validate/escape model-generated structured actions before execution;
- explicit confirmation for destructive/high-impact operations;
- constrain reachable resources, not just wording;
- redact/minimize secrets and sensitive data;
- bound iterations, spend, payload size and concurrency;
- audit logs for privileged actions where appropriate;
- tenant/user authorization at the real data/action boundary.

Security review should name residual and not-assessed risks; do not claim prompt wording alone makes an agent safe.
