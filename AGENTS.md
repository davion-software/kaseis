# AGENTS.md

Guidance for AI agents working in the Kaseis codebase.

## Project

**Kaseis Obras** is a vertical SaaS for materials control in Latin American construction. Wedge: **Inventory Truth** — reliable, reconciliable inventory via WhatsApp (Kapso) + web dashboard (Nuxt).

Detailed rules live in **`.cursor/rules/`** (`.mdc` files). Prefer those over generic framework advice. Product scope: `docs/product/`. Architecture: `docs/architecture/`.

| Rule file | When it applies |
| --------- | --------------- |
| `kaseis-core.mdc` | Always — stack, pilot ship gate, boundaries |
| `architecture.mdc` | `apps/**`, `packages/**` — hexagonal, DI, SOLID |
| `inventory-ledger.mdc` | Inventory / reconciliation — immutable ledger |
| `kapso-whatsapp.mdc` | Messaging / webhooks — confirm before stock |
| `nuxt-ui.mdc` | Vue/Nuxt UI — Nuxt UI, thin presentation |
| `better-auth.mdc` | Identity — sessions, Better Auth adapter |
| `security.mdc` | Always — multi-tenant, R2, secrets |
| `sentry.mdc` | Server/adapters — instrumentation |
| `github.mdc` | Always — conventional commits, PRs |
| `testing.mdc` | Always — layer test boundaries |

## Stack

Nuxt 4 · Nuxt UI · Better Auth · Railway (web, worker, Postgres, Redis) · Kapso · Cloudflare R2 · Sentry · GitHub

Do not introduce Clerk, WorkOS, Vercel-as-app-host, AWS-as-primary, Astro, Next.js, or Cloudflare Workers as the primary app host unless explicitly requested. Persistence adapters are named **`postgres`**, not `d1`.

## Key paths

```
apps/web/                         Nuxt app (UI + Nitro driving adapters)
packages/di/                      composition root (*.module.ts)
packages/shared/                  Result, shared utils
packages/modules/<feature>/       hexagonal modules
  domain/{entities,errors,ports}
  application/<use-case>/
  adapters/{postgres,better-auth,kapso,r2,schemas,mappers,errors}
  presentation/
docs/product/                     thesis, pilot scope, glossary
docs/architecture/                overview, hexagonal, ledger
docs/decisions/                   ADRs
docs/runbooks/                    Railway, Kapso, Sentry
.cursor/rules/                    agent rules
.cursor/commands/                 slash commands
.cursor/skills/                   project + copied skills
.agents/skills/                   skills installed via npx skills CLI
```

**Pilot modules:** `identity`, `worksites`, `inventory`, `messaging`, `reconciliation`.

## Commands

| Command | Purpose |
| ------- | ------- |
| `/scope` | Pilot vs MVP vs later |
| `/movement` | Safe ledger movement type changes |
| `/whatsapp-flow` | Kapso confirmation flows |
| `/reconcile` | Count → difference → adjustment |
| `/onboard-obra` | 48h onboarding checklist |
| `/adr` | New architecture decision |
| `/pr` | GitHub pull request |
| `/ship-check` | Pre-merge checklist |

## Skills (priority)

Project-owned: `inventory-truth`, `scope-gate`, `obra-onboarding`, `kapso-kaseis`.

Also in repo: `typescript-best-practices`, `unslop`, `use-railway`, `workers-best-practices`, `kapso-ai`, plus `.agents/skills/` installs (Nuxt UI, Nuxt/Vue, Kapso, Cloudflare/R2/wrangler, xlsx/docx, Sentry).

## Pilot ship gate

A change belongs in the pilot if it supports this loop:

1. Configure obra + critical catalog  
2. Approved initial inventory  
3. WhatsApp ingreso/salida with confirmation  
4. Stock query  
5. Physical count + reconciliation  
6. Dashboard alerts / differences  

Defer OCR productivo, purchases/invoices, tareo/CAPECO, native apps, ERP/SUNAT emission. See `docs/product/pilot-scope.md`.

## Before finishing work

When the toolchain exists:

```bash
# placeholder until packages are scaffolded
pnpm check   # or lint + typecheck
pnpm test
```

Until then: run `/ship-check`, ensure hexagonal boundaries, and do not commit secrets.

## Conventions

- Business logic and Postgres access in use cases / adapters — not Vue components.
- Only `packages/di` wires concrete adapters for production.
- WhatsApp never writes stock without confirmation use cases.
- Ledger: reverse or compensate; never silent edit.
- Multi-tenant: every query scoped by `organizationId`.
- Evidence: R2 private + signed URLs.
- Minimize scope — match docs and existing patterns; don't over-engineer.

## Docs

Start with:

- `docs/product/thesis.md`
- `docs/product/pilot-scope.md`
- `docs/architecture/overview.md`
- `docs/architecture/hexagonal.md`
- `docs/decisions/001-railway-cloudflare.md`
- `docs/decisions/002-auth-better-auth.md`
