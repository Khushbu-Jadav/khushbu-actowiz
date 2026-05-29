import pymongo
import json
from rich import print

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = myclient["eat_sure_db"]

collection = my_db["restaurants"]
collection.delete_many({})

with open(r"C:\python practice\eat_sure_scrape\scraped_data.json","r",encoding="utf-8") as f:
    data = json.load(f)

try:
    collection.insert_many(data)
    print("Data inserted successfully")
except Exception as e:
    print("Duplicate products skipped")
    print(e)