from config import alpha_key, news_key, twilio_sid, twilio_auth_token
from twilio.rest import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "symbol": STOCK_NAME,
    "function": "TIME_SERIES_DAILY",
    "apikey": alpha_key
}

r = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = r.json()

# print(data)

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#print(data["Time Series (Daily)"])
closing_stock_price = [value['4. close'] for (key, value) in data["Time Series (Daily)"].items()]
yesterday_price = closing_stock_price[0]

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yes_price = closing_stock_price[1]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(float(yesterday_price) - float(day_before_yes_price))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = diff/float(yesterday_price) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_diff > 0:
        ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        "apikey": news_key,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()
    articles = news_data["articles"]
    top_three = articles[:3]
    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    print(top_three)
        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in top_three]

    #TODO 9. - Send each article as a separate message via Twilio. 
    client = Client(twilio_sid, twilio_auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_ = "+17012531948",
            to = "+60194745451"
            )




else:
    print(percent_diff)


    #Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

