from os import read
from def_collect_tweets_array import save_tweets, get_tweets, load_file, remover_dup
import pandas as pd
import json

with open('Claro_filtrado.json', 'r', encoding='utf8') as json_file:
    data = json.load(json_file)
    tweets = [t["text"] for t in data["data"]]
    save_tweets(tweets, "claro_filtrado_teste")


#remover_dup('eletrobras_tweets_raw')

