from collections.abc import Iterable, Iterator
from .models import Transaction


def filter_transactions(
    transactions: Iterable[Transaction],
    min_amount: float,
) -> Iterator[Transaction]:
    for transaction in transactions:
        if transaction.amount >= min_amount:
            yield transaction


def format_transactions(
    transactions: Iterable[Transaction],
) -> Iterator[str]:
    for transaction in transactions:
        yield f"{transaction.transaction_id} | {transaction.customer} | ${transaction.amount:.2f}"
