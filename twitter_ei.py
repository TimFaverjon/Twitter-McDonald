import numpy as np
import tweepy
from tweepy import Stream
import tweepy.api
import requests
import time
import json
from textblob import TextBlob

consumer_key = "Lvj8ytu4zOTTrbS7KsI8i89T2"
consumer_secret = "UCOwM9mlt2Mljl4zRAPrDT8mPjuZrJQu37hdkcsBEbwX2SJSnt"
access_key="1139588267819618304-d8R3qmYSlPYpASwNLiG0o8reYEOP6l"
access_secret="XcANXc8nhYLGkWH1qK8WJ4tDf9BDFGdWF6Rr3cwkDBoe8"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth)

L = []
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        L.append(data)
        print(data)
        return True
    def on_error(self, status):
        print(status)
if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

stream = Stream(auth, l)
stream.filter(track=['macdonald'])
print(a["text"])

#for user in tweepy.Cursor(api.followers, screen_name="blackmirror").pages():
#i = 0
#while i < len(user):
#  print(i)
#  print(user[i].screen_name)
#ids.extend(user)
# i = i+ 1
#
#time.sleep(60)
# confirm account being used for OAuth
print ("API NAME IS: ", api.me().name)
