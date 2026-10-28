# packages/shared

Cross-cutting primitives shared by modules and apps.

## Expected contents

- `domain/result.ts` — `Result<T, E>` for expected failures
- Env validation helpers (Zod at composition boundary)
- Pure utils with no feature rules

Domain entities and feature ports live in `packages/modules/<feature>/domain`, not here.
