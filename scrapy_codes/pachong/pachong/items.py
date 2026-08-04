# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass
import scrapy

class MovieItem(scrapy.Item):
     link = scrapy.Field()
     title = scrapy.Field()
     rating = scrapy.Field()
     subject = scrapy.Field()
     
