import requests

emote = requests.post("https://shl-mp.p.mashape.com/webresources/jammin/emotionV2",
  headers={
    "X-Mashape-Key": "YP2AbnB4TVmsh3HU6FKUjIjdwf3yp1UfWfpjsnHp4XMSMSA8x6",
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  params={
    "lang": "en",
    "text": "Congress, get ready to do your job - DACA!"
  }).json()

print(emote)
