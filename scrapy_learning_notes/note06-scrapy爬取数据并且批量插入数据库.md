# 还是dbmv_crawler项目，我们来实现批量保存数据到数据库

## 1.为了方便操作，我创建了一个tb_top_movies2数据表，用来测试程序运行是否正确

![image-20260805143601508](./note06-scrapy爬取数据并且批量插入数据库.assets/image-20260805143601508.png)

## 2.打开pipelines.py,我们新建一个MovieDbBatchPipeline，可以复制MovieDbPipeline的代码然后进行适当修改

![image-20260805143642605](./note06-scrapy爬取数据并且批量插入数据库.assets/image-20260805143642605.png)

## 3.然后我们进入settings.py,配置MovieDbBatchPipeline并且注释调MovieDbPipeline的配置

![image-20260805143945804](./note06-scrapy爬取数据并且批量插入数据库.assets/image-20260805143945804.png)

## 4.运行程序，结果正确

![image-20260805154553088](./note06-scrapy爬取数据并且批量插入数据库.assets/image-20260805154553088.png)

## 注意，有时候你的ip会被网站封锁，此时需要使用代理，使用代理需要先设置好你的代理服务器，然后需要在构造请求对象的时候提交一个‘proxy’参数

![image-20260805200835658](./note06-scrapy爬取数据并且批量插入数据库.assets/image-20260805200835658.png)