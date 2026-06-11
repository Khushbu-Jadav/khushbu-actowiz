import pymongo
import json
from rich import print

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = myclient["carwale_database"]

collection = my_db["cars"]
collection.delete_many({})

with open(r"C:\python practice\carwale\carwale_data.json","r",encoding="utf-8") as f:
    data = json.load(f)

try:
    collection.insert_many(data)
    print("Data inserted successfully")
except Exception as e:
    print("Duplicate products skipped")
    print(e)