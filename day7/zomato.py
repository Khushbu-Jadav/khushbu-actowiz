import json
from rich import print

with open("data-2026216105652.json","r",encoding='utf-8') as f:
    data=json.load(f)

    res_data=[]

    days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

    cuisines=data['page_data']['sections']['SECTION_RES_HEADER_DETAILS']['CUISINES']

    timing=data["page_data"]["sections"]["SECTION_BASIC_INFO"]["timing"]["customised_timings"]["opening_hours"][0].get("timing")

    menu=data['page_data']['order']['menuList']['menus'][0]['menu']

    categories=data['page_data']['order']['menuList']['menus'][0]['menu']['categories']

    items=data['page_data']['order']['menuList']['menus'][0]['menu']['categories'][0]['category']['items']

    res_data.append(
        {
            "restaurant_id":data['page_info'].get('resId'),
            "restaurant_name":data['page_data']['sections']['SECTION_BASIC_INFO'].get('name'),
            "restaurant_url":data['page_info'].get('canonicalUrl'),
            "restaurant_contact":data['page_data']['sections']['SECTION_RES_CONTACT']['phoneDetails'].get('phoneStr'),
            "fssai_licence_number":data['page_data']['order']['menuList']['fssaiInfo'].get('text'),
            "address_info":{
                "full_address": data['page_data']['sections']['SECTION_RES_CONTACT'].get('address'),
                "region": data['page_data']['sections']['SECTION_RES_CONTACT'].get('country_name'),
                "city": data['page_data']['sections']['SECTION_RES_CONTACT'].get('city_name'),
                "pincode": data['page_data']['sections']['SECTION_RES_CONTACT'].get('zipcode'),
                "state":data.get('')
            },
            "cuisines":[
                {
                    "name":cuisine.get('name'),
                    "url":cuisine.get('url')
                }for cuisine in cuisines
            ],
            "timings":{
                day:{
                    "opening":timing.split(" ")[0],
                    "closing":timing.split(" ")[-1]
                }for day in days
            },
            "menu_categories":[
                {
                    "category":[
                        {
                             "name":cate.get('category').get('name'),

                    "items":[
                        {
                            "item_id":items[i].get('item').get('id'),
                            "item_name":items[i].get('item').get('name'),
                            "item_slugs":items[i].get('item').get('tag_slugs'),
                            "item_url":items[i].get('item').get('item_image_url'),
                            "item_description":items[i].get('item').get('desc'),
                            "item_price":float(0),
                            "is_veg":bool(items[i].get('item').get('dietary_slugs'))

                        }
                         for i in range(len(items))
                    ],
                    }for cate in categories
                ],
                }for i in range(len(menu))


            ]
        }
    )


print(res_data)

with open('zomato_data.json', 'w', encoding='utf-8') as f:
    # create new json file and store all the data
    json.dump(res_data, f, indent=4)

