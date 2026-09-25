---
title: "OpenAI Codex CLI"
last_verified: 2026-09-22
tool_version: "rust-v0.155.1 release observed; rolling official documentation"
verification: source-reviewed
status: "OFFICIAL"
sources:
  - "https://developers.openai.com/codex/cli"
  - "https://developers.openai.com/codex/auth"
  - "https://developers.openai.com/codex/config-advanced"
  - "https://learn.chatgpt.com/docs/agent-approvals-security"
  - "https://learn.chatgpt.com/docs/pricing"
  - "https://github.com/openai/codex"
  - "https://openrouter.ai/docs/cookbook/coding-agents/codex-cli"
---

# OpenAI Codex CLI

> **OFFICIAL** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** rust-v0.155.1 release observed; rolling official documentation. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What is it?

The official OpenAI terminal coding agent, published as `@openai/codex` and developed in [openai/codex](https://github.com/openai/codex) under Apache-2.0. Unrelated packages containing “Codex” are not interchangeable. A local CLI can still send its model requests to a cloud service.

## Best For

Repository analysis, reviewed edits, tests, local change review, and controlled terminal automation. The CLI, IDE extension, desktop application, and cloud service have different execution environments.

## Cost

**OPEN SOURCE** software. OpenAI model access uses an eligible ChatGPT account/plan allowance or separately billed API usage; availability and promotional free access can change. Do not assume an API key inherits a ChatGPT subscription. **LOCAL** OSS mode is another documented route with hardware costs and different models.

## Requirements

Git, a supported binary/runtime for your architecture, and access to your chosen provider. For the npm method, use a current Node LTS. Official installers and Homebrew are alternatives. Review project instructions and permission settings before authorizing commands.

## Supported Platforms

Official installation covers macOS, Linux, and native Windows; WSL provides a Linux environment on Windows. Native Termux is not established by the reviewed official platform instructions. Use SSH/browser access to a supported host if an Android native binary is unavailable.

## Installation

With supported Node installed, these commands work in PowerShell or a POSIX shell:

```bash
npm install -g @openai/codex
codex --version
```

macOS Homebrew alternative:

```bash
brew install --cask codex
```

The official page also provides native installers. Choose one method and keep its update mechanism consistent.

## Configuration

Run `codex` in a project and choose the available official sign-in method. `codex login status` checks the active method. API-key users can use the documented stdin login after securely loading `OPENAI_API_KEY`; never put the literal key in the command.

### Bash — API-key login

```bash
printenv OPENAI_API_KEY | codex login --with-api-key
```

### PowerShell — API-key login

```powershell
$env:OPENAI_API_KEY | codex login --with-api-key
```

Review `AGENTS.md`; `/init` can draft it, `/status` shows session state, `/permissions` controls actions, and `/review` helps inspect changes. Available sandbox behavior depends on platform and launch configuration. A “trusted” repository is not permission to deploy or erase files.

### Official local provider mode

After installing Ollama and pulling a suitable model, inspect `codex --help`, then use `codex --oss --local-provider ollama --model MODEL_ID`, replacing `MODEL_ID` with the exact installed tag. Tool use and context must be compatible; a small completion model is not automatically suitable.

OpenRouter documents a custom-provider route. See [routing](../providers/routing.md); this is provider-documented compatibility, not a guarantee of every OpenAI feature.

## First Command

```bash
codex
```

Prompt: `Inspect this repository, describe its entry points and tests, and suggest one small learning task. Do not change files.`

## Example Workflow

Use [the Git loop](../git/workflow.md). Have Codex identify a failing test, make a narrow edit, and run the project's own checks. Review commands as well as code. For scripts, investigate `codex exec --help` and set explicit execution boundaries rather than copying a permissive automation preset.

## Troubleshooting

- Wrong binary: check `codex --version` and the package publisher.
- Login on a remote machine: follow the official remote/device authentication options shown by your version; never send a token through an issue.
- Local-provider connection refused: ensure Ollama is running on the same machine or through the intended SSH tunnel.
- Model metadata warning through a custom provider: verify the current provider configuration and supported protocol, not just the base URL.
- Sandbox failure under PRoot: use a supported remote environment; do not globally disable protections.

## Documentation sources

- [Official Codex CLI](https://developers.openai.com/codex/cli)
- [Codex authentication](https://developers.openai.com/codex/auth)
- [Codex provider configuration and OSS mode](https://developers.openai.com/codex/config-advanced)
- [Codex permissions and sandboxing](https://learn.chatgpt.com/docs/agent-approvals-security)
- [Codex access and pricing](https://learn.chatgpt.com/docs/pricing)
- [codex upstream source and license](https://github.com/openai/codex)
- [OpenRouter-documented Codex integration](https://openrouter.ai/docs/cookbook/coding-agents/codex-cli)
