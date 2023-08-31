import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    res = (round(100 * (delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']].shape[0]) / (delivery.shape[0]), 2))
    return pd.DataFrame({"immediate_percentage": [res]})
