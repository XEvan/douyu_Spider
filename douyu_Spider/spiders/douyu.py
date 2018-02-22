import scrapy
from douyu_Spider.items import DouyuSpiderItem
import json

class Douyu(scrapy.Spider):
    name = "douyu"
    start_urls = ["https://apiv2.douyucdn.cn/gv2api/rkc/roomlist/2_270/0/20/android?client_sys=android"]

    def parse(self, response):
        content = json.loads(response.text)
	if content["error"] == 0:
	        data = content["data"]["list"]
	        for each in data:
			item = DouyuSpiderItem()
			roomLabel = []
			item["nickName"] = each["nickname"]
			item["roomID"] = each["room_id"]
			item["hotNumber"] = each["hn"]
			item["roomName"] = each["room_name"]
			item["roomPic"] = each["vertical_src"]
			labels = each["anchor_label"]
			for label in labels:
				roomLabel.append(label["tag"])
			item["roomLabel"] = ','.join(roomLabel)
			yield item
		for index in range(20, 1000, 20):
			url = "https://apiv2.douyucdn.cn/gv2api/rkc/roomlist/2_270/%s/20/android?client_sys=android"%str(index)
			yield scrapy.Request(url)
	else:
		print "No more information"	
