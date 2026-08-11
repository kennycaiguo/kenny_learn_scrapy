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