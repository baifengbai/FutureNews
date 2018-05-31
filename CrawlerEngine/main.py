# --*-- coding: utf-8 --*--
import os
import random
import sys
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(BASE_DIR)
import time
from CrawlerEngine.media_config import MEDIA as media_list
from CrawlerEngine.crawler import crawl
from CrawlerEngine.settings import CRAWL_INTERVAL


def start():
    random.shuffle(media_list)
    for m in media_list:
        for k, v in m.items():
            source = k
            for category, url in v.items():
                print("######", source, category, url, "######")
                crawl(url, source, category)
                print("\n")






if __name__ == '__main__':
    while True:
        start()
        time.sleep(60 * CRAWL_INTERVAL)
