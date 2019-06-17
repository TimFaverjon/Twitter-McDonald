import numpy as np
import tweepy
import tweepy.api
import requests

consumer_key = "Lvj8ytu4zOTTrbS7KsI8i89T2"
consumer_secret = "UCOwM9mlt2Mljl4zRAPrDT8mPjuZrJQu37hdkcsBEbwX2SJSnt"
access_key="1139588267819618304-d8R3qmYSlPYpASwNLiG0o8reYEOP6l"
access_secret="XcANXc8nhYLGkWH1qK8WJ4tDf9BDFGdWF6Rr3cwkDBoe8"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

def twitter_setup():
    api=tweepy.API(auth)
    return(api)




# confirm account being used for OAuth
#print ("API NAME IS: ", api.me().name)
