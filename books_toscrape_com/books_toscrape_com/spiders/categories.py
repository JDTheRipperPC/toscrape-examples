# -*- coding: utf-8 -*-
import scrapy

from ..items import BookCategory


class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        atags = response.xpath('//ul[@class="nav nav-list"]/li/ul/li/a')
        for tag in atags:
            yield BookCategory(
                href=tag.attrib['href'],
                name=tag.attrib['href'].split('/')[3],
                category=tag.css('*::text').get().strip()
            )
