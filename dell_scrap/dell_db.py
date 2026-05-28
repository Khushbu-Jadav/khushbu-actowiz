import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = myclient["dell_database"]

collection = my_db["laptops"]

with open(r"C:\python practice\dell_scrap\dell_scraped_data.json","r",encoding="utf-8") as f:
    data = json.load(f)

collection.insert_many(data)

print("Data inserted successfully")