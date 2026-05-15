from rich import print
import json
from lxml import html

with open(r"C:\python practice\day12\burgerking_location.html","r",encoding='utf-8') as f :
    data=f.read()

tree=html.fromstring(data)
locations=[]

stores = tree.xpath("//div[@class='store-info-box']")

for store in stores:
    outlet_name=store.xpath(".//li[@class='outlet-name']/div[@class='info-text']/a/@title")[0]

    address=" ".join(x.replace("                      ", " ").replace("\n ","") for x in store.xpath(".//li[@class='outlet-address']/div[@class='info-text']//span//text()"))
    res_add=address.split("-")[0].strip()

    pincode=store.xpath(".//li[@class='outlet-address']//span[@class='merge-in-next']//span[last()]/text()")[0]
    timing=store.xpath(".//li[@class='outlet-timings']//div[@class='info-text']//span/text()")[0]
    phone_number=store.xpath(".//li[@class='outlet-phone']/div[@class='info-text']/a/text()")[0].strip()
    website=store.xpath(".//li[@class='outlet-actions']//a[@class='btn btn-website']/@href")[0]
    map=store.xpath(".//li[@class='outlet-actions']//a[@class='btn btn-website']/@href")[0]

    
    locations.append({
        "name":outlet_name,
        "restarant_address":res_add,
        "pincode":pincode,
        "timing":timing,
        "phone_number":phone_number,
        "map":map,
        "website_link":website
    })

print(locations)

with open(r"C:\python practice\day12\burger_king.json","w",encoding='utf-8') as f:
    json.dump(locations,f,indent=4)