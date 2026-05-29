from rich import print
import json
from curl_cffi import requests
from lxml import html
import jmespath

all_headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.eatsure.com/ahmedabad/bapu-nagar',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    # 'cookie': '_gcl_au=1.1.1937136311.1780036036; _gcl_aw=GCL.1780036036.Cj0KCQjwz9_QBhD_ARIsADnSCfDTvbe1QE1l-ajs11j1XEiSlJGvFGx6oSJzQOg3kDB0mY37zb1Xi3UaAkOXEALw_wcB; _gcl_gs=2.1.k1$i1780036035$u79974787; _gid=GA1.2.600420139.1780036036; _gac_UA-165961364-3=1.1780036036.Cj0KCQjwz9_QBhD_ARIsADnSCfDTvbe1QE1l-ajs11j1XEiSlJGvFGx6oSJzQOg3kDB0mY37zb1Xi3UaAkOXEALw_wcB; _fbp=fb.1.1780036036224.371765060132781193; _clck=jsvri7%5E2%5Eg6g%5E0%5E2340; ESweb_sid=s%3Ad27e62e9-59ce-407c-9095-9604cbb7b0c1.3NFkLOaR5pqirmip%2BJLgBwTQOqm3VTx0FDEmMI6m%2FBU; slug=bapu-nagar; city_name=ahmedabad; store_id=10407; city_id=7384; store_map_location=%7B%2210407%22%3A%7B%22lat%22%3A%2223.0506370000001%22%2C%22lng%22%3A%2272.6117100000001%22%2C%22place_id%22%3A%22380016%22%7D%7D; locality_name=380016; WZRK_S_RK8-468-5K6Z=%7B%22p%22%3A3%7D; _clsk=7jl8s0%5E1780048820224%5E22%5E1%5Ex.clarity.ms%2Fcollect; _gat_UA-165961364-3=1; AMP_08b33bcecf=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI4MmUzZDRmMi02ZjIxLTQwYzctOTNkZi1iYmRjYWRiYjAxYWQlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzgwMDQ4NDkxNDI1JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc4MDA0OTAwMTQyNiUyQyUyMmxhc3RFdmVudElkJTIyJTNBMTk0JTJDJTIycGFnZUNvdW50ZXIlMjIlM0EwJTdE; _ga_WYV6N569KB=GS2.1.s1780045118$o3$g1$t1780049001$j58$l0$h1754872062; _ga=GA1.1.1724568469.1780036036',
}

all_response = requests.get(
    'https://www.eatsure.com/v1/api/get_all_brands?&store_id=10407&city_id=7384',
    headers=all_headers,
)

all_data = all_response.json()

with open(r"C:\python practice\eat_sure_scrape\all_json_data.json","w",encoding='utf-8') as f:
    json.dump(all_data,f,indent=4,ensure_ascii=False)

# headers = {
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'no-cache',
#     'pragma': 'no-cache',
#     'priority': 'u=1, i',
#     'referer': 'https://www.eatsure.com/faasos/ahmedabad/bapu-nagar',
#     'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
#     'sec-ch-ua-mobile': '?1',
#     'sec-ch-ua-platform': '"Android"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36',
#     # 'cookie': 'utm_source=google; utm_medium=google; utm_campaign=google; _gcl_au=1.1.1937136311.1780036036; _gcl_aw=GCL.1780036036.Cj0KCQjwz9_QBhD_ARIsADnSCfDTvbe1QE1l-ajs11j1XEiSlJGvFGx6oSJzQOg3kDB0mY37zb1Xi3UaAkOXEALw_wcB; _gcl_gs=2.1.k1$i1780036035$u79974787; _gid=GA1.2.600420139.1780036036; _gac_UA-165961364-3=1.1780036036.Cj0KCQjwz9_QBhD_ARIsADnSCfDTvbe1QE1l-ajs11j1XEiSlJGvFGx6oSJzQOg3kDB0mY37zb1Xi3UaAkOXEALw_wcB; _fbp=fb.1.1780036036224.371765060132781193; _clck=jsvri7%5E2%5Eg6g%5E0%5E2340; ESweb_sid=s%3Ad27e62e9-59ce-407c-9095-9604cbb7b0c1.3NFkLOaR5pqirmip%2BJLgBwTQOqm3VTx0FDEmMI6m%2FBU; slug=bapu-nagar; city_name=ahmedabad; store_id=10407; city_id=7384; store_map_location=%7B%2210407%22%3A%7B%22lat%22%3A%2223.0506370000001%22%2C%22lng%22%3A%2272.6117100000001%22%2C%22place_id%22%3A%22380016%22%7D%7D; locality_name=380016; _clsk=180d11z%5E1780042719824%5E10%5E1%5Ex.clarity.ms%2Fcollect; _gat_UA-165961364-3=1; _ga=GA1.1.1724568469.1780036036; WZRK_S_RK8-468-5K6Z=%7B%22p%22%3A3%7D; _ga_WYV6N569KB=GS2.1.s1780041434$o2$g1$t1780042791$j57$l0$h1638222962; AMP_08b33bcecf=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI4MmUzZDRmMi02ZjIxLTQwYzctOTNkZi1iYmRjYWRiYjAxYWQlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzgwMDQxNDQxMTkxJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc4MDA0Mjc5MTg2MyUyQyUyMmxhc3RFdmVudElkJTIyJTNBMTYwJTJDJTIycGFnZUNvdW50ZXIlMjIlM0EwJTdE',
# }

home_url="https://www.eatsure.com/ahmedabad/bapu-nagar"

cate_response=requests.get(home_url,impersonate="chrome120")
tree=html.fromstring(cate_response.text)

category_links=tree.xpath("//a[@data-qa='brandIcon']/@href")
url="https://www.eatsure.com"

restaurant_links=[url+link for link in category_links]

result=[]

brands = jmespath.search("data.data[]", all_data)
print(len(brands))

for brand in brands:
    brand_id = jmespath.search("brand_id", brand)
    brand_name = jmespath.search("brand_name", brand)
    source_id = jmespath.search("source_id", brand)

    api_url = f"https://www.eatsure.com/v1/api/get_all_products/brand_id/{brand_id}/store_id/10407/source_id/{source_id}"
    response = requests.get(api_url,headers=all_headers,impersonate="chrome120")

    data = response.json()

    products=jmespath.search("data.collections[].products[]",data)
    for product in products:
        result.append({
                "brand_name":jmespath.search("brand_name",product),
                "product_id":jmespath.search("product_id",product),
                "product_name":jmespath.search("product_name",product),
                "product_imageUrl":jmespath.search("product_imageUrl",product),
                "product_price":jmespath.search("price",product),
                "product_description":jmespath.search("big_description",product),
                "product_rating":jmespath.search("rating",product),
                "is_veg":bool(jmespath.search("is_veg",product)),
                "is_availabel":bool(jmespath.search("is_available",product)),
                "benefits":jmespath.search("benefits",product),
                "offer_tag":jmespath.search("offer_tags[]",product),
                "product_video_link":jmespath.search("product_video_link",product)
            })

print(result)
print(len(result))

with open (r"C:\python practice\eat_sure_scrape\scraped_data.json",'w',encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False)    

