import tweepy
import json
import sys
# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = "8TIPnyB7k3CRWS2gYCtd7GRIy"
consumer_secret = "EoQMo54FyWN4yxwtJIPSY2MnoiNLR8CXn2YLUITCpZmoDEu3Tf"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = "906313272680501248-EM6nDSoY0rbNgHwjVre2T1c0itpdkRb"
access_token_secret = "JRUdz2vtomDWbWjFjDhjshS65fUOTtVDldaJXRO3pHrHu"

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0x12)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweetId = 906318327508848640

print(api.statuses_lookup([tweetId])[0].text.translate(non_bmp_map))
for result in api.search("to:@DavidLawTennis", sinceId=tweetId, count=500):
    if(result.in_reply_to_status_id == tweetId):
        print(result.text.translate(non_bmp_map))
