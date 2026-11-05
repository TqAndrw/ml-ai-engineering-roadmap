import numpy as np

sales = np.array([
    [100.0, 120.0],
    [80.0,  90.0],
    [150.0, 200.0],
])

customer_totals = np.sum(sales, axis=1)
month_totals = np.sum(sales, axis=0)