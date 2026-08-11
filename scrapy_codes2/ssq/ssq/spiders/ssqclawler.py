import scrapy
from ssq.items import SsqItem


class SsqclawlerSpider(scrapy.Spider):
    name = "ssqclawler"
    allowed_domains = ["500.com"]
    start_urls = ["https://datachart.500.com/ssq/"]

    def parse(self, response):
        trs = response.xpath("//tbody[@id='tdata']/tr")
        for tr in trs:
            item = SsqItem()
            if tr.xpath("./@class").extract_first() == 'tdbck': # 一定要使用extract_first()提取文本才能够比较
                continue # 过滤调横线分隔符
            # red_balls = tr.xpath("./td[@class='chartBall01']/text()").extract() //ok
            # scrapy支持xpath和css混用
            item['red_balls'] =tr.css(".chartBall01::text").extract()  # 红色球
            item['blue_ball'] ="\t" + tr.css(".chartBall02::text").extract_first() # 蓝色球
            # item['series_num'] ="\t" + tr.css("td:nth-child(1)::text").extract_first().strip()   # 期号 ok,用strip()函数去除空格
            item['series_num'] = tr.xpath("./td[1]/text()").extract_first().strip()+"\t"    # 期号 ok,用strip()函数去除空格
            

            yield item