from src.app import Application
from src.TrendLocator import TrendLocator
import pandas as pd
import sys, json
import datetime

#future implementation
args = sys.argv[1:]

def main():

    config = json.load(open('config.json'))


    today = datetime.datetime.today()

    # This object is storing top hashtags from the given country 
    trends = TrendLocator(country=config["country"], top_count=config["top_hashtag_count"]).get_trends()

    
    # Place where you can specifiy hashtags or account names to search for
    # max_count - number of tweets to be returned per each hashtag/acc name (to be implemented better)
    ap = Application(max_count=config["tweets_per_hashtag"], hashtags=trends, accounts=['NEXTA', 'YourAnonNews'])


    # Place where you can choose which category you want to download (or you choose both)
    df = ap.id_getter(use_hashtags=config["use_hashtags"], use_accounts=config["use_accounts"])

    
    df = ap.tweets_collector(df)
    df.drop_duplicates('text', inplace=True)



    print("Saving to " + f"/src/data/{str(today.date())}-{str(today.hour)}-tweets.csv" )


    with pd.option_context('display.max_colwidth', 800):
        df.to_csv(f"src/data/{str(today.date())}-{str(today.hour)}-{str(today.minute)}-tweets.csv",columns=df.columns,index=False,encoding="utf-8")





if __name__ == '__main__':
    main()