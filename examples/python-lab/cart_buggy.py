"""Intentional learning fixture: shipping is wrong at the exact threshold."""
from decimal import Decimal


def total(subtotal: str) -> Decimal:
    amount = Decimal(subtotal)
    if amount < 0:
        raise ValueError("Subtotal must be nonnegative")
    shipping = Decimal("0.00") if amount > Decimal("50.00") else Decimal("5.00")
    return amount + shipping
