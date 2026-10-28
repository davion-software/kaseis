# packages/di

Status: placeholder directory. The responsibilities and paths below describe the target design; no implementation exists yet.

Composition root. Only this package (and tests) may wire concrete adapters to use cases.

## Convention

- One `*.module.ts` per feature module (e.g. `inventory.module.ts`)
- Factories construct: db / clients → adapters → use cases
- Nitro handlers and workers import wired use cases from here
- Prefer factory functions over a DI framework for the pilot

See [docs/architecture/HEXAGONAL.md](../../docs/architecture/HEXAGONAL.md) and `.cursor/rules/architecture.mdc`.
