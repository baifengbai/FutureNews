# --*-- coding: utf-8 --*--
import os
import sys
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(BASE_DIR)
import time
import platform
from pymongo import MongoClient
from selenium import webdriver
from bs4 import BeautifulSoup
from CrawlerEngine.check import check_fulture
from CrawlerEngine.settings import DB_PARAM

client = MongoClient(DB_PARAM['ip'], DB_PARAM['port'],
                     username=DB_PARAM['username'],
                     password=DB_PARAM['password'],
                     authSource='future_news',)


db = client[DB_PARAM['database']]

current_platform = platform.system()
if current_platform == 'Darwin':
    driver = webdriver.Chrome('/Users/nolan/Documents/chromedriver')

if current_platform == 'Linux':
    from selenium import webdriver
    from pyvirtualdisplay import Display
    display=Display(visible=0,size=(800,800))
    display.start()
    driver = webdriver.Chrome()


def baidu_crawler():
    try:
        url = 'https://www.toutiao.com/ch/news_finance/'
        driver.get(url)
        time.sleep(2)
        driver.implicitly_wait(30)


        js_down = "var q=document.documentElement.scrollTop=100000"
        js_up = "var q=document.documentElement.scrollTop=0"
        for i in range(3):
            driver.execute_script(js_down)
            time.sleep(2)
            driver.execute_script(js_up)
            time.sleep(1)






        # driver.set_page_load_timeout(30)
        # driver.set_script_timeout(30)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        items = soup.find_all('a')
        for i in items:
            title = i.string
            url = i.get('href')
            if title and check_fulture(title):
                print(title)
                print(url)
                data = {
                    'title': title,
                    'url': url,
                    'source': '今日头条',
                    'category': '互联网'
                }
                db.news.insert(data)



    except Exception as e:
        print(str(e))

    driver.close()




if __name__ == '__main__':
    baidu_crawler()