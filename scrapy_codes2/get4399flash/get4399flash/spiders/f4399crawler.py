import scrapy
from scrapy import Selector

from get4399flash.items import Flash4399Item



class F4399crawlerSpider(scrapy.Spider):
    name = "f4399crawler"
    allowed_domains = ["4399.com"]
    start_urls = ["http://www.4399.com/flash/"]

    def parse(self, response):
        #方式1，使用css来获取元素
        # sel = Selector(response)
        # lis = sel.css('#skinbody > div:nth-child(8) > ul > li')
        # for li in lis:
        #     item = Flash4399Item()
        #     item['link'] = "http://www.4399.com"+li.css("a").attrib['href']
        #     item['title'] ="\t"+ li.css('a>img').attrib['alt']
        #     item['type']  ="\t"+ li.css('em:nth-child(2)>a::text').extract_first()
        #     item['date']  ="\t"+ li.css('em:nth-child(3)::text').extract_first()

        #     yield item  
        # 方式2，使用xpath来获取元素
        lis = response.xpath("//ul[@class='n-game cf']/li")
        for li in lis:
            item = Flash4399Item()
            item['link'] ="http://www.4399.com"+ li.xpath("./a/@href").extract_first()
            item['title'] ="\t" + li.xpath('./a/img/@alt').extract_first()
            item['type']  ="\t"+ li.xpath('./em[1]/a/text()').extract_first()
            item['date']  ="\t"+ li.xpath('./em[2]/text()').extract_first()

            yield item
