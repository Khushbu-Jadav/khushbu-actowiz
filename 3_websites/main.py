import jmespath
from rich import print
from curl_cffi import requests
import json

cookies = {
    'optimizelyEndUserId': 'oeu1779694682491r0.3515372742166576',
    'shopflo_long_session_id': 'd342a3c1-7d49-408e-b9be-f44e2e6fb670',
    'shopflo_session_id': 'f17599ea-9d2b-462f-8335-1e6bd3d81cc4',
    '_gcl_au': '1.1.1734113001.1779694685',
    '_ga': 'GA1.1.1186877597.1779694689',
    '_scid': 'btmtlfUuE9rIza5kaT9iWVHuaRtQfTGe',
    'flo_index_hash': 'BOoTpfcD',
    '_sctr': '1%7C1779647400000',
    'tfpsi': 'd0a5808c-20c2-45a3-b3f7-623841ed1865',
    '_clck': '1atxrtc%5E2%5Eg6c%5E0%5E2336',
    '__ta_device': 'n6cig20OHSFcB7QLbjcVrJvFBQ62P2j8',
    '__ta_visit': '6DuNiscE4ynJCOb04iVpstqP9xYT4KsU',
    '_fbp': 'fb.1.1779694695070.880531856706664292',
    '__sts': 'eyJzaWQiOjE3Nzk2OTQ2OTUzMDcsInR4IjoxNzc5Njk0Njk1MzA3LCJ1cmwiOiJodHRwcyUzQSUyRiUyRnd3dy5jcm9jcy5pbiUyRm1lbi5odG1sJTNGcGFnZSUzRDEiLCJwZXQiOjE3Nzk2OTQ2OTUzMDcsInNldCI6MTc3OTY5NDY5NTMwN30%3D',
    '__stp': 'eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiJiMWI0YzI1Mi00NTY5LTQyZWYtYTRhYy1lMDZhNjlhYzk5MjcifQ%3D%3D',
    'GTM_10secs2pageviewAlreadyFired': 'true',
    '__pr.34ahoq': 'PyfPgcIJXv',
    '__stdf': 'MA%3D%3D',
    '__stgeo': 'IjAi',
    '__stbpnenable': 'MQ%3D%3D',
    'bxSesT': 'MTc3OTY5NDY5NjA1MA%3D%3D',
    'bxSesC': 'MTc3OTY5NDY5NjA1MA%3D%3D',
    'boxx_token_id': 'YjFiNGMyNTItNDU2OS00MmVmLWE0YWMtZTA2YTY5YWM5OTI3',
    '__stat': 'IkJMT0NLIg%3D%3D',
    'bxSegDetail': 'eyJieFNlc1QiOjE3Nzk2OTQ2OTYwNTAsInVzZXJUeXBlIjoibmV3IiwidXNlclJhbmRvbSI6MC43NDUxNzA2ODQ3NTEzOTEsInBydk12IjoiNTYwIiwicHViTXYiOiJib3h4IiwidXNlclNlZyI6Il9kZWZhdWx0IiwibW9kZWxTZWciOiJib3h4X19kZWZhdWx0In0%3D',
    'GTM_15secs2pageviewAlreadyFired': 'true',
    'g_state': '{"i_l":0,"i_ll":1779695054263,"i_b":"CrdpfXLf5ZxScgkKU0j5+Yh8JTvN4xflgSNoGKDOVqQ","i_e":{"enable_itp_optimization":0},"i_et":1779694687465}',
    '_scid_r': 'aVmtlfUuE9rIza5kaT9iWVHuaRtQfTGeJCd_mg',
    'cto_bundle': 'URbOb19EYSUyRndSNDlTOSUyQjhQclhJNVFVVVh1RkNPQUF1S2YxdFJJc1dBcnNTQnZTMlVzMEpkeW5ENkJjSDN6RlRWakExODlVOTdYYzdVb0xtbHpFaU9QU0l5QnF3aU1RZnRNRFprMGc0bmxJRnk5Z2VJVThVN0Q3bHNYY1BEY3RtR1lXNE9NalhrODZhS2JFRjFOd2dWZkt6QmRnJTNEJTNE',
    '_uetsid': 'b06266d0580c11f181b0b5d1319244f6',
    '_uetvid': 'b0630010580c11f180ce1d61a40a5829',
    '_clsk': '1fgvw3%5E1779695061270%5E4%5E1%5Ex.clarity.ms%2Fcollect',
    'GTM_ticker_view': "It's Sale Time:Up To,New User Exclusive:,Jibbitz Charms Deal:,Price Revision Notic,New User Exclusive:,New User Exclusive:,New User Exclusive:",
    '_ga_TLYZYXJLJJ': 'GS2.1.s1779694688$o1$g1$t1779695130$j60$l0$h1780055590',
    'GTM_pageviewCount': '5',
    'optimizelySession': '1779695137521',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': '',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.crocs.in/men.html?page=1',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'store': 'default',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'x-magento-cache-id': 'eb1adfa7ceaffc51e245cd359c1fa6d30fa786d8b030b03cd94ad733dcd51fdc',
    # 'cookie': 'optimizelyEndUserId=oeu1779694682491r0.3515372742166576; shopflo_long_session_id=d342a3c1-7d49-408e-b9be-f44e2e6fb670; shopflo_session_id=f17599ea-9d2b-462f-8335-1e6bd3d81cc4; _gcl_au=1.1.1734113001.1779694685; _ga=GA1.1.1186877597.1779694689; _scid=btmtlfUuE9rIza5kaT9iWVHuaRtQfTGe; flo_index_hash=BOoTpfcD; _sctr=1%7C1779647400000; tfpsi=d0a5808c-20c2-45a3-b3f7-623841ed1865; _clck=1atxrtc%5E2%5Eg6c%5E0%5E2336; __ta_device=n6cig20OHSFcB7QLbjcVrJvFBQ62P2j8; __ta_visit=6DuNiscE4ynJCOb04iVpstqP9xYT4KsU; _fbp=fb.1.1779694695070.880531856706664292; __sts=eyJzaWQiOjE3Nzk2OTQ2OTUzMDcsInR4IjoxNzc5Njk0Njk1MzA3LCJ1cmwiOiJodHRwcyUzQSUyRiUyRnd3dy5jcm9jcy5pbiUyRm1lbi5odG1sJTNGcGFnZSUzRDEiLCJwZXQiOjE3Nzk2OTQ2OTUzMDcsInNldCI6MTc3OTY5NDY5NTMwN30%3D; __stp=eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiJiMWI0YzI1Mi00NTY5LTQyZWYtYTRhYy1lMDZhNjlhYzk5MjcifQ%3D%3D; GTM_10secs2pageviewAlreadyFired=true; __pr.34ahoq=PyfPgcIJXv; __stdf=MA%3D%3D; __stgeo=IjAi; __stbpnenable=MQ%3D%3D; bxSesT=MTc3OTY5NDY5NjA1MA%3D%3D; bxSesC=MTc3OTY5NDY5NjA1MA%3D%3D; boxx_token_id=YjFiNGMyNTItNDU2OS00MmVmLWE0YWMtZTA2YTY5YWM5OTI3; __stat=IkJMT0NLIg%3D%3D; bxSegDetail=eyJieFNlc1QiOjE3Nzk2OTQ2OTYwNTAsInVzZXJUeXBlIjoibmV3IiwidXNlclJhbmRvbSI6MC43NDUxNzA2ODQ3NTEzOTEsInBydk12IjoiNTYwIiwicHViTXYiOiJib3h4IiwidXNlclNlZyI6Il9kZWZhdWx0IiwibW9kZWxTZWciOiJib3h4X19kZWZhdWx0In0%3D; GTM_15secs2pageviewAlreadyFired=true; g_state={"i_l":0,"i_ll":1779695054263,"i_b":"CrdpfXLf5ZxScgkKU0j5+Yh8JTvN4xflgSNoGKDOVqQ","i_e":{"enable_itp_optimization":0},"i_et":1779694687465}; _scid_r=aVmtlfUuE9rIza5kaT9iWVHuaRtQfTGeJCd_mg; cto_bundle=URbOb19EYSUyRndSNDlTOSUyQjhQclhJNVFVVVh1RkNPQUF1S2YxdFJJc1dBcnNTQnZTMlVzMEpkeW5ENkJjSDN6RlRWakExODlVOTdYYzdVb0xtbHpFaU9QU0l5QnF3aU1RZnRNRFprMGc0bmxJRnk5Z2VJVThVN0Q3bHNYY1BEY3RtR1lXNE9NalhrODZhS2JFRjFOd2dWZkt6QmRnJTNEJTNE; _uetsid=b06266d0580c11f181b0b5d1319244f6; _uetvid=b0630010580c11f180ce1d61a40a5829; _clsk=1fgvw3%5E1779695061270%5E4%5E1%5Ex.clarity.ms%2Fcollect; GTM_ticker_view=It\'s Sale Time:Up To,New User Exclusive:,Jibbitz Charms Deal:,Price Revision Notic,New User Exclusive:,New User Exclusive:,New User Exclusive:; _ga_TLYZYXJLJJ=GS2.1.s1779694688$o1$g1$t1779695130$j60$l0$h1780055590; GTM_pageviewCount=5; optimizelySession=1779695137521',
}

