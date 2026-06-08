# from curl_cffi import requests
# from lxml import html
# import json
# import re
# import jmespath
# from rich import print

# params={'encodedCT':'eyJIYXNNb3JlIjp0cnVlLCJTa2lwQ291bnQiOjI1LCJUb3RhbENvdW50IjoyNjMsIlByZXZpb3VzUGFnZVByb2R1Y3RJZHMiOlsiQlBRWlQ0M0ZXRDQ5IiwiQlZNMDAyTThISDBTIiwiOU5GNVM3TUxNOFhUIiwiOU5CTEdHSDQzS1pCIiwiOU5NNFdRN1RUSDNKIiwiOVBKRk1WQlAxNkNUIiwiOU5HTFNUMzFERzI2IiwiOU4ySjBGR1YzMERYIiwiOU5NRjNLWFQ0UDRHIiwiOU5WVjBNNzRXMDVDIiwiOVAzUEw3Nk4wS1daIiwiOVBKMDZUWlg0Tk1IIiwiOVBKV1JRUkpUSE5UIiwiOU45NjFCMTFGSjRXIiwiOU42WjhEUVhTUVdIIiwiOU5ESkxYRDJYMkRNIiwiOVA0VzhIMkhOTE40IiwiOVBOQkZDQ0cwTFBLIiwiOU5WQzlLV0pWTFQwIiwiOVAxSDhLMlYwTk5QIiwiOU5aRzcyU0gzSDRXIiwiOU5IRkRaUkQ3NTNSIiwiOU4yMVpDVjBKVzZWIiwiOU1XVjFNVjlMV0Y0IiwiOU1WWlRIMTdWNzUzIl19'}
# url="https://www.xbox.com/en-IN/games/all-games/console?PlayWith=XboxSeriesX%7CS,XboxOne,CloudGaming,XboxPlayAnywhere&Genre=Family+%26+kids"
# response = requests.get(
#         url,
#         params=params,
#         impersonate="chrome120")

# tree = html.fromstring(response.text)
# scripts = tree.xpath("//script/text()")

# result=[]

# for script in scripts:
#         if "__PRELOADED_STATE__" in script:
#             match = re.search(r"window\.__PRELOADED_STATE__\s*=\s*", script)
#             if match:
#                 start = match.end()

#                 decoder = json.JSONDecoder()
#                 data, _ = decoder.raw_decode(script, start)
            
#                 with open(r"C:\python practice\xbox_games\xbox_games_json.json", "w", encoding="utf-8") as f:
#                     json.dump(data, f, indent=4, ensure_ascii=False)

#                 product_summaries = jmespath.search("core2.products.productSummaries", data)

#                 encoded_ct=jmespath.search('core2.channels.channelData."BROWSE_CHANNELID=_FILTERS=GENRE=FAMILY & KIDS&PLAYWITH=CLOUDGAMING,XBOXONE,XBOXPLAYANYWHERE,XBOXSERIESX|S".data.encodedCT',data)
#                 print(encoded_ct)

#                 if product_summaries:
#                     print(len(product_summaries))
#                     for product_id, details in product_summaries.items():
                        
#                         title = details.get("title", "unknown").replace(" ", "-")
#                         optimalSkuId = details.get("optimalSkuId","unknown")

#                         game_name=details.get("title", "unknown")
#                         url = f"https://www.xbox.com/en-IN/games/store/{title}/{product_id}/{optimalSkuId}"  
#                         game_response = requests.get(url,impersonate="chrome120")

#                         result.append({
#                              "game_name":game_name,
#                              "game_url":url,
#                         })              
           
# print(result)




from curl_cffi import requests
import json
import re
from rich import print
from lxml import html
import jmespath

api_url = "https://emerald.xboxservices.com/xboxcomfd/browse?locale=en-IN"

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'ms-cv': '1kBKFurwBZajVdbw1JePqO.29',
    'origin': 'https://www.xbox.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.xbox.com/',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'x-ms-api-version': '1.1',
    'xbl-experiments': 'enableuhfcache,forcerefreshexp,forceservernav,enableaamscript,enableserversideuserfeatureassignments,enableserverauthv3',
}

