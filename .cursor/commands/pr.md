# Create pull request

Open a GitHub PR for the current branch using `gh`.

## Steps

1. `git status`, `git diff`, `git log` vs main — understand full branch history.
2. Push with `-u` if needed (`required_permissions: ["all"]` / network as required).
3. `gh pr create` with title and body:

```markdown
## Summary
- …

## Test plan
- [ ] …
```

4. Conventional commit style already on commits; do not force-push main.
5. Return the PR URL.
