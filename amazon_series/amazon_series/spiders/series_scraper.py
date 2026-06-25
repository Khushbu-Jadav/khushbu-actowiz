import scrapy
import hashlib
import gzip
import os
import json
import jmespath
from rich import print
from ..items import AmazonSeriesItem


class SeriesScraperSpider(scrapy.Spider):
    name = "series_scraper"
    allowed_domains = ["primevideo.com"]
    start_urls = ["https://www.primevideo.com/region/eu/detail/0TPA7F48GEJVGD8KKM1NC6QQ9Q"]

    series_data=[]
    def parse(self, response):
        folder = rf"C:\websites_pages\amazon_series"
        os.makedirs(folder, exist_ok=True)

        file_hash=hashlib.sha256(response.url.encode("utf-8")).hexdigest()
        with gzip.open(rf"C:\websites_pages\amazon_series\{file_hash}.html.gz","wb") as f:
            f.write(response.body)

        with open(rf"C:\python_training\amazon_series\amazon_spider_noir.json","r",encoding='utf-8') as f:
            data=json.load(f)

        
        print(data)

        pageTitleId=jmespath.search("init.preparations.body.atf.state.pageTitleId",data)
        # print("pagetitleid",pageTitleId)

        title = jmespath.search(f'init.preparations.body.atf.state.detail.headerDetail."{pageTitleId}".parentTitle',data)
        synopsis = jmespath.search(f'init.preparations.body.atf.state.detail.headerDetail."{pageTitleId}".synopsis',data)
        genres = jmespath.search(f'init.preparations.body.atf.state.detail.headerDetail."{pageTitleId}".genres[*].text',data)
        audio_languages=jmespath.search(f'init.preparations.body.atf.state.detail.headerDetail."{pageTitleId}".audioTracks[*]',data)
        subtitles=jmespath.search(f'init.preparations.body.atf.state.detail.headerDetail."{pageTitleId}".subtitles[*]',data)
        release_year=jmespath.search(f'init.preparations.body.atf.state.detail.headerDetail."{pageTitleId}".releaseYear',data)
        imdb_rating=jmespath.search(f'init.preparations.body.atf.state.imdb."{pageTitleId}".score',data)
        ranking=jmespath.search(f'init.preparations.body.atf.state.action.atf."{pageTitleId}".messages.highValueMessage.dvMessage.string',data)

        item=AmazonSeriesItem()

        item["series_id"]=pageTitleId
        item["title"]=title
        item["synopsis"]=synopsis
        item["genres"]=genres
        item["audio_languages"]=audio_languages
        item["subtitles"]=subtitles
        item["release_year"]=release_year
        item["imdb_rating"]=imdb_rating
        item["ranking"]=ranking
       
        self.series_data.append(dict(item))

        yield item
        print(item)
        # header_detail = jmespath.search("preparations.body.atf.state.detail.headerDetail", data)
        # print(header_detail)
        # gti_key = list(header_detail.keys())[0]
        # print("gti_key:",gti_key)
        # title = header_detail[gti_key].get("parentTitle") or header_detail[gti_key].get("title")
        # print("title:",title)

        with open("series_data.json","w",encoding="utf-8") as f:
            json.dump(self.series_data,f,indent=4,ensure_ascii=False)
