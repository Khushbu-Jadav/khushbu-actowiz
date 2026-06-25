# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category_name=scrapy.Field()
    book_title=scrapy.Field()
    book_url=scrapy.Field()
    book_image=scrapy.Field()
    book_price=scrapy.Field()
    in_stock=scrapy.Field()
    rating=scrapy.Field()
    

    
