---
title: "Lab 6: analyze a repository without edits"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://code.claude.com/docs/en/common-workflows"
---

# Lab 6: analyze a repository without edits

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Use evidence, not guesses

Start in this repository with a clean understanding of `git status`. Open an authenticated agent and give it this bounded prompt:

```text
Read this repository without changing files or running install commands.
Identify its purpose, documentation build, data sources, tests, and security
boundaries. Cite exact file paths for each claim. Name uncertain details.
Suggest one small contribution with an acceptance check. Do not infer that
source-reviewed integrations were tested on every operating system.
```

## Verify

Open each cited file. Confirm that the test commands exist and that the tool correctly distinguishes the static learning site from a model-calling application. Compare its recommendation with the roadmap. Run `git status` to ensure no unintended edits occurred.

This is a useful first task for any new provider: it checks context handling before you authorize a larger change. Never let a model's confidently named nonexistent file become your architecture documentation.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [Claude Code workflows](https://code.claude.com/docs/en/common-workflows)
