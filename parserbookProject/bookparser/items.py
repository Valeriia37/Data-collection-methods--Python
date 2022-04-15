# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookparserItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    authors = scrapy.Field()
    old_price = scrapy.Field()
    new_price = scrapy.Field()
    rating = scrapy.Field()
    _id = scrapy.Field()
    pass
