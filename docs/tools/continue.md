---
title: "Continue \u2014 CLI and IDE"
last_verified: 2026-09-22
tool_version: "CLI rolling docs; v2.0.0-vscode release is an IDE release, not a CLI version"
verification: source-reviewed
status: "OFFICIAL"
sources:
  - "https://docs.continue.dev/cli/quickstart"
  - "https://docs.continue.dev/cli/configuration"
  - "https://docs.continue.dev/customize/model-providers/top-level/ollama"
  - "https://docs.continue.dev/customize/model-providers/top-level/openrouter"
  - "https://docs.continue.dev/ide-extensions/install"
  - "https://github.com/continuedev/continue"
---

# Continue — CLI and IDE

> **OFFICIAL** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** CLI rolling docs; v2.0.0-vscode release is an IDE release, not a CLI version. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What is it?

An Apache-2.0 coding assistant with a terminal command, `cn`, and IDE extensions. [continuedev/continue](https://github.com/continuedev/continue) is upstream. CLI and extension releases are separate; never use an IDE version number as evidence of a tested CLI.

## Best For

Combining editor context with terminal work, teaching configuration files, and using documented provider definitions in a controlled project.

## Cost

**OPEN SOURCE / OPTIONAL PAID PROVIDER.** Continue account offerings and upstream model providers determine usage cost. A local Ollama configuration has hardware costs, while hosted model requests may be billed.

## Requirements

For the npm install path, Node 20+; a supported workstation environment. The default onboarding offers a Continue account or Anthropic key. A local config can select documented providers, but validate your installed CLI's behavior before relying on an entirely offline workflow.

## Supported Platforms

Upstream CLI instructions cover macOS, Linux, and Windows. IDE installations require a supported IDE. Native Android is not established by those instructions; PRoot and browser IDE extension compatibility require separate checks.

## Installation

The official CLI installation page provides native scripts and an npm tab. With supported Node, use:

```bash
npm install -g @continuedev/cli
cn --version
```

Install the IDE extension through the official marketplace link in the upstream IDE guide, not through a similarly named extension.

## Configuration

`cn --config PATH` selects a local YAML configuration; the normal default is `~/.continue/config.yaml`. The CLI configuration page points to the same model schema as the IDE.

The [Ollama example](https://github.com/Rohit-kumar-2674/termwise-atlas/blob/main/configs/continue-ollama.yaml.example) selects a local provider. The [OpenRouter example](https://github.com/Rohit-kumar-2674/termwise-atlas/blob/main/configs/continue-openrouter.yaml.example) references `${{ secrets.OPENROUTER_API_KEY }}` rather than containing a key. Use the documented environment/secret mechanism and check which configuration was loaded. A config parse success is not proof of account-free or offline operation.

## First Command

```bash
cn --readonly
```

Complete the supported authentication flow or choose your reviewed config. Ask for a summary of the repository before permitting writes.

## Example Workflow

Review one function in the IDE, then open the same branch in `cn`. Request a regression test and a scoped patch, keep tool approvals enabled, and run the project's checks. Shared config should describe models and rules; personal credentials stay private.

## Troubleshooting

- Wrong config: pass the intended file through `--config` and inspect `/config`.
- Unknown provider/model: use exact schema keys and model IDs from upstream documentation.
- Local model runs in Ollama but fails in Continue: lower the requested context or choose a smaller model.
- Unexpected cloud login/network activity: verify CLI versus IDE behavior and active config; do not describe the session as offline until observed.
- IDE/browser mismatch on mobile: use the CLI over SSH instead of assuming every desktop extension works in a browser.

## Documentation sources

- [Continue CLI quickstart](https://docs.continue.dev/cli/quickstart)
- [Continue CLI configuration](https://docs.continue.dev/cli/configuration)
- [Continue Ollama integration](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [Continue OpenRouter integration](https://docs.continue.dev/customize/model-providers/top-level/openrouter)
- [Continue IDE installation](https://docs.continue.dev/ide-extensions/install)
- [continue upstream source and license](https://github.com/continuedev/continue)
