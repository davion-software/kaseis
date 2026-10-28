# packages/shared

Status: placeholder directory. The responsibilities and paths below describe the target design; no implementation exists yet.

Cross-cutting primitives shared by modules and apps.

## Expected contents

- `domain/result.ts` — `Result<T, E>` for expected failures
- Env validation helpers (Zod at composition boundary)
- Pure utils with no feature rules

Domain entities and feature ports live in `packages/modules/<feature>/domain`, not here.