params = {
    'query': 'query GetCategories($id:String!$pageSize:Int!$currentPage:Int!$filters:ProductAttributeFilterInput!$sort:ProductAttributeSortInput){categories(filters:{category_uid:{in:[$id]}}){items{uid ...CategoryFragment __typename}__typename}products(pageSize:$pageSize currentPage:$currentPage filter:$filters sort:$sort){...ProductsFragment __typename}}fragment CategoryFragment on CategoryTree{uid meta_title meta_keywords meta_description id description name product_count banner_image banner_image_mobile image category_sub_heading_1 category_sub_heading_2 jibbitz jibbitz_widget black_letter golden_letter jibbitz_layout auth_required is_enable_featured_layout featured_layout_identifier_1 featured_layout_identifier_2 featured_layout_identifier_3 featured_layout_identifier_4 is_monsoon_theme_enabled category_block_tile __typename}fragment ProductsFragment on Products{items{id uid name crocs_primary_category is_jibbitable crocs_global_sku offer_text_background_color layer_color_text ndsl_color fit_text style_text gender_text price_range{minimum_price{discount{amount_off percent_off __typename}final_price{currency value __typename}regular_price{currency value __typename}__typename}__typename}sku small_image{url __typename}stock_status rating_summary __typename url_key url_suffix listing_title big_box product_labelstr offer_text offer_text_detail offer_text_secondary offer_text_detail_secondary color_variants_list{min_price max_price items{id url_key is_available is_current color_code more_plus __typename}__typename}}page_info{total_pages __typename}total_count __typename}',
    'operationName': 'GetCategories',
    'variables': '{"currentPage":1,"id":"MTE=","filters":{"category_uid":{"eq":"MTE="}},"pageSize":36,"sort":{"position":"ASC"}}',
}

