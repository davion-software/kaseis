# Inventory ledger

The stock figure is never an editable field. Balances are projections of an **immutable movement ledger**.

## Balance equation

```text
balance =
  INITIAL_BALANCE
  + receipts + returns_in + transfers_in
  − issues − returns_out − transfers_out
  ± approved adjustments
```

Balances in `InventoryBalance` must be rebuildable from confirmed movements.

## Confidence states

| State | Meaning | Treatment |
| ----- | ------- | --------- |
| Reconciled | Matches recent count within tolerance | OK for operational decisions |
| Estimated | Derived from movements; count aged | Show last count date; suggest count |
| Pending | Unconfirmed movements or incomplete docs | Surface in alerts |
| With difference | Physical ≠ digital | Motive, review, approval |
| Uninitialized | No approved initial inventory | Do not promise reliable stock |

## Invariants

1. Confirmed lines use a unit convertible to the material base unit.
2. Corrections reference the original event (`REVERSAL` or compensating adjustment). Never silent rewrite.
3. Attachments alone do not confirm a movement.
4. Preserve original WhatsApp text and normalized interpretation.
5. Webhooks and commands are idempotent (same key → same movement).
6. WhatsApp-originated movements require explicit confirmation before affecting stock.
7. Negative stock only with warning, motive, and configured permission.
8. Closed projects reject movements unless reopened.

## Confirmation flow (WhatsApp)

1. Parse intent (rules first, LLM fallback).
2. Resolve material/obra/location; ask if ambiguous.
3. Present structured summary + resulting balance estimate.
4. User: CONFIRMAR / CORREGIR / CANCELAR.
5. On confirm: write ledger + update balance projection + audit.

## Reconciliation flow

1. Select materials for count.
2. Record physical qty, location, user, evidence optional.
3. Compare to registered balance.
4. Classify difference; propose adjustment.
5. Approve per role/threshold.
6. Link count ↔ reconciliation ↔ adjustment; keep history.

See [../product/glossary.md](../product/glossary.md) and `.cursor/rules/inventory-ledger.mdc`.
