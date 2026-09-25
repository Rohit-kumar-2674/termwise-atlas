---
title: "Lab 1: improve a simple website"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
---

# Lab 1: improve a simple website

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Goal and starting point

Open `examples/website/index.html`. It is a working single-file learning log with a completion button. Your task is to add a short “Tomorrow” section without changing existing completion behavior. No JavaScript framework or API key is needed.

From the repository root:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory examples/website
```

Windows: replace `python3` with `py -3`; Termux: `python`. Open `http://127.0.0.1:8000`. Stop the server with `Ctrl+C`.

## Prompt

```text
Inspect examples/website/index.html. Add a Tomorrow section containing two
editable-in-source learning goals. Preserve the completion button behavior,
semantic HTML, contrast, and narrow-screen layout. Do not add dependencies.
Explain the intended changes before editing.
```

## Validate and review

At 360 px wide, check that text fits without horizontal scrolling. Tab to the button and activate it with the keyboard; its status must change and repeated completion must be prevented. Check the new heading order and text contrast. Use `git diff --check` and review the exact patch. A screenshot helps reviewers assess layout, but does not replace behavior checks.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
