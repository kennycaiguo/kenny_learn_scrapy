# 我们先来做一个抓取双色球数据的项目

## 1.创建项目，使用命令： scrapy startproject ssq

![image-20260807121541860](./note03-scrapy管道.assets/image-20260807121541860.png)

## 2.进入ssq项目，然后用下面的命令创建蜘蛛程序：scrapy genspider ssqclawler 500.com

![image-20260807121919468](./note03-scrapy管道.assets/image-20260807121919468.png)

## 3.我们需要修改start_url

![image-20260807122400583](./note03-scrapy管道.assets/image-20260807122400583.png)

## 4.我们需要在settings.py设置一下请求头的User-Agent参数

![image-20260807122833403](./note03-scrapy管道.assets/image-20260807122833403.png)

## 5.下面我们来爬取每一行的获奖号码，并且封装数据生成给管道

![image-20260807141242445](./note03-scrapy管道.assets/image-20260807141242445.png)

## 6.打开settings.py,把管道配置的内容取消注释，也就是启用管道功能

![image-20260807141542026](./note03-scrapy管道.assets/image-20260807141542026.png)

## 7.打开pipelines.py,我们编写配置管道的处理代码，我们先添加一个打印语句看看能否拿到数据

![image-20260807142142545](./note03-scrapy管道.assets/image-20260807142142545.png)

## 运行程序，是可以拿到数据的

![image-20260807142317889](./note03-scrapy管道.assets/image-20260807142317889.png)

## 我们可以使用这个命令把数据保持到一个csv文件里面：scrapy crawl ssqclawler -o ssqdata.csv

![image-20260807142549906](./note03-scrapy管道.assets/image-20260807142549906.png)

## 注意： 在parse方法中，yield 后面可以跟Request对象，Item对象，None或者字典对象，但是不能够跟列表或元组，会报错，还有，其实直接使用字典也是不推荐的。我们需要创建自己的Item类，继承自scrapy.Item.

## 9.我们打开items.py,发现scrapy已经帮我们生成一个类：SsqItem

![image-20260807152118069](./note03-scrapy管道.assets/image-20260807152118069.png)

## 10.我们需要对他进行改造，把那个注解删除，并且要继承自scrapy.Item,然后我们就在里面定义我们需要的字段

![image-20260807152549657](./note03-scrapy管道.assets/image-20260807152549657.png)

## 11.然后我们需要进入蜘蛛程序，把parse方法改造一下

![image-20260807154001520](./note03-scrapy管道.assets/image-20260807154001520.png)

## 12.再次运行项目，发现也是可以拿到数据的

![image-20260807154116599](./note03-scrapy管道.assets/image-20260807154116599.png)

## 另外，我们可以在settings.py里面配置日志级别，过滤一些我们不需要的日志输出

![image-20260807154624657](./note03-scrapy管道.assets/image-20260807154624657.png)

## 13.然后我们利用管道把数据存储到一个csv文件中（其实是可以不写的，直接使用scrapy crawl ssqclawler -o ssqdata2.csv即可，但是是excel文件的话需要写）

![image-20260810155616818](./note03-scrapy管道.assets/image-20260810155616818.png)

### 运行程序，是可以拿到数据的

![image-20260810155855165](./note03-scrapy管道.assets/image-20260810155855165.png)

## 14.不过，这样子效率不高，我们可以把代码优化一下，我们需要创建一个open_spider方法，在里面打开文件句柄并且掌握属性添加到self，然后在process_item方法里面不断写入数据，然后创建一个close_spider方法，在里面关闭我们的文件句柄

![image-20260810162632261](./note03-scrapy管道.assets/image-20260810162632261.png)

### 运行程序，也是可以拿到数据的

## 15.我们可以不写另外一个pipeline，把手机写入MySQL数据库，我们在pipelines.py里面创建一个新类SsqMysqlPipeline，先写一些骨架代码

![image-20260810170404210](./note03-scrapy管道.assets/image-20260810170404210.png)

## 16.然后我们需要在settings.py里面启用这个管线

![image-20260810170556589](./note03-scrapy管道.assets/image-20260810170556589.png)

## 17.然后我们需要在数据库里面创建一个ssq数据库，然后创建一个ssq_res表格

![image-20260810171524733](./note03-scrapy管道.assets/image-20260810171524733.png)

