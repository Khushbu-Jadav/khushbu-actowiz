from curl_cffi import requests
import json
import jmespath
from rich import print

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'access_token': 'null',
    'app_client': 'consumer_web',
    'app_version': '1010101010',
    'auth_key': 'c761ec3633c22afad934fb17a66385c1c06c5472b4898b866b7306186d0bb477',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'device_id': 'eb282ea60e01c454',
    'lat': '28.413333',
    'lon': '77.072833',
    'origin': 'https://blinkit.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://blinkit.com/s/?q=amul',
    'rn_bundle_version': '1009003012',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'session_uuid': 'b6ee0866-013a-4c06-b2be-8e506433c4ea',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36',
    'web_app_version': '1008010016',
    # 'cookie': '_ga_DDJ0134H6Z=GS2.2.s1779967333$o4$g1$t1779967832$j38$l0$h0; gr_1_deviceId=5788dbe9-f976-4119-82a3-fe05bcf68f0c; __cf_bm=4SeMlRpBcel2LsFxfagRngPfQLwFYQU8axKTnQnWZoE-1779968200.1239142-1.0.1.1-dgtSyUsmZdLjZqjcWl7rfBvUOKPSNuSEIzx2KASyQsSkY68HiFOZx83SYJLOnOe5BaO1ROlCRf6mhyAaPDPdOcMgt6.oMDJiNw9dyYUJGqmmVj8XJ_tw2UEwkyZWwzfu; _gcl_au=1.1.2093825443.1779968205; gr_1_lat=28.413333; gr_1_lon=77.072833; gr_1_locality=1849; gr_1_landmark=undefined; _cfuvid=OzY8nX59X3SVoN4HV.r2IqTfVdQ03yLvrAdp4RUDSiY-1779968201.8604012-1.0.1.1-TE3VDWemLw7XwmUp7vqsHolidqcc9WpqeNoO3mU34XA; _gid=GA1.2.949455147.1779968206; _gat_UA-85989319-1=1; _ga=GA1.1.1004733831.1779968206; _ga_JSMJG966C7=GS2.1.s1779967330$o5$g1$t1779968206$j58$l0$h0',
}

params = {
    'q': 'amul',
    'search_type': 'type_to_search',
}


response = requests.post('https://blinkit.com/v1/layout/search', params=params,headers=headers, impersonate="chrome120")

# print(response.json())
data=response.json()

with open(r"C:\python practice\blinkit_scrape\blinkit_json_data.json","w",encoding='utf-8') as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

with open(r"C:\python practice\blinkit_scrape\blinkit_json_data.json","r",encoding="utf-8") as f:
    milk_data=json.load(f)
    result=[]

    products=jmespath.search("response.snippets[*].data.atc_action.add_to_cart.cart_item",data)
    print(len(products))
    for product in products:
        result.append({
            "product_id":jmespath.search("product_id",product),
            "product_name":jmespath.search("product_name",product),
            "product_price":jmespath.search("price",product),
            "product_image":jmespath.search("image_url",product),
            "unit":jmespath.search("unit",product)
      
        })

print(result)
with open(r"C:\python practice\blinkit_scrape\blinkit_milk_scraped.json","w",encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False)
