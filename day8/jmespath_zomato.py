import json
from rich import print
import jmespath

with open(r"C:\python practice\day7\data-2026216105652.json","r",encoding='utf-8') as f:
    data=json.load(f)

    res_data=[]
    days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    menus = jmespath.search("page_data.order.menuList.menus[*]",data)

    res_data.append(
        {
            "restaurant_id" : jmespath.search("page_data.sections.SECTION_BASIC_INFO.res_id", data),
            "restaurant_name" : jmespath.search("page_data.sections.SECTION_BASIC_INFO.name", data),
            "restaurant_url": jmespath.search("page_info.canonicalUrl", data),
            "restaurant_contact":jmespath.search("page_data.sections.SECTION_RES_CONTACT.phoneDetails.phoneStr",data),
            "fssai_licence_number":jmespath.search("page_data.order.menu_List.fssaInfo.text",data),
            "address_info":{
                "full_address":jmespath.search("page_data.sections.SECTION_RES_CONTACT.address",data),
                "region":jmespath.search("page_data.sections.SECTION_RES_CONTACT.country_name",data),
                "city":jmespath.search("page_data.sections.SECTION_RES_CONTACT.city_name",data),
                "pincode": jmespath.search("page_data.sections.SECTION_RES_CONTACT.zipcode", data),
                "state": jmespath.search("page_data.sections.SECTION_RES_CONTACT.state", data)
            },
            "cuisines": jmespath.search("page_data.sections.SECTION_RES_HEADER_DETAILS.CUISINES[*].{name: name, url: url}",data),
            "timings":{
                    day: {
                        "open": jmespath.search("page_data.sections.SECTION_BASIC_INFO.timing.customised_timings.opening_hours[0].timing",data).split(" ")[0],
                        "close": jmespath.search("page_data.sections.SECTION_BASIC_INFO.timing.customised_timings.opening_hours[0].timing",data).split(" ")[-1]

                    } for day in days
            },
            "menu_categories":[
                {
                    "category_name":jmespath.search("category.name",category),
                    "items":[
                        {
                            "item_id": jmespath.search('item.id', item),
                            "item_name": jmespath.search('item.name',item),
                            "item_slugs": jmespath.search("item.tag_slugs",item),
                            "item_url": jmespath.search("item.item_image_url",item),
                            "item_description":jmespath.search("item.desc",item),
                            "item_price":float(0),
                            "is_veg":bool(jmespath.search("item.dietary_slugs",item))
                        }
                        for item in jmespath.search('category.items[*]', category)
                    ]
                }
                     for menu in menus for category in jmespath.search('menu.categories[*]', menu)
            ]
        }
    )


print(res_data)

with open('jmespath_zomato_data.json', 'w', encoding='utf-8') as f:
    # create new json file and store all the data
    json.dump(res_data, f, indent=4)
