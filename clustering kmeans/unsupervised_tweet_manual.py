import numpy as np
import tweepy
from tweepy import Stream
import tweepy.api
import requests
import time
import json
from textblob import TextBlob
import ast
import matplotlib.pyplot as plt
import pylab
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn import metrics
from sklearn.datasets import fetch_20newsgroups

def inertie(cluster1,cluster2,x):
    iner=0
    shape=x.shape
    for ntweet in range(shape[0]) :
        distance1,distance2=0,0
        for ntoken in range(shape[1]):
            distance1+=(x[ntweet,ntoken]-cluster1[ntoken])**2
            distance2+=(x[ntweet,ntoken]-cluster2[ntoken])**2
        iner+=min(distance1,distance2)
    return(iner)

with open("nouvelle_base.txt","r") as document :
    req = document.readlines()
    textes =[]
    for i in range(0,len(req),2):
        try :
            json_text = json.loads(req[i][:-1])["text"]
            #print(json_text)
            
            textes.append(json_text)
        
        except json.JSONDecodeError as e :
            print("erreur")
print(textes[1])
vectorizer = TfidfVectorizer(stop_words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "did","https","ll","jr","amp"])

X = vectorizer.fit_transform(textes)


true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)
print(X.shape[0])
print(X.shape[1])

cluster1=model.cluster_centers_[0]
cluster2=model.cluster_centers_[1]
inert=inertie(cluster1,cluster2,X)
print("inertie :" )
print(inert)

print("Top terms per cluster:")

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()

for k in range(4):
    print(order_centroids[0][k])

for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :30]:
        print(' %s' % terms[ind]),

print("\n")
print("Prediction")

