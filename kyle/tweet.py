import random
import tweepy
import json
import time
from decouple import config
import pandas as pd

VPS_DIRECTORY = "/Users/aigars/Desktop/rok-finance/marketing/kyle/data/"


def Tweet_type():
    Joke_p = 00  # C0 - post a joke from jokeDB
    Tweet_from_db_p = 100  # C1 - post an nft related tweet
    Quote_p = 0  # C2 - post an inspirational/joke quote
    Tweet_and_media_p = 0  # D0 - BAYC related post with media
    Meme_p = 0  # D1 - post a meme

    action = \
        ['Joke'] * Joke_p + \
        ['Tweet_from_db'] * Tweet_from_db_p + \
        ['Quote'] * Quote_p + \
        ['Tweet_and_media'] * Tweet_and_media_p + \
        ['Meme'] * Meme_p

    action = random.choice(action)
    return action


action = Tweet_type()
print('action:', action)

auth = tweepy.OAuthHandler(config('consumer_key_KYLE'), config(
    'consumer_secret_KYLE'))  # KYLE FOR TESTING
auth.set_access_token(config('access_token_KYLE'), config(
    'access_token_secret_KYLE'))  # KYLE FOR TESTING

api = tweepy.API(auth, wait_on_rate_limit=True)


###################################################
#################### EXECUTION ####################
if action == 'Joke':
    # print(xl.sheet_names)
    xl = pd.ExcelFile(
        "{}/jokes_db.xlsx".format(VPS_DIRECTORY))
    xl = xl.parse('Sheet1')

    # #Pushing random tweet:
    tweet_text = random.choice(xl["Joke"])
    api.update_status(status=tweet_text)

if action == 'Tweet_from_db':
    xl = pd.ExcelFile(
        "{}/tweetsdb.xlsx".format(VPS_DIRECTORY))
    xl = xl.parse('rokfinance')
    tweet_text = random.choice(xl["Tweet"])
    api.update_status(status=tweet_text)

# if action == 'C2':
#     # importing excel with quotes:
#     # print(xl.sheet_names)
#     xl = pd.ExcelFile(
#         "/Users/amustafajevs/Desktop/Q/nft/nft_doomer/ACC_0/data/quotes.xlsx")
#     xl = xl.parse('batch1')

#     # #Pushing random tweet:
#     tweet_text = random.choice(xl["Quotes"])
#     a.update_status(status=tweet_text)

# if action == 'D0':
#     # FIX: shis nestrada jo ir lidzigs jau poustotiem twiitiem
#     # random izvelets tweets:
#     tweet_text = random.choice(apes_tweets.list_tweets)
#     # random izvelets attels:
#     tweet_photo = random.choice(apes_photos.list_photos)
#     a.update_status_with_media(status=tweet_text, filename=tweet_photo)

# if action == 'D1':
#     back = os.getcwd()
#     r_hash = ["#jokes ", "#memes ", "#jokesoftheday ", "#humour "]
#     r_hash1 = ["#comedy ", "#lol ", "#fun ", "#memesdaily "]
#     r_hash2 = ["#meme ", "#lmao ", "#viral ", "#haha "]
#     # random izvelets tweets:
#     tweet_text = random.choice(r_hash), random.choice(
#         r_hash1), random.choice(r_hash2)
#     os.chdir("./ACC_0/data/memes/")  # random izvelets attels:
#     tweet_photo = random.choice(os.listdir(
#         "/Users/amustafajevs/Desktop/Q/nft/nft_doomer/ACC_0/data/memes"))

#     a.update_status_with_media(status=tweet_text, filename=tweet_photo)

#     os.chdir(back)

# if action == 'E0':
#     # random izvelets meklesanas vards:
#     keywords = ["crypto", "bitcoin", "SpaceX", "Binance",
#                 "CZ", "Elon Musk", "Vitalik Buterin", "ETH", "BTC"]
#     tweets = searchTweets(random.choice(keywords), max_res=10)
#     df_retweets = pd.DataFrame(tweets)

#     # random izvelets tweets:
#     rand_retw = random.randint(0, 9)
#     retweet_this_id = df_retweets['id'].iloc[rand_retw]

#     a.retweet(id=retweet_this_id)
