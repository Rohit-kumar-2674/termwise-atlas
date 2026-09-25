---
title: "Terminal basics without the mystery"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://docs.python.org/3/library/venv.html"
  - "https://nodejs.org/en/download"
---

# Terminal basics without the mystery

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Five words you need

A **terminal** displays a text session. A **shell** interprets commands. A **directory** is a folder. A **repository** is a project tracked by Git. An **environment variable** is a named setting passed to a process; it is not automatically secret.

Code blocks below contain commands, not the `$` or `>` prompt you might see beside them. Press Enter after a line. Read it first. Paths and file names may be case-sensitive, and spaces usually require quotes.

=== "Linux / macOS / Termux / WSL"

    ```bash
    pwd
    ls
    mkdir -p ~/projects
    cd ~/projects
    ```

=== "PowerShell"

    ```powershell
    Get-Location
    Get-ChildItem
    New-Item -ItemType Directory -Force "$HOME\projects"
    Set-Location "$HOME\projects"
    ```

=== "Command Prompt"

    ```bat
    cd
    dir
    mkdir "%USERPROFILE%\projects"
    cd /d "%USERPROFILE%\projects"
    ```

`cd ..` goes up one directory. `Ctrl+C` asks the running foreground program to stop. A blank password prompt may intentionally show nothing while you type. An error is evidence to investigate, not permission to add `sudo`.

## Check where a program comes from

Use `command -v python3` in a POSIX shell, `Get-Command python` in PowerShell, or `where python` in Command Prompt. Most tools support `--version` and `--help`, but flags are program-specific. Keep an error's first meaningful line and remove secrets before sharing it.

## Understand install commands

`npm` installs JavaScript packages; `pip` installs Python packages; OS package managers install system packages. `-g` in npm means a global package within the selected Node installation. A Python virtual environment isolates package dependencies for a project. Neither is a security sandbox.

A command containing `curl … | sh` downloads code and immediately executes it. Prefer the vendor's verified installation page and inspect the script before execution. Do not paste a command from a screenshot without understanding its source.

## Read a prompt before allowing it

`git status` inspects Git state. `git diff` shows edits. `git commit` records selected changes. `git push` uploads commits. Commands that delete files, change permissions, reset databases, spend money, or deploy services need a deliberate review. Learn the [Git loop](../git/workflow.md) next.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Node.js official downloads](https://nodejs.org/en/download)
