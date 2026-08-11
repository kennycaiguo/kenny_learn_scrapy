import scrapy
from gwallpaper.items import GwallpaperItem

class MzbzSpider(scrapy.Spider):
    name = "mzbz"
    allowed_domains = ["nevseoboi.com.ua"]
    start_urls = ["https://nevseoboi.com.ua/en/sexy-girls/31262-sexy-girls-97-30-wallpapers.html"]

    def parse(self, resp,**kwargs):
           imgs = resp.xpath("/html/body/div[1]/div[1]/div/article/div[2]/a/img")
           # print(imgs)
           for img in imgs:
               src = img.xpath("./@data-src").extract_first()
               yield scrapy.Request(
                   url=src,method='get',callback=self.parse_link
               )
              
   
    def parse_link(self, resp,**kwargs): # 这是scrapy中callback函数的签名，一定是这样的格式,注意，这里的resp和parse里面的resp不是同一个页面
           print(resp,type(resp))
           print(resp.url)
           item = GwallpaperItem()
           item['pic_src'] =resp.url
           item['name'] = resp.url.split("/")[-1]
   
           yield item
   