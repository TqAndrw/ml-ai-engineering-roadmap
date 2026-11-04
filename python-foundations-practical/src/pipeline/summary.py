from collections.abc import Iterable
from .models import Transaction
from .decorators import timer

@timer
def total_by_customer(
    transactions: Iterable[Transaction],
) -> dict[str, float]:
    totals: dict[str, float] = {}
    for transaction in transactions:
        if transaction.customer not in totals:
            totals[transaction.customer] = 0.0
        
        totals[transaction.customer] += transaction.amount
    return totals


def unique_customers(
    transactions: Iterable[Transaction],
) -> set[str]:
    return {transaction.customer for transaction in transactions}
