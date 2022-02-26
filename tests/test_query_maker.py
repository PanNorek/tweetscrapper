import unittest

# import selected elements, ex.:
from src.query_maker import *

class QueryMakerMethodsTest(unittest.TestCase):
    def test_url_builder_by_account_name(self):

        account_name = 'NEXTA'
        max_results = 10

        instance = QueryMaker(max_results)
        url = instance.url_builder_by_account_name(account_name, max_results)
        self.assertEqual(url, 'https://api.twitter.com/2/tweets/search/recent?query=NEXTA&expansions=author_id&tweet.fields=created_at&max_results=10')
        
    def test_url_builder_by_tweet_id(self):
        tweet_id = '123456789'
        instance = QueryMaker()
        url = instance.url_builder_by_tweet_id(tweet_id)
        self.assertEqual(url, 'https://api.twitter.com/2/tweets/123456789?tweet.fields=created_at,public_metrics,conversation_id&expansions=author_id')
    
    def test_url_builder_by_conversation_id(self):
        conversation_id = '123456789'
        max_results = 10
        instance = QueryMaker(max_results)
        url = instance.url_builder_by_conversation_id(conversation_id, max_results)

        self.assertEqual(url, 'https://api.twitter.com/2/tweets/search/recent?query=conversation_id:123456789&tweet.fields=in_reply_to_user_id,author_id,created_at,conversation_id,public_metrics&max_results=10')

    
    # def test_url_builder_by_tweets_id(self):
    #     tweet_ids = ['123456789', '987654321']
    #     instance = QueryMaker()
    #     urls = instance.url_builder_by_tweets_id(tweet_ids)
    #     self.assertEqual(urls, ['https://api.twitter.com/2/tweets/123456789?tweet.fields=created_at,public_metrics,conversation_id&expansions=author_id', 'https://api.twitter.com/2/tweets/987654321?tweet.fields=created_at,public_metrics,conversation_id&expansions=author_id'])

    def test_set_max_results(self):
        instance = QueryMaker()
        instance.set_max_results(10)
        self.assertEqual(instance.max_results, 10)
    
    def test_set_account_name(self):
        instance = QueryMaker()
        instance.set_account_name('NEXTA')
        self.assertEqual(instance.account_name, 'NEXTA')
    
    def test_set_filters(self):
        instance = QueryMaker()
        instance.set_filters(['wojna', 'Ukrainian'])
        self.assertEqual(instance.filters, ['wojna', 'Ukrainian'])
    
    def test_set_hashtag(self):
        instance = QueryMaker()
        instance.set_hashtag('wojna')
        self.assertEqual(instance.hashtag, 'wojna')
    
