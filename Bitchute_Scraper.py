import time
import random
import webbrowser
import pandas as pd
import urllib.request
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/Users/rock/tor/CC_bitChute/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://www.bitchute.com/channel/NaturalNews/')

for i in tqdm(range(15)):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

element = []
for i in driver.find_elements_by_class_name('spa'):
    element.append(i)

titles = [x.get_attribute('href') for x in element]

pd.DataFrame(titles).to_csv('BitChuteCC_titles2020.csv', index=False)
titles = pd.read_csv('BitChuteCC_titles2020.csv')

print(titles)
for i in titles['0'][34:-2]:
    print(i)

driver.quit()


# pd.DataFrame(pass0.split(',')).to_csv('leftover2020.csv', index=False)

catch = []
for i in tqdm(pass0.split(',')):
    # try:
    req = Request(i, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    mp4_link = soup.findAll('source', attrs={"type":"video/mp4"})[0]['src']
    vid_title = soup.findAll('h1', attrs={"class":"page-title"})[0].text.replace(' ', '_')+'.mp4'
    print(i)
    print(mp4_link)
    urllib.request.urlretrieve(mp4_link, vid_title)
    # except:
    #     catch.append(i)
    #     print(i)
    #     pass

pd.DataFrame(catch).to_csv('catch2_BitChuteCC_titles2020.csv', index=False)








