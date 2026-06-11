from curl_cffi import requests
import json
import jmespath
from rich import print
from lxml import html
import gzip
import time
import os

start_time = time.time()
os.makedirs(r"C:\python practice\carwale\pages", exist_ok=True)

cookies = {
    'CWC': 'ZxoMFstyATc6dYCoAH3223ohI',
    '_cwutmz': 'utmcsr%3Dgoogle%7Cutmgclid%3D%7Cutmccn%3D%28organic%29%7Cutmcmd%3Dorganic%7Cutmtrm%3D%7Cutmcnt%3D',
    'CurrentLanguage': 'en',
    '_abtest': '11',
    'languageSelected': 'en',
    '_gcl_au': '1.1.447229485.1781071514',
    '_ga': 'GA1.1.812366136.1781071514',
    '_carSearchType': '1',
    'BHC': 'ZxoMFstyATc6dYCoAH3223ohI',
    '_fbp': 'fb.1.1781071522187.954053609254515294',
    '_CustAreaId': '-1',
    '_CustAreaName': 'Select Area',
    '_CustZoneIdMaster': '',
    '_CustZoneMaster': 'Select Zone',
    '_CustCityIdMaster': '4',
    'versionstate': '{%223696%22:24306}',
    'versionStateOrder': '[3696]',
    '_pageviews_modelid': '-1',
    '_CustCityMaster': 'Bhopal',
    '_cwutmzsrc': 'G%7CG%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD',
    '_cwutmzmed': 'O%7CO%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN',
    'vernacularPopupClose': '1',
    '_AsktheExperts': '1',
    'FCCDCF': '%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%2219a77837-4b29-4d13-989e-96393eaed0af%5C%22%2C%5B1781071519%2C955000000%5D%5D%22%5D%5D%5D',
    'FCNEC': '%5B%5B%22AKsRol9jbBCLmtDx198bYP4PbyQjIKJwDWKsb6UOXH3rjMM0I4AjLo2mSucvDW6bSeZ70wIJMOgPUh98HcR14an97z10kSxSsF6zT7zqMvzGxSAHa_KorBXC-RRtbfP2P5PG-L8vFCn2e8L--3OiPcPAa1DNHjzA-Q%3D%3D%22%5D%5D',
    '_uetsid': '5f5fe430649211f1a59b358004330f52',
    '_uetvid': '5f5ff9f0649211f1a78a4fe40febe6ba',
    '_userModelHistory': '3696~2789',
    '__gads': 'ID=c77a5562218c31e6:T=1781072428:RT=1781073524:S=ALNI_Ma6IJduO8i43atk_9Ah0nN_FwBn3w',
    '__gpi': 'UID=000013c5c94bb395:T=1781072428:RT=1781073524:S=ALNI_MY4ZpMMh6iOdMNsgch5-E8lxqo6tg',
    '__eoi': 'ID=dc4ff6aa392130d6:T=1781072428:RT=1781073524:S=AA-AfjZT9NzM-yRoHT64fhMtZUqg',
    'bhs_cw': 'ZxoMFstyATc6dYCoAH3223ohI.QfmlUqdjfL.1781071499.1781073617.1781073709.1',
    '_ga_Z81QVQY510': 'GS2.1.s1781071514$o1$g1$t1781073725$j11$l0$h0',
    '_cwv': 'ZxoMFstyATc6dYCoAH3223ohI.ZxoMFstyATc6dYCoAH3223ohI.1781071499.1781073775.1781073881.1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    # 'cookie': 'CWC=ZxoMFstyATc6dYCoAH3223ohI; _cwutmz=utmcsr%3Dgoogle%7Cutmgclid%3D%7Cutmccn%3D%28organic%29%7Cutmcmd%3Dorganic%7Cutmtrm%3D%7Cutmcnt%3D; CurrentLanguage=en; _abtest=11; languageSelected=en; _gcl_au=1.1.447229485.1781071514; _ga=GA1.1.812366136.1781071514; _carSearchType=1; BHC=ZxoMFstyATc6dYCoAH3223ohI; _fbp=fb.1.1781071522187.954053609254515294; _CustAreaId=-1; _CustAreaName=Select Area; _CustZoneIdMaster=; _CustZoneMaster=Select Zone; _CustCityIdMaster=4; versionstate={%223696%22:24306}; versionStateOrder=[3696]; _pageviews_modelid=-1; _CustCityMaster=Bhopal; _cwutmzsrc=G%7CG%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD%7CD; _cwutmzmed=O%7CO%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN%7CNN; vernacularPopupClose=1; _AsktheExperts=1; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%2219a77837-4b29-4d13-989e-96393eaed0af%5C%22%2C%5B1781071519%2C955000000%5D%5D%22%5D%5D%5D; FCNEC=%5B%5B%22AKsRol9jbBCLmtDx198bYP4PbyQjIKJwDWKsb6UOXH3rjMM0I4AjLo2mSucvDW6bSeZ70wIJMOgPUh98HcR14an97z10kSxSsF6zT7zqMvzGxSAHa_KorBXC-RRtbfP2P5PG-L8vFCn2e8L--3OiPcPAa1DNHjzA-Q%3D%3D%22%5D%5D; _uetsid=5f5fe430649211f1a59b358004330f52; _uetvid=5f5ff9f0649211f1a78a4fe40febe6ba; _userModelHistory=3696~2789; __gads=ID=c77a5562218c31e6:T=1781072428:RT=1781073524:S=ALNI_Ma6IJduO8i43atk_9Ah0nN_FwBn3w; __gpi=UID=000013c5c94bb395:T=1781072428:RT=1781073524:S=ALNI_MY4ZpMMh6iOdMNsgch5-E8lxqo6tg; __eoi=ID=dc4ff6aa392130d6:T=1781072428:RT=1781073524:S=AA-AfjZT9NzM-yRoHT64fhMtZUqg; bhs_cw=ZxoMFstyATc6dYCoAH3223ohI.QfmlUqdjfL.1781071499.1781073617.1781073709.1; _ga_Z81QVQY510=GS2.1.s1781071514$o1$g1$t1781073725$j11$l0$h0; _cwv=ZxoMFstyATc6dYCoAH3223ohI.ZxoMFstyATc6dYCoAH3223ohI.1781071499.1781073775.1781073881.1',
}

