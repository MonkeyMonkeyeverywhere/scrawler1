import json
import re

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

regex = re.compile(
    '<dd.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?"name".*?<a.*?>(.*?)</a.*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?"score".*?"integer">(.*?)</i.*?"fraction">(.*?)</i>.*?</dd>',
    re.S)


def item_to_dict(item):
    return {
        'index': item[0],
        'image': item[1],
        'tittle': item[2].strip(),
        'actor': item[3].strip(),
        'time': item[4],
        'score': item[5].strip() + item[5].strip()
    }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        json_res = json.dumps(content, ensure_ascii=False)
        print(json_res)
        f.write(json_res + '\n')


def get_movie_by_page(offset):
    page_res = requests.get('https://maoyan.com/board/4?offset=' + str(offset), headers=headers)
    if 200 == page_res.status_code:
        text = page_res.text
        movie_titles = re.findall(regex, text)
        convert_res = map(item_to_dict, movie_titles)
        for m in convert_res:
            write_to_file(m)


for i in range(10):
    get_movie_by_page(i * 10)
