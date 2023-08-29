import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    ans = (tweets[tweets['content'].astype(str).map(len)>15])
    return ans[['tweet_id']]
