from fetch import Request_Data
from config import DEFAULT_HEADERS,MAIN_PAGE_SAVE_DIR
from lululemon_parser import parse_product_page
from db import execute_query
from queries import database_query, lululemon_product_query, insert_product_query
import json

url = "https://www.lululemon.com.hk/en-in/p/breezily-cinchable-hem-tank-top-trim/ci5vitmmvg.html?dwvar_ci5vitmmvg_color=035955"

execute_query(query=database_query)
execute_query("lululemon_db", query=lululemon_product_query)

req = Request_Data(
    url=url,
    headers=DEFAULT_HEADERS,
    path=MAIN_PAGE_SAVE_DIR
)

response = req.fetch_request(method="GET")

if response['is_success']:
    parsed_data = parse_product_page(response['body'],url)
    print(parsed_data)

    values = (parsed_data['product_id'],
              parsed_data['product_name'],
              parsed_data['product_url'],
              parsed_data['product_category'],
              parsed_data['product_price'],
              json.dumps(parsed_data['product_size']),
              json.dumps(parsed_data['image_url']),
              parsed_data['description']
             ) 
    execute_query("lululemon_db", query=insert_product_query, values=values)

    req.save_data_into_file(content=parsed_data, file_name="product_data.json")

else:
    print(response['error'])






