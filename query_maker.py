import requests


#This class is making query urls to the Twitter API
class QueryMaker:
    base_search_url = 'https://api.twitter.com/2/tweets/search/recent?query='
    conversation_id_search_url = 'https://api.twitter.com/2/tweets/search/recent?query=conversation_id:'
    advanced_search_url = 'https://api.twitter.com/2/tweets/'
    max_results: int
    

    def __init__(self, max_results =10 ) -> None:
        self.max_results = max_results

    def set_account_name(self, account_name: str) -> None:
        self.account_name = account_name

    def set_hashtag(self, hashtag: str) -> None:
        self.hashtag = hashtag

    def set_max_results(self, max_results: int) -> None:
        self.max_results = max_results
    
    def set_filters(self, filters: list) -> None:
        self.filters = filters
    
    def url_builder_by_hash(self,hashtag:str,max_results=10) -> str:
        ''' Function that returns an url to get tweets by hashtag
        request to the Twitter API returns a json file with these tweets attributes:
        created_at, text, author_id, id,
        '''
        self.max_results = max_results
        url = self.base_search_url + '%23' + hashtag + f"&expansions=author_id&tweet.fields=created_at&max_results={max_results}"
        return url
        # url = f'https://api.twitter.com/2/tweets/search/recent?query={hash}wojna&expansions=author_id&tweet.fields=created_at&max_results=10'

    def url_builder_by_account_name(self,account_name:str,max_results=10) -> str:
        ''' Function that returns an url to get tweets by account name
        request to the Twitter API returns a json file with these tweets attributes:
        created_at, text, author_id, id,
        '''
        self.max_results = max_results
        url = self.base_search_url + account_name + f"&expansions=author_id&tweet.fields=created_at&max_results={max_results}"
        return url

    def url_builder_by_tweet_id(self, tweet_id:str) -> str:
        ''' Function that returns an url to get tweet info by tweet id
        request to the Twitter API returns a json file with these tweets attributes:
        - public_metrics(e.g. retweets, likes, replies, quotes, ...)
        - author_id
        - author personalities
        - created_at
        - conversation_id
        '''
        url = self.advanced_search_url + tweet_id + "?tweet.fields=created_at,public_metrics,conversation_id&expansions=author_id"
        return url

    def url_builder_by_conversation_id(self, conversation_id:str,max_results=10) -> str:
        ''' Function that returns an url to get tweets by conversation id
        request to the Twitter API returns a json file with these tweets attributes:
        created_at, text, author_id, id,
        '''
        url = self.conversation_id_search_url + conversation_id + '&tweet.fields=in_reply_to_user_id,author_id,created_at,conversation_id,public_metrics&max_results=' + str(max_results)
        return url

    def url_builder_by_tweets_id(self, tweet_ids:list) -> str:
        ''' Function that returns a list of urls to get tweets info by tweet id
        request to the Twitter API returns a json file with these tweets attributes:


        Will be supported in the future
        '''

        url = self.advanced_search_url + f"id={tweet_ids}&tweet.fields=created_at&expansions=author_id"
        return url
  
