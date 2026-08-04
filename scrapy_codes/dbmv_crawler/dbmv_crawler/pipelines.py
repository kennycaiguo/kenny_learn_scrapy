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