import tweepy


import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


auth = tweepy.OAuthHandler( "8TIPnyB7k3CRWS2gYCtd7GRIy", "EoQMo54FyWN4yxwtJIPSY2MnoiNLR8CXn2YLUITCpZmoDEu3Tf")
auth.set_access_token("906313272680501248-EM6nDSoY0rbNgHwjVre2T1c0itpdkRb", "JRUdz2vtomDWbWjFjDhjshS65fUOTtVDldaJXRO3pHrHu")

api = tweepy.API(auth)

print("GETTING TRUMP MESSAGES")
print("---------------------------------------------------------------")
tweets = api.user_timeline("realDonaldTrump",count=10)
x=1
for tweet in tweets:
    print(str(x)+": "+tweet.text.translate(non_bmp_map))
    x+=1
print("---------------------------------------------------------------")
print()


print("FINDING #TRUMP")
print("---------------------------------------------------------------")

hashtagTrump = tweepy.Cursor(api.search, q='#Trump').items(10)

for tweet in hashtagTrump:
    print(tweet.text.translate(non_bmp_map))
print("---------------------------------------------------------------")