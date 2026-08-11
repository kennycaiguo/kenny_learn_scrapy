# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass

import scrapy

class GwallpaperItem(scrapy.Item):
    # define the fields for your item here like:
    # name: str | None = None
    name = scrapy.Field()
    pic_src = scrapy.Field()
    local_path = scrapy.Field()
