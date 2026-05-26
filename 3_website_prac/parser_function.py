import jmespath
from rich import print
from curl_cffi import requests
from config import cookies,headers,params
response = requests.get('https://www.crocs.in/graphql', params=params, cookies=cookies, headers=headers)

def extract_raw_data(
    url,
    path,
    headers=None,
    params=None,
    cookies=None,
):

    response = requests.get(
            url=url,
            headers=headers,
            params=params,
            cookies=cookies,
            impersonate="chrome120"
        )
    try:      
        data = response.json()
        result = jmespath.search(path, data) 
        return result

    except Exception as e:
        print("\nERROR:\n", e)
        return None


