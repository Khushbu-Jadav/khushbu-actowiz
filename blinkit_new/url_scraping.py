from curl_cffi import requests
import jmespath
import json
import os

url = [
    "https://blinkit.com/prn/minimalist-3.5-anti-dandruff-shampoo/prid/613108",
    "https://blinkit.com/prn/loreal-paris-hyaluron-pure-72h-purifying-shampoo/prid/610026",
    "https://blinkit.com/prn/clinic-plus-strong-long-shampoo-with-milk-proteins/prid/632512",
    "https://blinkit.com/prn/tresemme-hydra-matrix-shampoo/prid/724615",
    "https://blinkit.com/prn/loreal-paris-glycolic-gloss-shampoo/prid/693443",
    "https://blinkit.com/prn/head-shoulders-anti-dandruff-anti-hairfall-shampoo/prid/91026",
    "https://blinkit.com/prn/moxie-beauty-gentle-cleansing-shampoo/prid/559155",
    "https://blinkit.com/prn/tresemme-hair-fall-defense-shampoo/prid/345992",
    "https://blinkit.com/prn/bare-anatomy-anti-hairfall-shampoo/prid/500377",
    "https://blinkit.com/prn/tresemme-hairfall-defense-shampoo/prid/632519",
    "https://blinkit.com/prn/pantene-hair-science-silky-smooth-shampoo-with-vitamin-e/prid/403233",
    "https://blinkit.com/prn/pantene-hair-science-hairfall-control-shampoo-with-vitamin-b/prid/403229",
    "https://blinkit.com/prn/dove-hair-fall-rescue-shampoo-for-weak-hair/prid/23842",
    "https://blinkit.com/prn/pantene-silky-smooth-care-2-in-1-shampoo-conditioner/prid/429697",
    "https://blinkit.com/prn/pantene-miracle-rescue-biotin-strength-conditioner/prid/609751",
    "https://blinkit.com/prn/loreal-paris-total-repair-5-conditioner/prid/125152",
    "https://blinkit.com/prn/loreal-paris-glycolic-gloss-shine-sealing-conditioner/prid/691347",
    "https://blinkit.com/prn/moxie-beauty-ultra-hydrating-conditioner/prid/559154",
    "https://blinkit.com/prn/dove-hair-fall-rescue-conditioner/prid/906",
    "https://blinkit.com/prn/sunsilk-lusciously-thick-long-nourishing-conditioner-180-ml/prid/109243",
    "https://blinkit.com/prn/re-equil-oil-free-moisturizing-cream/prid/573309",
    "https://blinkit.com/prn/dot-key-ceramides-barrier-repair-moisturizer/prid/499585",
    "https://blinkit.com/prn/nivea-soft-daily-uv-light-moisturizing-cream/prid/659340",
    "https://blinkit.com/prn/minimalist-vitamin-b5-10-gel-moisturizer/prid/500361",
    "https://blinkit.com/prn/nivea-natural-glow-cell-repair-body-lotion/prid/315305",
    "https://blinkit.com/prn/hyphen-2-cica-exosomes-hydra-balance-face-moisturizer/prid/745761",
    "https://blinkit.com/prn/cerave-moisturizing-cream-with-ceramides/prid/679648",
    "https://blinkit.com/prn/minimalist-b12-repair-complex-5.5-face-moisturizer/prid/686982",
    "https://blinkit.com/prn/nivea-aloe-hydration-normal-skin-body-lotion-600-ml/prid/431745",
    "https://blinkit.com/prn/flicka-silk-touch-3-in-1-milk-moisturizing-cream-primer/prid/604685"
]
products ={}
folder_name = "pages"
os.makedirs(folder_name, exist_ok=True)
page = 1

