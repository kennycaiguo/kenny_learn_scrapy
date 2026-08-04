from scrapy import Selector
import scrapy

from dbmv_crawler.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        sel = Selector(response)
        lis = sel.css('#content > div > div.article > ol > li')

        for li in lis:
            # 每一个电影都需要创建一个MovieItem对象
            movieitem = MovieItem()
            movieitem['link']   = li.css("div.info>div.hd > a").attrib['href'] + '\t'
            movieitem['title']  = li.css("div.info > div.hd > a > span:nth-child(1)::text").extract_first() + '\t'
            movieitem['rating'] = li.css('div.info > div.bd > div > span.rating_num::text').extract_first() + '\t'
            movieitem['subject']= li.css('div.info > div.bd > p.quote > span::text').extract_first()

            yield movieitem
