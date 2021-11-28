import requests
import os
import json


bearer_token = os.environ.get("BEARER_TOKEN") # ADICIONAR BEARER TOKEN

search_url = "https://api.twitter.com/2/tweets/search/all"

query_tim = "(#Tim OR Tim) (vazamento de dados) -is:retweet"
query_params = {'query': query_tim, 'tweet.fields': 'created_at' , 'start_time': '2021-02-01T00:00:00Z', 'end_time': '2021-08-01T00:00:00Z', 'max_results': '500'}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params, headers={"content-type":"application/json;charset=UTF-8"})
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    retorno = json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False)

    f = open("Tim.txt","w",encoding='UTF-8')
    f.write(retorno)
    f.close()


if __name__ == "__main__":
    main()