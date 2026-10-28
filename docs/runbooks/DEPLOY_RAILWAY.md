# Runbook — Deploy Railway

Status: planned procedure. App routes, deployment commands, replay tooling, and recovery have not been implemented or verified.

Bootstrap steps for when the Nuxt app exists. Adjust service names to match the Railway project.

## Services (target)

| Service | Start | Needs |
| ------- | ----- | ----- |
| `web` | Nuxt production server | `DATABASE_URL`, auth, Kapso, R2, Sentry, Redis |
| `worker` | Same repo, worker entry | Same + queue consumer |
| Postgres | Railway plugin | — |
| Redis | Railway plugin | — |

## Checklist

1. Link repo / deploy from GitHub main (or Railway CLI).
2. Add Postgres and Redis; copy `DATABASE_URL` and `REDIS_URL` into `web` and `worker`.
3. Set secrets: `BETTER_AUTH_SECRET`, `BETTER_AUTH_URL`, `KAPSO_API_KEY`, `KAPSO_WEBHOOK_SECRET`, R2 keys, `SENTRY_DSN`.
4. Run migrations against Postgres before first traffic.
5. Generate public domain for `web`; point Kapso webhook URL to `https://<domain>/api/...`.
6. Verify health route and Sentry test event.
7. Keep `staging` and `production` environments separate.

## Rollback

Redeploy previous successful deployment in Railway UI; restore DB only from a tested backup procedure.
