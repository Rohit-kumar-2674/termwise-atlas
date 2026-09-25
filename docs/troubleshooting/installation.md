---
title: "Installation troubleshooting"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://nodejs.org/en/download"
  - "https://docs.python.org/3/library/venv.html"
  - "https://git-scm.com/docs"
  - "https://github.com/termux/termux-app"
  - "https://github.com/termux/proot-distro"
  - "https://docs.ollama.com/faq"
  - "https://docs.ollama.com/gpu"
  - "https://openrouter.ai/docs/api/reference/limits"
  - "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
  - "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository"
---

# Installation troubleshooting

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

Find the exact symptom, then check the cause before changing your system. Replace uppercase command placeholders deliberately. Never attach unredacted logs.

## Command not found

**SYMPTOM:** The shell cannot locate the requested executable.

**CAUSE:** Install missing, old PATH, or wrong environment.

**CHECK:** Use `command -v TOOL` in Bash, `Get-Command TOOL` in PowerShell, or `where TOOL` in CMD, replacing TOOL.

**FIX:** Install from the tool page, reopen the shell, and check that the installer’s executable directory is on your user PATH.

**VERIFY:** Run the tool’s documented `--version` command in the same shell.

## npm EACCES / permission denied

**SYMPTOM:** A global npm install cannot write its target directory.

**CAUSE:** Node or the npm prefix belongs to another user.

**CHECK:** Check `npm config get prefix` and whether Node came from a system package or a user-owned installation.

**FIX:** Use a supported user-owned Node installation. Do not run `sudo npm` or recursively change system ownership.

**VERIFY:** Reopen the shell, check Node/npm versions, then retry the official package install.

## Externally managed Python

**SYMPTOM:** pip refuses to modify the system Python.

**CAUSE:** The OS manages that Python environment.

**CHECK:** Check `python3 --version` and which interpreter the command uses.

**FIX:** Create `python3 -m venv .venv` and use its Python explicitly. Install the distro’s venv package if missing.

**VERIFY:** Run `.venv/bin/python -m pip --version`; Windows uses `.\.venv\Scripts\python.exe -m pip --version`.

## Package build failed

**SYMPTOM:** A dependency fails while compiling or has no matching wheel/binary.

**CAUSE:** Unsupported Python/Node major, architecture, libc, or missing compiler.

**CHECK:** Record OS, architecture, runtime versions, and the first meaningful compiler error; redact paths or values as needed.

**FIX:** Use the tool’s supported runtime. Install documented build prerequisites, or move to a supported host when no Android binary exists.

**VERIFY:** Install cleanly and run the package’s documented version check and a small task.

## Unsupported Node engine

**SYMPTOM:** npm reports that the selected package requires another Node version.

**CAUSE:** The installed runtime is outside the package’s supported range.

**CHECK:** Run `node --version` and read the package’s engines/installation requirements.

**FIX:** Install a supported current LTS from an official source. Do not treat `--force` as compatibility.

**VERIFY:** Run `node --version`, reinstall with the intended runtime, and launch the tool.

## pnpm / Corepack not found

**SYMPTOM:** A tutorial assumes a command your Node installation did not provide.

**CAUSE:** Corepack bundling and package-manager installation differ by release.

**CHECK:** Run `node --version`, `npm --version`, and `command -v pnpm` in Bash.

**FIX:** Follow pnpm’s current official installation method; do not assume Corepack is bundled.

**VERIFY:** Run `pnpm --version` and the project’s lockfile-preserving install command.

## PowerShell blocks npm.ps1

**SYMPTOM:** PowerShell refuses to execute the npm wrapper script.

**CAUSE:** Execution policy blocks the `.ps1` shim.

**CHECK:** Check whether `npm.cmd --version` works in the same terminal.

**FIX:** Use `npm.cmd` or the official tool’s native binary. Avoid changing machine-wide execution policy for this issue.

**VERIFY:** Run the intended npm command using `npm.cmd` and verify the installed tool.

## A similarly named program launches

**SYMPTOM:** The executable has unexpected help text or behavior.

**CAUSE:** An unrelated package or earlier PATH entry shadows the intended tool.

**CHECK:** Inspect its version and command location; compare the package publisher and repository with the tool page.

**FIX:** Remove only the identified incorrect package using its package manager, then install the official package.

**VERIFY:** Check the publisher, executable path, and version before authenticating.

## Documentation sources

- [Node.js official downloads](https://nodejs.org/en/download)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Git reference](https://git-scm.com/docs)
- [Termux installation and limitations](https://github.com/termux/termux-app)
- [PRoot-Distro upstream manual](https://github.com/termux/proot-distro)
- [Ollama FAQ and local-only configuration](https://docs.ollama.com/faq)
- [Ollama GPU support](https://docs.ollama.com/gpu)
- [OpenRouter rate limits](https://openrouter.ai/docs/api/reference/limits)
- [Google consumer CLI transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- [GitHub sensitive-data remediation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
