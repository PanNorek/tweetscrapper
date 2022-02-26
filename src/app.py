from src.TweetManager import *
import pandas as pd

class Application(TweetManager):
    '''Simple class that with some configuration and a big dose of luck you will get requested tweets. (Just kidding)
        Need to improve this class or rebuild it.
    '''
    limit_counter = 450
    max_count: int
    hashtags: list
    accounts: list
    cummulated_df: pd.DataFrame


    def __init__(self, max_count: int, hashtags: list, accounts: list)->None:
        super().__init__()
        self.hash_manager = HashTweetManager()
        self.account_manager = AccountTweetManager()
        self.index_manager = IndexTweetManager()
        self.max_count = max_count
        self.hashtags = hashtags
        self.accounts = accounts

    def id_getter(self,use_hashtags=True,use_accounts=False)->pd.DataFrame:
        """
        Function that returns a dataframe with tweets id from hashtags and accounts.
        Thats important because in this version you request twice for a specified tweet.
        Firstly to get all tweet ids and secondly to get the actual tweets data by id.
        Consider using this function only if you want to get all tweets (Twitter Api Essential Access Restrictions).

        Args:
        use_hashtags (bool): if you want to use hashtags.
        use_accounts (bool): if you want to use accounts.

        Returns:
        df (pd.DataFrame): dataframe with tweets id.
        """
        df = pd.DataFrame()
        if use_hashtags:
            for hashtag in self.hashtags:
                df = pd.concat([df,self.hash_manager.get_tweets_dataframe(hashtag,count = self.max_count,only_ids=True)]).drop_duplicates()
        if use_accounts:
            for account in self.accounts:
                 df = pd.concat([df,self.account_manager.get_tweets_dataframe(account,count = self.max_count,only_ids=True)]).drop_duplicates()
        return df

    def tweets_collector(self,dataframe:pd.DataFrame)->pd.DataFrame:
        """
        Function that returns a dataframe with specified tweets.
        Need future upgrade. It is just a temporary function to show basic actions.
        Args:
        dataframe (pd.DataFrame): dataframe with tweets id.
        Returns:
        df (pd.DataFrame): dataframe with tweets.
         """
        df = pd.DataFrame()
        for index in dataframe['id']:
            print('Downloading tweet with index:  ',index)
            df = pd.concat([df,self.index_manager.get_tweets_dataframe(index)]).drop_duplicates()
        return df
            