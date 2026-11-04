from collections.abc import Callable, Iterable

from .models import Transaction


def process_transactions(
    transactions: Iterable[Transaction],
    callback: Callable[[Transaction], None],
) -> None:
    #loop through each transaction and call the callback function
    for transaction in transactions:
        callback(transaction)

