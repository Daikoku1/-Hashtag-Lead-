# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InstascrapyEachItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    each_url = scrapy.Field()
    each_location = scrapy.Field()
    address_json = scrapy.Field()
    hash_tag = scrapy.Field()
    text = scrapy.Field()
    idx_name = scrapy.Field()