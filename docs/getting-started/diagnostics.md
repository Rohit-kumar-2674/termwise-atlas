---
title: "Check your environment"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.python.org/3/library/venv.html"
  - "https://git-scm.com/docs"
---

# Check your environment

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Read-only by default

From the repository root:

```bash
python3 scripts/doctor.py
```

Windows uses `py -3 scripts/doctor.py`; Termux can use `python scripts/doctor.py`. Python 3.11+ is required for this project's maintained scripts. The default report checks command availability, OS/architecture, and whether recognized environment variables are nonempty. **It never prints their values, calls a model, reads auth files, or uploads results.** A configured key is not necessarily valid or funded.

For machine-readable output:

```bash
python3 scripts/doctor.py --json
```

To run each installed tool's fixed `--version` command, explicitly opt in:

```bash
python3 scripts/doctor.py --probe-versions
```

Only enable probing in an environment whose installed executables you trust. Presence-only mode does not execute discovered tools. Version probes have timeouts and return a parsed version rather than raw output. The program does not evaluate shell expressions from tool names.

## Interpret the report

Optional programs can be absent; a missing Docker installation is not a failure if you aren't using containers. The report checks Git, Python, Node, npm, pnpm, Docker, Ollama, and the principal agents. “Available” means found on PATH, not integration-tested. Use the selected tool's own authentication status and a small approved task to verify provider access separately.

Check requirements explicitly in automation:

```bash
python3 scripts/doctor.py --require git --require python
```

The exit code becomes nonzero if a required executable is absent. To request setup instructions without installation, use `python3 scripts/wizard.py --platform android --goal cloud --ram 4`.

## Share a useful report

Read even a sanitized report before posting it. Include the failing command with keys removed, the first meaningful error, shell, architecture, tool version, and guide link. Never post `.env`, provider auth files, HTTP authorization headers, or full shell history. See [troubleshooting](../troubleshooting/index.md).

## Documentation sources

- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Git reference](https://git-scm.com/docs)
