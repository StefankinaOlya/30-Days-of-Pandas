import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Select the customers whose 'id' is not present in the orders DataFrame's 'customerId' column.
    df = views[views['author_id'] == views['viewer_id']]

    # Build a DataFrame that only contains the 'name' column and rename it as 'Customers'.
    df = df.rename(columns={'author_id': 'id'}).sort_values(by='id')

    return df[['id']].drop_duplicates()
