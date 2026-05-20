import json
from rich import print
from lxml import html
import requests

result=[]
base_url="https://www.rockwestcomposites.com/808-150-12.html"

response=requests.get(base_url)
tree=html.fromstring(response.content)

# print(response.content)
product_name=tree.xpath("//div[@class='row']//h1[@class='product-name']//text()")[0]
product_link="https://www.rockwestcomposites.com/808-150-12.html"
product_sku=tree.xpath("//div[@class='product-detail-right']//span[@class='product-id product-sku']//text()")[0].split(":")[1].strip()
product_price=tree.xpath("//div[@class='price']//span[@class='sales default-price']/text()")[1].split("$")[1].strip()

product_quantity=tree.xpath("//span[@class='product-stock-availability']/text()")[0].split(":")[1].strip()
is_available=True if int(product_quantity) >= 1 else False

application=tree.xpath("//tr[th='Application']/td[@class='has-value']/span/text()")[0]
materials=tree.xpath("//tr[th='Materials']/td[@class='has-value']/span/text()")[0]
pattern=tree.xpath("//tr[th='Pattern']/td[@class='has-value']/span/text()")[0]
angle_orner_style=tree.xpath("//tr[th='Angle Corner Style']/td[@class='has-value']/span/text()")[0]
angle_degree=tree.xpath("//tr[th='Angle Degree']/td[@class='has-value']/span/text()")[0]
angle_finish=tree.xpath("//tr[th='Angle Finish']/td[@class='has-value']/span/text()")[0]
angle_leg_length=tree.xpath("//tr[th='Angle Leg Length']/td[@class='has-value']/span/text()")[0]
angle_thickness=tree.xpath("//tr[th='Angle Thickness']/td[@class='has-value']/span/text()")[0]
thickness=tree.xpath("//tr[th='Thickness']/td[@class='has-value']/span/text()")[0]
length=tree.xpath("//tr[th='Length']/td[@class='has-value']/span/text()")[0]
length_max_continuous=tree.xpath("//tr[th='Length (max continuous)']/td[@class='has-value']/span/text()")[0]
weight=tree.xpath("//tr[th='Weight']/td[@class='has-value']/span/text()")[0]
max_operating_temp=tree.xpath("//tr[th='Max Operating Temp- (Tg)']/td[@class='has-value']/span/text()")[0]
hts_harmonized_tariff_code=tree.xpath("//tr[th='HTS - Harmonized Tariff Code']/td[@class='has-value']/span/text()")[0]
result.append({
    "product_name":product_name,
    "product_link":product_link,
    "product_sku":product_sku,
    "product_price":product_price,
    "product_quantity":product_quantity,
    "is_available":is_available,
    "product_additional_info":[
        {
            "application":application,
            "materials":materials,
            "pattern":pattern,
            "angle_corner_style":angle_orner_style,
            "angle_degree":angle_degree,
            "angle_finish":angle_finish,
            "angle_leg_length":angle_leg_length,
            "angle_thickness":angle_thickness,
            "thickness":thickness,
            "length":length,
            "length(max_continous)":length_max_continuous,
            "max_operating_temp(tg)":max_operating_temp,
            "HTS - Harmonized Tariff Code":hts_harmonized_tariff_code
        }
    ]
})

print(result)

with open(r"C:\python practice\day14\rock_west_scrap.json","w",encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False)

