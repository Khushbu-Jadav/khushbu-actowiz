import json
from lxml import html
from rich import print
import re


with open(r'C:\python practice\day13\dominoz.html', "r", encoding='utf-8') as f:
    data = f.read()
    result = []

    tree=html.fromstring(data)
    panels = tree.xpath("//div[contains(@class,'panel panel-default custom-panel')]")
    url='https://www.dominos.co.in'
    for panel in panels:
        pizza_name = panel.xpath("string(.//h4[contains(@class,'city-main-title')])").replace("\t", " ").replace("\n", " ").strip()

        link=panel.xpath(".//div[contains(@class,'media-body')]//a/@href")[0]
        restaurant_link=url+link

        image=panel.xpath(".//img[@class='panel-thumbs-img img-responsive img-rounded']/@src")
        image_link=url+image[0] if image else None

        city_name=panel.xpath(".//p[contains(@class,'city-main-sub-title')]/text()")
        address=panel.xpath(".//p[contains(@class,'grey-text mb-0')]/text()")
       
        address_text = address[0].strip() if address else None
       
        pincode_match=re.search(r"\d{6}",address_text) if address_text else None
        pincode=pincode_match.group() if pincode_match else None
        clean_address = re.sub(r"\d{6}", "", address_text).strip() if address_text else None
        new_address = re.sub(r'-\s*', ' ', clean_address).strip() if clean_address else None
        delivery_in=panel.xpath(".//p[contains(@class,'red-text mb-0')]/text()")
        cost=panel.xpath(".//span[contains(@class,'col-xs-9 col-md-9 pl0')]/text()")
        hours=" ".join(x.replace("\n","").replace("\t","") for x in panel.xpath(".//div[contains(@class,'col-xs-9 col-md-9 pl0 search-grid-right-text')]/text()"))
        open_status=" ".join(x.replace("\n","").replace("\t","") for x in panel.xpath(".//span[contains(@class,'green')]/text()"))

        good_for=panel.xpath(".//div[contains(@class,'clearfix mt-5')]//p[contains(@class,'mb-0')]/text()")
        call=" ".join(panel.xpath(".//div[@class='modal-body text-center']//p[@class='fontsize2 bold zred']/text()"))
        view_menu=panel.xpath(".//a[starts-with(@title,'View')]/@href")
        order_now=panel.xpath(".//form//a[@class='btn btn-primary order-now-button']/@href")
        result.append({
            "Pizza_name":pizza_name if pizza_name else None,
            "Restaurant_link":restaurant_link,
            "image_link":image_link,
            "city_name":city_name[0].strip() if city_name else None,
            "address":new_address,
            "pincode":pincode,
            "delivery_in":delivery_in[0].strip() if delivery_in else None,
            "cost":cost[0].strip() if cost else None,
            "hours":hours+open_status,
            "good_for":good_for[0].strip() if good_for else None,
            "call":call,
            "view_menu":view_menu[0].strip() if view_menu else None,
            "order_now":order_now[0].strip() if order_now else None
        
        })

print(result)
print(len(result))

with open(r"C:\python practice\day13\dominoz_loc_data.json","w",encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False)