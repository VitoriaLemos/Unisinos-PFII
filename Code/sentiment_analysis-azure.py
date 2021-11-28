import os
import json
import def_collect_tweets_array

# [START analyze_sentiment]
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.ai.textanalytics import EntityCertainty

endpoint = "[add endpoint]"
key = "[add key]"

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def sample_analyze_sentiment():

    # [START analyze_sentiment]
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient


    endpoint = "[add endpoint]"
    key = "[add key]"

    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    jsonfile = open("Tim_filtrado.json", "r", encoding='utf8')
    data = json.load(jsonfile)
    tweets = data["data"]
    

    f = open("SA_Tim_2.json", "w", encoding='utf8')

    for i in range(0, len(tweets), 8):
        group = tweets[i:i+8]

        result = text_analytics_client.analyze_sentiment([x['text'] for x in group], show_opinion_mining=True)

        for x in range(0, len(group)):
            sentiment = {
                "sentiment" : str(result[x].sentiment),
                "confidence" : str(result[x].confidence_scores),
            }
            group[x]['sentiment'] = sentiment

    f.write(json.dumps(tweets, indent=4))

    # [END analyze_sentiment]
    f.close()



if __name__ == '__main__':
    sample_analyze_sentiment()