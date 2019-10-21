# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode

import scrapy
from scrapy import Request

from behance.items import IndexItem


class BehanceimagesSpider(scrapy.Spider):
    name = 'behanceimages'
    allowed_domains = ['behance.net']
    start_urls = ['http://behance.net/']

    def start_requests(self):
        data = {}
        base_url = 'https://www.behance.net/v2/discover/photography?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['ordinal'] = page * 48
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        if result and result.get('category_projects'):
            for project in result.get('category_projects'):
                indexItem = IndexItem()
                indexItem['id'] = project.get('id')
                indexItem['name'] = project.get('name')
                indexItem['url'] = project.get('url')
                yield indexItem


