#Import Required libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
#Import Dependencies for sentiment analysis using our neural network
import tensorflow as tf
import numpy
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import alpaca_trade_api as tradeapi

finviz_url = "https://finviz.com/quote.ashx?t="
ticker = "NIO"
url = finviz_url + ticker

req = Request(url=url, headers={'user-agent': 'my-app/0.0.1'})
response = urlopen(req)

news_table = {}
html = BeautifulSoup(response)
news_table = html.find(id='news-table')
# news_table

dataRows = news_table.findAll('tr')
df = pd.DataFrame(columns=['News_Title', 'Time'])
for i, table_row in enumerate(dataRows):
    a_text = table_row.a.text
    td_text = table_row.td.text
    
    df = df.append({'News_Title': a_text, 'Time': td_text}, ignore_index=True)

# print(df)

with open('./tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
model = tf.keras.models.load_model('./model1.h5')

oov_tok = '<OOV>'
trunc_type = 'post'
padding_type='post'
vocab_size =1000
max_length = 142

def preprocessText(text):
    sequences = tokenizer.texts_to_sequences(text)
    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type,
                          truncating=trunc_type)
    return padded

prep = preprocessText(df.News_Title)
prep = model.predict(prep)
df['sent'] = np.argmax(prep, axis=-1)

api = tradeapi.REST("PKI99WOFTSXJT4D5S59G", "6J7paTPQsSDDvLQbeUtP2rqOV1aGNjGtI3wr6yQn", "https://paper-api.alpaca.markets")
account = api.get_account()
# print(account)

modeSentiment = df.sent.mode().iloc[0]

# print(df['sent'].value_counts().loc[2])

if df['sent'].value_counts().loc[0] > 30:
    api.submit_order(
        symbol="TSLA",
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print("BUY")
elif df['sent'].value_counts().loc[2] > 30:
    api.submit_order(
        symbol="TSLA",
        qty=1,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
    print("SELL")

else:
    print("Nothing to do, no thresholds triggered")
