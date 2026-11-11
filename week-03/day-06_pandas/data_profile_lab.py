import pandas as pd

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "customer": ["Alice", "Bob", "Alice", None, "Carol"],
    "amount": [120.0, 80.0, 50.0, 40.0, None]
})

customers = pd.DataFrame({
    "customer": ["Alice", "Bob", "Carol"],
    "city": ["Melbourne", "Sydney", "Brisbane"]
})
