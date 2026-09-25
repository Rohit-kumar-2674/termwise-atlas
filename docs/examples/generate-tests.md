---
title: "Lab 3: generate meaningful tests"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.python.org/3/library/venv.html"
  - "https://git-scm.com/docs"
---

# Lab 3: generate meaningful tests

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Read the contract first

`unique_words` in `examples/python-lab/text_tools.py` case-folds whitespace-delimited tokens and preserves first-seen order. Punctuation stays attached; empty input returns an empty list. These are externally visible requirements, not implementation details.

```bash
python3 -m unittest discover -s examples/python-lab -p 'test_*.py' -v
```

On Windows use `py -3`. The supplied tests cover representative baseline behavior, including Unicode case folding.

## Prompt

```text
Read unique_words and its docstring. Propose two additional edge cases that
are not already covered. Explain the expected values from the written contract.
Add focused unittest cases without changing production code or existing tests.
Avoid asserting the internal implementation or repeating the function in a test.
```

## Verify

Run the command again. Inspect whether new tests would catch an actual behavior regression. A test that merely asserts “result is a list” is too weak for a contract about order, case, and punctuation. Do not accept a changed expected value just to turn a failed test green.

## Documentation sources

- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Git reference](https://git-scm.com/docs)
