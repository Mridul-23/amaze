# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazeItem(scrapy.Item):
    name = scrapy.Field()
    id = scrapy.Field()
    dicounted_price = scrapy.Field()
    actual_price = scrapy.Field()
    dicount = scrapy.Field()
    Sold_by = scrapy.Field()
    review_count = scrapy.Field()
    images = scrapy.Field()
    Key_features = scrapy.Field()
    discription = scrapy.Field()