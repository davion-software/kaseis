# Kaseis

**Kaseis Obras** — materials operating system for Latin American contractors. Field teams register on WhatsApp; the company gets a reconciliable inventory and control dashboard.

> **Repo status:** Cursor agent setup, hexagonal docs, and monorepo skeleton. Nuxt app and Railway provisioning are next.

## Stack

| Layer | Choice |
| ----- | ------ |
| Web | Nuxt 4 + Nuxt UI |
| Auth | Better Auth |
| App host | Railway (`web` + `worker`) |
| Database | Railway Postgres |
| Queue | Railway Redis |
| WhatsApp | Kapso |
| Evidence | Cloudflare R2 |
| Errors | Sentry |
| Source | GitHub |

## Monorepo layout

```text
apps/web/                 Nuxt UI + Nitro (driving adapters)
packages/di/              composition root
packages/shared/          Result, shared utils
packages/modules/         feature modules (hexagonal)
docs/                     product, architecture, ADRs, runbooks
.cursor/                  rules, commands, skills
.agents/skills/           skills installed via `npx skills`
```

Each feature module uses `domain` → `application` → `adapters` → `presentation`. Persistence adapters live under `adapters/postgres/` (not D1). See [docs/architecture/hexagonal.md](docs/architecture/hexagonal.md).

## Pilot focus

Inventory Truth only: movements with confirmation, balances, counts, reconciliation, alerts. Details in [docs/product/pilot-scope.md](docs/product/pilot-scope.md).

## For AI agents

Read [AGENTS.md](./AGENTS.md) first. Project rules are in `.cursor/rules/`. Useful slash commands: `/scope`, `/movement`, `/whatsapp-flow`, `/reconcile`, `/onboard-obra`, `/adr`, `/pr`, `/ship-check`.

## Getting started (agents / docs)

```bash
# Explore docs
open docs/architecture/overview.md

# Cursor skills already vendored under .cursor/skills and .agents/skills
```

Application bootstrap (`pnpm` workspace, `nuxi`, Railway link) will be added in a follow-up.

## License

Proprietary — Davion Software.
