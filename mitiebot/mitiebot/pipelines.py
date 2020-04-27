# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
import time

from pymongo import MongoClient

from mitiebot.settings import logger


class MongoBasePipeline(object):
    collection_name = 'events'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_CONN_URI'),
            mongo_db=crawler.settings.get('MONGODB_DB_NAME')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        return item


class MongoPipeline(MongoBasePipeline):
    def process_item(self, item, spider):
        logger.debug('Updating "{0}" collection with item: {1}'.format(
            self.collection_name, item))
        result = self.db[self.collection_name].update_one(
            {
                'link': item.get('link'),
                'sourceId': item.get('source_id')
            },
            {
                '$set': {
                    'name': item.get('name'),
                    'location': item.get('location'),
                    'date': item.get('date'),
                    'flyer': item.get('flyer'),
                    'link': item.get('link'),
                    'description': item.get('description'),
                    'lowestPriceTicket': item.get('lowest_price_ticket'),
                    'tags': item.get('tags'),
                    'sourceId': item.get('source_id'),
                    'createdAt': datetime.datetime.utcfromtimestamp(
                        time.time())
                }
            },
            upsert=True
        )
        logger.info('Event {0} successfully: {1}'.format(
            'updated' if result.modified_count else 'created',
            item.get('name')))
        return item
