import requests as req
import mail
import scrapper
import text2voice
import voice2text
from bs4 import BeautifulSoup 
from flask import Flask, request
from flask_restful import Resource, Api
import json
from flask import jsonify
import os
import numpy as np
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import re
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/summarize/<topic>": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)
api = Api(app)
'''
@app.route("/<topic>")
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get(topic):
    r=req.get("https://everything2.com/?node="+topic)
    soup = BeautifulSoup(r.content, 'html5lib')
    data = soup.find_all("div",attrs={"class":"content"})

    feed = ""
    for i in data:
        feed=feed+i.text
    return feed
'''

@app.route("/summarize/<topic>")
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get(topic):
    r=req.get("https://everything2.com/?node="+topic)
    soup = BeautifulSoup(r.content, 'html5lib')
    data = soup.find_all("div",attrs={"class":"content"})

    feed = ""
    for i in data:
        feed=feed+i.text
    allOf=feed
    sentes=[]    
    sentes.append(sent_tokenize(allOf))
    sentese = [y for x in sentes for y in x]
    WE = {}
    f = open('glove.6B.100d.txt', encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        WE[word] = coefs
    f.close()
    clean_sentese = pd.Series(sentese).str.replace("[^a-zA-Z]", " ")
    clean_sentese = [s.lower() for s in clean_sentese]
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    def remove_stopwords(sen):
        sen_new = " ".join([i for i in sen if i not in stop_words])
        return sen_new
    clean_sentese = [remove_stopwords(r.split()) for r in clean_sentese]
    sentence_vectors = []
    for i in clean_sentese:
        if len(i) != 0:
            v = sum([WE.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
        else:
            v = np.zeros((100,))
        sentence_vectors.append(v)
    sim_mat = np.zeros([len(sentese), len(sentese)])
    for i in range(len(sentese)):
        for j in range(len(sentese)):
            if i != j:
                sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]

    import networkx as nx

    nx_graph = nx.from_numpy_array(sim_mat)
    scores = nx.pagerank(nx_graph)

    ranked_sentese = sorted(((scores[i],s) for i,s in enumerate(sentese)), reverse=True)
    c=0
    a=""
    for i in ranked_sentese:
        if "collect" in (i[1]) or "data" in (i[1]) or "use" in (i[1])  or "access" in (i[1]) or "time" in i[1] and "party" in (i[1]):
            a+=i[1]+'\n'
            c+=1
        if c==9:
            break
    return(a)

@app.route("/") 
def home_view(): 
    return "<h1>Welcome</h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(port=port)


