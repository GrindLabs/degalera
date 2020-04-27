import scrapy
from pymongo import MongoClient

from mitiebot import settings
from mitiebot.settings import logger


class DefaultSpider(scrapy.Spider):
    """
    This spider is just a template for the future spiders.
    
    Please, remove it or rename this file and class with the name of your 
    first spider.
    """
    name = 'default'

    def __init__(self, *args, **kwargs):
        super(DefaultSpider, self).__init__(*args, **kwargs)
        self.client = MongoClient(settings.MONGODB_CONN_URI)
        self.db = self.client.get_database(settings.MONGODB_DB_NAME)
        # self.start_urls = <the URLs must come from the database>
        # self.allowed_domains = <the domain list must come from the database>
        self.client.close()

    def parse(self, response):
        pass
