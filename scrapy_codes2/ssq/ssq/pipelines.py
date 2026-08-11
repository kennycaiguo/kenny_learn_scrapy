# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from ssq.settings import MYSQL
from pymongo import MongoClient

class SsqPipeline:
    def open_spider(self,spider): # 打开文件句柄并且保存起来
        print(f"{spider.name} start...")
        self.f = open("./ssq.csv",'a',encoding='utf-8')
        self.f.write("series_num,red_balls,blue_ball\n")

    def process_item(self, item): # 把数据写入文件
        # print(item)
        # 保存到csv文件中
        self.f.write(f"{item['series_num']},{'_'.join(item['red_balls'])},{item['blue_ball']}\n")     
        return item

    def close_spider(self,spider): #关闭文件句柄
        print(f"{spider.name} stop...")
        if self.f:
            self.f.close()

class SsqMysqlPipeline:
    def open_spider(self,spider): # 打开数据库连接
       print("start ")
       self.conn = pymysql.connect(
           host=MYSQL['host']
           ,port=MYSQL['port']
           ,user=MYSQL['user']
           ,passwd=MYSQL['pwd']
           ,database=MYSQL['db']
       )
       self.cursor = self.conn.cursor() # 创建游标，方便下面的数据操作

      

    def process_item(self, item): # 把数据写入数据库
        # print(item)
        sql= "insert into ssq_res(serial_num,red_balls,blue_ball) values(%s,%s,%s)"
        self.cursor.execute(sql,(item['series_num'],'_'.join(item['red_balls']),item['blue_ball']))
        self.conn.commit()        
        return item

    def close_spider(self,spider): #关闭数据库连接
        print(f"{spider.name} stop...")
        if self.conn:
            self.conn.close()

class SsqMongoPipeline:
    def open_spider(self,spider): # 打开数据库连接
       print("start ")
       self.client = MongoClient("mongodb://localhost:27017/")
       self.db = self.client['ssq']
       self.collection = self.db['ssq_res']

      

    def process_item(self, item): # 把数据写入数据库
        # print(item)
        self.collection.insert_one({"serial_num":item['series_num'],"red_balls":'_'.join(item['red_balls']),"blue_ball":item['blue_ball']})       
        return item

    def close_spider(self,spider): #关闭数据库连接
        print(f"{spider.name} stop...")
        if self.client:
            self.client.close()

        