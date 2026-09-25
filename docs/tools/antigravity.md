---
title: "Antigravity CLI and the Gemini migration"
last_verified: 2026-09-22
tool_version: "Rolling install/auth and plans documentation; no binary execution claimed"
verification: source-reviewed
status: "OFFICIAL \u00b7 CURRENT GOOGLE CONSUMER PATH"
sources:
  - "https://antigravity.google/docs/cli/install/"
  - "https://antigravity.google/docs/plans"
  - "https://antigravity.google/docs/cli/gcli-migration"
  - "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
---

# Antigravity CLI and the Gemini migration

> **OFFICIAL · CURRENT GOOGLE CONSUMER PATH** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Rolling install/auth and plans documentation; no binary execution claimed. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What is it?

Google's `agy` terminal experience associated with Antigravity. It is included here because Google's consumer Gemini CLI transition makes it relevant to current beginners. No open-source license for this client is asserted by this guide.

## Best For

Individuals following Google's current terminal offering and existing Gemini CLI users migrating supported settings. Keep the old environment until you have checked the new workflow.

## Cost

**FREE TIER / OPTIONAL PAID USAGE**, subject to account eligibility and current quotas. The plans page describes baseline limits for non-Pro/Ultra accounts and larger paid allowances; it does not promise unlimited agent work. Read overage settings before buying credits. The installation page separately documents a Gemini API-key mode; API pricing is separate from account quota.

## Requirements

A supported desktop operating system, network access, and the appropriate account or API entitlement. The native binary does not require a Node install. Back up personal configuration before approving a migration.

## Supported Platforms

Official installation covers macOS, Linux, and Windows. Remote SSH authentication has a documented flow. Native Android is not listed; use a supported remote host from a phone.

## Installation

### Linux / macOS — Bash

```bash
curl -fsSL https://antigravity.google/cli/install.sh -o agy-install.sh
less agy-install.sh
bash agy-install.sh
```

### Windows PowerShell

```powershell
Invoke-WebRequest https://antigravity.google/cli/install.ps1 -OutFile agy-install.ps1
Get-Content .\agy-install.ps1
```

After reviewing the script, run it according to your organization's PowerShell policy. If policy blocks execution, use the official supported installation alternative; do not weaken a managed policy. Reopen the terminal and inspect `agy --help`.

## Configuration

Start `agy` and use the supported browser or remote-SSH login flow. Keep authorization URLs and returned codes private. Inspect `/permissions` before tool use.

The current installation guide documents `modelProvider: "gemini"` in the user settings plus `GEMINI_API_KEY` in the process environment for BYOK. Merely setting the key is insufficient. The plans page contains broader BYOK limitations that are not fully aligned with the installation page; this hub marks that difference explicitly and treats the detailed install guide as a documented route requiring version-level validation.

No OpenRouter or Ollama integration is established by the sources reviewed here. “Custom Gemini endpoint” does not mean “any OpenAI-compatible API.”

## First Command

```bash
agy
```

Choose a small trusted project and ask it to describe the structure without editing files.

## Example Workflow

Make a branch, compare the old `GEMINI.md` instructions with the migration guide, and approve only the settings you want imported. Test a small explanation task, a single edit, and your test command. Do not migrate every plugin automatically: plugins may run code and access external services.

## Troubleshooting

- `agy` missing: reopen the shell and inspect the installer-reported user binary directory.
- Old Gemini sign-in fails: use this current flow if you are covered by the consumer transition.
- API key ignored: check the provider setting, variable name, and installed-version support.
- Migration output differs: features are not a one-to-one replacement; review the source migration page and keep backups.
- Quota exhausted: inspect `/usage` and the current plan; wait or choose another legitimate workflow.

## Documentation sources

- [Antigravity installation and authentication](https://antigravity.google/docs/cli/install/)
- [Antigravity plans](https://antigravity.google/docs/plans)
- [Antigravity migration](https://antigravity.google/docs/cli/gcli-migration)
- [Google consumer CLI transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
