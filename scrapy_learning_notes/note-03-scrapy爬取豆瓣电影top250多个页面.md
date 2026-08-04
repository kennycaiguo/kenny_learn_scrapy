# 1.先复习一下上一节课的内容

## 1.把上一课的pachong项目移动到G:\my_projects_2026\kenny_learn_scrapy\scrapy_codes里面，然后我们使用下面的命令创建一个dbmv_crawler项目

```
PS G:\my_projects_2026\kenny_learn_scrapy\scrapy_codes> scrapy startproject dbmv_crawler
```



## 2.然后我们进入dbmv_crawlerw文件夹里面，用下面的命令创建一个蜘蛛程序

```
PS G:\my_projects_2026\kenny_learn_scrapy\scrapy_codes\dbmv_crawler> scrapy genspider douban movie.douban.com
```



## 3.然后我们进入douban.py里面，先修改一下url

![image-20260803184854370](./note-03-scrapy爬取豆瓣电影top250多个页面.assets/image-20260803184854370.png)

## 4.然后我们需要打开Items.py,在里面创建一个MovieItem类，继承自scrapy.Item

![image-20260803185345950](./note-03-scrapy爬取豆瓣电影top250多个页面.assets/image-20260803185345950.png)

## 5.然后我们回到douban.py文件，继续编写parse方法

![image-20260803192733043](./note-03-scrapy爬取豆瓣电影top250多个页面.assets/image-20260803192733043.png)

## 6.然后我们需要打开settings.py,把请求头的USER-AGENT设置为浏览器，并且可以配置下载延迟的秒数

![image-20260803192252388](./note-03-scrapy爬取豆瓣电影top250多个页面.assets/image-20260803192252388.png)

## 7.然后我们使用scrapy crawl douban -o dbmv.csv启动爬虫并且把数据保持到dbmv.csv文件中

```
scrapy crawl douban -o dbmv.csv
```

## 8.然后就拿到一页数据了

![image-20260803194714782](./note-03-scrapy爬取豆瓣电影top250多个页面.assets/image-20260803194714782.png)

# 2.这一节课我们来学习爬取多页内容

## 1》想爬取多页内容，你必须知道每一页的开始值是多少，我们分析url，发现它其实有一个start参数

