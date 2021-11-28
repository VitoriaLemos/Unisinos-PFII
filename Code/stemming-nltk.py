import nltk
import pandas as pd
import numpy as np
from def_collect_tweets_array import save_tweets
import sys
from pathlib import Path

txt_folder = Path([path to files]).rglob('*.txt')
files = [x for x in txt_folder]

def stemming_texto(texto):
    stemmer = nltk.stem.RSLPStemmer()
    data_stemming = []

    for name in files:
        f = open(name, 'r', encoding='utf8')  
        text = f.read()
        for p in text.split():
            word = "".join([c for c in p if c not in punc]) 
            if word not in list_stopwords_nltk:
                data_stemming.append(word)

        #return data_stemming
        save_tweets(data_stemming, name, " ")
        f.close()
    
list_stopwords_nltk = nltk.corpus.stopwords.words('portuguese')
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

result_stemming = stemming_texto(files)