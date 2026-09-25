---
title: "Troubleshooting database"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://docs.python.org/3/library/venv.html"
  - "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository"
---

# Troubleshooting database

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Find the symptom

| Category | Entries |
| --- | --- |
| [Installation](installation.md) | Missing command, npm permissions, managed Python, native builds, Node versions, pnpm, PowerShell, wrong package |
| [Authentication and API](authentication.md) | 401, 403, 429, billing surprises, Gemini migration, environment mismatch, exposed keys |
| [Models and servers](models.md) | Missing model, connection refused, ports, memory, GPU/CUDA, tool calls, context |
| [Platforms and Git](platforms.md) | Termux storage, architecture crashes, browser previews, WSL, macOS, Cloud Shell, merge conflicts |

Every entry follows **SYMPTOM → CAUSE → CHECK → FIX → VERIFY**. A cause is a diagnostic hypothesis, not proof; perform the check before applying the fix.

## Capture a useful report

Include the guide URL, expected result, actual error, OS and shell, architecture, runtime/tool versions, and a minimal reproduction. Run the [doctor](../getting-started/diagnostics.md) for presence checks. A tool that exists on PATH may still have an unsupported provider or model.

Remove keys, auth headers, private URLs, personal paths, and sensitive code before posting. Do not attach entire `.env` or configuration directories. Security issues use the [security policy](https://github.com/Rohit-kumar-2674/termwise-atlas/security/policy), not public issue templates.

If the fix would delete data, disable security, spend money, or change a production service, stop and review its scope. Routine troubleshooting should not require “run everything as root.”

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [GitHub sensitive-data remediation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
