import pymongo
import json
from rich import print

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = myclient["dell_database"]

collection = my_db["laptops"]
collection.create_index("order_code", unique=True)

with open(r"C:\python practice\dell_scrap\dell_scraped_data.json","r",encoding="utf-8") as f:
    data = json.load(f)

try:
    collection.insert_many(data)
    print("Data inserted successfully")
except Exception as e:
    print("Duplicate products skipped")
    print(e)