## 18.回到pipelines.py,我们来完成保存数据到mysql的代码

![image-20260810174916984](./note03-scrapy管道.assets/image-20260810174916984.png)

### 运行程序，发现拿到数据了

![image-20260810175013676](./note03-scrapy管道.assets/image-20260810175013676.png)

## 19.上面的代码可以优化，我们把mysql数据库的信息添加到settings.py里面，这样子才比较合理

![image-20260810183321876](./note03-scrapy管道.assets/image-20260810183321876.png)

## 20.然后我们需要在pipelines.py里面当然这个设置，然后用它的key的值来填充connet函数

![image-20260810183453917](./note03-scrapy管道.assets/image-20260810183453917.png)

### 运行程序，也是可以拿到数据的

![image-20260810183525800](./note03-scrapy管道.assets/image-20260810183525800.png)

## 21.然后我们来学习把它保存到MongoDB，前提是先安装MongoDB数据库，然后安装MongoDB的python驱动： pip install pymongo，我以及安装好了

![image-20260810183636920](./note03-scrapy管道.assets/image-20260810183636920.png)

![image-20260810183708127](./note03-scrapy管道.assets/image-20260810183708127.png)

### 需要注意：scrapy需要mongodb8.0以上的版本，如果低于它，会报错

### 21.1 在pipelines.py里面新建一个类：SsqMongoPipeline，

![image-20260810184214890](./note03-scrapy管道.assets/image-20260810184214890.png)

### 然后我们在settings.py里面配置这个管线

![image-20260810184255389](./note03-scrapy管道.assets/image-20260810184255389.png)

### 21.2 然后我们来编写保存数据到MongoDB的代码

![image-20260810194207443](./note03-scrapy管道.assets/image-20260810194207443.png)

### 运行程序，拿到数据了

![image-20260810194301312](./note03-scrapy管道.assets/image-20260810194301312.png)

# 下面我们来使用文件来保存爬虫数据，我们需要爬取图片之家的美女桌面壁纸图片

## 1.回到双色球项目的上一级目录，输入scrapy startproject meinvbiz，创建一个美女壁纸项目

![image-20260811103754708](./note03-scrapy管道.assets/image-20260811103754708.png)

![image-20260811103733672](./note03-scrapy管道.assets/image-20260811103733672.png)



## 2.进入meinvbiz项目，输入scrapy genspider mnbz tupianzj.com，创建一个蜘蛛程序

![image-20260811104731616](./note03-scrapy管道.assets/image-20260811104731616.png)

## 3.然后我们需要修改一下start_urls,

![image-20260811105106026](./note03-scrapy管道.assets/image-20260811105106026.png)

### 然后在settings.py里面设置一下UA

![image-20260811105237754](./note03-scrapy管道.assets/image-20260811105237754.png)

## 4.我们的任务是抓取美女图片的高清大图，我们需要先在items.py里面完成我们MeinvbizItem类的编写

![image-20260811130844138](./note03-scrapy管道.assets/image-20260811130844138.png)

## 5.在parse方法里面，需要先获取a标签的herf属性然后发送请求获取图片，我们需要进行url拼接，注意使用scrapy里面的拼接方法比较方便，然后获得到的新url需要使用自己的callback函数来解析，注意创建好的请求对象需要用yield返回

![image-20260811114737084](./note03-scrapy管道.assets/image-20260811114737084.png)

## 5.创建parse_link方法，在这里解析新url，需要导入我们的MeinvbizItem

![image-20260811120820905](./note03-scrapy管道.assets/image-20260811120820905.png)



## 6.然后我们打开pipelines.py，在这里添加保存文件的代码。我们先不使用原来的管线，我们新建一个管线MeinvbizPicPipeline，注意这个类需要去下载图片，我们可以让他继承scrapy的管线模块提供的一个类ImagesPipeline，需要实现3个方法

![image-20260811123050818](./note03-scrapy管道.assets/image-20260811123050818.png)

## 7.然后我们需要在settings.py里面配置一下这个管线

![image-20260811123227217](./note03-scrapy管道.assets/image-20260811123227217.png)



## 8.此时你运行程序，你会发现，根本没有图片，有没有创建文件夹，因为我们需要设置一个文件夹来保存图片，我们进入settings.py,添加一个设置IMAGES_STORE

![image-20260811123739795](./note03-scrapy管道.assets/image-20260811123739795.png)



