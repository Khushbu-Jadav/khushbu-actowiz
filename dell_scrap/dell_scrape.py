import json
from rich import print
from lxml import html
from curl_cffi import requests

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://www.dellstore.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.dellstore.com/',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
}

response=requests.get("https://www.dellstore.com/laptops.html",headers=headers,impersonate="chrome120")
data=response.content.decode('utf-8')
base_url="https://www.dellstore.com/laptops.html"
result=[]

for page in range(1, 8):

    page_url = f"{base_url}?p={page}"
    response = requests.get(page_url,headers=headers,impersonate="chrome120")

    tree = html.fromstring(response.text)

    url="https:"

    category=tree.xpath("//ul[contains(@aria-label,'Computers & Accessories')]//a")
    products=tree.xpath("//div[@class='product-item-info']")
   
    for product in products:
        product_url=product.xpath(".//a[@class='product-item-link']/@href")
        product_name=product.xpath(".//strong//a[@class='product-item-link']/text()")
        product_price=product.xpath(".//span[@class='price']/text()")[0].replace("₹", "").replace(",", "").strip()
        product_images = product.xpath(".//img/@src")
        technical_specs = product.xpath(".//ul[@class='cf-hero-bts-list']/li")
        technical_details = {}

        for spec in technical_specs:
            key = spec.xpath("normalize-space(.//div[@class='ux-module-title'])")
            value = spec.xpath("normalize-space(.//div[@class='ux-module-content'])")

            if key and value:
                technical_details[key] = value

        offer_blocks = product.xpath(".//div[@class='modalpdpdata']/div[@class='offer-title']")

        special_offers = []

        for offer in offer_blocks:
            offer_title = offer.xpath("normalize-space(.//a)")
            offer_description = offer.xpath("normalize-space(following-sibling::div[@class='offer-description'][1])")
            special_offers.append({
                "offer_title": offer_title,
                "offer_description": offer_description
            })

        order_code = product.xpath(".//div[@class = 'ps-oc']/text()")[0].split(" ")[-1]
      
        result.append({
            "product_name":product_name[0].strip(),
            "product_url":product_url[0].strip(),
            "product_price":product_price,
            "product_images":product_images,
            "technical_details":technical_details,
            "special_offers": special_offers,
            "order_code":order_code
        })

print(result)
print(len(result))

with open(r"C:\python practice\dell_scrap\dell_scraped_data.json","w",encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False)