response = requests.get('https://www.carwale.com/', cookies=cookies, headers=headers)



with open(r"C:\python practice\carwale\carwale_data.json","r",encoding='utf-8') as f:
   data = json.load(f)

result=[]

masking_name=jmespath.search("homePage.makeList[*].maskingName",data)
print(len(masking_name))

base_url="https://www.carwale.com"

for name in masking_name:
    brand_url = f"{base_url}/{name}-cars/"

    car_response=requests.get(brand_url,cookies=cookies,headers=headers,impersonate="chrome120")
    car_data=car_response.text

    tree = html.fromstring(car_data)
    c_urls=tree.xpath("//a[@class='o-f o-aF o-jJ o-eQ']/@href")
     
    result.append({
        "brand":name,
        "brand_url": brand_url,
        "car_url":[base_url+c for c in c_urls]
    })

print(result)
print(len(result))

with open(r"C:\python practice\carwale\scraped_carwale.json","w",encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False)


i = 0
for brand in result:
    for url in brand["car_url"]:
        try:
            resp = requests.get(url, cookies=cookies, headers=headers, impersonate="chrome120", timeout=30)

            filename = f"C:\\python practice\\carwale\\pages\\car_{i+1}.html.gz"
            with gzip.open(filename, "wt", encoding="utf-8") as f:
                f.write(resp.text)

            print(f"[{i+1}] Saved: {filename} → {url}")
            i += 1

        except Exception as e:
            print(f"Error {url}: {e}")

end_time=time.time()
print(f"total saved:{i}")
print(f"time taken:{(end_time-start_time)/60:.2f}")