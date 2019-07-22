# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class JsonWritePipeline(object):

    def __init__(self, filedir, filename):
        self.filedir = filedir
        self.filename = filename

    @classmethod
    def from_crawler(cls, crawler):
        import pdb; pdb.set_trace()
        return cls(
            filedir=crawler.settings.get('JSON_FILEDIR'),
            filename=crawler.settings.get('JSON_FILENAME')
        )

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        pass


class BooksToscrapeComPipeline(object):
    def process_item(self, item, spider):
        return item