response = requests.get('https://www.crocs.in/graphql', params=params, cookies=cookies, headers=headers)

def extract_raw_data(
    url,
    path,
    method="GET",
    headers=None,
    params=None,
    cookies=None,
    json_data=None,
):

    if method == "POST":
        response = requests.post(
            url=url,
            headers=headers,
            params=params,
            cookies=cookies,
            json=json_data,
            impersonate="chrome120"
        )

    else:
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

crocs_url = "https://www.crocs.in/graphql"

crocs_path = "data.products.items"

crocs_products = extract_raw_data(
    url=crocs_url,
    path=crocs_path,
    headers=headers,
    params=params,
    cookies=cookies
)

print("\nCROCS PRODUCTS:\n")

print(crocs_products)

with open(r"C:\python practice\3_websites\output\crocks_data.json","w",encoding='utf-8') as f:
    json.dump(crocs_products,f,indent=4)


instagram_url = "https://www.instagram.com/p/DYj6SF0B5PQ/"


instagram_path = """
require[0][3][0].__bbox.require[0][3][1].__bbox.result.data.xdt_api__v1__media__media_id__comments__connection.edges
"""

inst_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'dpr': '1.5',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="148.0.7778.179", "Google Chrome";v="148.0.7778.179", "Not/A)Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'viewport-width': '1280',
    # 'cookie': 'csrftoken=_skVwtAIM_pqdDldckMyXO; datr=kXMBarimLEVyVcdnFBd9MXqi; ig_did=D8F4B5BE-1720-4C6B-B6D8-0203B3E68BB8; ig_nrcb=1; mid=agFzkgALAAHNERCVR91KgjYGYP3J; dpr=1.5; ps_l=1; ps_n=1; wd=1280x231',
}

