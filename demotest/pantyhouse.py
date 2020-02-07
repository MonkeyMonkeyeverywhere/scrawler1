import asyncio
import os
from time import sleep

from aiohttp import ClientSession
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "eager"  # 懒加载模式，不等待页面加载完毕
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36')
browser = webdriver.Chrome(options=chrome_options,
                           executable_path='C:\\Users\\lw\\Downloads\\chromedriver_win32\\chromedriver.exe',
                           desired_capabilities=capa)

loop = asyncio.get_event_loop()


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


async def save_pic(filename, url):
    headers = {
        'Cookie': '__cfduid=d32e184c9ba968c5676afc421deb09b651580954283; _ga=GA1.2.2004958734.1580954286; _gid=GA1.2.848701026.1580954286',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    # content = requests.get(url, headers=headers)
    async with ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            response = await response.read()
            with open(filename, 'wb') as f:
                f.write(response)


def get_chapters(index_url):
    url_list = []
    browser.get(index_url)
    browser.implicitly_wait(10)

    # 登陆
    login_flag = check_login()

    if not login_flag:
        username_input = browser.find_element_by_id('ls_username')
        password_input = browser.find_element_by_id('ls_password')

        username_input.send_keys('liluv')
        password_input.send_keys('qwe123!@#')

        browser.find_element_by_class_name('pn').click()
        sleep(5)
        print('登陆成功！')

    title = browser.title.split('【')[0]
    print(title)
    mkdir(title)
    comic_li_list = browser.find_elements_by_class_name('muludiv')

    for li in comic_li_list:
        href = li.find_element_by_tag_name('a').get_attribute("href")
        print(href)
        url_list.append(href)

    print('----获取章节列表完毕----')
    # browser.quit()
    comics = {'name': title, 'urls': url_list}
    return comics


def check_login():
    login_flag = False
    try:
        browser.find_element_by_id('ls_username')
        browser.find_element_by_id('ls_password')
    except:
        login_flag = True
    return login_flag


def get_pic(comics):
    start = 58
    comic_list = comics['urls'][start:]
    base_dir = comics['name']
    for i in range(len(comic_list)):
        new_i = i + start
        sleep(1)
        url = comic_list[i]
        browser.get(url)
        browser.implicitly_wait(5)
        dir_name = base_dir + '/' + base_dir + str(new_i + 1)
        mkdir(dir_name)
        # 漫画一共几张图
        img_list = browser.find_element_by_class_name('uk-zjimg').find_elements_by_tag_name('img')
        page_num = len(img_list)
        print('本章存储目录{}，一共{}页'.format(dir_name, page_num))
        for i in range(page_num):
            # if i > 106:
            print('-----下载图{}/{}-----'.format(str(i + 1), str(page_num)))
            pic_url = img_list[i].get_attribute('src')
            print(pic_url)
            file_name = dir_name + '/' + str(i) + '.png'
            loop.run_until_complete(save_pic(file_name, pic_url))
        print('-----当前章节\t{} 下载完毕-----'.format(browser.title.split('_')[0]))

    # browser.quit()
    print('-----所有章节下载完毕！-----')


if __name__ == '__main__':
    index_list = [
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&a=bofang&kuid=2681', # 连裤袜
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=1025',  # 铁路便当之旅
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=3070',  # 动感假面【1-5卷 全是中文】【已完结】
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=3279',  # 星星的故乡【1-7卷 全是中文】【已完结】
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=3246',  # 升天药局【1-2卷 全是中文】
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=3554',  # 妹妹的反向思考【1-3卷 全是中文】
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=3627',
        # 最强！都立葵坂高校棒球社【1-26卷 全是中文】【最強 ! 都立あおい坂高校野球部／Saikyou! Toritsu Aoizaka】【已完结】
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=1260',  # 艺界修罗道【1-3卷 全是中文】【已完结】
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=1289',  # 暗夜【1-4卷 全是中文】【已完结】
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=2997',  # 东京书店奋斗记【1-7卷 全是中文】【已完结】
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=658',
        # 黄昏的作战【1-4卷 全是中文】【夕ばえ作戦／Yuubae Sakusen】【已完结】
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=925',  # 间谍之家
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=929',  # 电影经纪人
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=993',  # 机神
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=1022'  # 怪物
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=1134',  # 非洲动物上班族
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=1217',  # 对某飞行员的追忆
        # 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&c=index&a=bofang&kuid=1333'  # 监狱学园
    ]
    # for index_url in index_list:
    #     comics = get_chapters(index_url)
    #     sleep(2)
    #     get_pic(comics)
    # browser.quit()

    # 监狱学园16页开始,
    index = 'http://www.zerobyw4.com/plugin.php?id=jameson_manhua&a=bofang&kuid=2681'
    comics = get_chapters(index)
    sleep(2)
    get_pic(comics)
