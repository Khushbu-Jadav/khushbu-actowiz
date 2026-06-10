from curl_cffi import requests
from lxml import etree
from rich import print
import pymongo
import gzip
import os
import time
import sys

start_time = time.time()

cookies = {
    'localization': 'IN',
    '_shopify_y': 'c6cd6b12-d7a3-442a-8f4d-65fc10ff4816',
    'WISHLIST_TOTAL': '0',
    'device_id': 'a324114f-0e3d-41f5-8826-3598baba0763',
    'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX18sx4GGWTs4bRfhIPO9X3tN69%2BklLDtJV6%2BWceXKPn9mr11BPU1fF3W',
    'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX18%2BJg7EL95BCrUmbIrsbGv380tq%2B%2BhjFYeD8Djon6eOwp0czpAYk4%2FN',
    '_gcl_au': '1.1.309948763.1779422882',
    'WISHLIST_PRODUCTS_IDS': '{}',
    'WISHLIST_PRODUCTS_IDS_SET': '1',
    'WISHLIST_UUID': 'null',
    'WISHLIST_IP_ADDRESS': '45.114.65.131',
    '_ga': 'GA1.1.373480132.1779422882',
    '_fbp': 'fb.1.1779422882048.62930116282673251',
    '_ga_Z7JGKLREKL': 'GS2.1.s1779428303$o2$g1$t1779428376$j60$l0$h0',
    '_shopify_s': '5472f4bd-1ce3-4d6a-8769-56d09df7cf04',
    '_shopify_analytics': ':AZ5N3fX4AAEAFi7MCiF-NT3xe4U_p3CAl9_eUveT0OLECT9vNMCl6cHwnx_cWcpN40qzYy9x1xuixbVz09XJw6zD5HDMnuyc8sCEe-NUsG5W1nVupkt2CGlc02nv7EWfh3kpU2o-uWZu2vcj:',
    '_shopify_marketing': ':AZ5N3fX4AAEAkrhY4dViWz43PrvcE0Ro23_Vm74Crmn7foRfvnsjB7jcOW3ytQO1Moi5AYJWhSVyQvs9FBAodFLimMRp5R0rxlpnX8Deq-BevzCYCh1iAQU1JdY4wEKniYsPe5ygJPA0zI2ho7yaz1cldZVf:',
    'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2B%2B3i5qXNZ3OoiDn%2FlwwGX%2FIZqsGT5mInk%3D',
    'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX180edUyLsPSXlb%2BfU6ckMGV7us1ryymxlRUlzjRhWH1q2xwSMjrzCa1Qif76spWmSWffaOa%2FMnfSA%3D%3D',
    'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19MUbcWTk8kElxJXrwjtWkh5R7UuDfMi6c%3D',
    'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2BeGjfQoPHbAAeENmykT9nxz1ZHV8439Lg%3D',
    'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX19w5xA7wPaHBbrWYAKi8SDRwhwJ4cyGGoY%3D',
    '_clck': 'k6ry6c%5E2%5Eg6r%5E0%5E2333',
    '_ga_FDHC4G288J': 'GS2.1.s1780996765$o4$g0$t1780996765$j60$l0$h0',
    '__insights_pid': 'd6d7df0a-dfbd-4ba0-ae3e-73bc1cd18ab6',
    'insights-session-id': 'a2c5b98a-8181-4de0-9266-4179d0dd1f30',
    '_shopify_essential': ':AZ5N3fXpAAEADxBnXpiAFE-9zq0VExvaiGylU-f1mtX1MdyDK-q-iUo0A9K3gqGAPQW3ggVFNBZhKCYhGJz2z-27odZxmAvISewbwUpzTlyTs5iLFYAIfCa8gr9p_k6-tlnxRPLHT8-yC4l5KY0SE7VTwH-8Otm0eBMD2S_fjD0wPf0aH_08WVNcBAqWiFbTiMuqAIC-igyGqQu3jW8ZU0f60_5N_0SRcVKmJiDYsYIe7QvyynLq1IHr8Op1bDo7ZXd5Iz09PL4pnzJ3Nl4yMvu6n4vbyVyA3t7DwoyD9Kkray_6P4_8oICAI8iTCyrM5rGNMaNF1g8Upo4h_8caZOStBD0v5mjd6_bjGwEWmTzy2STSPBZN1IUsRBS9f7iyGepkitczYrBr3OvzicdfedUOVIdVLWQfqjoj007ay5gRNL-b5dJxB5oHao3We2zeIbPLym5enXW83YUUXeUbGXUY4KYBMVlHXlRT-VLNoBGCDG9O51xAdl8F6y97YK-Gl-vFa5TLxOR35le4VXPR4HGZUKsscK8:',
    '_clsk': '18lm2wo%5E1780996766156%5E1%5E1%5Ex.clarity.ms%2Fcollect',
    '_ga_S44GWB7FM2': 'GS2.1.s1780996765$o4$g1$t1780996790$j35$l0$h1120886774',
    'rl_session': 'RudderEncrypt%3AU2FsdGVkX1%2BRXD6DNUEFZUqgcJ1iU7e3bIagcD%2FGoSZDqOcngOw6YY4sm8XDMADBSD48MUqXDl7Ao1jgnm0I4eyM%2F3fVr9SxWo2ltgp2Ee8JGnMuMIDTyFPX7x9DueuttYQL4Z9DGMnicKS%2B8xyKvw%3D%3D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    # 'cookie': 'localization=IN; _shopify_y=c6cd6b12-d7a3-442a-8f4d-65fc10ff4816; WISHLIST_TOTAL=0; device_id=a324114f-0e3d-41f5-8826-3598baba0763; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX18sx4GGWTs4bRfhIPO9X3tN69%2BklLDtJV6%2BWceXKPn9mr11BPU1fF3W; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18%2BJg7EL95BCrUmbIrsbGv380tq%2B%2BhjFYeD8Djon6eOwp0czpAYk4%2FN; _gcl_au=1.1.309948763.1779422882; WISHLIST_PRODUCTS_IDS={}; WISHLIST_PRODUCTS_IDS_SET=1; WISHLIST_UUID=null; WISHLIST_IP_ADDRESS=45.114.65.131; _ga=GA1.1.373480132.1779422882; _fbp=fb.1.1779422882048.62930116282673251; _ga_Z7JGKLREKL=GS2.1.s1779428303$o2$g1$t1779428376$j60$l0$h0; _shopify_s=5472f4bd-1ce3-4d6a-8769-56d09df7cf04; _shopify_analytics=:AZ5N3fX4AAEAFi7MCiF-NT3xe4U_p3CAl9_eUveT0OLECT9vNMCl6cHwnx_cWcpN40qzYy9x1xuixbVz09XJw6zD5HDMnuyc8sCEe-NUsG5W1nVupkt2CGlc02nv7EWfh3kpU2o-uWZu2vcj:; _shopify_marketing=:AZ5N3fX4AAEAkrhY4dViWz43PrvcE0Ro23_Vm74Crmn7foRfvnsjB7jcOW3ytQO1Moi5AYJWhSVyQvs9FBAodFLimMRp5R0rxlpnX8Deq-BevzCYCh1iAQU1JdY4wEKniYsPe5ygJPA0zI2ho7yaz1cldZVf:; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2B%2B3i5qXNZ3OoiDn%2FlwwGX%2FIZqsGT5mInk%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX180edUyLsPSXlb%2BfU6ckMGV7us1ryymxlRUlzjRhWH1q2xwSMjrzCa1Qif76spWmSWffaOa%2FMnfSA%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19MUbcWTk8kElxJXrwjtWkh5R7UuDfMi6c%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BeGjfQoPHbAAeENmykT9nxz1ZHV8439Lg%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19w5xA7wPaHBbrWYAKi8SDRwhwJ4cyGGoY%3D; _clck=k6ry6c%5E2%5Eg6r%5E0%5E2333; _ga_FDHC4G288J=GS2.1.s1780996765$o4$g0$t1780996765$j60$l0$h0; __insights_pid=d6d7df0a-dfbd-4ba0-ae3e-73bc1cd18ab6; insights-session-id=a2c5b98a-8181-4de0-9266-4179d0dd1f30; _shopify_essential=:AZ5N3fXpAAEADxBnXpiAFE-9zq0VExvaiGylU-f1mtX1MdyDK-q-iUo0A9K3gqGAPQW3ggVFNBZhKCYhGJz2z-27odZxmAvISewbwUpzTlyTs5iLFYAIfCa8gr9p_k6-tlnxRPLHT8-yC4l5KY0SE7VTwH-8Otm0eBMD2S_fjD0wPf0aH_08WVNcBAqWiFbTiMuqAIC-igyGqQu3jW8ZU0f60_5N_0SRcVKmJiDYsYIe7QvyynLq1IHr8Op1bDo7ZXd5Iz09PL4pnzJ3Nl4yMvu6n4vbyVyA3t7DwoyD9Kkray_6P4_8oICAI8iTCyrM5rGNMaNF1g8Upo4h_8caZOStBD0v5mjd6_bjGwEWmTzy2STSPBZN1IUsRBS9f7iyGepkitczYrBr3OvzicdfedUOVIdVLWQfqjoj007ay5gRNL-b5dJxB5oHao3We2zeIbPLym5enXW83YUUXeUbGXUY4KYBMVlHXlRT-VLNoBGCDG9O51xAdl8F6y97YK-Gl-vFa5TLxOR35le4VXPR4HGZUKsscK8:; _clsk=18lm2wo%5E1780996766156%5E1%5E1%5Ex.clarity.ms%2Fcollect; _ga_S44GWB7FM2=GS2.1.s1780996765$o4$g1$t1780996790$j35$l0$h1120886774; rl_session=RudderEncrypt%3AU2FsdGVkX1%2BRXD6DNUEFZUqgcJ1iU7e3bIagcD%2FGoSZDqOcngOw6YY4sm8XDMADBSD48MUqXDl7Ao1jgnm0I4eyM%2F3fVr9SxWo2ltgp2Ee8JGnMuMIDTyFPX7x9DueuttYQL4Z9DGMnicKS%2B8xyKvw%3D%3D',
}

