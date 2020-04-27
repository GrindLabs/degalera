# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MitieBotItem(scrapy.Item):
    name = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    flyer = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    lowest_price_ticket = scrapy.Field()
    tags = scrapy.Field()
    sourceId = scrapy.Field()
    created_at = scrapy.Field()
