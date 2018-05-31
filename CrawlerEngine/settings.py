from pytz import timezone


# MongoDB
DB_PARAM = {
    'database': 'future_news',
    'ip': '140.143.226.167',
    'port': 27017,
    'username': "nolan",
    'password': "bitcoin_kk",
}


# 新闻抓取频率(分钟)
CRAWL_INTERVAL = 120


# TimeZone
TZCHINA = timezone('Asia/Shanghai')
UTC = timezone('UTC')
TIMEOUT = 60