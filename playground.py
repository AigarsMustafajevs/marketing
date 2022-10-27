# Interpreter path: /Users/aigars/opt/anaconda3/bin/python
#

import tweepy
from decouple import config


auth = tweepy.OAuthHandler(config('consumer_key_KYLE'), config(
    'consumer_secret_KYLE'))  # KYLE FOR TESTING
auth.set_access_token(config('access_token_KYLE'), config(
    'access_token_secret_KYLE'))  # KYLE FOR TESTING

# auth = tweepy.OAuthHandler(config('consumer_key_AM'), config(
#     'consumer_secret_AM'))  # KYLE FOR TESTING
# auth.set_access_token(config('access_token_AM'), config(
#     'access_token_secret_AM'))  # KYLE FOR TESTING

api = tweepy.API(auth, wait_on_rate_limit=True)


# get userid:
user = api.get_user(screen_name='DustinWalkerRF')

# post tweet withc text only


def post_tweet(text):
    api.update_status(text)

# post tweet with media
# note: used media and tweets should be market or placed elseware


def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media)


def favourite(tweet_id):
    api.create_favorite(str(tweet_id))


def unfavourite(tweet_id):
    api.destroy_favorite(str(tweet_id))


def retweet(tweet_id):
    api.retweet(str(tweet_id))


def unretweet(tweet_id):
    api.unretweet(str(tweet_id))

# not working:


def reply(tweet_id, message):
    tweet = api.get_status(str(tweet_id))
    username = tweet.user.screen_name
    reply = api.update_status(f'@{username} ' + message, str(tweet_id))

# scrape tweets:


def user_timeline(username):
    ot = []  # original tweet
    replies = []  # replies for someone
    rts = []  # retweets
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode='extended').items(10):
        if tweet.full_text.startswith('@'):
            replies.append(tweet.full_text)
        elif tweet.full_text.startswith('RT @'):
            rts.append(tweet.full_text)
        else:
            ot.append(tweet.full_text)
    print(len(ot))
    print(len(replies))
    print(len(rts))

    return ot, replies, rts


# timeline = user_timeline('elonmusk')

# print(timeline[1])
# print(timeline)

def follow(screen_name):
    api.create_friendship(screen_name)


#######DEPLOY########
print(user.id)
# post_tweet("is this code working?")
# upload_media("name", "/data/media/gift.jpg")
# favourite(1584948976897626112)
# unfavourite(1584948976897626112)
# retweet(1584948976897626112)
# unretweet(1584948976897626112)
# print(api.get_status(str(1584948976897626112)))
# reply(1584948976897626112, "this is a test message") #not working

follow(1584860617940271105)
