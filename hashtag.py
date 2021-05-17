from selenium import webdriver
from time import *
import pandas as pd
from selenium.webdriver.common.keys import Keys

chromedriver = ("/chromedriver") #path to chromedriver
browser = webdriver.Chrome(executable_path=chromedriver)


def tags(hashtag,tags_arr,post_arr):
    browser.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
    sleep(4)

    search = browser.find_element_by_xpath('//input[@placeholder="Search"]')
    search.send_keys("#"+hashtag)
    sleep(2)

    tag_list = browser.find_elements_by_xpath('//span[@class="Ap253"]')
    posts = browser.find_elements_by_xpath('//div[@class="Fy4o8"]//span//span')
    for i in range(len(tag_list)):
        #print(tag_list[i].text+" - "+posts[i].text)
        tags_arr.append(tag_list[i].text)
        post_arr.append(posts[i].text)

browser.get("https://www.instagram.com/explore/tags/bitcoin")
sleep(5)

id = browser.find_element_by_xpath('//input[@aria-label="Phone number, username, or email"]')
id.send_keys('') #enter username

password = browser.find_element_by_xpath('//input[@aria-label="Password"]')
password.send_keys('') #enter password
password.send_keys(Keys.RETURN)
sleep(5)

l = ['crypto','bitcoin','ethereum','blockchain','xrp','binance','invest','litecoin','decentralised']

tags_arr = list()
post_arr = list()
for i in l:
    tags(i,tags_arr,post_arr)

data = {'Hashtags':tags_arr,'Posts':post_arr}
df = pd.DataFrame(data)
df.to_excel('tags.xlsx')

