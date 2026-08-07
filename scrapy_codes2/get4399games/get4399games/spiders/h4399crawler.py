import scrapy
from scrapy import Selector
from get4399games.items import H4399GameItem


class H4399crawlerSpider(scrapy.Spider):
    name = "h4399crawler"
    allowed_domains = ["h.4399.com"]
    start_urls = ["https://h.4399.com"]

    def parse(self, response):
        sel = Selector(response)
        lis = sel.css("div.module.mod-list.mod-recommend > div.bd > ul > li")
        # print(lis)
        for li in lis:
            item = H4399GameItem()
            item['link'] = li.css('div.icon>a').attrib["href"][2:]
            item['title'] = li.css('div.icon>a').attrib["data-name"]
            item['imgsrc'] = "https:" + li.css('div.icon>a>img').attrib['src']   

            yield item
