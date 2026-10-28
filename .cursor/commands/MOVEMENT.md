# Add or change a movement type

Safely extend the inventory ledger.

## Steps

1. Confirm scope with `/SCOPE` / `docs/PILOT_SCOPE.md`.
2. Read `docs/architecture/LEDGER.md` and `.cursor/rules/inventory-ledger.mdc`.
3. Update domain entities/ports in `packages/modules/inventory` as needed.
4. Add use case under `application/<use-case>/` returning `Result`.
5. Implement `adapters/postgres` + schemas/mappers; wire in `packages/di`.
6. Ensure confirmation + idempotency for WhatsApp-originated paths.
7. Add unit tests for invariants (no silent edit; reversal; duplicate key).
8. Apply skill `inventory-truth`.

## Do not

- Edit confirmed rows in place
- Write ledger from Vue or raw Kapso handlers without use cases
