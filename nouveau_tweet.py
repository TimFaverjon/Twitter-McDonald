import numpy as np
import tweepy
from tweepy import Stream
import tweepy.api
import requests
import time
import json
from textblob import TextBlob


def is_in_doc(doc,nb):
    with open(doc,"r") as document :
        req = document.readlines()
        for i in range(len(req)):
            if int(req[i]) == nb :
                return True
    return False

def nombre_de_tweet(doc):
    with open(doc,"r") as document :
        req = document.readlines()
    return (len(req)-1)/2 +1

def note_sentiment(doc):
    positif = 0
    negatif = 0
    with open(doc,"r") as document :
        req = document.readlines()
        for i in range(int(len(req)/2)):
            json_text = dic(req[2*i])["text"]
            simple_text = TextBlob(json_text)
            if simple_text.sentiment[0]>=0 :
                positif += simple_text.sentiment[0]
            else :
                negatif += simple_text.sentiment[0]

    return positif, negatif

#Connexion à l'API
consumer_key = "Lvj8ytu4zOTTrbS7KsI8i89T2"
consumer_secret = "UCOwM9mlt2Mljl4zRAPrDT8mPjuZrJQu37hdkcsBEbwX2SJSnt"
access_key="1139588267819618304-d8R3qmYSlPYpASwNLiG0o8reYEOP6l"
access_secret="XcANXc8nhYLGkWH1qK8WJ4tDf9BDFGdWF6Rr3cwkDBoe8"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth)

#ouverture des deux fichiers utiles : celui qui recense les tweets sous format json; celui qui recense les id pour ne pas avoir de doublons
fichier = open("twitt.txt", "a")
id = open("doc_id.txt","a")

#print(note_sentiment("twitt.txt"))
#boucle de recherche avec gestion d'erreur : si trop de requêtes sont effectuées, le programme s'arrête pendant 15 minutes
while True :
    try :
        #Recherche de Tweets
        query = '#metoo'
        max_tweets = 180
        public_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]


        for tweet in public_tweets:
            if tweet.lang == "en" and not is_in_doc("doc_id.txt",tweet.id):
                id.write(str(tweet.id)+"\n")
                simple_text = TextBlob(tweet.text)
                print(simple_text.sentiment)
                json_str = json.dumps(tweet._json)
                fichier.write(json_str)
                fichier.write("\n"+"\n")
        print(nombre_de_tweet("twitt.txt"))

    except tweepy.TweepError as e:
        print(e.reason+"\n"+"\n"+"le nombre de tweet est toujours de" + str(nombre_de_tweet("twitt.txt")))
        time.sleep(900)





