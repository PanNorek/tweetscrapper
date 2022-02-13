from TweetManager import *
import pandas as pd

class Application(TweetManager):
    max_count: int
    hashtags: list
    accounts: list
    cummulated_df: pd.DataFrame


    def __init__(self, max_count: int, hashtags: list, accounts: list):
        super().__init__()
        self.hash_manager = HashTweetManager()
        self.account_manager = AccountTweetManager()
        self.index_manager = IndexTweetManager()
        self.max_count = max_count
        self.hashtags = hashtags
        self.accounts = accounts

    def turn_shit_into_gold(self,use_hashtags=True,use_accounts=False):
        df = pd.DataFrame()
        if use_hashtags:
            for hashtag in self.hashtags:
                df = pd.concat([df,self.hash_manager.get_tweets_dataframe(hashtag,count = self.max_count,only_ids=True)]).drop_duplicates()
        if use_accounts:
            for account in self.accounts:
                 df = pd.concat([df,self.account_manager.get_tweets_dataframe(account,count = self.max_count,only_ids=True)]).drop_duplicates()
        return df

    def turn_gold_into_diamond(self,dataframe:pd.DataFrame):
        df = pd.DataFrame()
        for index in dataframe['id']:
            print('Downloading tweet with index:  ',index)
            df = pd.concat([df,self.index_manager.get_tweets_dataframe(index)]).drop_duplicates()
        return df
            