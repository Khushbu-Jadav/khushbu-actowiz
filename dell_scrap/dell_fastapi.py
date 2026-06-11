from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List
import json

app=FastAPI()

client=MongoClient("mongodb://localhost:27017")

db=client["dell_database"]
collection=db["laptops"]

new_db=client["new_dell_database"]
new_collection=new_db["laptops"]

class Product(BaseModel):
    category_url:str
    product_name:str
    product_url:str
    product_price:float
    product_images:List[str]

@app.get("/products/{product_url:path}")
def get_product(product_url:str):
    product=collection.find_one({"product_url":product_url},{"_id":0})
    if not product:
        return {"error":"product not found"}
    return product

@app.post("/products/import")
def import_products():
    with open("C:\python practice\dell_scrap\dell_scraped_data.json", "r", encoding="utf-8") as f:
        products = json.load(f)

    new_collection.delete_many({})

    for p in products:
        product = Product(**p)
        new_collection.insert_one(product.dict())

    return {"message": f"{len(products)} products imported successfully"}