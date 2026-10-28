# Hexagonal architecture

Kaseis follows **feature-module hexagonal** layout with dependency injection at a single composition root. Adapted from the RutaSec pattern; persistence adapters live under `postgres/` (Railway Postgres), not Cloudflare D1.

## Dependency flow

```text
Nuxt pages / module presentation/
  → Nitro server routes (driving adapters)
  → use case interfaces + *UseCase
  → domain ports (outbound I/O contracts)
  → adapters (postgres, kapso, better-auth, r2)
  → Zod schemas + mappers
  → Postgres / Kapso / Better Auth / R2
```

Pages and Vue components call the module **public API** or DI-wired use cases — never adapters, Drizzle, or `getDb()` directly.

## Monorepo layout

```text
apps/web/                         # Nuxt 4 + Nuxt UI + Nitro routes
packages/di/                      # composition root (*.module.ts)
packages/shared/                  # Result, shared utils
packages/modules/<feature>/
  domain/
    entities/
    errors/
    ports/
  application/
    <use-case>/                   # interface + *UseCase
  adapters/
    postgres/                     # or better-auth/, kapso/, r2/
    schemas/
    mappers/
    errors/
  presentation/                   # Vue components
  index.ts                        # public exports
```

**Pilot modules:** `identity`, `worksites`, `inventory`, `messaging`, `reconciliation`.

## Nomenclature

| Concept | Name |
| ------- | ---- |
| Outbound domain contract | `InventoryPort` in `domain/ports/` |
| Persistence / external implementation | `PostgresInventoryAdapter`, `KapsoMessagingAdapter` |
| Application contract | `ConfirmIssue`, `RecordPhysicalCount` (no `Port` suffix) |
| Application implementation | `ConfirmIssueUseCase` |
| Row / external DTO | Zod in `adapters/schemas/`, mapped in `adapters/mappers/` |

**Rule:** the `Port` suffix is reserved for **domain** outbound contracts only.

## Composition root (`packages/di`)

- Only `packages/di/*.module.ts` may instantiate db clients, adapters, and use cases for production.
- Nitro handlers and workers resolve wired use cases from DI modules.
- Tests may construct adapters or doubles inline.
- Prefer factory functions over a DI framework for the pilot.

## Layer rules

### Domain

- No Nuxt, Vue, Drizzle, Kapso, Better Auth, `fetch`, Zod, or adapters.
- camelCase entities; `snake_case` stays in schemas.
- Ports describe I/O; entities hold pure rules.

### Application

- One folder per use case.
- I/O-bound use cases depend on **ports**, never concrete adapters.
- Return `Result<T, DomainError>` for expected failures.
- No SQL, HTTP, or Zod.

### Adapters

- Implement ports (`*Adapter`).
- Own all I/O.
- Map infra/validation failures in `adapters/errors/` before returning to use cases.

### Presentation / Nitro

- Thin handlers: unwrap `Result`, map to HTTP, Sentry spans.
- Components render and dispatch; no ledger rules or auth enforcement beyond calling server APIs.

## Cross-module

- Allowed: module A use case → module B **domain port** via public export.
- Forbidden: A → B adapters/schemas/mappers; circular module deps.

## SOLID (pragmatic)

- **S** — one use case per folder; one module per bounded feature
- **O** — extend with new use cases/adapters
- **L** — adapters honor the full port contract
- **I** — small ports, not mega-repositories
- **D** — application depends on ports; adapters depend on domain shapes

## Avoid

- Top-level `domain/` / `application/` outside modules
- Instantiating adapters outside `packages/di` (except tests)
- SQL or Zod in Vue components, domain, or application
- `*Port` on use case names
- Leaking `snake_case` into domain entities
