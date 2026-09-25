---
title: "Windows: choose your terminal"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://nodejs.org/en/download"
  - "https://docs.python.org/3/library/venv.html"
  - "https://code.claude.com/docs/en/setup"
  - "https://developers.openai.com/codex/cli"
  - "https://learn.microsoft.com/en-us/windows/wsl/install"
---

# Windows: choose your terminal

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Choose a route

Windows Terminal is a window that hosts shells; PowerShell, Command Prompt, Git Bash, and WSL are different environments inside it. Install a tool in the environment where the repository lives. **Recommended for Linux-oriented projects: [WSL Ubuntu](wsl.md).** Native Windows is a valid option when the tool documents it.

| Shell | Suitable workflow | Important difference |
| --- | --- | --- |
| PowerShell | Native Claude Code, Codex, Gemini/Antigravity, Node tools | Environment variables use `$env:NAME` |
| Command Prompt | Native binaries and npm commands | Variables use `set NAME=value`; prefer secure prompts for keys |
| Git Bash | Git plus POSIX-style shell commands | It is not Linux; Linux-only binaries do not work |
| WSL Ubuntu | Linux tools, Python virtual environments, Git | Its packages, paths, and home directory are separate |

## Native setup

1. Install [Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/install), [Git for Windows](https://git-scm.com/downloads/win), [Node LTS](https://nodejs.org/en/download), and [Python](https://www.python.org/downloads/windows/) from their official sites. Select x64 or ARM64 for the actual device.
2. Reopen your terminal after installation. Do not keep retrying in a shell with an old PATH.
3. Run these checks in **PowerShell**:

```powershell
git --version
node --version
npm.cmd --version
py -3 --version
Get-Command git,node,python -ErrorAction SilentlyContinue
```

If PowerShell blocks `npm.ps1`, use `npm.cmd`. You do not need to disable machine-wide execution policy. Use a currently supported Node LTS; a tool's minimum supported version is not a recommendation to keep an end-of-life runtime.

## Your first workspace

```powershell
New-Item -ItemType Directory -Force "$HOME\projects" | Out-Null
Set-Location "$HOME\projects"
git clone https://github.com/Rohit-kumar-2674/termwise-atlas.git
Set-Location termwise-atlas
py -3 scripts/doctor.py
```

Choose [Codex](../tools/codex.md), [Claude Code](../tools/claude-code.md), [OpenCode](../tools/opencode.md), or another entry in the [matrix](../getting-started/comparison.md). Follow exactly one install method. Native Claude Code now treats Git Bash as optional, but Git itself remains useful. Its native Windows environment does not offer the same sandbox as supported Linux environments.

For Python tools, use an isolated environment instead of installing into Windows' system Python. Aider's page describes its installer. For local inference, install the [Windows Ollama application](../providers/ollama.md); model memory requirements still apply.

## Command Prompt and Git Bash

In **Command Prompt**, inspect an executable with `where node`; use `cd /d C:\path\to\project` to change drive and folder. In **Git Bash**, use `command -v node`, `pwd`, and `cd ~/projects`. Do not copy PowerShell `$env:` syntax into either shell. See [secure environment variables](../security/api-keys.md) for secret input without a literal key in command history.

## Verify and troubleshoot

Start the CLI with `--version`, then open a disposable Git branch and ask it to summarize the repository without editing. If npm installed successfully but the command is absent, check `npm config get prefix` and your user's PATH. If a native dependency has no ARM64 build, use a documented alternative or remote host; renaming a binary does not change its architecture.

For WSL virtualisation, filesystem performance, and Windows/Linux networking problems, continue to [the dedicated WSL guide](wsl.md).

## Documentation sources

- [Node.js official downloads](https://nodejs.org/en/download)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Claude Code installation](https://code.claude.com/docs/en/setup)
- [Official Codex CLI](https://developers.openai.com/codex/cli)
- [Microsoft WSL installation](https://learn.microsoft.com/en-us/windows/wsl/install)
