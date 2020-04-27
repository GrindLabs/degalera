# -*- coding: utf-8 -*-

# Define here the loaders for your items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/loaders.html

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
from slugify import slugify

from mitiebot.items import MitieBotItem


class MitieBotItemLoader(ItemLoader):
    default_item_class = MitieBotItem
    default_output_processor = TakeFirst()
    tags_in = MapCompose(slugify, lambda t: t.split('-'))
    lowest_price_ticket_in = MapCompose(lambda p: float('{0:.2f}'.format(p)))
