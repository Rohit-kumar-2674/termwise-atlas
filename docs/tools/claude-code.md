---
title: "Claude Code"
last_verified: 2026-09-22
tool_version: "v2.1.280 release observed; rolling official docs"
verification: source-reviewed
status: "OFFICIAL"
sources:
  - "https://code.claude.com/docs/en/setup"
  - "https://code.claude.com/docs/en/authentication"
  - "https://code.claude.com/docs/en/common-workflows"
  - "https://code.claude.com/docs/en/permissions"
  - "https://code.claude.com/docs/en/third-party-integrations"
  - "https://docs.ollama.com/integrations/claude-code"
  - "https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration"
---

# Claude Code

> **OFFICIAL** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** v2.1.280 release observed; rolling official docs. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What is it?

Anthropic's terminal coding assistant can inspect a repository, propose edits, and request shell actions. The official product and a third-party gateway are different support relationships. [Upstream repository](https://github.com/anthropics/claude-code); the software is proprietary, not an MIT/Apache open-source agent.

## Best For

Understanding unfamiliar code, scoped bug fixes, refactors, test generation, and working through reviewed Git changes. Start with an explanation task before permitting writes.

## Cost

**PAID ACCESS** on the official Anthropic route: an eligible Pro, Max, Team, Enterprise, or Console account is required. A free claude.ai account is not sufficient. API billing and subscription allowances are separate. Installing the client does not grant model usage.

Ollama and OpenRouter publish their own compatibility routes. Those do not provide free Anthropic inference or alter Claude Code's software terms.

## Requirements

Use an upstream-listed x64/ARM64 desktop environment, network access for installation and cloud models, and a Git repository. The native installer does not require Node; the current npm route requires Node 22+. Have a backup and know your project's test command.

## Supported Platforms

Official setup covers Windows 10 1809+, macOS 13+, and listed Linux distributions. WSL 2 is a useful Windows route. Native Android is not listed; PRoot is a **COMMUNITY / EXPERIMENTAL** environment. Git Bash is optional on current native Windows; check the shell selected by your installed version. Sandboxing availability differs: native Windows and WSL 1 do not have the same support as WSL 2.

## Installation

Choose one route. Downloading an installer is not the same as reviewing it; read it before execution.

### Linux / WSL / macOS — Bash

```bash
curl -fsSL https://claude.ai/install.sh -o claude-install.sh
less claude-install.sh
bash claude-install.sh
claude --version
```

### Windows PowerShell

```powershell
winget install --id Anthropic.ClaudeCode --exact
```

Reopen the terminal, then run `claude --version`. CMD users can run the same WinGet command from Command Prompt. macOS users who already use Homebrew may instead run `brew install --cask claude-code`. Avoid mixing installation methods.

## Configuration

Run `claude` inside a trusted project and complete the official browser login. For Console usage, supply your own `ANTHROPIC_API_KEY` through the [secure input pattern](../security/api-keys.md); review the account/key confirmation. Normal `.env` files are not automatically loaded.

Inside the session, use `/help`, `/status`, `/model`, and `/permissions` to inspect the active setup. `/init` helps draft `CLAUDE.md`; review it as repository code. Record test commands and boundaries, not passwords. Use smaller tasks when context fills; inspect a session summary before continuing.

### Provider-documented routes

**Ollama-documented compatibility; not an Anthropic local-model support promise:** install both tools, read the [local-only guide](../providers/ollama.md), then run `ollama launch claude`. Select a downloaded, tool-capable local model explicitly; a cloud-tagged model is remote inference. Large context settings can exceed laptop memory.

**OpenRouter-documented gateway; experimental outside the stated compatibility:** see [routing recipes](../providers/routing.md). OpenRouter only guarantees its Claude Code route with Anthropic's first-party provider. Do not assume arbitrary free models work.

## First Command

```bash
claude
```

Then type: `Explain this repository and its test commands. Do not modify files or run installation commands.`

## Example Workflow

Create a branch using the [Git loop](../git/workflow.md). Ask for the cause of one failing test, inspect the proposed plan, and permit only the relevant edits. Run the test yourself, review `git diff`, and commit named files. Ask the agent to report anything it could not validate. Never permit a push merely because the agent suggests one.

## Troubleshooting

- `command not found`: reopen the shell; use `claude doctor` after PATH works.
- Wrong account or provider: check `/status`; resolve stale credentials through the documented logout flow. Do not delete the entire configuration directory as a first step.
- Install returns HTML/403: verify the official download URL and supported location; do not disable certificate checks or bypass access restrictions.
- Local model fails to use tools: verify context and tool support. A successful chat response is not an agent compatibility test.
- Permission prompt surprises you: stop and inspect `/permissions`, repository instructions, and plugins.

## Documentation sources

- [Claude Code installation](https://code.claude.com/docs/en/setup)
- [Claude Code authentication](https://code.claude.com/docs/en/authentication)
- [Claude Code workflows](https://code.claude.com/docs/en/common-workflows)
- [Claude Code permissions](https://code.claude.com/docs/en/permissions)
- [Claude Code deployment and gateways](https://code.claude.com/docs/en/third-party-integrations)
- [Ollama-documented Claude Code integration](https://docs.ollama.com/integrations/claude-code)
- [OpenRouter-documented Claude Code integration](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration)
