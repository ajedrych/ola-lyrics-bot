import tweepy
import os
from dotenv import load_dotenv

load_dotenv()
api = tweepy.Client(bearer_token=os.getenv("BEARER_TOKEN"), consumer_key= os.getenv("CONSUMER_KEY"), consumer_secret=os.getenv("CONSUMER_SECRET"), access_token=os.getenv("ACCESS_TOKEN"), access_token_secret=os.getenv("ACCESS_TOKEN_SECRET") )

def get_tweet(id):
    tweet = api.get_tweet(id, expansions=['author_id'], user_fields=['username'])
    return tweet

#Search recent ten quote tweets or mention - tweet must contain the phrase "olalyricsbot"
def quote_tweets(query, max_results):
    tweets = api.search_recent_tweets(query=query, max_results=max_results)
    results = []
    if not tweets.data is None and len(tweets.data) > 0:
        for tweet in tweets.data:
            twt = get_tweet(tweet['id'])
            obj = {}
            obj['id'] = tweet.id
            obj['username'] = twt.includes['users'][0].username
            obj['text'] = tweet.text
            results.append(obj)
    return results