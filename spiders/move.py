# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import MoveItem
from scrapy.spiders import Request
class MoveSpider(scrapy.Spider):
    name = 'move'
    allowed_domains = ['movie.douban.com']
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES' : {
        'DouBanTop250.pipelines.Doubantop250Pipeline': 300,
    }
    }
    def start_requests(self):
        with open('DouBanTop250/top250.json', 'r', encoding='utf-8') as f:
            for i in json.loads(f.read()):
                move_name = i['name']
                if len(move_name.split(' ')) > 1: move_name = move_name.split(' ')[0]
                yield Request(meta={'name':move_name},url=i['inq_url'],callback=self.parse)
    def parse(self, response):
        next_url=str(response.xpath('//*[@id="paginator"]/a[@class="next"]/@href').extract_first()).split('&percent_type=')[0]
        reviews = MoveItem()
        reviews['move_inq']=response.xpath('//*[@id="comments"]/div[@class="comment-item"]/div/p/span/text()').extract()
        move_name=response.meta['name']
        reviews['move_name']=str(move_name)
        yield reviews
        if next_url=='None':
            pass
        else:
            if float(next_url.split('&limit=20')[0].split('?start=')[-1])<201:
                yield Request(url=response.urljoin(next_url),callback=self.parse,dont_filter=True,meta={'name':move_name})