for url1 in url:
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'access_token': 'null',
        'app_client': 'consumer_web',
        'app_version': '1010101011',
        'auth_key': 'c761ec3633c22afad934fb17a66385c1c06c5472b4898b866b7306186d0bb477',
        'cache-control': 'no-cache',
        # 'content-length': '0',
        'content-type': 'application/json',
        'device_id': '506c64a082072a94',
        'is-response-compression-enabled': 'false',
        'lat': '23.052294699999997',
        'lon': '72.6423354',
        'origin': 'https://blinkit.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': url1,
        'rn_bundle_version': '1009003012',
        'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'session_uuid': '3c12ebe2-40f9-4f95-84ee-515c319ac7cb',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
        'web_app_version': '1008010016',
        'x-age-consent-granted': 'false',
        # 'cookie': '_fbp=fb.1.1779689379491.336827773188248839; gr_1_deviceId=862733a4-d99d-4bd3-95c0-2f68438c6307; _gid=GA1.2.1485079175.1781169212; gr_1_lat=23.052294699999997; gr_1_lon=72.6423354; gr_1_locality=Ahmedabad; gr_1_landmark=undefined; city=Chennai; __cf_bm=xjMYRifX4ciZJBnQs0U3pnXT95MCsyE9R4IYjjCUAMY-1781240393.026509-1.0.1.1-Ev2eV6D.N3R97jU3k7VgyDm6Xf6Jm_IYI9aY28B9XRBInq9cyLtwxQhTxyWM9ALifcnYPzZvYWW6U7I4xHP0fD.Rn6OD2LOBvLHtdxCP64GtThS6OSIQJkiNSIEscv8h; _cfuvid=TEjuj0_a2VP4mulhslRaCbWN1jM3dEI6JSvh5pJQ6Vc-1781240445.9236848-1.0.1.1-4tBsN5OChR0uFlIp6bKLojfQ6EC4YhN7rYfNDGqi3TM; _ga=GA1.2.1163602471.1779689379; _ga_DDJ0134H6Z=GS2.2.s1781240445$o12$g1$t1781240748$j60$l0$h0; _ga_JSMJG966C7=GS2.1.s1781240442$o16$g1$t1781240859$j60$l0$h0; _gcl_au=1.1.1792842843.1779689379',
    }

    product_id = url1.split("/")[-1]

    print(product_id)
    response = requests.post(f'https://blinkit.com/v1/layout/product/{product_id}', headers=headers,impersonate="chrome120")

    if response.status_code == 200:
        # print("sucess")
        json_data = response.json()
        # print(json_data)

        with open(f"{folder_name}/{product_id}.json", "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

        print(f"Saved page_{page}.json")

        page += 1
        ptype = jmespath.search(
            "response.snippets[].data.items[].tracking.common_attributes.ptype",json_data)

        category = None
        if isinstance(ptype, list):
            for p in ptype:
                if p:
                    category = p.lower()
                    break

        if not category:
            category = "unknown"

        image = jmespath.search("response.snippets[0].data.itemList[0].data.click_action.show_gallery.assets[*].image_url",json_data)
        title = jmespath.search("response.snippets[0].data.itemList[0].tracking.widget_meta.child_widget_title",json_data)
        ml = jmespath.search("response.snippets[4].data.horizontal_item_list[0].data.selected_state_data.title.text",json_data)
        price = jmespath.search("response.snippets[4].data.horizontal_item_list[0].data.selected_state_data.subtitle2.text",json_data)
        replace_time = jmespath.search("response.snippet_list_updater_data.attributes_to_add_for_expanding_vpd.payload.snippets_to_add[0].data.horizontal_item_list[0].data.click_action.open_bottom_sheet.data.response.snippets[0].data.title.text",json_data)
        support = jmespath.search("response.snippet_list_updater_data.attributes_to_add_for_expanding_vpd.payload.snippets_to_add[0].data.horizontal_item_list[1].data.click_action.open_bottom_sheet.data.response.snippets[2].data.subtitle.text",json_data)
        delevery = jmespath.search("response.snippet_list_updater_data.attributes_to_add_for_expanding_vpd.payload.snippets_to_add[0].data.horizontal_item_list[2].data.click_action.open_bottom_sheet.data.response.snippets[0].data.title.text",json_data)
        key = jmespath.search("response.snippet_list_updater_data.expandkey_information0.payload.snippets_to_add[*].data.title.text",json_data)
        value = jmespath.search("response.snippet_list_updater_data.expandkey_information0.payload.snippets_to_add[*].data.subtitle.text",json_data)
        key1 = jmespath.search("response.snippet_list_updater_data.expandinfo0.payload.snippets_to_add[*].data.title.text",json_data)
        value1 = jmespath.search("response.snippet_list_updater_data.expandinfo0.payload.snippets_to_add[*].data.subtitle.text",json_data)
        
        result = {
            "title": title,
            "images": image,
            "ml": ml,
            "price": price,
            "replace_time": replace_time,
            "support": support,
            "delivery": delevery,
            "product_id": product_id,
            "category": category
        }

        if key and value:
            result.update(dict(zip(key, value)))

        if key1 and value1:
            result.update(dict(zip(key1, value1)))

        if category not in products:
            products[category] = []

        products[category].append(result)
        
with open(r"C:\python practice\blinkit_new\product_scraped.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)