# 这个网站的数据下载不了，可能是网站反爬了

# 我们来爬取另外一个网站

https://nevseoboi.com.ua/en/sexy-girls/31262-sexy-girls-97-30-wallpapers.html

## 1.回到工作区文件夹，输入scrapy startproject gwallpaper创建一个gwallpaper项目

![image-20260811134126821](./note03-scrapy管道.assets/image-20260811134126821.png)



## 2.进入gwallpaper项目文件夹，输入命令：scrapy genspider mzbz nevseoboi.com.ua创建一个蜘蛛程序

![image-20260811134340005](./note03-scrapy管道.assets/image-20260811134340005.png)

## 3.修改一下他的start_urls

![image-20260811134427394](./note03-scrapy管道.assets/image-20260811134427394.png)

## 4.打开items.py,添加下面的代码

![image-20260811134612412](./note03-scrapy管道.assets/image-20260811134612412.png)

## 5.编写我们的蜘蛛程序里面的parse方法和自定义的回调parse_link方法

![image-20260811134810775](./note03-scrapy管道.assets/image-20260811134810775.png)

## 6.进入pipelines.py,创建一个新的管线，继承自scrapy.pipelines.images 包里面的ImagesPipeline类，需要实现他的3个方法

![image-20260811135155036](./note03-scrapy管道.assets/image-20260811135155036.png)

## 7.然后我们需要到settings.py 里面配置我们的管线和配置一个文件夹来保存文件

![image-20260811140019897](./note03-scrapy管道.assets/image-20260811140019897.png)



## 8.还要在settings.py里面配置UA

![image-20260811140132603](./note03-scrapy管道.assets/image-20260811140132603.png)

## 运行程序，可以拿到数据了

![image-20260811140948090](./note03-scrapy管道.assets/image-20260811140948090.png)

### 需要注意，scrapy下载图片功能依赖pillow库，如果你没有安装，就会报错

![image-20260811141058820](./note03-scrapy管道.assets/image-20260811141058820.png)

#### 此时只需要执行 ：pip install pillow即可

### 在pipelines中，那个return可以改为yield，而且在你需要批量下载的时候，只能用yield

# 现在，我们来做一个扩展，把我们爬取的图片的url和别的存储路径保存到mysql数据库中

## 1.需要在mysql中创建一个gwallpaper数据库，在里面创建一个girlspic数据表

![image-20260811145210297](./note03-scrapy管道.assets/image-20260811145210297.png)

## 2.在pipelines.py里面创建一个基于mysql的管线，其实是从双色球项目粘贴来的需要修改

![image-20260811150351746](./note03-scrapy管道.assets/image-20260811150351746.png)

## 3.然后我们在settings.py里面配置这个管线



## 4.然后我们需要在settings.py里面配置MySQL的连接参数

![image-20260811145855491](./note03-scrapy管道.assets/image-20260811145855491.png)

## 5.回到pipelines.py,导入mysql连接配置对象

![image-20260811150427480](./note03-scrapy管道.assets/image-20260811150427480.png)



## 6.我们发现我们的管线配置有问题，我们修改一下

![image-20260811153433396](./note03-scrapy管道.assets/image-20260811153433396.png)

## 7.为了能够顺利保存数据，我们需要在GwallpaperImagePipeline里面的item_completed函数里面封装一下item，注意需要把item返回，否则后面拿不到数据

![image-20260811152900192](./note03-scrapy管道.assets/image-20260811152900192.png)

## 8.我们需要修改一下items的代码，添加一个local_path字段

![image-20260811151448520](./note03-scrapy管道.assets/image-20260811151448520.png)

## 9.然后我们修改一下GwallpaperMysqlPipeline管线的代码

![image-20260811153340937](./note03-scrapy管道.assets/image-20260811153340937.png)

### 运行程序，发现数据拿到了

![image-20260811153646596](./note03-scrapy管道.assets/image-20260811153646596.png)

## 一定要注意管线执行的先后顺序，弄错了程序工作不正常

### 这个网站是一个简单网站，只有一页，如果有多页，可以参考note1文件夹里面的笔记

如果网站有下一页，可以在parse方法里面添加姓名的代码，注意此时仍然使用parse方法来解析

![image-20260811155905386](./note03-scrapy管道.assets/image-20260811155905386.png)

前提是这些页面的处理逻辑是一样的。
