# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode

import scrapy
from scrapy import Request

from image360.items import ImageItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        data = {}
        base_url = 'https://images.so.com/zj?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        if result and result.get('list'):
            for image in result.get('list'):
                item = ImageItem()
                item['id'] = image.get('id')
                item['url'] = image.get('qhimg_url')
                item['title'] = image.get('group_title')
                item['thumb'] = image.get('qhimg_thumb_url')
                yield item
