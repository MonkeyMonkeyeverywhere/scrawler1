from urllib.parse import urlencode

from pyquery import PyQuery as pq
from requests import Session, ReadTimeout

from weixin.config import MAX_FAILED_TIME, VALID_STATUSES
from weixin.db import RedisQueue
from weixin.mysql import Mysql
from weixin.request import WeixinRequest


class Spider(object):
    base_url = 'http://weixin.sogou.com/weixin'
    keyword = '音乐'
    headers = {
        'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Cookie': r'SUV=001FEE0FB4AB4D145D4E81C7735F6459; CXID=3872AB295921C7969B609B319794B3E5; SUID=DDFD41DE4D238B0A5D99F6F900015E3F; ad=mjjoFyllll2NuKbilllllVLBds6lllllT64dTyllllGlllllxA7ll5@@@@@@@@@@; ABTEST=6|1571370396|v1; SNUID=6E003BDB4147D7656C029D4942A59758; IPLOC=JP; weixinIndexVisited=1; JSESSIONID=aaa2tTSrf3Uka_wAXLt1w; ppinf=5|1571370524|1572580124|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0NTolRTYlOUMlQUElRTYlOUQlQTUlRTYlQjQlQkUlRTklODclOEUlRTklODMlOEV8Y3J0OjEwOjE1NzEzNzA1MjR8cmVmbmljazo0NTolRTYlOUMlQUElRTYlOUQlQTUlRTYlQjQlQkUlRTklODclOEUlRTklODMlOEV8dXNlcmlkOjQ0Om85dDJsdUp6Skh6SjJXekRJNVNIN0JheUh3eWtAd2VpeGluLnNvaHUuY29tfA; pprdig=ZfpG28MuceM5w7fSFh4eAwHlAMQM5ZBrGKmneQabQifaB7zs0d9nuvfu6N4nxKYn-efFvLnsOwSx_2gmYrhPr8DGKNC8dAFvlwyYWGP75POvhZ4Vj19fQ0poAkfCUUbRvlXoun7IlKpu3H1IMjpi2TbqnOzYrrsT2Su1njHV3oU; sgid=14-43801777-AV2pNhxOtp76POhiaTPKVXIA; ppmdig=1571370525000000e4a4078b121d23d0465e4258b6a1c1bd; sct=1',
        'Host': 'weixin.sogou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    session = Session()
    queue = RedisQueue()
    mysql = Mysql()

    def get_proxy(self):
        pass

    def start(self):
        """
        构造第一个请求
        :return:
        """
        self.session.headers.update(self.headers)
        request_url = self.base_url + '?' + urlencode({'query': self.keyword, 'type': 2})
        self.queue.add(WeixinRequest(url=request_url, callback=self.parse_index, need_proxy=False))

    def parse_index(self, response):
        """
        解析索引页
        :return:
        """
        doc = pq(response.text)
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            href = item.attr('href')
            yield WeixinRequest(url=href, callback=self.parse_detail, need_proxy=False)
        next_page = doc('#sogou_next').attr('href')
        if next_page:
            url = self.base_url + str(next_page)
            yield WeixinRequest(url=url, callback=self.parse_index, need_proxy=False)

    def parse_detail(self, response):
        """
                解析详情页
                :param response: 响应
                :return: 微信公众号文章
                """
        doc = pq(response.text)
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('.rich_media_content').text(),
            'date': doc('#post-date').text(),
            'nickname': doc('#js_profile_qrcode > div > strong').text(),
            'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        }
        yield data

    def request(self, weixin_request):
        """
        执行请求
        :param weixin_request:
        :return:
        """
        try:
            if weixin_request.need_proxy:
                proxy = self.get_proxy()
                if proxy:
                    proxies = {
                        'http': 'http://' + proxy,
                        'https': 'https://' + proxy
                    }
                    return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout,
                                             allow_redirects=False, proxies=proxies)
            return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout,
                                     allow_redirects=False)
        except (ConnectionError, ReadTimeout) as e:
            print(e)

    def error(self, weixin_request):
        """
        请求错误处理
        :param weixin_request:
        :return:
        """
        weixin_request.fail_time = weixin_request.fail_time + 1
        print('Request Failed', weixin_request.fail_time, 'Times', weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(weixin_request)

    def schedule(self):
        """
        调度
        :return:
        """
        while not self.queue.empty():
            weixin_request = self.queue.pop()
            print('Schedule', weixin_request.url)
            callback = weixin_request.callback
            response = self.request(weixin_request)
            if response and response.status_code in VALID_STATUSES:
                results = list(callback(response))
                if results:
                    for result in results:
                        print('New Result', type(result))
                        if isinstance(result, WeixinRequest):
                            self.queue.add(result)
                        if isinstance(result, dict):
                            self.mysql.insert('articles', result)

    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