with open(
    r"C:\python practice\3_websites\instagram.json",
    "r",
    encoding="utf-8"
) as f:

    instagram_data = json.load(f)

instagram_comments = jmespath.search(
    instagram_path,
    instagram_data
)

print("\nINSTAGRAM COMMENTS:\n")

print("comments", instagram_comments)

with open(
    r"C:\python practice\3_websites\output\instagram_comments.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        instagram_comments,
        f,
        indent=4,
        ensure_ascii=False
    )


booking_url ="https://www.booking.com/searchresults.html?aid=304142&label=gen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4Ar_uz9AGwAIB0gIkYzZjZmM2ZWQtZTMzYS00M2NjLTg0MGMtMTVkNWI3MzBlZTVl2AIB4AIB&dest_id=-2098033&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&chal_t=1779696115997&force_referer" 


booking_headers = {
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'ect': '4g',
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
      # 'cookie': 'pcm_consent=analytical%3Dtrue%26countryCode%3DIN%26consentId%3Dbbe58835-545e-4107-a3ca-6974079ca61c%26consentedAt%3D2026-05-25T10%3A47%3A25.546Z%26expiresAt%3D2026-11-21T10%3A47%3A25.546Z%26implicit%3Dtrue%26marketing%3Dtrue%26regionCode%3DGJ%26regulation%3Dnone%26legacyRegulation%3Dnone; pcm_personalization_disabled=0; cors_js=1; BJS=-; bkng_sso_session=e30; bkng_sso_ses=e30; _gid=GA1.2.292533712.1779706052; _gcl_au=1.1.426499483.1779706052; bkng_prue=1; cgumid=8hAkYV9JYUJHanA2eDNKaUZCc0J5azQ1YnBab2Y3NWVWOWVLOFBNcFZNQ25YWkFKTzNoZ3FVOTRrekZhWDJwMVV1cHklMkY; _yjsu_yjad=1779706053.beb88df9-897b-494e-b406-f3cc230750f8; FPID=FPID2.2.4a1d4zlFmmnjntFzh0jJ6zp1Y8ofN2FmyGZqN7dSR6s%3D.1779706052; FPAU=1.1.426499483.1779706052; FPLC=aw8VG2N%2FGNbcmZqijU61Y46OwGCEapDwq1S0W2S5%2F%2BkIG8dwKAafNDPz6BMJIQ6H6VkpGQGJ%2BFIKz7l%2BY4aiJwlh6Q3qfqWDp8V5H5nX%2FCeg39%2B1OPcHaWUMXsmQfg%3D%3D; __gads=ID=b8e2728c4caa4b31:T=1779707922:RT=1779707922:S=ALNI_MYkbju_kDbz2QGaWXftSphZp67hhQ; __gpi=UID=0000142f63ebe81a:T=1779707923:RT=1779707923:S=ALNI_Maa5nlfHTDzVdwXJ70-ryrRQXHDNQ; __eoi=ID=ef9dcaa2f4fd82b9:T=1779707923:RT=1779707923:S=AA-AfjYJ1lra7i-JHy0Keax9n19r; g_state={"i_l":0,"i_ll":1779708660910,"i_b":"KaxuOqzyCT/wbCYNxpVCWliYRemulMh8uVc5TJkyppE","i_e":{"enable_itp_optimization":0},"i_et":1779706051932}; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1779706051228&isGpcEnabled=0&datestamp=Mon+May+25+2026+17%3A01%3A01+GMT%2B0530+(India+Standard+Time)&version=202501.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=8411802c-7cd3-4e8c-80ac-eabe70f60b3c&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _rdt_uuid=1779706052504.26d4573e-7e7f-4276-8813-30acc1fb9b38; _ga=GA1.1.1736742068.1779706052; _ga_A12345=GS2.1.s1779708662$o2$g1$t1779708662$j60$l0$h980288956; _uetsid=22843640582711f1809c4144a1908482; _uetvid=22859700582711f1924ac3df0ce1a48c; cto_bundle=hajO819ZRmpGOEhuUWF0TTZiOU83TmIySkpmNHpoJTJCVGtySiUyQmhoVXF1eDFwOEl1MmFUNHZkOTRpbzdNT2xxU1VJYXJ3TjFzQXNKYkoxSUt1TzJxTUl2WXc1UyUyQjhQSHRZTVZFclNPSWFZbGNxUHRHN3FOMHRrJTJCVlQzMXNYVkVlTmVOVTZKUlFhdFpjOU5TR015MFNxaDI5clNYZyUzRCUzRA; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbca8KLfxLPedzeLp7N3sVrmaAY%2B2meFrYzRtAlC8SjoaBvCOdmoTet1QyGJvrkUHr5eEfk3vCefGvgsW0uOIGWLid9H9livcLCNcfyeeUdAVgumJTFKsVdYweF1tY9CY%2FKM%2Bn5tZThvHqgYZ39E4CNGfyndP6hUoFUYvcFpTQjvU%3D; bkng_sso_auth=CAIQi4nT0gIaZtyfASR9cLbOTBQWRjKwVmyghEu5RG9oLfQ40WtwwpLnoKohHvrKEbXyWI4Pxx0+nfsBtDZObhpFW86u+/2HvSmyGuK4VINtft65O/TKSdGDRZNk+0U9ejK2TvNKBkLwmqPh9FOfSQ==; aws-waf-token=d09662ce-090e-463b-baf5-12926f36abba:BQoAmY9VgDQfAAAA:b2pqKMAW3a89Ab2PG0111lj3fOSi059oiIL7DkQCuU+B3LvjlpD8tHZnmaC5UVZ9dWMPvf/92mLVipqwgpKt5i8u0F9ZeyaNwSQ4a33NA+Vy82irgo7URxMayt6fcBLKZcBE55Yd11CinzzpiZVErn6Zzn7JK7jwz2Rq8vpYIog3omVHBNBzp/TeLdjes+GXr9eJK/99VLsh8snev3pUpg6MZL3bF2ZcZtbOl5Mz2VfjRjj45B/BfJu66B+SY2tjgYc=',
}
cookies = {
    'pcm_personalization_disabled': '0',
    'bkng_sso_auth': 'CAIQi4nT0gIaZjgUpj3A95ZXrlN9NzMLu7bh9BFW72098di984d9zkPV//v1dvRX6k5OW7E9gTwsYG0fmapWZFuzjfq1ZCao+cMzG6m3i9w8I3teFO5JOUMUqHNCQCjrN9WxAIlvupXWXWQG+G0N7Q==',
    'pcm_consent': 'analytical%3Dtrue%26countryCode%3DIN%26consentId%3Ddaf36391-d1f3-40ef-b8e5-52d0df9034b2%26consentedAt%3D2026-05-25T12%3A57%3A53.778Z%26expiresAt%3D2026-11-21T12%3A57%3A53.778Z%26implicit%3Dtrue%26marketing%3Dtrue%26regionCode%3DGJ%26regulation%3Dnone%26legacyRegulation%3Dnone',
    'cors_js': '1',
    'FPID': 'FPID2.2.VccFp88%2FkyBSP3Al9khoRy%2F%2BLVQKq5yIfskD5tKpYIQ%3D.1779713810',
    'FPLC': 'YsnBz2ua1fqfBZ%2FVtKn33%2BInhowMPOeH7HtoSeWQiE9XAQu9O%2F4Zotvw23h%2BRyYDse%2BeQenVPJlDNkF7JYhuzxmagI0ZbSsziEZ97DQNx9ebD%2FWYbtMcIs2KJMAa3A%3D%3D',
    'FPAU': '1.2.1013970163.1779713874',
    'BJS': '-',
    'bkng_sso_ses': 'e30',
    'bkng_sso_session': 'e30',
    'pcm_pac': '%5B%2262744ec37d5b3ffb6c8d3131767785a81a5a6dd82d85e816354fdd3800d60958%22%2C6%5D',
    '_gcl_au': '1.1.1043584388.1779713879',
    'bkng_prue': '1',
    'cgumid': 'lYwJG19JYUJHanA2eDNKaUZCc0J5azQ1YnBab2Y3NWVWOWVLOFBNcFZNQ25YWkFMZnRDM3dtMWwlMkZXVTBCZEI3bSUyRnhheg',
    '_gid': 'GA1.2.490373971.1779713879',
    '_yjsu_yjad': '1779713879.00aa9302-f137-4fb2-b150-157930b26922',
    '_gat': '1',
    'bk_nav_search': '%7B%22u%22%3A%22https%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Faid%3D304142%26label%3Dgen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4Ar_uz9AGwAIB0gIkYzZjZmM2ZWQtZTMzYS00M2NjLTg0MGMtMTVkNWI3MzBlZTVl2AIB4AIB%26dest_id%3D-2098033%26dest_type%3Dcity%26group_adults%3Dnull%26no_rooms%3Dnull%26group_children%3Dnull%22%2C%22t%22%3A1779713896335%2C%22p%22%3A%22searchResults%22%7D',
    'OptanonConsent': 'implicitConsentCountry=nonGDPR&implicitConsentDate=1779713878744&isGpcEnabled=0&datestamp=Mon+May+25+2026+18%3A28%3A16+GMT%2B0530+(India+Standard+Time)&version=202501.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=4992b00e-ffea-4f8d-9c54-8e9f1596d641&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Faid%3D304142%26label%3Dgen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4Ar_uz9AGwAIB0gIkYzZjZmM2ZWQtZTMzYS00M2NjLTg0MGMtMTVkNWI3MzBlZTVl2AIB4AIB%26dest_id%3D-2098033%26dest_type%3Dcity%26group_adults%3Dnull%26req_adults%3Dnull%26no_rooms%3Dnull%26group_children%3Dnull%26req_children%3Dnull%26chal_t%3D1779696115997%26force_referer&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1',
    'g_state': '{"i_l":0,"i_ll":1779713896712,"i_b":"+N1rToOJIQhr521Pr+VzxAmOUjbeHawxZuta0fzOEK8","i_e":{"enable_itp_optimization":0},"i_et":1779706051932}',
    '_ga': 'GA1.1.1245390343.1779713879',
    '_ga_A12345': 'GS2.1.s1779711829$o3$g1$t1779713896$j40$l0$h278008677',
    '_rdt_uuid': '1779713879405.67a5d9b9-99cd-4ce1-9d6d-4a13879e4477',
    'cto_bundle': 'VqyRtV9ObU1JVFQ2cHFUYm1hazBFQUZmMW5LTGZjeCUyRjVSQ09UR1NYdm45WGRMT3duWmJSUmdWTFRmZ3JmTXZiYnAlMkJHc3VQSFllQXJISExuSlI0NzB6cHdEV1Y4a09Ib1VZeUtSclN0U1IlMkJiQlduNnVUamZnd3RWamYxN1laVjlCaG9EamwyRUg5JTJGN0tvUGdrTUJ0RiUyQlJTTjlnJTNEJTNE',
    '_uetsid': '5b694560583911f18a3c5fb20fa0c494',
    '_uetvid': '5b69b320583911f18c0093728b129c72',
    'bkng': '11UmFuZG9tSVYkc2RlIyh9YSvtNSM2ADX0BnR0tqAEmjuzafumWkKSRuNEsQUJG5Ay4iV0edZSTsv8gU5wDWYuhDCmjhXfZjKTjyadLCZmunuFAq6H3bKubn6kKHWzhMLg25U7d4kzY9xwnVG40YzrtbHbJTH1%2BGUjmzNRSNXzJB2izen8fxF32VZbgxtL4l%2Fp140CuyXPwJK9nR6yXryK3g%3D%3D',
    'aws-waf-token': 'd09662ce-090e-463b-baf5-12926f36abba:BQoAfqdZwpsgAAAA:HLy3hAvQMQxUDnMlv1fbkQ5GNHZgo+4oWdyV7vEr/mslGrhir0bGeJZFqM1Pkd3ZtHgJ/65JLnFapikz4W6pyq+WnxECccR1nD0PAQTthRHrOud+uIPcd67xLNiKW0VNpLr5mJZln2VrL6hMv7xJWNf+KWTCdwTHRUU6fGbotytR75S/eypXV5+0Rseaiq6Tj6AsDORNapcN/0OjoLHwl0QXHldpJLBeWjkJBXUu5ErzeZrmMH/+h4HS5haYKeb+U8I=',
}

booking_path = "ROOT_QUERY.searchQueries.*.results"

with open(
    r"C:\python practice\3_websites\booking.json",
    "r",
    encoding="utf-8"
) as f:

    booking_data = json.load(f)

booking_hotels = jmespath.search(
    booking_path,
    booking_data
)

print("\nBOOKING HOTELS:\n")

print(booking_hotels)

with open(
    r"C:\python practice\3_websites\output\booking_hotels.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        booking_hotels,
        f,
        indent=4,
        ensure_ascii=False
    )