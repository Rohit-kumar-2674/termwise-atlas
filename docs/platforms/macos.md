---
title: "macOS: Apple Silicon and Intel"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.brew.sh/Installation"
  - "https://nodejs.org/en/download"
  - "https://docs.ollama.com/macos"
  - "https://code.claude.com/docs/en/setup"
---

# macOS: Apple Silicon and Intel

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Check the machine first

```bash
sw_vers
uname -m
```

`arm64` normally means Apple Silicon; `x86_64` is Intel or a translated shell. Keep your terminal, Homebrew, runtime, and native packages on the same intended architecture. Mixing Rosetta and native ARM packages is a common source of installation failures.

## Install prerequisites

Install Homebrew only using the instructions on [brew.sh](https://brew.sh/) and review the installer before running it. Follow the installer's printed PATH instructions for your actual prefix; do not assume `/usr/local` on Apple Silicon.

```bash
brew --version
brew install git python node@24
```

Homebrew may keep versioned Node keg-only. Follow `brew info node@24` for your shell's PATH, reopen it, and verify:

```bash
git --version
python3 --version
node --version
npm --version
```

Use a supported Node LTS. Never “fix” ownership by recursively changing permissions on system folders. The command-line developer tools may be requested during package installation; follow Apple's dialog.

## Choose a workflow

- **Cloud account:** [Claude Code](../tools/claude-code.md), [Codex](../tools/codex.md), or [Google's current CLI path](../tools/antigravity.md).
- **Your own provider key:** [Aider](../tools/aider.md), [OpenCode](../tools/opencode.md), or [Continue](../tools/continue.md).
- **Local:** [Ollama](../providers/ollama.md), then a compatible agent. Current Ollama requires macOS 14+; Apple Silicon supports GPU inference, while Intel Macs use CPU inference. Check the upstream requirement again before an OS upgrade.

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/Rohit-kumar-2674/termwise-atlas.git
cd termwise-atlas
python3 scripts/doctor.py
```

Follow the chosen tool's guide. Use its official signed installer or documented package, not a mirror containing a similarly named binary.

## Permissions and performance

Grant access to a project folder only when needed. Full Disk Access should not be a routine prerequisite for an AI coding assistant. If macOS blocks an app, verify the publisher and consult the official installation instructions; do not disable Gatekeeper globally.

Apple Silicon uses unified memory shared by the OS, applications, and model. A 16 GB Mac does not have 16 GB of memory available for model weights. Start with a smaller quantized model and modest context, then measure pressure in Activity Monitor. See [hardware planning](../providers/hardware.md).

## Documentation sources

- [Homebrew installation](https://docs.brew.sh/Installation)
- [Node.js official downloads](https://nodejs.org/en/download)
- [Ollama macOS requirements](https://docs.ollama.com/macos)
- [Claude Code installation](https://code.claude.com/docs/en/setup)
