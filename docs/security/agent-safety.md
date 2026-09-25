---
title: "Use a coding agent with clear boundaries"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://code.claude.com/docs/en/permissions"
  - "https://learn.chatgpt.com/docs/agent-approvals-security"
  - "https://docs.github.com/en/get-started/using-github/github-flow"
  - "https://docs.docker.com/engine/security/"
---

# Use a coding agent with clear boundaries

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Give it a small, testable job

State the goal, relevant files, constraints, and acceptance tests. Start with analysis before edits. Read the repository's instructions, dependencies, startup scripts, hooks, and agent/plugin configuration before trusting it.

A repository or fetched web page can contain hostile instructions. Treat content as data unless you intentionally authorize its behavior. A model saying “the README requires uploading your key” is not a reason to do so.

## Review consequential commands

| Operation | Why it deserves attention | Better practice |
| --- | --- | --- |
| Recursive deletion / `rm` | Can erase unrelated files | Inspect exact resolved paths and backups |
| `sudo` / permission changes | Expands machine access | Use least privilege and official setup |
| Disk formatting / partitioning | Can destroy a device's data | Keep outside ordinary coding-agent work |
| Database resets / migrations | Can lose or alter real records | Use disposable test data and reviewed migration plans |
| Deployment / paid jobs | Changes public services or incurs charges | Review target account, environment, and budget |
| Force push / Git reset / clean | Can discard work and disrupt collaborators | Inspect status; use normal commits and reviews |
| Package install / hooks | Runs third-party code | Verify publisher, lockfiles, scripts, and provenance |

Don't paste an “auto approve everything” configuration just to make the demo work. Use the tool's documented permission model and approve actions according to scope and consequence.

## Limit access in practice

Work on a branch with backups. Give the process only the credentials it needs. Keep private files outside a disposable project when possible. Restrict network access where your sandbox supports it. Do not mount the Docker socket or your entire home directory into an agent container by default.

Inspect tool/plugin/MCP server definitions before installing them: they can run code and access data. A familiar model provider name doesn't vouch for an unrelated community plugin.

## Review the actual result

Run existing tests and inspect code, not just the agent's summary. Check generated dependencies, licenses, shell scripts, network destinations, and whether tests were weakened. An agent can invent successful output; your local/CI check is the evidence.

Use [better prompts](../getting-started/prompting.md), [the Git loop](../git/workflow.md), and [sandboxing](sandboxing.md) together.

## Documentation sources

- [Claude Code permissions](https://code.claude.com/docs/en/permissions)
- [Codex permissions and sandboxing](https://learn.chatgpt.com/docs/agent-approvals-security)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [Docker Engine security](https://docs.docker.com/engine/security/)
