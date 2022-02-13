from app import Application
from TweetManager import *
import requests
# ap = IndexTweetManager()
# df = ap.get_tweets_dataframe('1492650525594042369')
# print(df.head())
id = '1492650525594042369'

url = 'https://api.twitter.com/2/tweets/'+ id + "?tweet.fields=created_at,public_metrics,conversation_id&expansions=author_id"

response = requests.get(url,headers=AuthorizationManager('api_keys.json').get_bearer_header())
print(response.json())
# ap = Application(max_count=20, hashtags=['wojna', 'Putin'], accounts=['krzysztofbosak', 'RobertWinnicki'])
# df = ap.turn_shit_into_gold(use_hashtags=True, use_accounts=True)
# df = ap.turn_gold_into_diamond(df)
# print(df.head(20))