import time

import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\matia\\Documents\\GitHub\\cmu-hackathon-2017\\chromedriver.exe')
driver.get("https://twitter.com/realDonaldTrump/status/906320446882271232")


element = driver.find_element_by_class_name('permalink-tweet')

#element.send_keys(Keys.CONTROL , Keys.END)
for x in range(50):
    for y in range(3):
        element.send_keys(Keys.SPACE)
    time.sleep(1)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.execute_script("window.scrollBy(0, 500);")

post_elems = driver.find_elements_by_class_name("tweet-text")

for post in post_elems:
    print(post.text)

driver.quit()
