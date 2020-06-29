import tweepy
import time

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")

auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = ["#Python", "#Tweepy"]
Number_Tweets = 500


for tweet in tweepy.Cursor(api.search.items, search).items(Number_Tweets):
    try:
        print("Tweet Liked")
        tweet.favorite()  # OR  #tweet.retweet()

        time.sleep(10)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
