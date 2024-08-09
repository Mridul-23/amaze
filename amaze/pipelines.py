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
        

        if item['article_id']:
            item['article_id'] = item['article_id'].strip()
        
        
        if item['product_type']:
            item['product_type'] = item['product_type'].strip()
            

        if item['discounted_price']:
            item['discounted_price'] = item['discounted_price'].strip().replace(',', '').replace('₹', '').strip()

        if item['actual_price']:
            item['actual_price'] = item['actual_price'].strip().replace(',', '').replace('₹', '').strip()
        else:
            item['actual_price'] = item['discounted_price']

        if item['discount']:
            item['discount'] = item['discount'].strip().replace('Off', '').strip()
            if item['discount'] == "(Incl. of all taxes)":
                item['discount'] = "0%"


        if item['sold_by']:
            item['sold_by'] = item['sold_by'].strip()
        

        if item['review_count']:
            item['review_count'] = item['review_count'].strip().replace('(', '').replace(')', '').strip()
        

        if item['images']:
            item['images'] = [ image.split('?')[0] for image in item['images'] if image ]
        

        if item['key_features']:
            item['key_features'] = [feature.replace(" "," ") for feature in item['key_features'] if feature.replace(" "," ")]
            item['key_features'] = [feature.replace("×","x") for feature in item['key_features'] if feature.replace("×","x")]
        
        if item['description']:
            item['description'] = [desc.strip() for desc in item['description'] if desc.strip()]
            item['description'] = [desc.replace("’", "\'") for desc in item['description'] if desc.replace("’", "\'")]

        return item