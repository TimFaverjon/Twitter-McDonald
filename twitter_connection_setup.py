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

consumer_key1 = 'qhwNIR7TiN8J9cvDdS7TLmjTc'
consumer_secret1 = 'ycRFm8Tes4ym2fEArDsodDmlLqsJwdXWCbxpvFnsla74ToigHp'
access_key1='1062264629043388416-mBsoGA2Duy4nDrfO5OYlC8goYPlshL'
access_secret1='NXKkNI3eK0gGZCyZic17cDuiCf0JiXxOHDsnr7nq6udfr'
auth1 = tweepy.OAuthHandler(consumer_key1, consumer_secret1)
auth1.set_access_token(access_key1, access_secret1)

def twitter_setup1():
    api=tweepy.API(auth1)
    return(api)

consumer_key2 = '9AbFNUJwmjr0BYQEgYqgVEyOT'
consumer_secret2 = 'tI7DOyZQYJ6Y095jeP04lJow5KDaRlH09NRMrN20d8xlTr8QnR'
access_key2='1062621191830208518-hKy0EqFjrBxOGSv2sEzCELLiCVSdGS'
access_secret2='ZO2oKgh7lLr0h8EXxjRgdkjxdquMrDL9CwlPqtwImrNYT'
auth2 = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
auth2.set_access_token(access_key2, access_secret2)

def twitter_setup2():
    api=tweepy.API(auth2)
    return(api)

consumer_key3 = "VQgoRfkiDJUM8LhATVZiEolOQ"
consumer_secret3 = "4WwEhs58IWJqeLiTWYL9C5xX26xNuw7nM037Mw8czDTAFAZSSW"
auth3 = tweepy.OAuthHandler(consumer_key3, consumer_secret3)

def twitter_setup3():
    api=tweepy.API(auth3)
    return(api)

# confirm account being used for OAuth
#print ("API NAME IS: ", api.me().name)
