# 1.scrapy的安装

![image-20260806125857056](./note002.scrapy的初步使用.assets/image-20260806125857056.png)

![image-20260806130202448](./note002.scrapy的初步使用.assets/image-20260806130202448.png)

# 2.scrapy的使用，这里我们来爬取4399小游戏的数据

## 1.创建项目： scrapy startproject get4399games （注意：项目名称不能以数字开头）

![image-20260806131119374](./note002.scrapy的初步使用.assets/image-20260806131119374.png)

## 注意，外层的get4399games是项目文件夹，里面的get4399games是项目的根目录，导自己的模块需要以里面的get4399games为参照

## 2.进入get4399games里面

![image-20260806131159006](./note002.scrapy的初步使用.assets/image-20260806131159006.png)

## 3.创建一个蜘蛛程序，用来解析页面，使用命令scrapy genspider h4399crawler h.4399.com

![image-20260806135516583](./note002.scrapy的初步使用.assets/image-20260806135516583.png)

![image-20260806140836271](./note002.scrapy的初步使用.assets/image-20260806140836271.png)

## 4.我们需要先在items.py里面编写一个 H4399GameItem类继承自scrapy.Item,然后创建我们感兴趣的字段

![image-20260806143547058](./note002.scrapy的初步使用.assets/image-20260806143547058.png)



## 5.然后我们来编写蜘蛛程序里面的parse方法，需要先在网站上面点击右键-》检查，然后用工具来定位元素，然后用css来找到这个元素，注意我们需要导入上面的类

![image-20260806143654076](./note002.scrapy的初步使用.assets/image-20260806143654076.png)

## 6.然后我们来运行爬虫，使用命令scrapy crawl h4399crawler -o h4399data.csv

![image-20260806143851566](./note002.scrapy的初步使用.assets/image-20260806143851566.png)

## 7.如果我们的代码编写完全正确，我们就可以得到数据

![image-20260806143939532](./note002.scrapy的初步使用.assets/image-20260806143939532.png)

# 3.然后我们再创建一个项目get4399flash，我们爬取这个页面：http://www.4399.com/flash/

 ## 1》scrapy startproject  get4399flash

![image-20260806145046335](./note002.scrapy的初步使用.assets/image-20260806145046335.png)

## 2》在终端中定位到get4399flash这个文件夹

![image-20260806145207657](./note002.scrapy的初步使用.assets/image-20260806145207657.png)

## 3》创建一个蜘蛛程序scrapy genspider f4399crawler 4399.com，然后我们需要进入蜘蛛程序里面把开始url改为： http://www.4399.com/flash/

![image-20260806150420684](./note002.scrapy的初步使用.assets/image-20260806150420684.png)

## 4>打开items.py，在里面新建一个Flash4399Item类继承scrapy.Item,注意，这个网站的图片是用懒加载或者使用js动态生成图片的方式来渲染的，scrapy爬取不到他的src，所以我们只爬取游戏的网址，游戏名称、游戏的分类和游戏发布的时间

![image-20260806161738073](./note002.scrapy的初步使用.assets/image-20260806161738073.png)

## 5》然后我们进入蜘蛛程序，编写parse函数的代码如下

![image-20260806161855098](./note002.scrapy的初步使用.assets/image-20260806161855098.png)

## 6》使用命令scrapy crawl f4399crawler -o f4399data.csv运行项目，然后就可以拿到数据

![image-20260806162100950](./note002.scrapy的初步使用.assets/image-20260806162100950.png)

## 上面是使用css来获取数据，我们还可以使用xpath来获取数据，只需要修改一下parse方法

```
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

```



### 使用命令：scrapy crawl f4399crawler -o f4399data2.csv运行程序，发现可以拿到数据了

![image-20260806171041884](./note002.scrapy的初步使用.assets/image-20260806171041884.png)

## 注意，默认scrapy项目的管道pipeline是没有开启的，如果你需要存储数据，你可以在settings.py里面开启管道

![image-20260806175201884](./note002.scrapy的初步使用.assets/image-20260806175201884.png)

# scrapy项目的使用流程

![image-20260807114514723](./note002.scrapy的初步使用.assets/image-20260807114514723.png)

![image-20260807114853545](./note002.scrapy的初步使用.assets/image-20260807114853545.png)

![image-20260807115114396](./note002.scrapy的初步使用.assets/image-20260807115114396.png)