#!/usr/bin/env python

import tweepy
from textblob import TextBlob

consumer_key = "0viFHJblJwCwzOYG45FIj7r1l"
consumer_secret = "XXlVrJg6LmWlwK0V23yHzGP6ZkfKha5AX6pphG1TZQq02fO94u"

access_token = "409367607-qbHxmG6vilgB37KGFnGbNhsh1mYq3RvjeOTxssya"
access_token_secret = "aTlQXvjIQBTEh1iumCNdNEMpBGjGhpz5cQ25QyAKiEkrg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
