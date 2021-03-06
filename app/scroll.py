import os

import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def getReplies(tweetLink):
    chromedriver_path = os.environ.get('CHROMEDRIVER', './chromedriver')
    driver = webdriver.Chrome(chromedriver_path)
    driver.get(tweetLink)

    try:
        element = driver.find_element_by_class_name('permalink-tweet')
    except selenium.common.exceptions.NoSuchElementException:
        print("Invalid tweet.")
        driver.quit()
        return []

    while not driver.find_element_by_class_name("stream-end").is_displayed():
        element.send_keys(Keys.CONTROL, Keys.END)

    post_elems = driver.find_elements_by_class_name("tweet-text")

    text_elems = list(map(lambda post: post.text, post_elems))

    driver.quit()

    return text_elems


if __name__ == '__main__':
    getReplies("https://twitter.com/realDonaldTrump/status/906320446882271232")
