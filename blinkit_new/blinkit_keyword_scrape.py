import jmespath
from rich import print
from curl_cffi import requests
import json
from collections import defaultdict

cookies = {
    'gr_1_deviceId': '90150920-3b66-4929-8561-74856f7d2c8e',
    '_cfuvid': '8BcxudkvfPoRMrbt9BdmK_wzy0o8AxfhvX4gHVo5YSU-1781425261.8647273-1.0.1.1-9NBGa0_Fr8y8OhEae0peOCEv_tEefy2LtKuwPQFgPj0',
    '_gcl_gs': '2.1.k1$i1781425261$u260607710',
    '_gid': 'GA1.2.1251388173.1781425263',
    '_fbp': 'fb.1.1781425263481.584705402268735859',
    '_gcl_aw': 'GCL.1781431922.Cj0KCQjwornRBhCrARIsAON5exEFaWPivZcjpeluIN6d9UJUV5zZqLh68dXFQBITB-JuRAAgx5zhDs8aApaEEALw_wcB',
    '_ga': 'GA1.2.974372306.1781425263',
    '_gat_UA-85989319-1': '1',
    '_gcl_au': '1.1.1292529424.1781425262',
    '__cf_bm': '5xubYwDP2z7ni91hfZM1oHTDKF0QeZQGLZx3Q0qscCM-1781434215.4289317-1.0.1.1-Kf7uO0DsRuIXiDbmGTOxkMKws2Vejc3jotmuSHgua3GNGowM8xKinPM20jH5UnPALGAldHCwgCkfk03whKzqy4eKifa0Er61RvG3wN5lIC_rzKBI_uHRksJjQ9y5ecRp',
    '_gac_UA-85989319-1': '1.1781434217.Cj0KCQjwornRBhCrARIsAON5exEFaWPivZcjpeluIN6d9UJUV5zZqLh68dXFQBITB-JuRAAgx5zhDs8aApaEEALw_wcB',
    'gr_1_lat': '21.2043355',
    'gr_1_lon': '72.8401923',
    'gr_1_locality': 'Surat',
    '_ga_DDJ0134H6Z': 'GS2.2.s1781434214$o3$g1$t1781434242$j32$l0$h0',
    '_ga_JSMJG966C7': 'GS2.1.s1781434214$o3$g1$t1781434251$j23$l0$h0',
    'gr_1_landmark': 'undefined',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'access_token': 'null',
    'app_client': 'consumer_web',
    'app_version': '1010101010',
    'auth_key': 'c761ec3633c22afad934fb17a66385c1c06c5472b4898b866b7306186d0bb477',
    # 'content-length': '0',
    'content-type': 'application/json',
    'device_id': 'd72e996e04afe01f',
    'lat': '21.2043355',
    'lon': '72.8401923',
    'origin': 'https://blinkit.com',
    'priority': 'u=1, i',
    'referer': 'https://blinkit.com/s/?q=shampoo',
    'rn_bundle_version': '1009003012',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'session_uuid': 'a99bab7f-36fb-4d84-87bf-d212f01475ee',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'web_app_version': '1008010016',
    # 'cookie': 'gr_1_deviceId=90150920-3b66-4929-8561-74856f7d2c8e; _cfuvid=8BcxudkvfPoRMrbt9BdmK_wzy0o8AxfhvX4gHVo5YSU-1781425261.8647273-1.0.1.1-9NBGa0_Fr8y8OhEae0peOCEv_tEefy2LtKuwPQFgPj0; _gcl_gs=2.1.k1$i1781425261$u260607710; _gid=GA1.2.1251388173.1781425263; _fbp=fb.1.1781425263481.584705402268735859; _gcl_aw=GCL.1781431922.Cj0KCQjwornRBhCrARIsAON5exEFaWPivZcjpeluIN6d9UJUV5zZqLh68dXFQBITB-JuRAAgx5zhDs8aApaEEALw_wcB; _ga=GA1.2.974372306.1781425263; _gat_UA-85989319-1=1; _gcl_au=1.1.1292529424.1781425262; __cf_bm=5xubYwDP2z7ni91hfZM1oHTDKF0QeZQGLZx3Q0qscCM-1781434215.4289317-1.0.1.1-Kf7uO0DsRuIXiDbmGTOxkMKws2Vejc3jotmuSHgua3GNGowM8xKinPM20jH5UnPALGAldHCwgCkfk03whKzqy4eKifa0Er61RvG3wN5lIC_rzKBI_uHRksJjQ9y5ecRp; _gac_UA-85989319-1=1.1781434217.Cj0KCQjwornRBhCrARIsAON5exEFaWPivZcjpeluIN6d9UJUV5zZqLh68dXFQBITB-JuRAAgx5zhDs8aApaEEALw_wcB; gr_1_lat=21.2043355; gr_1_lon=72.8401923; gr_1_locality=Surat; _ga_DDJ0134H6Z=GS2.2.s1781434214$o3$g1$t1781434242$j32$l0$h0; _ga_JSMJG966C7=GS2.1.s1781434214$o3$g1$t1781434251$j23$l0$h0; gr_1_landmark=undefined',
}

