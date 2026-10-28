# apps/web

Status: placeholder directory. The responsibilities and paths below describe the target design; no implementation exists yet.

Nuxt 4 application: dashboard UI (Nuxt UI) and Nitro server routes that act as **driving adapters**.

## Responsibilities

- Pages, layouts, and feature UI imported from `packages/modules/*/presentation`
- Nitro routes / server handlers that resolve use cases from `packages/di`
- Better Auth HTTP handler mounting
- Kapso webhook entrypoint (ack fast, enqueue work)

## Must not

- Call Postgres, Kapso, or R2 directly from Vue components
- Contain domain rules or ledger math
- Instantiate adapters outside DI (except tests)

See [docs/architecture/HEXAGONAL.md](../../docs/architecture/HEXAGONAL.md).
