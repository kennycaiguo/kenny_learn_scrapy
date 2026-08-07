# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass

import scrapy


# @dataclass
# class SsqItem:
#     # define the fields for your item here like:
#     # name: str | None = None
#     pass

class SsqItem(scrapy.Item):
   series_num = scrapy.Field() #期号
   red_balls  = scrapy.Field() #红色球
   blue_ball  = scrapy.Field() #蓝色球
