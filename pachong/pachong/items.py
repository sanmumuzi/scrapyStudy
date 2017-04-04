# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PachongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CsdnItem(scrapy.Item):
    blog_name1 = scrapy.Field()
    blog_url1 = scrapy.Field()


class BiliIndexItem(scrapy.Item):
    info_title = scrapy.Field()
    info_style_item = scrapy.Field()
    info_count_item_play = scrapy.Field()
    info_count_item_fans = scrapy.Field()
    info_count_item_review = scrapy.Field()
    info_update = scrapy.Field()
    info_cv = scrapy.Field()
    info_desc_wrp = scrapy.Field()




