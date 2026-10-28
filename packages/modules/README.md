# packages/modules

Status: placeholder directory. The responsibilities and paths below describe the target design; no implementation exists yet.

Feature modules (vertical slices) using hexagonal layers.

## Pilot modules

| Module | Responsibility |
| ------ | -------------- |
| `identity` | Better Auth, sessions, memberships |
| `worksites` | Organizations, projects (obras), locations |
| `inventory` | Catalog, ledger movements, balances |
| `messaging` | Kapso webhooks, conversation state, confirmations |
| `reconciliation` | Physical counts, differences, adjustments |

## Layout per module

```text
<feature>/
  domain/
    entities/
    errors/
    ports/
  application/
    <use-case>/
  adapters/
    postgres/          # persistence (Railway Postgres + Drizzle)
    better-auth/       # identity only
    kapso/             # messaging only
    r2/                # attachments
    schemas/           # Zod row/DTO shapes
    mappers/
    errors/
  presentation/        # Vue components for apps/web
  index.ts             # public API
```

Persistence adapter folder is **`postgres`**, not `d1` (see [ADR 0001](../../docs/adr/0001_RAILWAY_AND_CLOUDFLARE.md)).

Cross-module rule: depend on another module’s **domain ports** via its public `index.ts`, never on its adapters.
