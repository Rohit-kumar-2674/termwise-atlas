---
title: "Eight practical labs"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://aider.chat/docs/usage.html"
  - "https://docs.ollama.com/cli"
  - "https://openrouter.ai/docs/quickstart"
---

# Eight practical labs

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

Each lab starts from a small, inspectable project. None of the repository's tests call a model API. You can complete the exercises manually or ask a configured coding agent for help.

| Lab | You learn | Validation |
| --- | --- | --- |
| [1. Build a website](build-a-website.md) | Scoped HTML/CSS edits and preview | Browser, keyboard, narrow viewport |
| [2. Fix a bug](fix-a-bug.md) | Reproduce a boundary error, make a small fix | Five independent acceptance checks |
| [3. Generate tests](generate-tests.md) | Turn a written contract into meaningful tests | Standard-library unittest |
| [4. Refactor Python](refactor-python.md) | Preserve behavior while improving clarity | Existing tests and diff review |
| [5. Build a React app](react-app.md) | Follow scripts and keep a reproducible lockfile | Node tests and production build |
| [6. Analyze a repository](analyze-repository.md) | Read-only investigation with evidence | Verify cited files and commands |
| [7. Use local Ollama](local-ollama.md) | Connect local inference to a coding client | Endpoint/model check and reviewed output |
| [8. Use OpenRouter](openrouter-agent.md) | Exact model IDs, provider budgets, key handling | Small request and usage check |

Before each lab, use `git status` and a branch. After each, inspect the actual diff. Don't commit your local keys or the ignored `practice/` workspace.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [Aider usage](https://aider.chat/docs/usage.html)
- [Ollama CLI reference](https://docs.ollama.com/cli)
- [OpenRouter quickstart](https://openrouter.ai/docs/quickstart)
