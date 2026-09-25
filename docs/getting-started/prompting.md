---
title: "Ask for changes you can verify"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://aider.chat/docs/usage.html"
  - "https://code.claude.com/docs/en/common-workflows"
---

# Ask for changes you can verify

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Use a repeatable brief

| Part | What to include |
| --- | --- |
| Context | Language, framework, and what the project does |
| Task | One concrete behavior to add or fix |
| Constraints | Scope, compatibility, budget, data/privacy limits |
| Files | Starting points; let the agent inspect dependencies |
| Expected result | Observable behavior and edge cases |
| Validation | Existing tests/build commands and manual checks |

## Example: a broken React build

```text
Context: This is an existing React project.
Task: Find why the production build fails.
Constraints: Do not redesign the UI or upgrade unrelated dependencies.
Files: Start with package.json, the lockfile, and the first build error.
Expected result: The current application builds with the smallest justified change.
Validation: Run the documented build and existing tests. Report actual results,
changed files, and any checks you could not run. Inspect first; wait before edits.
```

## Example: a local-model exercise

```text
Explain examples/python-lab/cart.py. Do not change files or run commands.
Point out one boundary case to test. Use only the supplied code as evidence.
If you need another file, name it instead of guessing its contents.
```

## Iterate deliberately

If the result is wrong, provide the actual error and a smaller task. Remove keys and private data from logs. Ask for alternatives when a fix introduces a dependency or changes public behavior. Don't reward a huge patch merely because it looks impressive; a small, understandable correction is easier to keep correct.

Models can miss requirements or claim checks they didn't run. Keep the acceptance test independent of the generated implementation, and use [Git review](../git/workflow.md) as your final inspection.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [Aider usage](https://aider.chat/docs/usage.html)
- [Claude Code workflows](https://code.claude.com/docs/en/common-workflows)
