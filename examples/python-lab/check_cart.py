"""Run independent acceptance checks against an explicitly selected lab module."""
import argparse
import importlib.util
from decimal import Decimal
from pathlib import Path


def evaluate(path: Path) -> list[str]:
    spec = importlib.util.spec_from_file_location("learner_cart", path)
    if spec is None or spec.loader is None:
        raise ValueError("Provide a Python module path")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    failures = []
    for value, expected in [("0", "5"), ("49.99", "54.99"), ("50.00", "50.00"), ("51", "51")]:
        actual = module.total(value)
        if actual != Decimal(expected):
            failures.append(f"subtotal={value}: expected {expected}, received {actual}")
    try:
        module.total("-1")
    except ValueError:
        pass
    else:
        failures.append("negative subtotal must raise ValueError")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("module", type=Path)
    args = parser.parse_args()
    failures = evaluate(args.module)
    print("\n".join(failures) if failures else "All 5 cart acceptance checks passed.")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
