from parser_function import extract_raw_data
import json
import jmespath
from config import crocs_path,crocs_url,headers,params,cookies,instagram_path,booking_path

crocs_products = extract_raw_data(
    url=crocs_url,
    path=crocs_path,
    headers=headers,
    params=params,
    cookies=cookies
)

print("\nCROCS PRODUCTS:\n")

print(crocs_products)

with open(r"C:\python practice\3_website_prac\output\crocks_data.json","w",encoding='utf-8') as f:
    json.dump(crocs_products,f,indent=4)




with open(r"C:\python practice\3_website_prac\instagram.json","r",encoding="utf-8") as f:
    instagram_data = json.load(f)

instagram_comments = jmespath.search(instagram_path,instagram_data)

print("\nINSTAGRAM COMMENTS:\n")
print("comments", instagram_comments)

with open(r"C:\python practice\3_website_prac\output\instagram_comments.json","w",encoding="utf-8") as f:
    json.dump(instagram_comments,f,indent=4,ensure_ascii=False)




with open(r"C:\python practice\3_website_prac\booking.json","r",encoding="utf-8") as f:
    booking_data = json.load(f)

booking_hotels = jmespath.search(booking_path,booking_data)

print("\nBOOKING HOTELS:\n")
print(booking_hotels)

with open(r"C:\python practice\3_website_prac\output\booking_hotels.json","w",encoding="utf-8") as f:
    json.dump(booking_hotels,f,indent=4,ensure_ascii=False)
