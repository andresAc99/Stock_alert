#!pip3 install twilio
#pip install yfinance
#pip install ta
import os
from twilio.rest import Client
from twilio_config import *
import time

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import yfinance as yf
import numpy as np # linear algebra
import pandas as pd
import ta  # Technical Analysis library
from sklearn.preprocessing import MinMaxScaler
from datetime import date
from datetime import datetime
from datetime import timedelta

#Día actual
today = date.today()

#Día 3 atras 
yesterday = today - timedelta(days = 3)

# Define the tickers
tickers = ['DVA', 'NU', 'AMD', 'QCOM', 'JXN']

# Define the date range (yesterday to today)
today = datetime.today().strftime('%Y-%m-%d')
yesterday = (datetime.today() - timedelta(days=3)).strftime('%Y-%m-%d')

# Download data for all tickers
new_data = yf.download(tickers, start=yesterday, end=today)

# Select only the 'Close' column
close_data = new_data['Close']

close_data_reset = close_data.reset_index()  # To turn the 'Date' index into a column
melted_data = pd.melt(close_data_reset, id_vars=['Date'], value_vars=tickers, 
                      var_name='Ticker', value_name='Price')

result = melted_data[['Ticker', 'Price']]

# Create the message with date and close data
messagex = '\nHola! \n\n\nEl tu tracking stock del: ' + yesterday +' es: \n\n\n ' + str(result)
messagex

PHONE_NUMBER

time.sleep(2)
account_sid = TWILIO_ACCOUNT_SID 
auth_token = TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body= messagex,
                     from_=PHONE_NUMBER,
                     to='+XXXXXXX'
                 )

print('Mensaje Enviado ' + message.sid)

