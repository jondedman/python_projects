import requests
from twilio.rest import Client
import os
import dotenv
from datetime import datetime, timedelta
import time

dotenv.load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_key = os.environ.get('ALPHA_KEY')
news_key = os.environ.get('NEWS_KEY')

day_before_yesterday = datetime.now() - timedelta(days=2)
day_before_yesterday = day_before_yesterday.strftime('%Y-%m-%d')
yesterday = datetime.now() - timedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')

stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alpha_key}'
r = requests.get(stock_url)
stock_data = r.json()

yesterday_close = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
day_before_yesterday_close = float(stock_data['Time Series (Daily)'][day_before_yesterday]['4. close'])

percentage_difference = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100
print(yesterday_close)
print(day_before_yesterday_close)
print(percentage_difference)

if percentage_difference > 5:
    print('Get News')

news_url = f'https://newsapi.org/v2/?q={COMPANY_NAME}&from={day_before_yesterday}&to={yesterday}&sortBy=popularity&apiKey={news_key}'
n = requests.get(news_url)
news_data = n.json()

top_three_articles = news_data['articles'][:3]


title_1 = top_three_articles[0]['title']
url_1 = top_three_articles[0]['url']
title_2 = top_three_articles[1]['title']
url_2 = top_three_articles[1]['url']
title_3 = top_three_articles[2]['title']
url_3 = top_three_articles[2]['url']




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
