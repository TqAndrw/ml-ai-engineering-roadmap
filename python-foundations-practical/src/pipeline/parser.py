from .models import Transaction


class TransactionParseError(Exception):
    pass


def parse_transaction(raw: dict) -> Transaction:
    transaction_id = raw.get("transaction_id")
    if not transaction_id:
        raise TransactionParseError("Transaction ID is required")

    customer = raw.get("customer")
    if not customer:
        raise TransactionParseError("Customer is required")

    try:
        amount = float(raw["amount"])
    except KeyError as e:
        raise TransactionParseError("Amount is required") from e
    except (TypeError, ValueError) as e:
        raise TransactionParseError("Amount must be numeric") from e

    return Transaction(
        transaction_id=transaction_id,
        customer=customer,
        amount=amount,
    )