# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from itemadapter import ItemAdapter
from .items import BluorngItem



class BluorngPipeline:

        def process_item(self, item, spider):
            if isinstance(item,BluorngItem):
                my_conn=mysql.connector.connect(
                    user="root",
                    host="localhost",
                    password="actowiz",
                    database=None
                )
                my_cur=my_conn.cursor()
                my_cur.execute("CREATE DATABASE IF NOT EXISTS blueorng")
                my_conn.connect(database="blueorng")
                my_cur.execute("""CREATE TABLE IF NOT EXISTS blueorng_details(
                            id int primary key not null auto_increment,
                            product_name TEXT,
                            product_url TEXT,
                            product_price TEXT)
                            """)
                
                
                my_cur.execute("INSERT INTO blueorng_details(product_name,product_url,product_price) values(%s,%s,%s)",
                                (item.get('product_name'),
                                item.get('product_url'),
                                item.get('product_price'),
                                ))
                
                my_conn.commit()
                my_conn.close()
                return item
            print("data inserted")