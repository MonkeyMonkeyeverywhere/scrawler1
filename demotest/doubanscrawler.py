import time
from urllib.parse import urlencode
from venv import logger

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}


def get_page(offset):
    params = {
        'q': 'jay',
        'start': offset,
        'cat': 1003
    }
    url = 'https://www.douban.com/j/search?' + urlencode(params)
    try:
        res = requests.get(url)
        items_json = res.json()['items']
        for i in items_json:
            soup = BeautifulSoup(i, 'lxml')
            print(soup.find('a')['title'])
            print('\n=================================\n')
    except Exception:
        logger.info('request error')


for i in range(10):
    print('========爬取第%s页========\n' % (i + 1))
    get_page(i * 10)
    time.sleep(1)
