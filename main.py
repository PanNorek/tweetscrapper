from src.app import Application
from src.TrendLocator import TrendLocator
import pandas as pd
import sys
import datetime

#future implementation
args = sys.argv[1:]

def main():
    today = datetime.datetime.today()

    # This object is storing top hashtags from the given country 
    trends = TrendLocator(country="Poland", top_count=2).get_trends()

    
    # Place where you can specifiy hashtags or account names to search for
    # max_count - number of tweets to be returned per each hashtag/acc name (to be implemented better)
    ap = Application(max_count=10, hashtags=trends, accounts=['NEXTA', 'YourAnonNews'])


    # Place where you can choose which category you want to download (or you choose both)
    df = ap.id_getter(use_hashtags=True, use_accounts=False)


    df = ap.tweets_collector(df)
    df.drop_duplicates('text', inplace=True)
    print("Saving to " + f"/src/data/{str(today.date())}-{str(today.hour)}-tweets.csv" )
    with pd.option_context('display.max_colwidth', 800):
        df.to_excel(f"src/data/{str(today.date())}-{str(today.hour)}-{str(today.minute)}-tweets.xlsx",columns=df.columns,index=False,encoding="utf-8")





if __name__ == '__main__':
    main()