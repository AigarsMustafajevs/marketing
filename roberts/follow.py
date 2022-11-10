import random
import tweepy
import json
import time
from decouple import config

VPS_DIRECTORY = "/Users/aigars/Desktop/rok-finance/marketing/roberts/data/"


def getClient():
    client = tweepy.Client(
        bearer_token=config('bearer_token_RM'),
        consumer_key=config('consumer_key_RM'),
        consumer_secret=config('consumer_secret_RM'),
        access_token=config('access_token_RM'),
        access_token_secret=config('access_token_secret_RM'))
    return client


def readJson(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)


def writeJson(filepath, data):
    with open(filepath, 'w') as fp:
        json.dump(data, fp)


def followPeople():
    following_path = "{}/following.json".format(VPS_DIRECTORY)
    following = readJson(following_path)

    to_follow_path = "{}/tofollow.json".format(VPS_DIRECTORY)
    to_follow = readJson(to_follow_path)

    account = random.choice(to_follow)
    accountId = account['userId']

    client = getClient()

    results = client.get_users_followers(
        id=accountId, max_results=follow_count)

    account_followers = results.data
    if len(account_followers) > 0:
        for x in account_followers:
            if not x.id in following:
                try:
                    client.follow_user(x.id)
                    following.append(x.id)
                    print('Successfylly followed: {}'.format(x.username))
                    time.sleep(xtime)
                except:
                    print('Trouble following {}'.format(x.username))
            else:
                print('Already following {}'.format(x.username))
    writeJson(following_path, following)


xtime = random.randint(5, 120)
follow_count = random.randint(1, 20)

followPeople()
