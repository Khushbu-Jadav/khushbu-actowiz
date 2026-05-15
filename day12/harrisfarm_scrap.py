# from lxml import html
# from rich import print

# with open(r"C:\python practice\day12\harrisfarm.html","r",encoding='utf-8') as f :
#     data=f.read()

# # print(data)
# tree=html.fromstring(data)
# res_data=[]
# categories=tree.xpath("//div[@class='sidebar_menu']//li//a//span[@class='']/text() | //div[@class='sidebar_menu']//li/button/text()"
#                       )
# categories=categories[:32]
# url="https://www.harrisfarm.com.au"
# links=tree.xpath("//div[@class='sidebar_menu']//li//a//@href")
# category_links = [url + link for link in links]

# for i in range(len(category_links)):
#     res_data.append({
#         "categories_name":categories,
#         "category_links":category_links
#     })

# print(res_data)



from lxml import html
from rich import print
import json

with open(r'C:\python practice\day12\harrisfarm.html', "r", encoding='utf-8') as f:
    data = f.read()
    result = []

    tree = html.fromstring(data) 

    result = tree.xpath("//div[text()='Shop Categories']/following-sibling::li/a")

    base_url = "https://www.harrisfarm.com.au"

    categories = []

    for i in result:
        name = i.text_content().strip()
        link = i.get("href")
        full_link = base_url + link

        category_data = {
            "category_name": name,
            "category_link": full_link
        }
        categories.append(category_data)

for category in categories:
    print(category)

with open(r"C:\python practice\day12\new_harrisfarm.json","w",encoding='utf-8') as f:
    json.dump(categories,f,indent=4)
