from collections.abc import Callable

from .models import Transaction


def make_min_amount_filter(
    min_amount: float,
) -> Callable[[Transaction], bool]:
    def filter_func(transaction: Transaction) -> bool:
        return transaction.amount >= min_amount
    
    return filter_func
