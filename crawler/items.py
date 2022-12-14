# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    vote = scrapy.Field()
    answer = scrapy.Field()
    view = scrapy.Field()
    pass
