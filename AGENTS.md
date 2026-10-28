# AGENTS.md

Guidance for AI agents working in the Kaseis codebase.

## Project

**Kaseis Obras** is a vertical SaaS for materials control in Latin American construction. Focus: **Inventory Truth**, reliable, reconciliable inventory via WhatsApp (Kapso) + web dashboard (Nuxt).

Detailed rules live in **`.cursor/rules/`** (`.mdc` files). Prefer those over generic framework advice. Product scope: [pilot scope](docs/PILOT_SCOPE.md). Architecture: [technical design](docs/TECHNICAL_DESIGN.md) and `docs/architecture/`.

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

## Current state

Documentation and placeholder directories only. No application code, manifests, migrations, CI, or runnable tests exist. Stack, runtime flows, and package contents below are targets. Do not claim deployment or verified behavior from these docs.

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
GLOSSARY.md                       domain vocabulary
docs/PRODUCT.md                   product purpose and behavior
docs/PILOT_SCOPE.md               pilot limits and targets
docs/TECHNICAL_DESIGN.md          runtime and module design
docs/OPEN_QUESTIONS.md            unresolved policy and suggested defaults
docs/architecture/                hexagonal boundaries and ledger details
docs/adr/                         numbered ADRs (NNNN_TITLE.md)
docs/runbooks/                    Railway, Kapso, Sentry
.cursor/rules/                    agent rules
.cursor/commands/                 slash commands
.cursor/skills/                   project + copied skills
.agents/skills/                   skills installed via npx skills CLI
```

**Pilot modules:** `identity`, `worksites`, `inventory`, `messaging`, `reconciliation`.

## Commands

Cursor command filenames use English UPPER_SNAKE_CASE, so their slash names match the filenames. Earlier lowercase names have been replaced. Outside Cursor, read the corresponding file in `.cursor/commands/` and carry out its checklist.

| Command | Purpose |
| ------- | ------- |
| `/SCOPE` | Pilot vs MVP vs later |
| `/MOVEMENT` | Safe ledger movement type changes |
| `/WHATSAPP_FLOW` | Kapso confirmation flows |
| `/RECONCILE` | Count → difference → adjustment |
| `/ONBOARD_OBRA` | 48h onboarding checklist |
| `/ADR` | New architecture decision |
| `/PR` | GitHub pull request |
| `/SHIP_CHECK` | Pre-merge checklist |

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

Defer OCR productivo, purchases/invoices, tareo/CAPECO, native apps, ERP/SUNAT emission. See `docs/PILOT_SCOPE.md`.

## Before finishing work

When the toolchain exists:

```bash
# placeholder until packages are scaffolded
pnpm check   # or lint + typecheck
pnpm test
```

Until then: follow [.cursor/commands/SHIP_CHECK.md](.cursor/commands/SHIP_CHECK.md), run `python3 scripts/check_docs.py` and `git diff --check`, and inspect staged changes for secrets. Do not run placeholder package commands as if they exist.

## Conventions

- Business rules belong in domain/application; Postgres access belongs only in adapters. Vue components render and call server APIs.
- Only `packages/di` wires concrete adapters for production.
- WhatsApp never writes stock without confirmation use cases.
- Ledger: reverse or compensate; never silent edit.
- Multi-tenant: every query scoped by `organizationId`.
- Evidence: R2 private + signed URLs.
- Minimize scope — match docs and existing patterns; don't over-engineer.

## Documentation conventions

- Keep documentation in English, retaining Spanish field vocabulary where defined in the glossary.
- Use English UPPER_SNAKE_CASE for documentation filenames. Preserve the filenames README.md, AGENTS.md, GLOSSARY.md, and SKILL.md. Leave vendored skill filenames and contents unchanged.
- Maintain one canonical document per subject. Update rules, commands, project-owned skill references, and relative links when moving docs. Leave copied and installed skill bundles untouched.
- Record unresolved questions with their reason and a suggested default in `docs/OPEN_QUESTIONS.md`. A default is not an approved decision.
- Preserve accepted ADR history. New decisions use the next four-digit number under `docs/adr/NNNN_TITLE.md`; mark superseded decisions and link replacements.
- Do not promote a proposed API, schema, deployment, metric definition, or policy to implemented behavior without evidence.

## Docs

Start with:

- [Glossary](GLOSSARY.md)
- [Open questions](docs/OPEN_QUESTIONS.md)
- [Onboarding](docs/runbooks/ONBOARD_OBRA.md)
- [Product](docs/PRODUCT.md)
- [Pilot scope](docs/PILOT_SCOPE.md)
- [Technical design](docs/TECHNICAL_DESIGN.md)
- [Hexagonal architecture](docs/architecture/HEXAGONAL.md)
- [Hosting decision](docs/adr/0001_RAILWAY_AND_CLOUDFLARE.md)
- [Identity decision](docs/adr/0002_BETTER_AUTH.md)
