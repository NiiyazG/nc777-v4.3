# Saboteur Attack Catalog

Pick attacks that fit the chosen second lens; do not enumerate all categories by ritual.

## Input / representation
null/missing, empty, boundary, oversized, malformed, special characters, encoding/locale/timezone, duplicate/conflicting fields.

## State / sequence
invalid transition, stale state, repeat action, double-click, replay, out-of-order steps, retry after partial completion.

## Concurrency / idempotency
simultaneous updates, duplicate request, lost update, race, retry storm, idempotency-key misuse.

## Dependency / partial failure
timeout, slow dependency, malformed upstream response, partial success, unavailable optional dependency, inconsistent cache/source.

## Authorization / misuse
nonexistent/other-user IDs, horizontal/vertical privilege boundary, direct object access, bypassing UI-only restriction, unexpected actor.

## Resource / limits
large payload/list, expensive query/path, unbounded retry, memory/disk/socket exhaustion, rate-limit edge.

## Recovery / observability
what happens after interruption, restart, rollback, duplicate recovery, missing logs/metrics, misleading success response.

For each attack: define oracle first, then reproduction and evidence.
