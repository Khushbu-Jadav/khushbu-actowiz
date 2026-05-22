from parsel import Selector

def parse_product_page(html,product_url):

    selector = Selector(text=html)

    product_id=selector.xpath("//div/@data-flits-product-id").get()
    product_name = selector.xpath('//meta[@property="og:title"]/@content').get()
    product_price=selector.xpath("//meta[@property='og:price:amount']/@content").get()
    img_url=selector.xpath("//div[contains(@class,'product-single__media')]//img/@src").getall()
    image_url = ["https:" + img for img in img_url]
    description = selector.xpath('//meta[@property="og:description"]/@content').get()
    product_category =selector.xpath("//nav[contains(@class,'breadcrumbs')]/text()[last()]").get().strip()
    #product_size = selector.xpath("//input[@name='Size' and (contains(@checked,'checked') or not(contains(@class,'is-disabled')))]/@value").getall()
    product_size=selector.xpath("//input[@name='Size']/@value").getall()
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
