# De-Sloppify Checklist

> Shared snippet referenced by: `executing-plans`, `verification-loop`, `plankton-code-quality`

Run this checklist on **every changed file** after each implementation step, before marking the step complete.

```
DE-SLOPPIFY CHECKLIST:
- [ ] Remove console.log / print / debugger / breakpoints
- [ ] Remove TODO comments that were just resolved
- [ ] Remove unused imports
- [ ] Remove dead code paths
- [ ] Ensure consistent formatting (indentation, spacing)
- [ ] Ensure variable names are descriptive (no `x`, `temp`, `foo`)
- [ ] Remove commented-out old code
- [ ] Fix obvious inconsistencies introduced during implementation
```

**Rules:**

- Do NOT change behavior or logic during de-sloppify. If you find a logic bug, fix it as a named separate step.
- Run de-sloppify BEFORE running tests. Tests on messy code fail for the wrong reasons.

**Quick grep check:**

```bash
git diff --name-only HEAD | xargs grep -l "console\.log\|debugger\|TODO\|FIXME\|pdb\.set_trace\|import pdb" 2>/dev/null
```
