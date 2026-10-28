# Technical design

## Implementation status

All runtime flows below are target behavior. Only documentation and placeholder directories exist. No API contract, database schema, migration, worker entry point, or deployment is implemented here.

[Product](PRODUCT.md) owns user behavior. [Pilot scope](PILOT_SCOPE.md) owns delivery limits. [Open questions](OPEN_QUESTIONS.md) tracks unresolved policies and infrastructure contracts.

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
  → Nitro route (verify signature, durable acceptance, 200)
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

Details: [Hexagonal architecture](architecture/HEXAGONAL.md), [Inventory ledger](architecture/LEDGER.md), [Hosting decision](adr/0001_RAILWAY_AND_CLOUDFLARE.md).

## Module ownership

| Module | Owns |
| ------ | ---- |
| `identity` | Users, sessions, memberships, authorization context |
| `worksites` | Organizations, obras, location context |
| `inventory` | Catalog, immutable movements, rebuildable balances |
| `messaging` | Kapso integration, conversation state, proposed confirmations |
| `reconciliation` | Counts, differences, approval and linked adjustments |

The detailed layer contracts and naming rules live in [hexagonal architecture](architecture/HEXAGONAL.md). `packages/di` alone constructs production clients, adapters, and use cases. Domain and application code contain no SQL, HTTP, or Zod. Browser components call server APIs; they never execute server use cases or adapters directly.

## Stock writes and retry boundaries

[Ledger rules](architecture/LEDGER.md) define business invariants. The persistence implementation must make duplicate detection, movement recording, balance projection updates, and audit consistent. The exact transaction and concurrency protocol is not selected yet.

A valid webhook needs recoverable acceptance before acknowledgement. A crash between accepting an event and scheduling its job must not lose the command. The durable inbox or enqueue strategy, retry limits, and replay tools remain open. Redis keys alone are not a specified permanent uniqueness guarantee.

Confirmation must identify the proposal the user reviewed. The implementation still needs rules for expired proposals and simultaneous changes to stock. Repeated confirmation cannot append another movement. A reply failure after a successful commit cannot undo the stock write or justify a duplicate write.

## Identity and evidence boundaries

Better Auth supplies email/password sessions through the identity adapter. Server use cases require authenticated membership and the appropriate register, approve, or administer permission. Client-supplied organization and project IDs are not proof of access.

Every query and mutation is scoped by `organizationId`, and by `projectId` for obra-specific data. Session and vendor types stay out of other modules' domain contracts. Evidence remains private in R2; validate upload size and type, and authorize short-lived signed URL issuance. Limits, expiry, and retention are unresolved.

Never expose credentials through `NUXT_PUBLIC_*`, logs, or client bundles. Preserve original message text for audit under a retention policy still to be agreed. Sentry captures unexpected infrastructure failures with organization and project context, without unnecessary personal data. Expected domain failures return `Result` values.

## Verification and operations

Domain and application tests use port doubles. Adapter integration tests exercise local Postgres, mappings, constraints, and tenant isolation. Future end-to-end checks cover the product acceptance loop and failed delivery retries. No test framework is installed yet.

The [deployment](runbooks/DEPLOY_RAILWAY.md), [webhook](runbooks/KAPSO_WEBHOOKS.md), and [incident](runbooks/INCIDENT_SENTRY.md) runbooks are preparation guides. Migrations, health routes, backup restoration, recovery objectives, and production credentials are prerequisites still to implement or provision. Do not claim production readiness from these documents.
