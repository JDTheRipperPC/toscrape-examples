# -*- coding: utf-8 -*-
import scrapy


class ByCategorySpider(scrapy.Spider):
    name = 'by_category'
    allowed_domains = ['books.toscrape.com']

    def __init__(self, category=None, *args, **kwargs):
        super(ByCategorySpider, self).__init__(*args, **kwargs)
        if category is None:
            raise ValueError('Argument category is None.')
        # TODO: validate category exists
        self.start_urls = [
            'http://books.toscrape.com/catalogue/category/books/{code}'.format(
                code=category)
        ]

    def parse(self, response):
        for article in response.xpath('//article'):
            yield {
                'name': article.css('h3 a::text').get().encode('utf-8'),
                'price': article.css('div[@class="product_price"]')
            }
