from fetch import Request_Data
from config import DEFAULT_HEADERS, MAIN_PAGE_SAVE_DIR
from parsers.bonkers_parser import parse_product_page as bonkers_parser
from parsers.only_parser import parse_product_page as only_parser
from parsers.lululemon_parser import parse_product_page as lululemon_parser
from db import execute_query
from queries import (database_query,bonker_product_query,only_product_query,
                    lululemon_product_query,bonkers_insert_query,only_insert_query,
                    lululemon_insert_query)
import json

websites = [
    {
        "site_name": "bonkers",
        "url": "https://www.bonkerscorner.com/collections/bonkers-x-anushka-sen/products/azure-trim-knit-co-ord-set-1",
        "database": "fashion_db",
        "create_table_query": bonker_product_query,
        "insert_query": bonkers_insert_query,
        "parser": bonkers_parser
    },

    {
        "site_name": "only",
        "url": "https://www.only.in/products/902477001-cropped-check-print-shirt",
        "database": "fashion_db",
        "create_table_query": only_product_query,
        "insert_query": only_insert_query,
        "parser": only_parser
    },

    {
        "site_name": "lululemon",
        "url": "https://www.lululemon.com.hk/en-in/p/breezily-cinchable-hem-tank-top-trim/ci5vitmmvg.html?dwvar_ci5vitmmvg_color=035955",
        "database": "fashion_db",
        "create_table_query": lululemon_product_query,
        "insert_query": lululemon_insert_query,
        "parser": lululemon_parser
    }
]

execute_query(query=database_query)

for site in websites:
    execute_query(site["database"],query=site["create_table_query"])

    req = Request_Data(url=site["url"],headers=DEFAULT_HEADERS,path=f"{MAIN_PAGE_SAVE_DIR}/{site['site_name']}")

    response = req.fetch_request(method="GET")

    if response["is_success"]:

        parsed_data = site["parser"](response["body"],site["url"])
        print(parsed_data)
        
        values = (

            parsed_data['product_id'],
            parsed_data['product_name'],
            parsed_data['product_url'],
            parsed_data['product_category'],
            parsed_data['product_price'],
            json.dumps(parsed_data['product_size']),
            json.dumps(parsed_data['image_url']),
            parsed_data['description']
        )
        execute_query(site["database"],query=site["insert_query"],values=values)
        req.save_data_into_file(content=parsed_data,file_name="product_data.json")

    else:
        print(response["error"])


