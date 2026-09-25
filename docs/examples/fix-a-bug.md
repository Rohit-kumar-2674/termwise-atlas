---
title: "Lab 2: fix a boundary bug"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://docs.python.org/3/library/venv.html"
---

# Lab 2: fix a boundary bug

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Reproduce without damaging the reference

Shipping is 5.00 below a subtotal of 50.00, and free **at or above** 50.00. Negative input is invalid. The labelled buggy fixture mishandles exactly 50.00.

From the repository root, prepare a disposable copy (Python makes this command work across shells):

```bash
python3 -c "from pathlib import Path; import shutil; Path('practice').mkdir(exist_ok=True); shutil.copy('examples/python-lab/cart_buggy.py', 'practice/cart.py')"
python3 examples/python-lab/check_cart.py practice/cart.py
```

Windows: use `py -3` instead of `python3`. The initial check **should fail** for the exact threshold. `practice/` is ignored so experiments don't become accidental commits.

## Prompt

```text
The contract is free shipping at or above 50.00; otherwise shipping is 5.00.
Negative amounts must raise ValueError. Inspect practice/cart.py and the
acceptance checker. Fix only the implementation, not the checker. Keep Decimal.
Run the checker and explain why the boundary case failed.
```

## Verify

```bash
python3 examples/python-lab/check_cart.py practice/cart.py
python3 examples/python-lab/check_cart.py examples/python-lab/cart_reference.py
```

Both should pass after the fix. Compare your change with the reference only after you understand the failing condition. To propose a real project fix, edit its tracked implementation and create a PR with a regression test; do not upload the deliberately broken learning fixture as production code.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
