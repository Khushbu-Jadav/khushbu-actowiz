import json
from lxml import html
from rich import print
import requests

result = []
base_url = "https://quotes.toscrape.com"

for i in range(1,11):
    url=f"{base_url}/page/{i}/"
    response=requests.get(url)
    tree=html.fromstring(response.content)
    quotes=tree.xpath("//div[contains(@class,'quote')]")
 
    for quote in quotes:
        line=quote.xpath(".//span[contains(@class,'text')]/text()")[0]
        author=quote.xpath(".//small[@class='author']/text()")[0]
        
        about=quote.xpath(".//span//a/@href")[0]
        about_author=base_url+about

        tags = quote.xpath(".//div[@class='tags']//a[@class='tag']/@href")
        tag_links = [base_url + t for t in tags]

        result.append({
            "line":line,
            "author":author,
            "about_author":about_author,
            "tags": tag_links
        })

print(result)

with open(r"C:\python practice\day13\quotes_to_scrap.json","w",encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False)

print(len(result))