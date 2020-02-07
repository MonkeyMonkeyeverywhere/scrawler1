import os
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "eager"  # 懒加载模式，不等待页面加载完毕
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36')
browser = webdriver.Chrome(options=chrome_options,
                           executable_path='C:\\Users\\lw\\Downloads\\chromedriver_win32\\chromedriver.exe',
                           desired_capabilities=capa)


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def save_pic(filename, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    content = requests.get(url, headers=headers).content
    with open(filename, 'wb') as f:
        f.write(content)


def get_chapters(index_url):
    url_list = []
    browser.get(index_url)
    browser.implicitly_wait(10)

    title = browser.title.split('_')[0]
    # print(title)
    mkdir(title)
    comic_li_list = browser.find_element_by_id('chapter-list-0').find_elements_by_tag_name('li')

    for li in comic_li_list:
        href = li.find_element_by_tag_name('a').get_attribute("href")
        print(href)
        url_list.append(href)

    print('----获取章节列表完毕----')
    # browser.quit()
    comics = {'name': title, 'urls': url_list}
    return comics


def get_pic(comics):
    comic_list = comics['urls']
    base_dir = comics['name']
    wait = WebDriverWait(browser, 30)
    for url in comic_list[0:2]:
        browser.get(url)
        browser.implicitly_wait(5)
        dir_name = base_dir + '/' + browser.title.split('_')[0]
        mkdir(dir_name)
        # 漫画一共多少页
        page_num = len(browser.find_elements_by_tag_name('option'))
        print('本章存储目录{}，一共{}页'.format(dir_name, page_num))
        # 找到下一页按钮
        wait.until(EC.presence_of_element_located((By.ID, 'next')))
        next_page = browser.find_element_by_id('next')
        for i in range(page_num):
            sleep(2)
            print('----第{}页----'.format(str(i + 1)))
            wait.until(EC.presence_of_element_located((By.ID, 'mangaFile')))
            pic_url = browser.find_element_by_id('mangaFile').get_attribute('src')
            print(pic_url)
            file_name = dir_name + '/' + str(i) + '.jpg'
            save_pic(file_name, pic_url)
            next_page.click()
        print('-----当前章节\t{} 下载完毕-----'.format(browser.title.split('_')[0]))

    browser.quit()
    print('-----所有章节下载完毕！-----')


if __name__ == '__main__':
    comics = get_chapters('https://tw.manhuagui.com/comic/34860/')
    sleep(2)
    get_pic(comics)
