import scrapy
from amaze.items import AmazeItem

class ItemspiderSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["jiomart.com"]
    start_urls = ["https://www.jiomart.com/c/electronics/mobiles-tablets/mobiles/32118"]

    custom_settings = {
        'DOWNLOAD_DELAY': 2,  
        'CONCURRENT_REQUESTS': 1,  
        'AUTOTHROTTLE_ENABLED': True, 
        'AUTOTHROTTLE_START_DELAY': 2,  
        'AUTOTHROTTLE_MAX_DELAY': 10,  
        'FEEDS': {'yourFileName.json': {'format': 'json', 'overwrite': False}}
    }

    def parse(self, response):
        items = response.css('.plp-card-wrapper')[:100]
        for item in items:
            url = item.css('.plp-card-wrapper::attr(href)').get()
            yield response.follow(url, callback=self.parse_item)

    def parse_item(self, response):
        price_span = response.css('.product-price span::text').getall()
        
        item = AmazeItem()

        item['name'] = response.css("#pdp_product_name::text").get()
        item['article_id'] = response.css(".product-article-detail span::text").get()
        item['product_type'] = response.xpath("//th[contains(text(), 'Product Type')]/following-sibling::td/text()").get()
        item['discounted_price'] = price_span[0]
        item['actual_price'] = response.css(".line-through::text").get()
        item['discount'] = price_span[1]
        item['sold_by'] = response.css("#buybox_soldby_container h2::text").get()
        item['review_count'] = response.css(".review-count::text").get()
        item['images'] = response.css(".swiper-thumb-slides-img::attr(src)").getall()
        item['key_features'] = response.css(".product-key-features-list li::text").getall()
        item['description'] = response.css("#pdp_description::text").getall()

        yield item
