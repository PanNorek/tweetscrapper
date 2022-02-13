from app import Application
from TweetManager import *
import sys

args = sys.argv[1:]

def main():
    ap = Application(max_count=20, hashtags=['wojna', 'Putin'], accounts=['krzysztofbosak', 'RobertWinnicki'])
    df = ap.turn_shit_into_gold(use_hashtags=True, use_accounts=True)
    df = ap.turn_gold_into_diamond(df)
    df.drop_duplicates('text', inplace=True)
    with pd.option_context('display.max_colwidth', 800):
        df.to_csv("data/tweets.csv",columns=df.columns,index=False)





if __name__ == '__main__':
    main()