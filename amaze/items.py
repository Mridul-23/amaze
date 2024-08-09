# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazeItem(scrapy.Item):
    name = scrapy.Field()
    article_id = scrapy.Field()
    product_type = scrapy.Field()
    discounted_price = scrapy.Field()
    actual_price = scrapy.Field()
    discount = scrapy.Field()
    sold_by = scrapy.Field()
    review_count = scrapy.Field()
    images = scrapy.Field()
    key_features = scrapy.Field()
    description = scrapy.Field()