import json
from idlelib.iomenu import encoding

from rich import print
import jmespath

with open("vans.json","r",encoding="utf-8") as f:
    data=json.load(f)
    res_data=[]

    for product in jmespath.search("products[*]", data):
        # for gallery in jmespath.search("gallery[*]", product):
            res_data.append({
                "product_name":jmespath.search("name",product),
                "image_url": jmespath.search("gallery[*].src", product),
                "product_link": "https://www.vans.com/" + jmespath.search("url",product),
                "price":jmespath.search("price.highOriginal",product),
                "discount":float(jmespath.search("price.highOriginal",product)-jmespath.search("price.highCurrent",product))
            })

print(res_data)

with open('vans_data.json', 'w', encoding='utf-8') as f:
    json.dump(res_data, f, indent=4)