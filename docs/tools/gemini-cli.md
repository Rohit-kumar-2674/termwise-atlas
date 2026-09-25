---
title: "Gemini CLI"
last_verified: 2026-09-22
tool_version: "v0.60.0 release observed; consumer transition notice takes precedence"
verification: source-reviewed
status: "OFFICIAL \u00b7 CONSUMER ACCESS TRANSITIONED"
sources:
  - "https://geminicli.com/docs/get-started/installation/"
  - "https://geminicli.com/docs/get-started/authentication/"
  - "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
  - "https://geminicli.com/docs/resources/quota-and-pricing/"
  - "https://geminicli.com/docs/reference/commands/"
  - "https://github.com/google-gemini/gemini-cli"
---

# Gemini CLI

> **OFFICIAL · CONSUMER ACCESS TRANSITIONED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** v0.60.0 release observed; consumer transition notice takes precedence. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What is it?

Google's Apache-2.0 terminal agent for working with Gemini models. [Source repository](https://github.com/google-gemini/gemini-cli). It can inspect files, make edits, and invoke shell tools with the configured permission policy.

## Best For

Existing supported enterprise installations and users intentionally using the documented paid Gemini/Vertex API route. For a new individual Google-account workflow, read [Antigravity CLI](antigravity.md) first.

## Cost

**OPEN SOURCE** client; **PAID API REQUIRED / ENTERPRISE ENTITLEMENT** for the retained access paths established by Google's transition announcement. The June 18, 2026 consumer cutoff covers Gemini Code Assist for individuals and Google AI Pro/Ultra access to this CLI.

Some quota pages still describe the former individual free allowance. This guide does not promise that allowance. Gemini API's separate model-specific free tiers are not proof that this particular CLI/authentication combination still accepts them. Verify access in your account before sending work.

## Requirements

Official installation recommends Node 20+, Bash/Zsh/PowerShell, and a supported network location. Use a current Node LTS from its official distribution and a user-writable npm environment. A service may require a project, enabled API, billing, and assigned IAM permissions.

## Supported Platforms

The reviewed installation page lists macOS 15+, Windows 11 24H2+, and Ubuntu 20.04+ recommendations. Linux variants may work without being a separate certification. Native Termux and PRoot are **COMMUNITY / EXPERIMENTAL**. Cloud Shell may already contain `gemini`; check before installing.

## Installation

On Windows PowerShell, Linux Bash, or macOS Terminal after installing supported Node:

```bash
node --version
npm --version
npm install -g @google/gemini-cli
gemini --version
```

The commands themselves are cross-shell; environment-variable syntax is not. Use the platform guide if npm reports a permission error. Do not add `sudo` to an npm global install.

## Configuration

For a supported API-key route, make `GEMINI_API_KEY` available to the process with [secure input](../security/api-keys.md), start `gemini`, and choose the matching authentication method. Vertex and enterprise users should follow their organization's documented project and IAM setup. Authentication proves identity; it does not guarantee quota.

Use `GEMINI.md` for project context and `.geminiignore` to reduce irrelevant context. Ignore files are not a security boundary. Inspect `/help`, `/model`, `/stats`, and the permission prompts in your installed version. This guide establishes no native OpenRouter or Ollama route for Gemini CLI.

## First Command

```bash
gemini
```

Prompt: `Explain the files in this small project. Identify the test command. Do not edit anything.` If consumer sign-in reports migration, follow the migration guide instead of repeatedly reinstalling.

## Example Workflow

On a new branch, ask for one regression test before the fix. Review any shell invocation, run the test, apply a minimal fix, and inspect the diff. Commit only the relevant files. Keep API secrets out of `GEMINI.md` and shell transcripts.

## Troubleshooting

- Consumer login stops serving requests: read the transition notice and move to the supported current product.
- 401: confirm authentication mode and whether the key was revoked; do not print it.
- 403: inspect account, project, API and IAM eligibility. Do not create alternate accounts to evade policy.
- 429: inspect the applicable quota and wait for its reset; repeated retries can worsen it.
- Native module failures on Android: use the [Debian guide](../platforms/android-debian.md) or remote workspace; Linux support is not Android certification.

## Documentation sources

- [Gemini CLI installation](https://geminicli.com/docs/get-started/installation/)
- [Gemini CLI authentication](https://geminicli.com/docs/get-started/authentication/)
- [Google consumer CLI transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- [Gemini CLI quota page (read with transition notice)](https://geminicli.com/docs/resources/quota-and-pricing/)
- [Gemini CLI commands](https://geminicli.com/docs/reference/commands/)
- [gemini-cli upstream source and license](https://github.com/google-gemini/gemini-cli)
