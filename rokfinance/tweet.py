import random
import tweepy
import json
import time
from decouple import config
import pandas as pd

VPS_DIRECTORY = "/Users/aigars/Desktop/rok-finance/marketing/rokfinance/data/"


def Tweet_type():
    Joke_p = 00  # C0 - post a joke from jokeDB
    Tweet_from_db_p = 100  # C1 - post an nft related tweet
    Quote_p = 00  #
    Tweet_and_media_p = 0  #
    Meme_p = 00  # D1 -

    action = \
        ['Joke'] * Joke_p + \
        ['Tweet_from_db'] * Tweet_from_db_p + \
        ['Quote'] * Quote_p + \
        ['Tweet_and_media'] * Tweet_and_media_p + \
        ['Meme'] * Meme_p  # only media

    action = random.choice(action)
    return action


action = Tweet_type()
print('action:', action)


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
