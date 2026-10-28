# Runbook — Sentry incidents

## Setup (when app exists)

- `SENTRY_DSN` on Railway `web` and `worker`
- Instrument Nitro handlers and worker jobs with spans (see `.cursor/rules/sentry.mdc`)
- Tag: `organizationId`, `projectId` when available (never PII beyond need)

## Triage

1. Open issue in Sentry; note release and environment.
2. Correlate with Railway logs for the same timeframe.
3. For Kapso/webhook errors: confirm idempotency and whether stock was affected.
4. If ledger inconsistency suspected: stop related jobs; rebuild balance from movements for the material; audit trail first.

## Severity

| Level | Example | Action |
| ----- | ------- | ------ |
| Sev1 | Confirmed stock write without user confirm / duplicate movements | Page founder; freeze writes if needed |
| Sev2 | Webhook ack failures / worker down | Fix deploy; replay safe idempotent events |
| Sev3 | UI-only errors | Fix in next PR |
