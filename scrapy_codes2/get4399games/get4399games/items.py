# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass

import scrapy


@dataclass
class Get4399GamesItem:
    # define the fields for your item here like:
    # name: str | None = None
    pass

class H4399GameItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    imgsrc = scrapy.Field()