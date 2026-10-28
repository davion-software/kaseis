# ADR 001 — Railway + Cloudflare

- **Status:** Accepted
- **Date:** 2026-07-13

## Context

Kaseis needs a transactional inventory ledger, WhatsApp webhooks (Kapso), async jobs (alerts, summaries), private evidence storage, and a Nuxt dashboard. Early team size is small; pilot is 1–3 design partners.

Candidates considered: Railway, Cloudflare (full stack), Vercel, AWS.

## Decision

- **Primary app platform:** Railway — Nuxt web, worker, Postgres, Redis.
- **Complement:** Cloudflare R2 for evidence objects; optional DNS/CDN later.
- **Not primary:** Vercel (weak fit for long workers + ledger), AWS (ops heavy for pilot), Cloudflare Workers as sole host (Postgres + Nuxt complexity).

## Consequences

- Single mental model for deploy/env for the pilot.
- R2 requires separate Cloudflare credentials and signed URL patterns.
- Conversation state starts in Postgres/Redis on Railway; Workers/DO can be revisited if WhatsApp volume demands edge orchestration.
