# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    roomID = scrapy.Field()
    nickName = scrapy.Field()
    hotNumber = scrapy.Field()
    roomName = scrapy.Field()
    roomLabel = scrapy.Field()
    roomPic = scrapy.Field()
    roomStatus = scrapy.Field()
