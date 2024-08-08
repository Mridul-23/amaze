# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AmazePipeline:
    def process_item(self, item, spider):

        if item['name']:
            item['name'] = item['name'].strip()
        

        if item['id']:
            item['id'] = item['id'].strip()
        

        if item['dicounted_price']:
            item['dicounted_price'] = item['dicounted_price'].strip().replace(',', '').replace('₹', '').strip()
        

        if item['actual_price']:
            item['actual_price'] = item['actual_price'].strip().replace(',', '').replace('₹', '').strip()
        

        if item['dicount']:
            item['dicount'] = item['dicount'].strip().replace('%', '').strip()
        

        if item['Sold_by']:
            item['Sold_by'] = item['Sold_by'].strip()
        

        if item['review_count']:
            item['review_count'] = item['review_count'].strip().replace('(', '').replace(')', '').strip()
        

        if item['images']:
            item['images'] = [image.strip() for image in item['images'] if image.strip()]
        

        if item['Key_features']:
            item['Key_features'] = [feature.strip() for feature in item['Key_features'] if feature.strip()]
        

        if item['discription']:
            item['discription'] = [desc.strip() for desc in item['discription'] if desc.strip()]

        return item