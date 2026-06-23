import scrapy
import jmespath
from rich import print
import json
import gzip
import re
from ..items import InstamartItem

class InstamartScrapeSpider(scrapy.Spider):
    name = "instamart_scrape"
    allowed_domains = ["instamart.in"]
    start_urls = ["https://instamart.in"]

    def parse(self, response):
        # print(response.body)
        file_name=response.url

        with gzip.open(f"C:/websites_pages/instamart_pages/{file_name}.html.gz",'wb') as f:
            f.write(response.body)

        category_urls=response.xpath("//ul[@class='_1bnFr']//li[@class='_2lXSA _3Lhg6']//a//@href").getall()
        print(category_urls)

        with open("json_script.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        self.products_data = []

        product_name=jmespath.search("productV2.itemData.displayName",data)
        product_desc=jmespath.search("productV2.itemData.variations[*].shortDescription",data)[0]
        product_price=jmespath.search("productV2.itemData.variations[*].price.offerPrice.units",data)[0]
        product_image=jmespath.search("productV2.itemData.variations[*].imageIds",data)[0]
        product_quantity=jmespath.search("productV2.itemData.variations[*].quantityDescription",data)[0]

        item=InstamartItem()
        item["product_name"]=product_name
        item["product_description"]=product_desc
        item["product_price"]=product_price
        item["product_images"]=product_image
        item["product_quantity"]=product_quantity

        yield item

        # print("product_name:",product_name)
        # print("product_description:",product_desc)
        # print("product_price:",product_price)
        # print("product_images:",product_image)
        # print("product_quantity:",product_quantity)
        
        # print(product_urls)
       
        
