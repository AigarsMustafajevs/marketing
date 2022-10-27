import tweepy
from decouple import config
import random
import json
import time
import pandas

# unfollow/follow DB location
# VPS_DIRECTORY = "/Users/aigars/Desktop/rok-finance/marketing/data"


auth = tweepy.OAuthHandler(config('consumer_key_KYLE'), config(
    'consumer_secret_KYLE'))  # KYLE FOR TESTING
auth.set_access_token(config('access_token_KYLE'), config(
    'access_token_secret_KYLE'))  # KYLE FOR TESTING

api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(
    bearer_token=config('bearer_token_KYLE'),
    consumer_key=config('consumer_key_KYLE'),
    consumer_secret=config('consumer_secret_KYLE'),
    access_token=config('access_token_KYLE'),
    access_token_secret=config('access_token_secret_KYLE'))

xtime = random.randint(5, 30)
follow_count = random.randint(1, 5)


# def readJson(filename):
#     with open(filename, 'r', encoding='utf-8') as fp:
#         return json.load(fp)
ff = "/Users/aigars/Desktop/rok-finance/marketing/data/tofollow.json"
f = open("/Users/aigars/Desktop/rok-finance/marketing/data/tofollow.json")
data = json.load(f)
# print(data)
# for i in data['username']:
#     print(i)

f.close()


def readJson(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        return print(json.load(fp))


readJson(ff)


def writeJson(filepath, data):
    with open(filepath, 'w') as fp:
        json.dump(data, fp)


# client.follow_user(22205703)

# def follow(screen_name):
#     api.create_friendship(screen_name)


# follow('DustinWalkerRF')

# following_path = "/Users/aigars/Desktop/rok-finance/marketing/data/following.json"
# following = readJson("/Users/aigars/Desktop/rok-finance/marketing/data/following.json")

def followPeople():
    # following_path = "{}/following.json".format(VPS_DIRECTORY)
    following = readJson(
        "/Users/aigars/Desktop/rok-finance/marketing/data/following.json")

    # to_follow_path = "{}/tofollow.json".format(VPS_DIRECTORY)
    to_follow = readJson(
        "/Users/aigars/Desktop/rok-finance/marketing/data/tofollow.json")

    account = random.choice(to_follow)
    accountId = account['userId']

    client = client

    # if max_Results broken replace with any number from 1 to 10
    results = client.get_users_followers(
        id=accountId, max_results=follow_count)

    account_followers = results.data

    if len(account_followers) > 0:
        for x in account_followers:
            client.follow_user(x.id)
            print('Successfylly followed: {}'.format(x.username))
            # so varetu aizvietot ar randbetween 5-120 seconds ( if broken replace x with 5)
            time.sleep(xtime)


followPeople()
