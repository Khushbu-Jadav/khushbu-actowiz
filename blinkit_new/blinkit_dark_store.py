from fastapi import FastAPI
from curl_cffi import requests

app = FastAPI()

cookies = {
    '_fbp': 'fb.1.1779968206638.415657942909143944',
    'gr_1_deviceId': '91d70fec-1b4e-446d-8c0c-d90d3b79c7c7',
    '_gid': 'GA1.2.1928383295.1781181343',
    '_gcl_au': '1.1.2093825443.1779968205',
    '__cf_bm': 'omjqGrmDn2p3eFw7gOgCoe2rvkf27x63Ptxdaq1eBNk-1781266926.0982254-1.0.1.1-FBUKTZQfEAK2nNO9cbyjtZ.x9x6KfAZhra.D19ONZHJQWowH0F2rrPkgOcey1ArhDe01YyKET3vsje6r3F1XWTX3xWAci70meINcuUhd8sU8dpSJm5YDsB_hE7B5IpGl',
    '_cfuvid': '2RuwP_oske07.IE3QQbVw4zpcRlriuNdonJ_Z4ihGeY-1781266926.0982254-1.0.1.1-ma5DTeUcvKhXJM4_rE5YnK1yqrEGjbp7WKCXhNR3PPY',
    '_gat_UA-85989319-1': '1',
    '_ga': 'GA1.1.1004733831.1779968206',
    '_ga_JSMJG966C7': 'GS2.1.s1781267324$o15$g1$t1781267325$j59$l0$h0',
    '_ga_DDJ0134H6Z': 'GS2.2.s1781267326$o13$g0$t1781267326$j60$l0$h0'
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'access_token': 'null',
    'app_client': 'consumer_web',
    'app_version': '52434332',
    'auth_key': 'c761ec3633c22afad934fb17a66385c1c06c5472b4898b866b7306186d0bb477',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'device_id': 'eb282ea60e01c454',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://blinkit.com/?srsltid=AfmBOopfMm4SgSyHkqGAPqwb0xUoK9YKy6TtZ5wbNk1eAtZG-BTOfbgo',
    'rn_bundle_version': '1009003012',
    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'session_uuid': 'e31fd194-ed41-4d98-8b1d-cb276577a508',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'web_app_version': '1008010016',
    # 'cookie': '_fbp=fb.1.1779968206638.415657942909143944; gr_1_deviceId=91d70fec-1b4e-446d-8c0c-d90d3b79c7c7; city=Chennai; _gid=GA1.2.1928383295.1781181343; _gcl_au=1.1.2093825443.1779968205; gr_1_locality=Ahmedabad; __cf_bm=omjqGrmDn2p3eFw7gOgCoe2rvkf27x63Ptxdaq1eBNk-1781266926.0982254-1.0.1.1-FBUKTZQfEAK2nNO9cbyjtZ.x9x6KfAZhra.D19ONZHJQWowH0F2rrPkgOcey1ArhDe01YyKET3vsje6r3F1XWTX3xWAci70meINcuUhd8sU8dpSJm5YDsB_hE7B5IpGl; _cfuvid=2RuwP_oske07.IE3QQbVw4zpcRlriuNdonJ_Z4ihGeY-1781266926.0982254-1.0.1.1-ma5DTeUcvKhXJM4_rE5YnK1yqrEGjbp7WKCXhNR3PPY; _gat_UA-85989319-1=1; _ga=GA1.1.1004733831.1779968206; _ga_JSMJG966C7=GS2.1.s1781267324$o15$g1$t1781267325$j59$l0$h0; _ga_DDJ0134H6Z=GS2.2.s1781267326$o13$g0$t1781267326$j60$l0$h0; gr_1_lat=23.048907399999997; gr_1_lon=72.6058584; gr_1_landmark=Ahmedabad%2C%20Gujarat%20380016%2C%20India',
}

INDIA_LAT = "20.5937"
INDIA_LNG = "78.9629"

@app.get("/serviceable/{pincode}")
def check_pincode(pincode: str):

    session_token = "e7f0b667-15de-48d9-8102-691ad5b84396"

    response = requests.get(
        "https://blinkit.com/location/autoSuggest",
        params={
            "query": pincode,
            "lat": INDIA_LAT,
            "lng": INDIA_LNG,
            "session_token": session_token,
        },
        headers=headers,
        cookies=cookies,
        impersonate="chrome120",
    )

    auto_data = response.json()

    print("FULL AUTOSUGGEST RESPONSE:", auto_data)
    print("autoSuggest status:", response.status_code)

    if response.status_code != 200:
        return {
            "pincode": pincode,
            "error": f"autoSuggest failed: {response.status_code}",
            "detail": response.text
        }

    suggestions = auto_data.get("ui_data", {}).get("suggestions", [])

    if not suggestions:
        return {
            "pincode": pincode,
            "is_serviceable": False,
            "message": "No location found"
        }

    selected = None

    for item in suggestions:
        if item.get("title", {}).get("text") == pincode:
            selected = item
            break

    if selected is None:
        selected = suggestions[0]

    place_id = selected.get("meta", {}).get("place_id")
    title = selected.get("title", {}).get("text")
    description = selected.get("subtitle", {}).get("text")

    print(f"Found: {title} | {description} | place_id: {place_id}")

    info_response = requests.get(
        "https://blinkit.com/location/info",
        params={
            "place_id": place_id,
            "title": title,
            "description": description,
            "is_pin_moved": "false",
            "session_token": session_token,
        },
        headers=headers,
        cookies=cookies,
        impersonate="chrome120",
    )

    print("INFO STATUS:", info_response.status_code)
    print("INFO RESPONSE:", info_response.text)

    if info_response.status_code != 200:
        return {
            "pincode": pincode,
            "error": f"location/info failed: {info_response.status_code}",
            "detail": info_response.text
        }

    info_data = info_response.json()

    coordinate = info_data.get("coordinate", {})
    location_info = info_data.get("location_info", {})

    return {
        "pincode": pincode,
        "matched_pincode": location_info.get("postal_code"),
        "city": location_info.get("city"),
        "state": location_info.get("state"),
        "lat": coordinate.get("lat"),
        "lon": coordinate.get("lon"),
        "is_serviceable": info_data.get("is_serviceable", False)
    }