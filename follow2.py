import tweepy
from decouple import config
import random
import json
import time

def readJson(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        return print(json.load(fp))
    
def writeJson(filepath, data):
    with open(filepath, 'w') as fp:
        json.dump(data, fp)
        
def getClient():
    client = tweepy.Client(
        bearer_token=config('bearer_token_KYLE'),
        consumer_key=config('consumer_key_KYLE'),
        consumer_secret=config('consumer_secret_KYLE'),
        access_token=config('access_token_KYLE'),
        access_token_secret=config('access_token_secret_KYLE'))
    return client

follow_count = 5
xtime = 5

def followPeople():
    following_path = "/Users/aigars/Desktop/rok-finance/marketing/data/following.json"
    following = readJson(following_path)

    to_follow_path = "/Users/aigars/Desktop/rok-finance/marketing/data/tofollow.json"
    to_follow = readJson(to_follow_path)

    account = random.choice(to_follow)
    accountId = account['userId']
    
    print(accountId)

    # client = getClient()

    # results = client.get_users_followers(id=accountId, max_results=follow_count)

    # account_followers = results.data
    # if len(account_followers) > 0:
    #     for x in account_followers:
    #         if not x.id in following:
    #             try:
    #                 client.follow_user(x.id)
    #                 following.append(x.id)
    #                 print('Successfylly followed: {}'.format(x.username))
    #                 time.sleep(xtime)
    #             except:
    #                 print('Trouble following {}'.format(x.username))
    #         else:
    #             print('Already following {}'.format(x.username))
    # writeJson(following_path, following)

followPeople()

