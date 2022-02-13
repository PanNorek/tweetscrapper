from AuthorizationManager import AuthorizationManager
from query_maker import QueryMaker
import requests
import pandas as pd
class TweetManager:
    '''Base class for getting tweets'''
    
    def __init__(self):
        self.auth = AuthorizationManager('api_keys.json').get_bearer_header()
        self.query = QueryMaker()
        

class HashTweetManager(TweetManager):
    '''Class for getting tweets by hashtag'''

    def __init__(self, filename='tweets.json'):
        super().__init__()
        self.filename = filename
        
        
    def get_tweets_dataframe(self,hashtag:str,count:int,only_ids=False) -> pd.DataFrame:
        '''Function that returns a dataframe with tweets from hashtag'''
        self.hashtag = hashtag
        self.url = self.query.url_builder_by_hash(self.hashtag,count)
        response = requests.get(self.url, headers=self.auth)
        assert response.status_code == 200
        df = pd.json_normalize(response.json()['data'])
        if only_ids:
            df = df[['id']]
        return df

    def get_tweets_to_json(self,hashtag:str,count:int) -> None:
        '''Function that returns a json file with tweets from hashtag'''
        self.hashtag = hashtag
        self.url = self.query.url_builder_by_hash(self.hashtag,count)
        response = requests.get(self.url, headers=self.auth)
        assert response.status_code == 200
        try:
            with open(self.filename, 'wb') as f:
                f.write(response.content)
            print('Successfully got tweets')
        except:
            print('File already exists')
        
            
class AccountTweetManager(TweetManager):
    '''Class for getting tweets by account'''
    def __init__(self, filename='tweets.json'):
        super().__init__()
        self.filename = filename
        
        
    def get_tweets_dataframe(self,account_name:str,count:int,only_ids=False) -> pd.DataFrame:
        '''Function that returns a dataframe with tweets from account_name'''
        self.account_name = account_name
        self.url = self.query.url_builder_by_account_name(self.account_name,count)
        response = requests.get(self.url, headers=self.auth)
        assert response.status_code == 200
        df = pd.json_normalize(response.json()['data'])
        if only_ids:
            df = df[['id']]
        return df


    def get_tweets_to_json(self,account_name:str,count:int) -> None:
        '''Function that returns a json file with tweets from account_name'''
        self.account_name = account_name
        self.url = self.query.url_builder_by_account_name(self.account_name,count)
        response = requests.get(self.url, headers=self.auth)
        assert response.status_code == 200
        try:
            with open(self.filename, 'wb') as f:
                f.write(response.content)
            print('Successfully got tweets')
        except:
            print('File already exists')
    

class IndexTweetManager(TweetManager):
    '''class to get tweets by index'''
    def __init__(self, filename='tweets.json'):
        super().__init__()
        self.filename = filename
        
        
    def get_tweets_dataframe(self,index:str) -> pd.DataFrame:
        '''Function that returns a dataframe with tweets from index'''
        self.index = index
        self.url = self.query.url_builder_by_tweet_id(self.index)
        response = requests.get(self.url, headers=self.auth)
        assert response.status_code == 200
        df = pd.json_normalize(response.json()['data'])
        return df

    def get_tweets_to_json(self,index:str) -> None:
        '''Function that returns a json file with tweets from index'''
        self.index = index
        self.url = self.query.url_builder_by_tweet_id(self.index)
        response = requests.get(self.url, headers=self.auth)
        assert response.status_code == 200
        try:
            with open(self.filename, 'wb') as f:
                f.write(response.content)
            print('Successfully got tweets')
        except:
            print('File already exists')
