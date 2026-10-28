# Kaseis Obras

Kaseis helps Latin American construction teams keep materials inventory that they can explain and reconcile. Field teams record movements through WhatsApp; supervisors review stock, evidence, and differences in a web dashboard.

The first pilot focuses on Inventory Truth: an approved starting count, confirmed movements, stock queries, physical counts, and reconciliation. It targets 1–3 design partners, one obra per pilot, and 20–50 critical materials.

## Repository status

This repository contains product and architecture documentation, agent guidance, installed skills, and placeholder package directories. It has no application code, package manifests, migrations, CI workflow, or runnable tests. Deployment and recovery are not verified here.

The target stack is Nuxt 4 with Nuxt UI and Nitro, Better Auth, Railway web and worker services, Postgres, Redis, Kapso for WhatsApp, Cloudflare R2 for private evidence, and Sentry. These are design choices, not provisioned resources demonstrated by this repository.

## Read the context

- [Product](docs/PRODUCT.md): users, operating loop, responsibilities, and boundaries.
- [Pilot scope](docs/PILOT_SCOPE.md): limits, included work, exclusions, and success targets.
- [Glossary](GLOSSARY.md): domain terms used across product and engineering.
- [Technical design](docs/TECHNICAL_DESIGN.md): runtime, modules, security, and implementation status.
- [Architecture decisions](docs/adr/): accepted hosting and identity decisions.
- [Open questions](docs/OPEN_QUESTIONS.md): unresolved policies and suggested defaults.
- [Runbooks](docs/runbooks/): deployment, webhook recovery, incidents, and assisted onboarding.
- [Agent guidance](AGENTS.md): conventions, rules, and repository commands.

## Repository layout

```text
apps/web/                 Placeholder for Nuxt UI and Nitro routes
packages/di/              Placeholder for production composition root
packages/shared/          Placeholder for shared Result and utilities
packages/modules/         Placeholder for feature modules
docs/                     Product, technical design, ADRs, runbooks
.cursor/                  Rules, commands, project and copied skills
.agents/skills/           Installed third-party skills
```

## Work locally

Read the product, pilot scope, and technical design before scaffolding packages. There is no install, development, build, or test command yet. `pnpm check` and `pnpm test` are intended checks once the toolchain exists.

For documentation changes, run `python3 scripts/check_docs.py` and `git diff --check`. The documentation check covers project Markdown and rule files. Installed and copied skill bundles remain unchanged.

## License

Proprietary. Davion Software.
