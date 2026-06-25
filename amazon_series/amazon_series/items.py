# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonSeriesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    series_id=scrapy.Field()
    title=scrapy.Field()
    synopsis=scrapy.Field()
    genres=scrapy.Field()
    audio_languages=scrapy.Field()
    subtitles=scrapy.Field()
    release_year=scrapy.Field()
    imdb_rating=scrapy.Field()
    ranking=scrapy.Field()
