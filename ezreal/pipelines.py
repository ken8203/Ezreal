# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from playhouse.sqlite_ext import SqliteExtDatabase
from ezreal.models import Poems

class PreprocessingPipeline(object):
    def process_item(self, item, spider):
        pattern = r"：(.*?)\n"
        for key in item.keys():
            match = re.search(pattern, item[key])
            if match:
                item[key] = match.group(1)
        return item

class SqlitePipeline(object):
    def open_spider(self, spider):
        Poems.create_table()

    def process_item(self, item, spider):
        Poems.create(**item)
        return item
