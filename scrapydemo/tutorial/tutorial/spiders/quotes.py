# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for qoute in quotes:
            item = QuotesItem()
            item['text'] = qoute.css('.text::text').extract_first()
            item['author'] = qoute.css('.author::text').extract_first()
            item['tags'] = qoute.css('.tags .tag::text').extract()
            yield item
        next_page = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next_page)
        print('next page ========================>'+url)
        yield scrapy.Request(url=url, callback=self.parse)
