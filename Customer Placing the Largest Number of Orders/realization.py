import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order = orders.groupby(['customer_number'])['customer_number'].agg(['count']).reset_index()
    order = order.sort_values(by="count", ascending=False)
    return order[['customer_number']][0:1]
