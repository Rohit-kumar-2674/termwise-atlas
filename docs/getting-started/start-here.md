---
title: "START HERE"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://docs.ollama.com/cli"
  - "https://openrouter.ai/docs/quickstart"
  - "https://antigravity.google/docs/plans"
  - "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
---

# START HERE

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## 1. What device do you have?

You need a place to edit files, a tool to help with code, and a model to answer it. They can run on different machines.

| I have… | Open this guide |
| --- | --- |
| An Android phone | [Android first](../platforms/android.md) |
| A Windows computer | [Windows](../platforms/windows.md), or [Ubuntu inside WSL](../platforms/wsl.md) |
| A Linux computer | [Linux](../platforms/linux.md) |
| A Mac | [macOS](../platforms/macos.md) |
| A Chromebook | [ChromeOS](../platforms/chromeos.md) |
| Only a browser | [Codespaces](../platforms/codespaces.md) or [Cloud Shell](../platforms/cloud-shell.md) |

No command-line experience? Read [terminal basics](terminal-basics.md) first. You can read this entire guide on GitHub without installing anything.

## 2. Where should the AI run?

**On your own computer:** follow [Ollama](../providers/ollama.md). You download a model and your hardware performs the work. Small models can run on CPUs, but may be slow or unreliable at complex edits. Start with [hardware planning](../providers/hardware.md). Downloading a model initially needs internet access.

**On a cloud provider:** choose a tool with an account allowance or use your own API key. The provider processes selected code. “Free tier” means limited access under that provider's rules, not unlimited or permanently free access. Read [costs](costs.md) and [key security](../security/api-keys.md).

**I don't know yet:** use the [interactive setup chooser](choose.md). It asks about the device, local/cloud preference, and memory. It never asks for a key or installs software.

## 3. Pick one route

| Goal | Sensible starting route | What to check |
| --- | --- | --- |
| Learn Git and prompts without spending | Run our Python/HTML labs manually | No AI account needed for the fixtures |
| Local inference | Ollama + Aider | Memory, model quality, local endpoint |
| Provider choice | OpenRouter + Aider or OpenCode | Exact model price, tool support, quota |
| Eligible Google consumer allowance | Antigravity CLI | Current account eligibility and quota |
| Official OpenAI experience | Codex | Account eligibility or API budget; OSS is separate |
| Official Anthropic experience | Claude Code | Eligible paid access; no subscription bypass |

The [compatibility database](comparison.md) explains official versus provider-documented support. Choose one tool initially; ten installed agents are ten things to debug.

## 4. Make your first safe change

1. Complete your platform setup and run the [doctor](diagnostics.md).
2. Read your chosen tool page; verify its version and authentication method.
3. Open the [website lab](../examples/build-a-website.md) or [Python bug lab](../examples/fix-a-bug.md).
4. Create a Git branch. Ask the agent to inspect before editing.
5. Review the diff and run the lab's check. Commit only what you understand.

**Success:** you can explain which files changed, where the model ran, whether it cost money, and how you verified the result. That's a working development workflow.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [Ollama CLI reference](https://docs.ollama.com/cli)
- [OpenRouter quickstart](https://openrouter.ai/docs/quickstart)
- [Antigravity plans](https://antigravity.google/docs/plans)
- [Google consumer CLI transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
