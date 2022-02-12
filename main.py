from AuthorizationManager import AuthorizationManager
from query_maker import QueryMaker
import requests, json

hash = '%23'
space = '%20'
# curl https://api.twitter.com/2/tweets/search/recent?query=cat%20has%3Amedia%20-grumpy&tweet.fields=created_at&max_results=100 -H "Authorization: Bearer $BEARER_TOKEN"
# url ='https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular&max_results=10' #url to get tweets
# &tweet.fields=created_at&expansions=author_id&user.fields=created_at&user.expansions=author_id
# url=f'https://api.twitter.com/2/tweets/search/recent?query=W_Kowal&tweet.fields=created_at&expansions=author_id&max_results=10'
url=f'https://api.twitter.com/2/users?ids=3073691557&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,url,username,verified,withheld&expansions=pinned_tweet_id'
# url = f'https://api.twitter.com/2/tweets/search/recent?query={hash}wojna&expansions=author_id&tweet.fields=created_at&max_results=10'
# filters='&sort_order=relevancy&max_results=100' #filters to get tweets
    
# https://api.twitter.com/2/tweets/search/recent?query=from:TwitterDev&tweet.fields=created_at&expansions=author_id&user.fields=created_at

auth = AuthorizationManager('api_keys.json').get_bearer_token()
q = QueryMaker()
q.set_account_name('W_Kowal')
q.set_max_results(10)
url = q.url_builder_by_account_name('W_Kowal',10)
# url = q.url_builder_by_hash('wojna',10)
r = requests.get(url,headers={'Authorization': 'Bearer ' + auth})
print(r.status_code)
if r.status_code == 200:
    print("Successfully got tweets")
    print(r.json())
    with open('file_name5.json', 'wb') as f:
        f.write(r.content)





# headers = AuthorizationManager('api_keys.json').get_keys()
# with open('api_keys.json','r') as f:
#     keys = json.load(f)
#     r = requests.get(url, headers={'Authorization': 'Bearer ' + keys['Bearer_Token']})
#     print(r.status_code)
#     if r.status_code == 200:
#         print("Successfully got tweets")
#         print(r.json())
#         with open('file_name3.json', 'wb') as f:
#             f.write(r.content)
#qm = QueryMaker(url, keys, filters)
#print(qm.get_query())