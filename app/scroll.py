import time
import os

import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def getReplies(tweetLink):
    chromedriver_path = os.environ.get('CHROMEDRIVER', './chromedriver')
    driver = webdriver.Chrome(chromedriver_path)
    driver.get(tweetLink)

    element = driver.find_element_by_class_name('permalink-tweet')

    #lastHeight = element.pagesourse
    for x in range(30):
        element.send_keys(Keys.CONTROL, Keys.END)
        time.sleep(1)
        #if(lastHeight==element.scrollHeight):
        #    break
        #lastHeight=element.scrollHeight

    post_elems = driver.find_elements_by_class_name("tweet-text")

    text_elems = list(map(lambda post: post.text, post_elems))

    driver.quit()

    return text_elems


if __name__ == '__main__':
    getReplies("https://twitter.com/realDonaldTrump/status/906320446882271232")
