# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass
import scrapy


@dataclass
class Get4399FlashItem:
    # define the fields for your item here like:
    # name: str | None = None
    pass


class Flash4399Item(scrapy.Item):
    link = scrapy.Field()     # 游戏的链接
    title = scrapy.Field()    # 游戏名称
    type = scrapy.Field()     # 游戏分类
    date = scrapy.Field()     # 游戏发布时间