product_api={
    "shampoo":"shampoo",
    "Conditioner":"Conditioner",
    "Moisturizer":"Moisturizer",
    "Hair Oil":"Hair Oil",
    "Shampoo+Conditioner":"Shampoo+Conditioner",
    "Conditioner+Moisturizer":"Conditioner+Moisturizer"
}

all_products={}
base_url="https://blinkit.com"

for key,value in product_api.items():
    params = {
        'offset': '25',
        'limit': '25',
        'actual_query': value,
        'last_snippet_type': 'product_card_snippet_type_2',
        'last_widget_type': 'listing_container',
        'page_index': '1',
        'q': value,
        'search_count': '370',
        'search_method': 'basic',
        'search_type': 'type_to_search',
        'tab_position': '0',
        'total_entities_processed': '1',
        'total_pagination_items': '370',
    }



    response = requests.post('https://blinkit.com/v1/layout/search', params=params, cookies=cookies, headers=headers,impersonate='chrome120')

    if response.status_code == 200:
        try:
            data = response.json()
        except:
            print(" Not JSON response")
            print(response.text[:500])
            continue
    else:
        print(" Request failed:", response.status_code)
        continue

    with open(r"C:\python practice\blinkit_new\blinkit_data.json","w",encoding='utf-8') as f :
        json.dump(data,f,indent=4,ensure_ascii=False)

    with open(r"C:\python practice\blinkit_new\blinkit_data.json","r",encoding="utf-8") as f:
        new_data=json.load(f)

        keyword_results = []

        products=jmespath.search("response.snippets[*].data.atc_action.add_to_cart.cart_item",new_data)

        for product in products:
            product_name = jmespath.search("product_name", product)
            product_id   = jmespath.search("product_id", product)
            slug = product_name.lower().replace(" ", "-")
            product_url = base_url + "/prn/" + slug + "/prid/" + str(product_id)

            keyword_results.append({
                "product_id":product_id,
                "product_name":product_name,
                "product_url":product_url,
                "product_brand":jmespath.search("brand",product),
                "product_quantity":jmespath.search("quantity",product),
                "product_price":jmespath.search("price",product),
                "product_image":jmespath.search("image_url",product),
                "product_unit":jmespath.search("unit",product)
            })

        all_products[key]=keyword_results
        print(len(keyword_results))

with open(r"C:\python practice\blinkit_new\new_scraped_data.json", "w", encoding="utf-8") as f:
    json.dump(all_products, f, indent=4, ensure_ascii=False)

# print(all_products)
# print(len(all_products))

product_map = defaultdict(list)

for keyword, products in all_products.items():
    for product in products:
        pid = product['product_id']

        product_map[pid].append({
            "keyword": keyword,
            "name": product['product_name'],
            "brand": product['product_brand'],
            "price": product['product_price']
        })

common_products = {}

for pid, entries in product_map.items():
    if len(entries) > 1 :
        common_products[pid] = entries

for pid, entries in common_products.items():
    print(f"\nProduct ID: {pid}")

    for e in entries:
        print(f"  {e['keyword']} → {e['brand']} ")