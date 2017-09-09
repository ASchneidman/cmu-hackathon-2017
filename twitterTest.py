import tweepy

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = "8TIPnyB7k3CRWS2gYCtd7GRIy"
consumer_secret = "EoQMo54FyWN4yxwtJIPSY2MnoiNLR8CXn2YLUITCpZmoDEu3Tf"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = "906313272680501248-EM6nDSoY0rbNgHwjVre2T1c0itpdkRb"
access_token_secret = "JRUdz2vtomDWbWjFjDhjshS65fUOTtVDldaJXRO3pHrHu"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print(api.statuses_lookup([906282980653617152])[0].text)
