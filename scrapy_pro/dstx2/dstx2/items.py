# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Dstx2Item(scrapy.Item):
    num = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
