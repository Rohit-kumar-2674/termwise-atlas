---
title: "GitHub from clone to pull request"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://docs.github.com/en/get-started/using-github/github-flow"
  - "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository"
---

# GitHub from clone to pull request

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Clone the right repository

For a public project:

```bash
git clone https://github.com/Rohit-kumar-2674/termwise-atlas.git
cd termwise-atlas
git remote -v
```

Cloning does not grant push permission. To contribute, fork the project on GitHub and clone your fork instead, or add your fork as a remote after inspecting its URL. Authenticate using GitHub's documented browser/credential-manager, GitHub CLI, or SSH-key flow. An account password is not a Git-over-HTTPS access token. Never place a token in the URL.

Set commit identity to the name and address you want recorded in Git. GitHub offers a no-reply address in account settings; copy your actual value there if you want that privacy option. Identity configuration is not authentication.

## Branch, commit, push

Follow [the Git loop](workflow.md). Branch names should describe a small task. Commit selected files, push the branch, then open **Compare & pull request** on GitHub. Explain the problem, how the patch changes behavior, and what ran successfully. Include the tested tool version and OS for setup-guide changes.

Check the CI results and review the diff in the browser. Respond to review with small follow-up commits. Don't paste keys into logs or screenshots to prove a provider works.

## Resolve a conflict carefully

With your work saved, fetch and merge the latest base branch:

```bash
git fetch origin
git merge origin/main
```

For fork contributions, the upstream remote may be named `upstream` instead of `origin`; verify before merging. If Git reports conflicts, inspect `git status`, read both versions, and edit the conflict markers into the intended final content. Don't accept “ours” or “theirs” blindly. Stage each resolved file, run checks, review the staged diff, and complete the merge commit.

If you need to stop an in-progress merge, `git merge --abort` is the relevant operation; understand how it interacts with pre-existing work. A force push is not an ordinary conflict fix.

## Ignore files before they become history

`.gitignore` keeps matching untracked files out of routine staging. It does not erase previously committed files and does not prevent an AI process reading them. Use `git check-ignore -v .env` to inspect a rule. This project keeps secrets, local tool state, build output, and environments out of source commits.

If a key was committed, [revoke it first](../security/api-keys.md). A later deletion commit leaves the old value in history. Coordinate any history cleanup using GitHub's current remediation procedure.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [GitHub sensitive-data remediation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
