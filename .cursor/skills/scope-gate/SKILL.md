---
name: scope-gate
description: Classify work into Kaseis pilot, MVP commercial, or later roadmap before implementing. Use when adding features, reviewing requests, or when scope is unclear.
---

# Scope Gate

## Phases

| Phase | Allowed themes |
| ----- | -------------- |
| Pilot | Capture, confirm, ledger, counts, alerts, minimal dashboard, CSV export |
| MVP commercial | Multi-obra, locations, suppliers, partial receipt, assisted OCR, roles, Excel import |
| Later | Request-to-Receive, cost control, P2P, ERP, intelligence |
| Never (now) | Tareo/CAPECO as core, SUNAT emission, native app |

## Process

1. Open `docs/PILOT_SCOPE.md`.
2. Assign phase.
3. If not pilot and user did not explicitly expand scope: stop and propose the smallest pilot-shaped alternative.
4. If pilot: name which ship-gate step it improves.

## Output format

- **Phase:** …
- **Decision:** implement | defer
- **Reason:** …
