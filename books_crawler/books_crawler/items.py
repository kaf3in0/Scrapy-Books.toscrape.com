# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    stock = scrapy.Field()
    description= scrapy.Field()
    rating= scrapy.Field()
    price= scrapy.Field()
    title = scrapy.Field()

    # Those are not just simple containers
    # They are reserved scrapy fields
    image_urls = scrapy.Field()
    images = scrapy.Field()
    