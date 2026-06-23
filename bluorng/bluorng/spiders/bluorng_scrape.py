import scrapy
import gzip
import os
import json
from scrapy.cmdline import execute
from bluorng.items import BluorngItem

class BluorngScrapeSpider(scrapy.Spider):
    name = "bluorng_scrape"
    allowed_domains = ["bluorng.com"]
    start_urls = ["https://bluorng.com/collections/summer-basics"]

    def parse(self, response):
        base_url = "https://bluorng.com"
        file_name=response.url.split("/")[-1]

        with gzip.open(f"C:/websites_pages/bluorng_pages/{file_name}.html.gz",'wb') as f:
            f.write(response.body)

        products = response.xpath("//div[contains(@class,'card-wrapper')]")
        self.products_data = []

        for product in products:
            href = product.xpath(".//a/@href").get()
            name = product.xpath(".//h3[contains(@class,'card__heading')]/a/text()").get()
            price = product.xpath(".//span[@class='price-item price-item--sale price-item--last']/text()").get()

            item = BluorngItem()
            item["product_url"] = base_url + href if href else None
            item["product_name"] = name.strip() if name else None
            item["product_price"] = price.strip().replace("RS. ", "") if price else None

            self.products_data.append(dict(item))

            yield item

            file_name=item["product_url"].split("/")[-1]

            with gzip.open(f"C:/websites_pages/bluorng_pages/{file_name}.html.gz",'wb') as f:
                f.write(response.body)

        print(self.products_data)
        with open("products.json", "w", encoding="utf-8") as f:
            json.dump(self.products_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    execute("scrapy crawl bluorng_scrape".split())


