import requests
import os
from dotenv import load_dotenv
load_dotenv()
import snowflake.connector
from datetime import datetime

MASSIVE_API_KEY = os.getenv('MASSIVE_API_KEY')
DS = datetime.now().strftime('%Y-%m-%d')
LIMIT = 1000

def extract_tickers():
    url = f'https://api.massive.com/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={MASSIVE_API_KEY}'
    response = requests.get(url)
    tickers = []

    data = response.json()
    for ticker in data['results']:
        tickers.append(ticker)

    while 'next_url' in data:
        print('Requesting next page', data['next_url'])
        response = requests.get(data['next_url'] + f'&apiKey={MASSIVE_API_KEY}')
        data = response.json()
        #print(data)
        for ticker in data['results']:
            ticker['ds'] = DS
            tickers.append(ticker)

    example_ticker =  {'ticker': 'ZWS', 
        'name': 'Zurn Elkay Water Solutions Corporation', 
        'market': 'stocks', 
        'locale': 'us', 
        'primary_exchange': 'XNYS', 
        'type': 'CS', 
        'active': True, 
        'currency_name': 'usd', 
        'cik': '0001439288', 
        'composite_figi': 'BBG000H8R0N8', 	'share_class_figi': 'BBG001T36GB5', 	
        'last_updated_utc': '2025-09-11T06:11:10.586204443Z',
        'ds': '2025-09-25'
        }

    fieldnames = list(example_ticker.keys())
    # Load to Snowflake instead of CSV
    #load_to_snowflake(tickers, fieldnames)
    print(len(tickers))

if __name__ == '__main__':
    extract_tickers()