response = requests.get('https://www.only.in/sitemap.xml', cookies=cookies, headers=headers)

root=etree.fromstring(response.content)
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

all_links = root.xpath("//sm:loc/text()", namespaces=ns)

product_sitemaps = [l for l in all_links if "sitemap_products" in l]
# print(product_sitemaps)

product_url=[]

for p in product_sitemaps:
    time.sleep(10)
    resp = requests.get(p, cookies=cookies, headers=headers, impersonate="chrome120", timeout=30)
    child_root = etree.fromstring(resp.content)
    links = [l for l in child_root.xpath("//sm:loc/text()", namespaces=ns) if "/products/" in l]
    product_url.extend(links)
    print(len(links))
    time.sleep(2)

print(len(product_url))
print(product_url[0])



myclient = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = myclient["only_db"]

collection = my_db["product_urls"]
collection.delete_many({})
collection.insert_many([{"product_url": u} for u in product_url])
print("Data Inserted")



os.makedirs("pages", exist_ok=True)


start = int(sys.argv[1])
end = int(sys.argv[2])

print(f"Processing URLs from {start} to {end}")

for i, url in enumerate(product_url[start:end],start=start):
    try:
        resp = requests.get(url, cookies=cookies, headers=headers, impersonate="chrome120", timeout=30)
        
        filename = f"pages/product_{i+1}.html.gz"
        with gzip.open(filename, "wt",encoding='utf-8') as f:
            f.write(resp.text)
        
        print(f"[{i+1}/{len(product_url)}] Saved: {filename}")

    except Exception as e:
        print(f"Error {url}: {e}")

end_time = time.time()

print(f"\nExecution Time: {(end_time - start_time)/60:.2f} minutes")
print("Done!")