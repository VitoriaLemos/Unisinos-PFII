
import numpy as np
import json
import glob
from pathlib import Path
from pprint import pprint
import pandas as pd

#Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel, ldamodel

#spacy
import spacy
from nltk.corpus import stopwords

#vis
import pyLDAvis
import pyLDAvis.gensim_models

from smart_open import open  # for transparently opening remote files
from gensim import corpora
from def_collect_tweets_array import save_tweets, get_tweets, load_file, remover_dup

# load the files from a folder
txt_folder = Path([path to files]).rglob('*.txt')
files = [x for x in txt_folder]

for file in files:

    news_article = open(file, 'r', encoding='utf8').read()
    preprocessed_article = gensim.utils.simple_preprocess(news_article, deacc=False)
    id2word = corpora.Dictionary([preprocessed_article])
    corpus = [id2word.doc2bow(preprocessed_article)]


    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=3,
                                                random_state=100,
                                                update_every=1,
                                                chunksize=100,
                                                passes=10,
                                                alpha="auto")

    top_topics = lda_model.top_topics(corpus,topn=5)

    # Print the Keyword in the topics
    print(file)
    pprint(top_topics)
    print('\n')
