# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass

import scrapy


@dataclass
class DbmvCrawlerItem:
    # define the fields for your item here like:
    # name: str | None = None
    pass

class MovieItem(scrapy.Item):
    link = scrapy.Field() #    电影详情页面的超链接
    title = scrapy.Field() #   电影标题
    rating = scrapy.Field() #  电影评分
    subject = scrapy.Field() # 电影主题
    