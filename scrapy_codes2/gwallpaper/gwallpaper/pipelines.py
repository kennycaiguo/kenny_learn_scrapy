# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import pymysql
from gwallpaper.settings import MYSQL

class GwallpaperPipeline:
    def process_item(self, item):
        return item

class GwallpaperMysqlPipeline:
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
        sql= "insert into girlspic(name,pic_src,local_path) values(%s,%s,%s)"
        self.cursor.execute(sql,(item['name'],item['pic_src'],item['local_path']))
        self.conn.commit()        
        return item

    def close_spider(self,spider): #关闭数据库连接
        print(f"{spider.name} stop...")
        if self.conn:
            self.conn.close()


class GwallpaperImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info): # 下载图片
        return scrapy.Request(item['pic_src'])
    
    def file_path(self, request, response = None, info = None, *, item = None): # 处理图片保存路径
        file_name = request.url.split("/")[-1]
        return f"images/{file_name}"

    def item_completed(self, results, item, info):  # 完成后的通知
        # return super().item_completed(results, item, info)
        ok,info = results[0]
        item['local_path'] = info['path']
        print(results)
        
        return item