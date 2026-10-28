# Reconcile physical count

Implement or extend count → difference → adjustment → approval.

## Steps

1. Read `docs/architecture/LEDGER.md` reconciliation section.
2. Work in `packages/modules/reconciliation` (+ inventory ports).
3. Never delete prior movements when applying a count.
4. Link PhysicalCount ↔ Reconciliation ↔ Adjustment movement.
5. Respect approval thresholds / roles from identity membership.
6. Tests: within tolerance (no adjustment), outside tolerance (proposed adjustment), unauthorized approve.

Apply skill `inventory-truth`.
