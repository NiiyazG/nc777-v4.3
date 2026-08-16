# Review Smells — deeper Reviewer heuristics

Use as prompts for doubt, not as mandatory style rules.

## Simplicity
- Can this be materially simpler without hiding complexity elsewhere?
- Is an abstraction introduced before multiple real use cases justify it?
- Did refactoring reduce complexity or merely move it?
- Are names encoding real domain concepts or implementation accidents?

## Architecture
- Did feature-specific branching leak into an unrelated shared control flow?
- Did a shared module absorb logic that belongs to one feature/domain?
- Is dependency direction consistent with ownership and change frequency?
- Is duplication cheaper/safer than the proposed abstraction at this stage?

## Correctness
- Which invariant is assumed rather than enforced?
- Which state transition is impossible in the happy-path story but possible in reality?
- What happens on partial completion, retry, duplicate request or stale data?

## Security
- Does authorization happen at the actual resource/action boundary?
- Is untrusted data reinterpreted in another context (SQL/HTML/shell/path/model/tool)?
- Are secrets/data copied into logs, prompts, URLs or client-visible artifacts?

## Performance
- Does work scale with users/items/requests in an unexpected dimension?
- Is caching masking invalidation/correctness risk?
- Are retries/backpressure bounded?
