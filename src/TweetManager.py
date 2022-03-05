from src.AuthorizationManager import AuthorizationManager
from src.query_maker import QueryMaker
import requests, time
import pandas as pd
class TweetManager:
    '''Base class for getting tweets'''
    
    def __init__(self)->None:
        self.auth = AuthorizationManager('api_keys.json').get_bearer_header()
        self.query = QueryMaker()
        self.limit = 450
        

class HashTweetManager(TweetManager):
    '''Class for getting tweets by hashtag'''

    def __init__(self,lang, filename='tweets.json')->None:
        super().__init__()
        self.filename = filename
        
        
       
    def get_tweets_dataframe(self,hashtag:str,count:int,only_ids=False) -> pd.DataFrame:
        '''Function that returns a dataframe with tweets from hashtag
            Need update because of api limits.
            Args:
            hashtag (str): hashtag you want to get tweets from.
            count (int): number of tweets you want to get.
            only_ids (bool): if you want to get only ids of tweets.
            Returns:
            df (pd.DataFrame): dataframe with tweets.

            Need future improvements!
        '''
        self.hashtag = hashtag
        self.url = self.query.url_builder_by_hash(self.hashtag,count)
        try:
            
            response = requests.get(self.url, headers=self.auth)
            assert response.status_code == 200
        except:
            print('Error for hashtag {}!' .format(self.hashtag))
            self.url = self.query.url_builder_for_uncommon_tags(self.hashtag,count)
            try:
                response = requests.get(self.url, headers=self.auth)
                print('Error for hashtag {} repared - new request built!'.format(self.hashtag))
                assert response.status_code == 200
            except:
                print('Error confirmed -> {}!' .format(self.hashtag))
                return None
            # time.sleep(15*60)

        # print(response.json())
        # try:
        #     if response.json()['meta']['result_count'] == 0:
        #         return None
        # except:
        #     return None
        try:
            df = pd.json_normalize(response.json()['data'])
        except:
            print('Error for hashtag {}!' .format(self.hashtag))
            return None
        if only_ids:
            df = df[['id']]
        return df

    def get_tweets_to_json(self,hashtag:str,count:int) -> None:
        '''
        Function that returns a json file with tweets from hashtag

        Args:
        hashtag (str): hashtag you want to get tweets from.
        count (int): number of tweets you want to get.
        
        '''
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
    def __init__(self, filename='tweets.json')->None:
        super().__init__()
        self.filename = filename
        
        
    def get_tweets_dataframe(self,account_name:str,count:int,only_ids=False) -> pd.DataFrame:
        '''
        Function that returns a dataframe with tweets from account_name

        Args:
        account_name (str): account name you want to get tweets from.
        count (int): number of tweets you want to get.
        only_ids (bool): if you want to get only ids of tweets.
        '''
        self.account_name = account_name
        self.url = self.query.url_builder_by_account_name(self.account_name,count)
        response = requests.get(self.url, headers=self.auth)
        assert response.status_code == 200
        
        df = pd.json_normalize(response.json()['data'])
        if only_ids:
            df = df[['id']]
        return df


    def get_tweets_to_json(self,account_name:str,count:int) -> None:
        '''
        Function that returns a json file with tweets from account_name
        Args:
        account_name (str): account name you want to get tweets from.
        count (int): number of tweets you want to get.
        '''
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
        '''
        Function that returns a dataframe with tweets from index
        Args:
        index (str): index you want to get tweets from.
        Returns:
        df (pd.DataFrame): dataframe with tweets.
        '''
        self.index = index
        self.url = self.query.url_builder_by_tweet_id(self.index)
        response = requests.get(self.url, headers=self.auth)
        assert response.status_code == 200,'Status code: ' + str(response.status_code)
        
        df = pd.json_normalize(response.json()['data'])
        return df

    def get_tweets_to_json(self,index:str) -> None:
        '''
        Function that returns a json file with tweets from index
        
        Args:
        index (str): index you want to get tweets from.
        '''
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
