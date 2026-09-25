---
title: "Lab 4: refactor while keeping behavior"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.python.org/3/library/venv.html"
  - "https://git-scm.com/docs"
---

# Lab 4: refactor while keeping behavior

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Establish the baseline

Read `summarize_tasks` in `examples/python-lab/text_tools.py` and its tests. Missing `done` means incomplete, truthy `done` means complete, and input records must not be mutated.

```bash
python3 -m unittest discover -s examples/python-lab -p 'test_*.py' -v
```

## Prompt

```text
Refactor summarize_tasks only if it improves readability. Preserve the public
signature, truthiness behavior, missing-key behavior, output fields, and lack
of mutation. Do not add dependencies or change tests to fit an implementation.
Explain the trade-off; keeping the current implementation is acceptable.
```

## Verify

Run the existing checks and review the function with an empty list, missing key, true, false, and other truthy values. Confirm the input list is unchanged. A shorter function is not automatically a better function; refuse a clever rewrite that hides the contract.

## Documentation sources

- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Git reference](https://git-scm.com/docs)
