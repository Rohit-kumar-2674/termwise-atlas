---
title: "Lab 5: build a React learning checklist"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://vite.dev/guide/"
  - "https://nodejs.org/en/download"
  - "https://git-scm.com/docs"
---

# Lab 5: build a React learning checklist

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Install and run the supplied project

Use a current Node LTS compatible with Vite. This example includes an exact package lock. From the repository root:

```bash
cd examples/react-checklist
npm ci
npm test
npm run build
npm run dev -- --host 127.0.0.1
```

Open the URL Vite prints. On a remote cloud container, use its authenticated port-forwarding workflow; phone localhost is not the remote host. Native Android builds may fail because of native dependencies—use [the Android guide](../platforms/android.md) rather than an unreviewed binary replacement.

## Prompt

```text
Inspect this React checklist. Add an All / Remaining view control while keeping
completion state and semantic button/checkbox behavior. Do not add a package.
Keep the pure filtering logic in tasks.js and test observable filtering behavior.
Run npm test and npm run build. Report any check you could not execute.
```

## Verify

Toggle tasks, switch views, and check the progress count and accessible names. Reloading currently resets state; persistence is not part of this task. Test at phone width and with the keyboard. Inspect the lockfile diff: a UI filter should not require unrelated dependency updates.

## Documentation sources

- [Vite getting started](https://vite.dev/guide/)
- [Node.js official downloads](https://nodejs.org/en/download)
- [Git reference](https://git-scm.com/docs)
