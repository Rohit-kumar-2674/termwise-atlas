---
title: "The Git + AI development loop"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://docs.github.com/en/get-started/using-github/github-flow"
---

# The Git + AI development loop

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Inspect before changing

Run these commands inside the project, after reading its README and repository instructions:

```bash
git status
git diff
git switch -c learn/small-fix
```

If the working tree contains someone else's changes, stop and understand them. Do not reset or clean the repository to make an agent's job easier. Commit your own checkpoint or make a separate worktree when appropriate.

Prompt: `Inspect this project and its test commands. Explain the likely cause of the issue. Do not edit files yet.` Review the plan. Then authorize one bounded change and name the files or behavior that should stay in scope.

## Make a small change and validate it

Ask the agent to run the project's own tests and report their actual result. Read commands before approving execution. A test failure that already existed is different from a regression; record the baseline when possible.

```bash
git diff --stat
git diff --check
git diff
```

Review new files with `git status` too: an untracked file does not appear in a normal `git diff`. Look for unexpected dependencies, configuration changes, generated files, disabled tests, secret values, network calls, and modifications outside the requested scope.

## Stage deliberately

Example for a single known file you actually changed:

```bash
git add docs/getting-started/start-here.md
git diff --cached
git commit -m "Clarify the beginner setup path"
```

Replace the path and message with your actual change. Avoid reflexively using `git add .` when credentials, exports, or unrelated edits may be present. The staged diff is the exact content that will be committed.

## Publish for review

```bash
git push -u origin learn/small-fix
```

This uploads to the configured remote and requires permission. Verify `git remote -v` does not contain a credential. Open a pull request with the problem, change, checks run, and limitations. Never claim that the model tested something merely because it suggested a command.

If a change is too large to review, split it before committing. Git is a review and recovery tool, not an excuse to run destructive commands freely.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
