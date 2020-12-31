import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "w5VvCSKaoWXHxFLhj26Q87Rzi" #"Enter API Key"
# api secret key
api_secret_key = "lOBvhjGPT8T7lVND7QrK5zSrn1QZlDweuBHRfjF8pwyjcKLd1k" #"Enter API secret Key"
# access token
access_token = "75977001-d4mgRDngfUcbQyxwkLyxRMgFpiPLE20jKg2p3Bq65" #"Enter Access Token"
# access token secret
access_token_secret = "Q1PdQzZnbjnuzbrKM5hcItBRsN8JHvtdyYXI5YY0OSZSx" #"Enter Access Token Secret"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)
