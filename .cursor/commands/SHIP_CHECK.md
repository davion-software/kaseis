# Ship check

Pre-merge checklist for Kaseis changes.

## Verify

- [ ] Change fits pilot ship gate (`docs/PILOT_SCOPE.md`) or user explicitly asked for later phase
- [ ] Hexagonal boundaries respected (no SQL/Zod in domain/application/Vue)
- [ ] DI wiring only in `packages/di` for new adapters
- [ ] Ledger: no silent edits; confirmation + idempotency if WhatsApp path
- [ ] Multi-tenant filters present on new queries
- [ ] No secrets committed
- [ ] Types/lint/tests pass when toolchain exists
- [ ] Sentry/logging considered for new server paths
- [ ] Docs/ADR updated if architecture or product scope changed

Report pass/fail per item; fix blockers before claiming done.
