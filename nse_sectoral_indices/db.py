import pymongo
import json
from rich import print
import jmespath

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = myclient["nse_db"]

collection = my_db["sectoral_indices"]
collection.delete_many({})

top_coll=my_db["top_gainers"]
top_coll.delete_many({})

bottom_coll=my_db["bottom_losers"]
bottom_coll.delete_many({})

with open(r"C:\python practice\nse_sectoral_indices\scraped_sectoral_data.json","r",encoding="utf-8") as f:
    data = json.load(f)

all_stocks = jmespath.search("[*].sectoral_data[]", data)

seen = set()
unique_stocks = []
for stock in all_stocks:
    if stock["symbol"] not in seen:
        seen.add(stock["symbol"])
        unique_stocks.append(stock)

top_20_gainers = sorted(unique_stocks, key=lambda x: x["change_percentage"] or 0, reverse=True)[:20]
bottom_20_losers = sorted(unique_stocks, key=lambda x: x["change_percentage"] or 0, reverse=False)[:20]

try:
    collection.insert_many(data)
    top_coll.insert_many(top_20_gainers)
    bottom_coll.insert_many(bottom_20_losers)
    print("Data inserted successfully")
except Exception as e:
    print("Duplicate products skipped")
    print(e)