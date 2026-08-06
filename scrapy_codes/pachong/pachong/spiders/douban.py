import scrapy
from scrapy import Selector
from pachong.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        sel = Selector(response)
        lis =  sel.css('#content > div > div.article > ol > li')
        for li in lis:
            movie_item = MovieItem()
            movie_item['link']    = li.css('div.info > div.hd > a').attrib['href']+'\t'
            movie_item['title']   = li.css('div.info > div.hd > a > span:nth-child(1)::text').extract_first()+'\t'
            movie_item['rating']  = li.css('div.info > div.bd > div > span.rating_num::text').extract_first()+'\t'
            movie_item['subject'] = li.css("div.info > div.bd > p.quote > span::text").extract_first()
            
            yield movie_item
           