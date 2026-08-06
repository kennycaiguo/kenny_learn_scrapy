# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
import pymysql

from dbmv_crawler.items import MovieItem


class DbmvCrawlerPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title="豆瓣电影Top250"
        self.sheet.append(('详情路径','名称', '评分', '名言'))

    def process_item(self, item:MovieItem,spider):
        self.sheet.append((item['link'],item['title'],item['rating'],item['subject']))
        return item

    def close_spider(self,spider):
        self.wb.save("db_movie_top250.xlsx")

class MovieDbPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",port=3306,user='root',passwd='root',database='dbmovies',charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()



    def process_item(self,item:MovieItem,spider):
        link = item.get('link','')
        title = item.get('title','')
        rating = item.get('rating',0)
        subject = item.get('subject','')
        self.cursor.execute("insert into tb_top_movies(link,title,rating,subject) values(%s,%s,%s,%s)",(link,title,rating,subject))
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()

class MovieDbBatchPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",port=3306,user='root',passwd='root',database='dbmovies',charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()
        self.data = [] #先把数据添加到这个列表，然后在关闭爬虫的时候一次把这个列表里面的数据插入数据库


    def process_item(self,item:MovieItem,spider):
        link = item.get('link','')
        title = item.get('title','')
        rating = item.get('rating',0)
        subject = item.get('subject','')
        self.data.append((link,title,rating,subject))
        if len(self.data) > 100: # 每100条数据做一次提交
            self.save_to_db() # 把列表的数据提交到数据库后，需要清空列表的内容防止重复添加数据
        return item

    def save_to_db(self):
        self.cursor.executemany("insert into tb_top_movies2(link,title,rating,subject) values(%s,%s,%s,%s)",self.data)
        self.conn.commit()
        self.data.clear()

    def close_spider(self,spider):
        # 在关闭爬虫之前一定要检查还有没有数据没有提交，如果有，需要提交到数据库
        if len(self.data)>0:
            self.save_to_db()
        self.conn.close()