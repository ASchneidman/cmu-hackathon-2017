from bs4 import BeautifulSoup

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

html_doc = open('web.html', encoding="utf8").read().translate(non_bmp_map)
soup = BeautifulSoup(html_doc, 'html.parser')

tweets = soup.findAll("p", { "class" : "tweet-text" })
for tweet in tweets:
    print(tweet)
