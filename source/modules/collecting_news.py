# import modules, key stored in config
import config
import requests
import pandas as pd

# gets headlines from news source as csv
def get_headlines(source):
    api_endpoint = 'https://newsapi.org/v2/everything'
    headers = {'Authorization': f'Bearer {config.news_key}'}
    params = {'sources': source}

    response = requests.get(api_endpoint, headers=headers, params=params)
    data = response.json()
    df = pd.json_normalize(data['articles'])
    df.to_csv(source + '.csv',index=False)