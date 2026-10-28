# ADR 0002 — Better Auth

- **Status:** Accepted
- **Date:** 2026-07-13

## Context

Dashboard auth needs sessions for admins/supervisors. Alternatives: Clerk, Better Auth, WorkOS.

Pilot ICP is small Peruvian contractors; SSO/enterprise can wait. Domain must stay decoupled from the auth vendor (hexagonal `identity` module).

## Decision

Use **Better Auth** with email/password and sessions for the pilot.

- Auth tables and session resolution live in `packages/modules/identity`
- Adapter folder: `adapters/better-auth/`
- Application code depends on identity **ports**, not Better Auth types
- Defer social login, WorkOS SSO, and heavy RBAC until MVP commercial

## Consequences

- Lower vendor lock-in and cost vs Clerk for early stage.
- More ownership of schema, cookies, and Nuxt integration.
- WorkOS remains an option later via a new adapter implementing the same ports.

This accepted design predates implementation. See the [technical design](../TECHNICAL_DESIGN.md) for current repository status.
