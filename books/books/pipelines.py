# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import BooksItem
import mysql.connector

class BooksPipeline:
      def process_item(self, item, spider):
        pass
        if isinstance(item,BooksItem):
            conn=mysql.connector.connect(
                user="root",
                host="localhost",
                password="actowiz",
                database=None
            )
            cur=conn.cursor()
            cur.execute("create database if not exists books_db")
            conn.connect(database="books_db")
            cur.execute("""create table if not exists books_data(
                        id int primary key not null auto_increment,
                        book_url VARCHAR(255),
                        book_title TEXT,
                        book_price varchar(255),
                        book_image VARCHAR(500),
                        in_stock VARCHAR(255),
                        rating VARCHAR(255)
                        )
                    """)
            cur.execute("INSERT INTO books_data(book_url,book_title,book_price,book_image,in_stock,rating) values(%s,%s,%s,%s,%s,%s)",
                                (
                                item.get('book_url'),
                                item.get('book_title'),
                                item.get('book_price'),
                                item.get('book_image'),
                                item.get('in_stock'),
                                item.get('rating')
                                ))
            conn.commit()
            conn.close()
            return item
        print("data inserted")

