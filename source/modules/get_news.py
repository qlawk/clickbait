# key stored in config
import config
import pandas as pd
import requests

# get headlines from news source as csv
def get_headlines(source):

    # endpoint refers to News API url
    api_endpoint = 'https://newsapi.org/v2/everything'
    headers = {'Authorization': f'Bearer {config.news_key}'}

    # sources are news network names
    params = {'sources': source}

    response = requests.get(api_endpoint, headers=headers, params=params)
    data = response.json()

    #  normalized json as a dataframe
    df = pd.json_normalize(data['articles'])
    
    # saving dataframe as a csv file
    df.to_csv(source + '.csv',index=False)