import random
import tweepy
import json
import time
from decouple import config
import pandas as pd

VPS_DIRECTORY = "/Users/aigars/Desktop/rok-finance/marketing/rokfinance/data/"

action = ['Tweet_from_db']

auth = tweepy.OAuthHandler(config('consumer_key_RF'), config(
    'consumer_secret_RF'))
auth.set_access_token(config('access_token_RF'), config(
    'access_token_secret_RF'))

api = tweepy.API(auth, wait_on_rate_limit=True)


if action == 'Tweet_from_db':
    xl = pd.ExcelFile(
        "{}/tweetsdb.xlsx".format(VPS_DIRECTORY))
    xl = xl.parse('rokfinance')
    tweet_text = random.choice(xl["Tweet"])
    api.update_status(status=tweet_text)
