from rich import print
from lxml import html
from curl_cffi import requests
import jmespath
import json
import time

url="https://tv.apple.com/in"
response=requests.get(url,impersonate="chrome120")

result=[]

with open(r"C:\python practice\apple_tv_scrape\apple_json_data.json","r",encoding="utf-8") as f:
    data = json.load(f)

categories=jmespath.search("data[].data.shelves[7].items[].contextAction.url[]",data)

for cate in categories:
    cate_respose=requests.get(cate)
    new_data=cate_respose.text
    tree=html.fromstring(new_data)

    sub_categories=tree.xpath("//h2[contains(@class,'title svelte-wpob41 title-link')]/a/@href")
    shows=tree.xpath("//div[contains(@class,'lockup-container svelte-n3nezg')]/a/@href")

    for show_url in shows:
        time.sleep(1)
        shows_response = requests.get(show_url,impersonate="chrome120",timeout=30)
        show_data = shows_response.text
       
        show_tree = html.fromstring(show_data)
        scripts=show_tree.xpath("//script[@type='application/json']/text()")
        
        title = None
        
        for script in scripts:
            try:
                json_data = json.loads(script)
                title = jmespath.search("data[0].data.shelves[0].items[0].title",json_data)
                if title:
                    print(title)
                    break
            except:
                pass
        # print(show_url)
        # print("scripts found:", len(scripts))
        # json_data = json.loads(scripts)
        # print(json_data.keys())
        #print(json_data["data"][0]["data"]keys())
        # print(jmespath.search("data[0].data", json_data))
        # print(type(json_data["data"][0]["data"][1]["shelves"]))
        # title=jmespath.search("data[0].data.shelves[0].items[0].title",json_data)
        # print(title)
    
    # print(new_data[:1000])
    result.append({
        "category_url":cate,
        "sub_categories":sub_categories[0],
        "shows":shows,
        "title":title
    })
print(result)

with open (r"C:\python practice\apple_tv_scrape\scraped_appletv.json",'w',encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False) 
# data=response.text
# print(data)



# result=[]
# categories=tree.xpath("//h2[.//span[contains(.,'Browse All Apple')]] /ancestor::div[contains(@class,'section')]//a[contains(@class,'lockup svelte-n3nezg')]/@href")
# category_links = [
#     "https:" + link if link.startswith("//")
#     else link
#     for link in categories
# ]
# print(category_links)

# for cate in categories:
#     category=cate.xpath("./@href")
#     result.append({
#         "category_url":category[0]

#     })
# print(result)