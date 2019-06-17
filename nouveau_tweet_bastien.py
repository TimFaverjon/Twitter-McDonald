import numpy as np
import tweepy
from tweepy import Stream
import tweepy.api
import requests
import time
import json
from textblob import TextBlob
import ast

import twitter_connection_setup as tcs

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
    nb_positif = 0
    nb_neutre = 0
    nb_negatif = 0
    positif = 0
    negatif = 0
    with open(doc,"r") as document :
        req = document.readlines()
        #print(json.loads(req[0][:-1]))
        print("a")
        for i in range(0,len(req),2):
            try :
                json_text = json.loads(req[i][:-1])["text"]
                print(json_text)
                simple_text = TextBlob(json_text)
                if simple_text.sentiment[0]>0 :
                    positif += simple_text.sentiment[0]
                    nb_positif+=1
                if simple_text.sentiment[0]<0 :
                    negatif += simple_text.sentiment[0]
                    nb_negatif+=1
                if simple_text.sentiment[0] == 0 :
                    nb_neutre += 1

            except json.JSONDecodeError as e :
                print("erreur")

    return positif, negatif, nb_positif, nb_negatif, nb_neutre


#Connexion à l'API
api=tcs.twitter_setup3()

#ouverture des deux fichiers utiles : celui qui recense les tweets sous format json; celui qui recense les id pour ne pas avoir de doublons
fichier = open("twitt.txt", "a")
id = open("doc_id.txt","a")

print(note_sentiment("twitt.txt"))
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




