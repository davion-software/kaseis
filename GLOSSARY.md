# Kaseis materials control

These terms describe the materials inventory context. Spanish field terms are kept where they name the same business concept.

## Sites and catalog

**Organization**:
The customer company that owns its obras and their inventory records.

**Project (obra)**:
A construction site belonging to an organization. Use obra for field conversations and project for the equivalent English term.
_Avoid_: Treating project and organization as interchangeable.

**Location**:
A warehouse, work front, or inventory point within an obra. Multiple-location workflows are outside the established pilot scope.

**Material**:
A catalog item with a base unit, packaging, aliases, and minimum stock level.

**Material alias**:
A field or supplier name that identifies a catalog material.

## Inventory

**Inventory Truth**:
The ability to explain a stock balance, its confidence, and its differences from physical quantities.

**Inventory movement**:
A confirmed event that changes registered stock and whose original record remains unchanged.

**Movement line**:
A material, quantity, unit, origin or destination, and any recorded cost within a movement.

**Inventory balance**:
The registered quantity of a material at an inventory point, derived from confirmed movements.

**Initial balance**:
The approved physical quantity that establishes starting inventory.

**Stock receipt (ingreso)**:
A movement that adds material to inventory. Supplier purchasing and partial delivery management are separate workflows.

**Issue (salida)**:
A movement that removes material from inventory for use or consumption.

**Return in**:
Material returned into inventory, such as unused material returned from a work front.

**Return out**:
Material returned out of inventory, such as a return to a supplier.

**Transfer**:
Material moved between inventory points, with a corresponding outgoing and incoming quantity. Its pilot inclusion remains unresolved.

**Adjustment**:
An approved increase or decrease that records a justified correction to stock.

**Reversal**:
A movement that cancels the stock effect of an earlier movement while preserving both records.

**Confirmation (confirmación)**:
The user's explicit acceptance of a proposed WhatsApp movement before it affects stock.

## Physical control and review

**Physical count**:
The quantity of material observed at a location on a recorded date by an identified person.

**Reconciliation**:
The comparison of physical and registered stock, including the difference, its reason, and any linked approved adjustment.

**Confidence state**:
The description of how much trust to place in registered stock: reconciled, estimated, pending, with difference, or uninitialized.

**Receipt**:
A delivery record with supplier, document, and partial quantities, planned for commercial MVP.
_Avoid_: Using receipt without qualification when stock receipt is meant.

**Attachment**:
A photo or document linked as evidence to a business record.

**Alert**:
An exception with a severity, owner, and resolution to review.

**Conversation**:
A field interaction with an active obra context and a pending action, if any.

**Audit event**:
A permanent record of a sensitive action and who performed it.
