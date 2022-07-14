# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class MoveItem(scrapy.Item):
    #电影名字
    move_name=scrapy.Field()
    #电影短评
    move_inq= scrapy.Field()
class Doubantop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影序号（排名）
    number = scrapy.Field()
    # 电影名字
    name = scrapy.Field()
    # 电影又名
    name_two = scrapy.Field()
    # 电影评分
    score = scrapy.Field()
    # 评论人数
    comment = scrapy.Field()
    # 电影封面（链接）
    image_urls = scrapy.Field()
    # 电影导演
    director = scrapy.Field()
    # 电影编剧
    scenarist = scrapy.Field()
    # 电影主演
    lead = scrapy.Field()
    # 电影上映时间
    time = scrapy.Field()
    # 电影地区
    place = scrapy.Field()
    # 电影分类
    classify = scrapy.Field()
    #电影主要类型
    maintypes=scrapy.Field()
    # 电影语言
    language = scrapy.Field()
    # 电影片长
    length = scrapy.Field()
    # 电影简介
    synopsis = scrapy.Field()
    # 短评链接
    inq_url = scrapy.Field()

