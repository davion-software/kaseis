# Glossary

| Term | Meaning |
| ---- | ------- |
| **Organization** | Customer company; multi-tenant isolation boundary |
| **Project (obra)** | Active construction site under an organization |
| **Location** | Warehouse, front, or inventory point within a project |
| **Material** | Normalized catalog identity (base unit, packaging, aliases, minimum) |
| **MaterialAlias** | Field/supplier terms that resolve to a material |
| **InventoryMovement** | Immutable ledger header for an inventory event |
| **InventoryMovementLine** | Material, qty, unit, origin/destination, cost on a movement |
| **InventoryBalance** | Materialized balance; always rebuildable from confirmed movements |
| **PhysicalCount** | Recorded physical quantity for a material/location/date |
| **Reconciliation** | Difference between digital and physical, with motive and linked adjustment |
| **Receipt** | Delivery registration (supplier, document, partial quantities) — MVP+ |
| **Attachment** | Photo or document in R2 linked to an entity |
| **Alert** | Exception with severity, owner, and resolution |
| **Conversation** | WhatsApp flow state and active obra context (Kapso + messaging module) |
| **AuditEvent** | Immutable record of sensitive actions |
| **Inventory Truth** | Ability to explain a balance, its confidence, and physical differences |
| **Confirmación** | Explicit user confirm before a WhatsApp-originated movement affects stock |
| **Idempotency** | Same webhook/message/document must not create duplicate movements |

## Movement types (pilot+)

`INITIAL_BALANCE`, `RECEIPT`, `ISSUE`, `RETURN_IN`, `RETURN_OUT`, `TRANSFER_OUT`, `TRANSFER_IN`, `ADJUSTMENT_POSITIVE`, `ADJUSTMENT_NEGATIVE`, `REVERSAL`
