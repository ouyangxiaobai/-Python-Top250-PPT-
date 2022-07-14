# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import json
import os
from scrapy.pipelines.images import ImagesPipeline
class Doubantop250Pipeline(object):
    def __init__(self):
        if not os.path.exists('DouBanTop250/top250.json'):
            self.ranking = open('DouBanTop250/top250.json', 'wb+')
            self.ranking.write('[\n'.encode('utf-8'))
    def process_item(self, item, spider):
        if spider.name=='top250':
            # '''下面这段是写入txt。
            move_name = item['name']
            if len(move_name.split(' ')) > 1: move_name = move_name.split(' ')[0]
            with open(r'DouBanTop250/Result/' + move_name + '/' + move_name + '.txt', 'a', encoding='utf-8') as f:
                r_list = ['电影排名', '电影名字', '电影又名', '电影评分', '评论人数', '导演', '编剧', '主演', '上映时间', '地区', '分类','主要类型', '语言', '片长', '简介',
                          '短评链接']
                s_list = ['number', 'name', 'name_two', 'score', 'comment', 'director', 'scenarist', 'lead', 'time',
                          'place', 'classify','maintypes', 'language', 'length', 'synopsis', 'inq_url']
                for i in range(len(r_list)):
                    f.write(r_list[i] + ':' + str(item[s_list[i]]) + '\n')
                f.write('\n')
            # '''
            text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
            self.ranking.write(text.encode('utf-8'))
            return item
        else:
            with open('DouBanTop250/Result/'+item['move_name']+'/'+item['move_name']+'影评.txt','a+', encoding='utf-8') as f:
                for i in item['move_inq']:
                    f.write(i+'\n')
            f.close()
            return item


    def close_spider(self, spider):
        if spider.name == 'top250':
            self.ranking.seek(-2, 1)
            self.ranking.write('\n]'.encode('utf-8'))
            self.ranking.close()


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['image_urls'], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        '''图片保存的路径'''
        item = request.meta['item']
        img_name = item["name"]
        if len(img_name.split(' ')) > 1:
            img_name =img_name.split(' ')[0]
        path = '/' + img_name + '/' + img_name + '.jpg'
        return path

    '''图片下载后返回下结果，观察是否成功。'''

    def item_completed(self, results, item, info):
        return item