# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class DouyuSpiderPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host="localhost", db='douyuInfo',user='root',passwd='evan',charset='utf8')
	self.cur = self.conn.cursor()

    def process_item(self, item, spider):
	roomID = str(item["roomID"])
	nickName = item["nickName"]
	hotNumber = str(item["hotNumber"])
	roomName = item["roomName"]
	roomLabel = item["roomLabel"]
	roomPic = item["roomPic"]

	sql = 'insert into douyu(roomID, nickName, hotNumber, roomName, roomLabel, roomPic) values("'+roomID+'", "'+nickName+'", "'+hotNumber+'", "'+roomName+'", "'+roomLabel+'", "'+roomPic+'");'
	#sql = 'insert into douyu(roomID, nickName, hotNumber, roomName, roomLabel) values("'+roomID+'", "'+nickName+'", "'+hotNumber+'", "'+roomName+'", "'+roomLabel+'");'
	self.cur.execute(sql)
	self.conn.commit()

        return item
    def close_spider(self, spider):
	self.conn.close()
