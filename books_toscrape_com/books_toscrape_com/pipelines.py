# -*- coding: utf-8 -*-
import os


class JsonPipeline(object):

    def __init__(self, filename):
        self.filename = filename
        self.f = open(self.filename, 'w')

    @classmethod
    def from_crawler(cls, crawler):
        nameformat = crawler.settings.get('JSON_PIPELINE_FORMAT')
        name = nameformat % {
            "name": crawler.spider.name,
            "json_filename": getattr(crawler.spider, 'json_filename', crawler.spider.name)
        }
        # import pdb; pdb.set_trace()
        return cls(
            filename='{directory}{name}'.format(
                directory=crawler.settings.get('JSON_PIPELINE_OUTPUT'),
                name=name
            )
        )

    def open_spider(self, spider):
        self.f.write('[\n')

    def close_spider(self, spider):
        self.f.write(']\n')
    
    def process_item(self, item, spider):
        self.f.write('{item}\n'.format(item=item))


class BooksToscrapeComPipeline(object):
    def process_item(self, item, spider):
        return item