channel_key = "BROWSE_CHANNELID=_FILTERS=GENRE=FAMILY & KIDS&PLAYWITH=CLOUDGAMING,XBOXONE,XBOXPLAYANYWHERE,XBOXSERIESX|S"
filters = "eyJHZW5yZSI6eyJpZCI6IkdlbnJlIiwiY2hvaWNlcyI6W3siaWQiOiJGYW1pbHkgJiBraWRzIn1dfSwiUGxheVdpdGgiOnsiaWQiOiJQbGF5V2l0aCIsImNob2ljZXMiOlt7ImlkIjoiWGJveFNlcmllc1h8UyJ9LHsiaWQiOiJYYm94T25lIn0seyJpZCI6IkNsb3VkR2FtaW5nIn0seyJpZCI6Ilhib3hQbGF5QW55d2hlcmUifV19fQ=="

encoded_ct = ""
result = []
page = 1
total_items = None

# ---- step 1: collect all game urls ----
while True:
    payload = {
        "Filters": filters,
        "ReturnFilters": False,
        "ChannelKeyToBeUsedInResponse": channel_key,
        "EncodedCT": encoded_ct,
        "ChannelId": "",
    }

    response = requests.post(api_url, json=payload, headers=headers, impersonate="chrome120")

    if not response.text:
        break

    data = response.json()

    channel = data.get("channels", {}).get(channel_key, {})
    product_ids = [p.get("productId") for p in channel.get("products", [])]

    product_summaries_list = data.get("productSummaries", [])
    product_summaries = {item.get("productId"): item for item in product_summaries_list}

    encoded_ct = channel.get("encodedCT", "")

    if total_items is None:
        total_items = channel.get("totalItems")

    for product_id in product_ids:
        details = product_summaries.get(product_id, {})
        title = details.get("title", "unknown").replace(" ", "-")
        optimalSkuId = details.get("optimalSkuId", "unknown")
        game_url = f"https://www.xbox.com/en-IN/games/store/{title}/{product_id}/{optimalSkuId}"
        result.append({
            "game_name": details.get("title", "unknown"),
            "game_url": game_url,
        })

   # print(f"Page {page}: {len(product_ids)} games | Total so far: {len(result)}/{total_items}")
    page += 1

    if not encoded_ct:
        break

print(f"\nTotal URLs collected: {len(result)} games")


for i, game in enumerate(result):
   # print(f"Fetching details {i+1}/{len(result)}: {game['game_name']}")

    game_response = requests.get(game["game_url"], impersonate="chrome120")
    tree = html.fromstring(game_response.text)
    scripts = tree.xpath("//script/text()")

    for script in scripts:
        if "__PRELOADED_STATE__" in script:
            match = re.search(r"window\.__PRELOADED_STATE__\s*=\s*", script)
            if match:
                start = match.end()
                decoder = json.JSONDecoder()
                detail_data, _ = decoder.raw_decode(script, start)

                product_summaries = detail_data.get("core2", {}).get("products", {}).get("productSummaries", {})
                detail_product_id = list(product_summaries.keys())[0]  # get first key

                rating=jmespath.search('averageRating', product_summaries.get(detail_product_id, {}))
                thumbnail_url = product_summaries.get(detail_product_id, {}).get("images", {}).get("poster",{}).get("url")
                game_descrition=product_summaries.get(detail_product_id, {}).get("description")
                publisher_name=product_summaries.get(detail_product_id,{}).get("publisherName")
             
                game_images=jmespath.search('images.screenshots[*].url', product_summaries.get(detail_product_id, {}))
                release_date_raw = jmespath.search('releaseDate', product_summaries.get(detail_product_id, {}))
                published_date = release_date_raw.split("T")[0] if release_date_raw else None
               
                developer_name=jmespath.search('developerName', product_summaries.get(detail_product_id, {}))
                genre=jmespath.search('categories[*]', product_summaries.get(detail_product_id, {}))
                capabilities=jmespath.search('capabilities', product_summaries.get(detail_product_id, {}))
                available_on=jmespath.search('availableOn', product_summaries.get(detail_product_id, {}))
                offers=jmespath.search('specificPrices.purchaseable[*].listPrice', product_summaries.get(detail_product_id, {}))
                operating_system=jmespath.search('systemRequirements', product_summaries.get(detail_product_id, {}))
                content_rating=jmespath.search('contentRating.rating', product_summaries.get(detail_product_id, {}))
                feature_list=jmespath.search('contentRating.descriptors', product_summaries.get(detail_product_id, {}))

            break

print("All details fetched!")
print(result)

with open(r"C:\python practice\xbox_games\xbox_games_scraped_data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

