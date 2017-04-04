# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class PachongPipeline(object):
#     def process_item(self, item, spider):
#         return item

class StocksSpiderPipeline(object):
    def open_spider(self, spider):
        self.f = open("BaiduStockInfo.txt", "w")

    def process_item(self, item, spider):
        try:
            # print("**************************************")
            # print(type(item))
            # print("item = ", item)
            if item is not None:
                line = str(dict(item)) + "\n"
                self.f.write(line)
            # print("line:", line)
            # print("---------------------------------------")
        except:
            pass
        return item

    def close_spider(self, spider):
        self.f.close()


from pachong import settings
# from pachong.items import BiliIndexItem        # 为什么显示没用到这条语句
from pymongo import MongoClient

host = settings.MONGODB_HOST
port = settings.MONGODB_PORT
dbname = settings.MONGODB_DBNAME
collection = settings.MONGODB_COLLECTION

class BiliIndexPipeline(object):
    def __init__(self):
        client = MongoClient(host=host, port=port)
        db = client[dbname]
        self.collenction = db[collection]

    def process_item(self, item, spider):
        # for data in item:
        #     self.collenction.insert(dict(data))
        self.collenction.insert(dict(item))
        return item
















