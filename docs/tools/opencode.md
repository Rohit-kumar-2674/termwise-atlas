---
title: "OpenCode"
last_verified: 2026-09-22
tool_version: "v1.18.32 release observed"
verification: source-reviewed
status: "OFFICIAL"
sources:
  - "https://opencode.ai/docs/"
  - "https://opencode.ai/docs/providers/"
  - "https://openrouter.ai/docs/cookbook/coding-agents/opencode-integration"
  - "https://github.com/anomalyco/opencode"
---

# OpenCode

> **OFFICIAL** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** v1.18.32 release observed. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What is it?

The MIT-licensed agent from [anomalyco/opencode](https://github.com/anomalyco/opencode), with terminal, desktop, and editor workflows. Use the `opencode-ai` npm package; older or similarly named projects are not necessarily the same tool.

## Best For

Switching documented providers, interactive repository work, and using a local model with an agent interface after verifying tool support.

## Cost

**FREE / OPEN SOURCE** client, **OPTIONAL PAID PROVIDER**. OpenCode's hosted offerings, subscriptions, third-party APIs, and free promotions have their own terms. A built-in provider is not a free allowance.

## Requirements

A compatible terminal and platform binary, Git, and a configured provider. The npm distribution downloads a platform-specific executable. Check architecture and libc when installing on an unusual Linux environment.

## Supported Platforms

Linux and macOS; upstream offers Windows installs and recommends WSL for the fullest experience. Native Android and PRoot remain **COMMUNITY / EXPERIMENTAL**, even where npm completes successfully.

## Installation

Using supported Node/npm on the selected host:

```bash
npm install -g opencode-ai
opencode --version
```

Read the official installation page for platform-specific package managers. Keep your package manager's optional dependencies enabled; the required binary may be delivered that way.

## Configuration

Run `opencode`, use `/connect`, and select OpenRouter for a key-backed provider. Use `/models` to select an exact model; inspect pricing before using it. The interface stores credentials, so treat its auth store as a secret.

For Ollama, use the credential-free [OpenCode example](https://github.com/Rohit-kumar-2674/termwise-atlas/blob/main/configs/opencode-ollama.json.example), choosing a model that your machine can run. Ollama's OpenAI-compatible endpoint ends in `/v1`; its native API base does not. Do not confuse the two.

## First Command

```bash
opencode
```

Select a configured provider/model, then ask: `Map this repository and identify the tests. Ask before edits or shell commands.`

## Example Workflow

Initialize project context only after reviewing the repository. Switch to planning for a small bug, review the plan, permit a focused patch, and run tests. Inspect `git diff --stat` first to catch unexpected bulk rewrites, then read the actual patch.

## Troubleshooting

- No models: verify `/connect` completed and the selected provider has accessible models.
- Authentication does not match shell variables: inspect which configuration source is active; do not share the auth file.
- Ollama tool calls fail: confirm the exact model supports tools and increase context only within memory limits.
- Android native crash: a matching CPU architecture is insufficient if the libc/runtime differs. Use the supported-host route.

## Documentation sources

- [OpenCode installation](https://opencode.ai/docs/)
- [OpenCode providers](https://opencode.ai/docs/providers/)
- [OpenRouter OpenCode integration](https://openrouter.ai/docs/cookbook/coding-agents/opencode-integration)
- [opencode upstream source and license](https://github.com/anomalyco/opencode)
