import requests
import os
from dotenv import load_dotenv
load_dotenv()

MASSIVE_API_KEY = os.getenv('MASSIVE_API_KEY')

url = f'https://api.massive.com/v3/reference/tickers?market=stocks&active=true&order=asc&limit=100&sort=ticker&apiKey={MASSIVE_API_KEY}'
response = requests.get(url)
tickers = []

data = response.json()
for ticker in data['results']:
    tickers.append(ticker)

print(len(tickers))