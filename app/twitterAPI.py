import tweepy

consumer_key = "8TIPnyB7k3CRWS2gYCtd7GRIy"
consumer_secret = "EoQMo54FyWN4yxwtJIPSY2MnoiNLR8CXn2YLUITCpZmoDEu3Tf"
access_token = "906313272680501248-EM6nDSoY0rbNgHwjVre2T1c0itpdkRb"
access_token_secret = "JRUdz2vtomDWbWjFjDhjshS65fUOTtVDldaJXRO3pHrHu"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getUser(user):
    tweets = api.user_timeline(user,count=500)
    return list(map(lambda tweet: tweet.text, tweets))

def getHashtag(hashtag):
    tweets = tweepy.Cursor(api.search, q=hastag).items(500)
    return list(map(lambda tweet: tweet.text, tweets))
