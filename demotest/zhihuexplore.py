import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}


def get_zhihu_collection_by_page(page):
    page_res = requests.get('https://www.zhihu.com/collection/31180103?page=' + str(page), headers=headers)
    if 200 == page_res.status_code:
        soup = BeautifulSoup(page_res.text, 'lxml')
        question_div = soup.select('.zm-item')
        for item in question_div:
            question = item.find('h2').find('a').get_text()
            author = item.find(class_="author-link").get_text() if item.find(class_="author-link") else ''
            answer = item.find(class_='js-collapse-body').find(class_='content').get_text()
            print(question + '\n' + author + '\n' + answer + '\n')
            print('\n====================================\n')
            with open('zhihu_collect.txt', 'a', encoding='utf-8') as f:
                f.write(question + '\n' + author + '\n' + answer + '\n')
                f.write('\n====================================\n')


for i in range(10):
    get_zhihu_collection_by_page(i + 1)
