# Scope gate

Classify the current request against Kaseis product phases before implementing.

## Steps

1. Read `docs/product/pilot-scope.md` and `docs/product/thesis.md`.
2. Label the work as one of: **pilot** | **MVP commercial** | **later roadmap** | **out of product**.
3. If not pilot (unless the user explicitly asks for MVP+), refuse scope creep: explain why and what pilot alternative exists.
4. If pilot: list the ship-gate steps it supports and proceed with minimal change.
5. Apply skill `scope-gate` if available.

## Output

- Phase label
- In/out decision
- Next implementation step (or deferral note)
