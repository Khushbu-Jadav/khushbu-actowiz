import json
from rich import print
from lxml import html
from curl_cffi import requests

#response=requests.get("https://www.pcmag.com/picks/the-best-laptops",impersonate="chrome120")
response=requests.get("https://www.pcmag.com/picks/the-best-headphones",impersonate="chrome120")
data=response.content.decode('utf-8')

result=[]
tree=html.fromstring(data)

url="https://www.pcmag.com"

products=tree.xpath("//div[contains(@class, 'flex flex-col gap-6')]//div[contains(@class, 'flex flex-col gap-y-6')]")

for product in products:
    heading=product.xpath(".//div[contains(@class,'flex flex-wrap items-center justify-start text-sm font-bold leading-tight')]/text()")
    product_name=product.xpath(".//h3[@class='font-stretch-condensed line-clamp-3 text-base font-bold leading-tight md:w-full']//a/text()")
    product_url=product.xpath(".//h3[@class='font-stretch-condensed line-clamp-3 text-base font-bold leading-tight md:w-full']//a/@href")
    product_img =product.xpath(".//img[@class = 'order-last aspect-video w-[120px] border border-gray-300 md:order-first']//@data-image-loader")
    price=product.xpath(".//span[@class='inline-block']/text()")
    description = product.xpath(".//p[@class = 'text-sm leading-normal']/text()")
    # pros=product.xpath(".//h4[contains(text(),'Pros')]/following-sibling::ul//li//span/text()")
    
    pros = [p.strip() for p in product.xpath(".//h4[contains(text(),'Pros')]/following-sibling::ul/li//text()")if p.strip()]

    # cons=product.xpath(".//h4[contains(text(),'Cons')]/following-sibling::ul//li//span/text()")

    cons=[p.strip() for p in product.xpath(".//h4[contains(text(),'Cons')]/following-sibling::ul//li//span/text()")if p.strip()]
    rating = product.xpath(".//div[@class = 'text-sm']/text()")
    review=product.xpath(".//a[@class='inline-flex w-fit text-sm font-bold text-red-400 underline hover:text-red-500']/@href")

    result.append({
        "heading":heading[0].strip() if heading else None,
        "product_name":product_name[0].strip(),
        "product_url":product_url[0].strip(),
        "image_url":product_img[0].strip(),
        "product_price":price[0].strip().split('$')[1],
        "product_description":description[0].strip(),
        "pros":pros,
        "cons":cons,
        "rating":rating[0].strip(),
        "review":url+review[0] if review else None
    })

print(result)

with open(r"C:\python practice\pcmag_scrap\pcmag_scraped_data.json","w",encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False)