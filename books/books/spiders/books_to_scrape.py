import scrapy
from books.items import BooksItem
import json
import gzip
import hashlib
from rich import print

class BooksToScrapeSpider(scrapy.Spider):
    name = "books_to_scrape"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    books_data=[]


    def parse(self, response):
        # file_hash = hashlib.sha256(response.url.encode("utf-8")).hexdigest()

        # with gzip.open(rf"C:\websites_pages\books_pages\{file_hash}.html.gz","wb") as f:
        #     f.write(response.body)

        category_urls = response.xpath("//ul[@class='nav nav-list']//ul//a/@href").getall()

        for category_url in category_urls:
            yield scrapy.Request(response.urljoin(category_url),callback=self.parse_category)

            file_hash = hashlib.sha256(response.url.encode("utf-8")).hexdigest()

            with gzip.open(rf"C:\websites_pages\books_pages\{file_hash}.html.gz","wb") as f:
                f.write(response.body)

    def parse_category(self, response):
        file_hash = hashlib.sha256(response.url.encode("utf-8")).hexdigest()

        with gzip.open(rf"C:\websites_pages\books_pages\{file_hash}.html.gz","wb") as f:
            f.write(response.body)

        category_name = response.xpath("//div[@class='page-header action']/h1/text()").get()

        books = response.xpath("//article[@class='product_pod']")

        for book in books:
            book_url = book.xpath(".//h3/a/@href").get()
            book_title = book.xpath(".//h3/a/@title").get()
            book_image = book.xpath(".//div[@class='image_container']//img/@src").get()
            book_price = book.xpath(".//p[@class='price_color']/text()").get()
            in_stock = "".join(book.xpath(".//p[@class='instock availability']//text()").getall()).strip()

            rating = (book.xpath(".//p[starts-with(@class,'star-rating')]/@class").get().split()[-1])

            item = BooksItem()

            item["category_name"] = category_name
            item["book_url"] = response.urljoin(book_url)
            item["book_title"] = book_title
            item["book_image"] = response.urljoin(book_image)
            item["book_price"] = book_price
            item["in_stock"] = in_stock
            item["rating"] = rating

            self.books_data.append(dict(item))

            yield item
            print(item)

        next_page = response.xpath("//li[@class='next']/a/@href").get()

        if next_page:
            yield scrapy.Request(response.urljoin(next_page),callback=self.parse_category)

        with open("books_data.json","w",encoding="utf-8") as f:
            json.dump(self.books_data,f,indent=4,ensure_ascii=False)


