from parsel import Selector

def parse_product_page(html,product_url):

    selector = Selector(text=html)

    product_id=selector.xpath("//div[@class='h-stack gap-5']//wishlist-button/@data-product_id").get()
    product_name = selector.xpath("//div[@class='h-stack gap-5']//wishlist-button/@data-product-title").get()
    product_price=selector.xpath("//div[@class='h-stack gap-5']//wishlist-button/@data-product-price").get()
    img_url=list(set(selector.xpath("//scroll-carousel//div[contains(@class,'product-gallery__media')]//img/@src").getall()))
    image_url = ["https:" + img for img in img_url]
    description = selector.xpath('//meta[@name="description"]/@content').get()
    product_category =selector.xpath("//div[@class='h-stack gap-5']//wishlist-button/@data-product-category").get()
    product_size=list(set(selector.xpath("//label[contains(@class,'block-swatch')]//span/text()").getall()))

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
