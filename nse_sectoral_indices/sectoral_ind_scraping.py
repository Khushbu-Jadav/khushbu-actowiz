from rich import print
import json
from curl_cffi import requests
import jmespath

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.nseindia.com/market-data/live-market-indices',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    # 'cookie': 'AKA_A2=A; _ga=GA1.1.677588674.1780289116; ak_bmsc=62FD2E74716ECA877001DA9651ED3DCE~000000000000000000000000000000~YAAQz68nF+a1r0GeAQAALgGAgQCiLIvb+Hi0ZTM0As+fFrNvcASvoMtmoAs7pwng6SoW/MbwI2J8hI/4b0w9sGT9F/eJkm7e2TYmwBtlOxhNDQok5t8kKqcYreP5qOWl9JAP9BCTCqdukHupCAdGIzACMKWGfzQ1GzynDnRWEThCKqBdXMNGNkLCEvDv0k5pIFkVtQZMbK5brOOJhyBfDFtoFkMjB+2/J7bAHNIVSWsyqTNzRYijHzw+eY5pH/Vwk3IdZrqQUluipt7r8YLeVOveZ0b0mKoHdG4ynMTqu4xaIr4UCDEBxPd/RyOQBwXS9OvvOYBDs3IjALUBsN92UqMkX7imdTD/YVqzLHn1NiWMf6HVpHHjPrOGHfqHXknh6iQGlUOmiZwq0m0D+TNijlYmi9nwkWU0jkqbnZKA64JGQ8mGRH3H8a2J5e3H/xi2fdQtIsNTM+5GaNReTHGS920=; nsit=bFLgCxuhTCrI-zamL_8b4AJp; bm_sz=460C253963D39755F7F018A8D0D98037~YAAQz68nFyiIsEGeAQAArjuDgQDt+onV0zIPn56kGIjxMVoqwe+xnTOkDe0XaRzScN4bzpjsQ60dzti4WgsgvDb+UM/AkBmb+I9lm0hUXMySaw+v7gLhMkqXezxI30brSsLAAGEXdBqp85YwDachReZpaxtSLJeN5fnV4EfVvJ5wH7wBCSrRIgw3fUW2v/XQDpUBA0rIx70FeTIXTq7AtfZBBAqcjlB70xr0QfbkwMyxDlX8UGAbmiAtBcsuSeBOmE/wWIdPfpxZCDIR5rpE0W50MvmQdmha9T2CmVtgztjeNky+IbAva3b9oZPat8YiIOQU5JQNfqkkYlpU8zXSw85yk04L944kWbw8Mj0HWpHCJGjXobn8sxY8Ekv+Xiq2hI27zv+/TFAAGwoVN14vap5PGnPuwDlk3eVz3Nlfs9e81G0=~4408130~3552052; _abck=FE3E5A64D250EFFF357440C4474AF7D1~0~YAAQz68nF46IsEGeAQAA0D2DgQ8Dyly6SN28GL7pF2/S5S71mVxSkM5QreqvFlJdKlCaKPVotH8D62jdDw2kILknBUBxSxna/qToiYnT/T32RJrX/4vA3S1Hcg5KeJuaZz4P+N3maGl4hnGWXOaLH9d5wVIen6b6jloTCivfJAfNes8E1EkJnf7N0z11+iiqZ1Es/YC0qVZCvFFM8BgvUMDU33y7tArCjq+jrwTzMJw1N24F4oT5KGfanXArSQRbHeRz3nBqw0nfdl70KN9quBR008Tu3sf3rVAxA/N0/Ameh7gENRP8cGm02WxGRyEbJ3floNbLCeFO8p5nNQS16VVjiHqRMFqG4gERSIS3EEmMoiI+7IW47eDyjjlbvAxoxWlJNWa60g8Vn3K957JHvyFtluNzO5nk4sr5Mtt4ekwg2rNC4ReZi0uQTiY8hkEa353uFG45XI8nX/gJxHEf6mStgMWOrX0nv6Huzkr/As82dag4ODIWHE8XeJ75SGT+9u/oj1YeCKhspE9Vw7z60AfyCxR0xHLW/o4b+MonqzQSZzgns8X3yAhHJXfW4ZWR+uX7mzuRXgLYBC+9/bfNxbSjFgtVhvD3/3Fb5G0+sIRavsKMBPTcpAKTsaMCyCK0QIcPaFY9EyxM2Jg=~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2f+4J1PhskJmkcfrS4eC3Sjdlf8sO94IEKasJITDI%2fSiuo7Nr2lNL2u2ctdppNIaq6lwIyjYFUz9WtdmD+%2f0CJTTXa%2fdAuNY1iNQx~-1; RT="z=1&dm=nseindia.com&si=5a761881-04b7-4548-a186-17096a6dfb7f&ss=mpuq68no&sl=1&se=8c&tt=145&bcn=%2F%2F684d0d47.akstat.io%2F"; _ga_87M7PJ3R97=GS2.1.s1780289115$o1$g1$t1780289329$j59$l0$h0; bm_sv=1D2CB3DEE4154AC1A2CE7747594E4A2A~YAAQz68nF9iJsEGeAQAAOEKDgQD0r5Ck1sYaJBmbXUcmkBnTDFims3VTsQ8rQNH4Z5Ro5D6asrSLmTnhNC0oB1XKNkpKc/z1bNsL544MEUF3yipzX6N9NXCppFddDJxTUmVPvIZTzfsSV579PlI96K+h9j8Q2Y6IELL1W3FeBjzh3Z9MvABmQhRsMAGyeuNrDRRc897JLoSYqcK4yBnw0roJyBUZEwV4dYIOYpzikUmcOFe5zbbBUfY/HqPRifMHa+sR~1',
}

response = requests.get('https://www.nseindia.com/api/allIndices',headers=headers)

all_data = response.json()

with open(r"C:\python practice\nse_sectoral_indices\sectoral_json_data.json","w",encoding='utf-8') as f:
    json.dump(all_data,f,indent=4,ensure_ascii=False)

result=[]

sectorals=jmespath.search("data[?key=='SECTORAL INDICES']",all_data)

for sectoral in sectorals:
    index_symbol=jmespath.search("indexSymbol",sectoral)
    index_name=index_symbol.replace(" ","%20")

    api_url=f"https://www.nseindia.com/api/equity-stock-indices?index={index_name}"
    api_response=requests.get(api_url,headers=headers,impersonate="chrome120")
    # print(api_url)
    data=api_response.json()
    # print(data)
    
    result.append({
            "sectoral_indices":jmespath.search("index",sectoral),
            "sectoral_data":[{
            "symbol":jmespath.search("symbol",d),
            "open":jmespath.search("open",d),
            "dayHigh":jmespath.search("dayHigh",d),
            "dayLow":jmespath.search("dayLow",d),
            "previousClose":jmespath.search("previousClose",d),
            "ltp":jmespath.search("lastPrice",d),
            "change":jmespath.search("change",d),
            "change_percentage":jmespath.search("pChange",d),
            "volume(shares)":jmespath.search("totalTradedVolume",d),
            "value(crores)":jmespath.search("totalTradedValue",d),
            "52W H(year high)":jmespath.search("yearHigh",d),
            "52W L(yearLow)":jmespath.search("yearLow",d),
            "percentage_Change_30days":jmespath.search("perChange30d",d),
            "date":jmespath.search("lastUpdateTime",d)
            }for d in jmespath.search("data", data)]
        })
print(result)

with open (r"C:\python practice\nse_sectoral_indices\scraped_sectoral_data.json",'w',encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False) 



