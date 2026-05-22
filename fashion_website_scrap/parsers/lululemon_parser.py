from parsel import Selector
BASE_URL = "https://www.lululemon.com.hk"

def parse_product_page(html,product_url):

    selector = Selector(text=html)

    product_id=selector.xpath("//input[@name='productID']/@value").get()
    product_name = selector.xpath('//meta[@property="og:title"]/@content').get()
    product_price=selector.xpath("//span[@class='markdown-prices']/span[@aria-hidden='true']/text()").get()
    # image_url = selector.xpath('//meta[@property="og:image"]/@content').get()
    image_url=selector.xpath("//div[contains(@class,'image-grid-wrapper')]//picture/img/@data-src").getall()
    description = selector.xpath('//meta[@name="description"]/@content').get()
    product_category =selector.xpath("//div[contains(@class,'container product-detail product-wrapper new-elevated-pdp')]/@data-product-category").get()
    product_size=list(set(selector.xpath("//input[@data-attr-value]/@data-attr-value").getall()))

    return {
        "product_id":product_id,
        "product_name": product_name,
        "product_url":product_url,
        "product_price": product_price,
        "product_category": product_category,
        "product_size":product_size,
        "image_url": image_url,
        "description": description
    }
