# Verification Gate Checklist

> Shared snippet referenced by: `executing-plans`, `verification-loop`, `verification-before-completion`, `single-flow-task-execution`

Run this gate before marking any phase, step, or task as complete.

## Automated Checks

| Check    | Command                                       | Pass Criteria                  |
| -------- | --------------------------------------------- | ------------------------------ |
| Build    | `rtk proxy bun run build` (or equivalent)     | Exit code 0                    |
| Types    | `rtk tsc` (or `pyright`, `go vet`)            | 0 type errors                  |
| Lint     | `rtk lint` (or `ruff check`, `golangci-lint`) | 0 errors (warnings documented) |
| Tests    | `rtk bun test` (or equivalent)                | All pass, coverage >= 80%      |
| Security | `grep -rn "password\|api_key\|secret" src/`   | 0 hardcoded secrets            |

## Manual Checks

- [ ] Feature works as expected (manual walkthrough)
- [ ] Edge cases handled (empty input, null, 0, max values)
- [ ] Error states are graceful (no raw stack traces to users)
- [ ] No regressions in adjacent systems
- [ ] Changes are intentional (no accidental whitespace or debug edits)

## Decision Matrix

| Build | Types | Lint | Tests | Result                        |
| ----- | ----- | ---- | ----- | ----------------------------- |
| Fail  | -     | -    | -     | **BLOCKED — fix build first** |
| Pass  | Fail  | -    | -     | **BLOCKED — fix types**       |
| Pass  | Pass  | Fail | -     | **BLOCKED — fix lint**        |
| Pass  | Pass  | Pass | Fail  | **BLOCKED — fix tests**       |
| Pass  | Pass  | Pass | Pass  | **READY**                     |

## Rule

Do NOT proceed to the next phase or mark complete until all automated checks pass. Treat warnings as failures in blocking phases unless explicitly documented and accepted.
