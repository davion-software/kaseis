# Architecture overview

## Platforms

| Layer | Where | Role |
| ----- | ----- | ---- |
| Web + API | Railway `web` (Nuxt/Nitro) | Dashboard, Better Auth, Kapso webhook ack |
| Worker | Railway `worker` | Async jobs: Kapso processing, alerts, summaries, exports |
| Database | Railway Postgres | Ledger, catalog, auth, audit |
| Queue / locks | Railway Redis | BullMQ (or equivalent), idempotency keys |
| Evidence | Cloudflare R2 | Private photos/documents, signed URLs |
| Messaging | Kapso | WhatsApp Business Platform |
| Errors | Sentry | Web + worker |
| Source | GitHub | CI and PRs |

## Runtime flow

```text
Kapso webhook
  → Nitro route (verify signature, idempotency, 200)
  → enqueue job
  → worker: conversation / intent → confirmation
  → confirmed → inventory use case → Postgres ledger
  → optional reply via Kapso API
  → optional attachment → R2
```

## App topology (target)

```text
apps/web                 Nuxt UI + Nitro driving adapters
packages/di              composition root
packages/shared          Result, shared utils
packages/modules/*       hexagonal feature modules
```

## Non-goals for day-one infra

- Cloudflare Workers / Durable Objects as primary app host
- Vercel as application platform
- AWS as primary cloud
- Productive OCR pipeline

Details: [hexagonal.md](./hexagonal.md), [ledger.md](./ledger.md), [../decisions/001-railway-cloudflare.md](../decisions/001-railway-cloudflare.md).
