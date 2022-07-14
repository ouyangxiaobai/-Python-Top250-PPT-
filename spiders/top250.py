# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import *
from ..loaders import *
from scrapy.loader.processors import *
class Top250Spider(CrawlSpider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow='subject\/\d*\/', restrict_xpaths='//div[@class="info"]//div'), callback='top250_parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//span[@class="next"]//a[contains(.,"后页>")]')),  # 翻页功能
    )

    def top250_parse_item(self, response):
        loader = NewsLoader(item=Doubantop250Item(), response=response)
        loader.add_xpath('name', './/*[@id="content"]/h1/span[@property="v:itemreviewed"]/text()', TakeFirst())  # 电影名字
        loader.add_xpath('image_urls', './/*[@id="mainpic"]/a/img/@src',TakeFirst())  # 电影封面（链接）
        loader.add_xpath('number', './/*[@id="content"]/div[1]/span[@class="top250-no"]/text()')  # 电影排名
        loader.add_xpath('score', './/*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')  # 电影评分
        loader.add_xpath('comment', './/*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')  # 评论人数
        loader.add_xpath('director', './/*[@id="info"]/span[1]/span[2]/a[@rel="v:directedBy"]/text()')  # 电影导演
        loader.add_xpath('scenarist', './/*[@id="info"]/span[2]/span[2]/a/text()')  # 电影编剧
        #如果scrapy没有重写add_xpath方法，可以试着把下面这个命令注释去掉
        # loader.add_value('scenarist','Null') #如果loader没有数据会报错，所以当add_xpath获取不到数据时，就会有add_value添加Null字段，防止报错
        loader.add_xpath('lead', './/*[@id="info"]/span[@class="actor"]//a/text()')  # 电影主演
        # loader.add_value('lead','Null')
        loader.add_xpath('classify', './/*[@id="info"]/span[@property="v:genre"]/text()')  # 电影类型
        movetypes= response.xpath('//*[@id="interest_sectl"]/div[2]/a/text()').extract()
        movetypes.sort()
        move_maintypes=movetypes[-1].split('% ')[-1].strip('片')
        loader.add_value('maintypes',move_maintypes)#主要类型，为了之后分析
        onelist = ['place', 'language', 'name_two']
        twolist = ["制片国家/地区:", "语言:", "又名:"]
        for x, y in zip(onelist, twolist):
            loader.add_xpath(x, './/*[@id="info"]/span[contains(text(),"' + y + '")]/following-sibling::text()',
                             TakeFirst())
        # loader.add_value('name_two','Null')
        loader.add_xpath('time', './/*[@id="info"]/span[@property="v:initialReleaseDate"]/text()')  # 上映时间
        loader.add_xpath('length', './/*[@id="info"]/span[@property="v:runtime"]/text()')  # 电影片长
        loader.add_xpath('synopsis', './/*[@id="link-report"]//span[@property="v:summary"]',
                         re='(?<=\u3000\u3000).*?(?=\n)')  # 电影简介
        loader.add_xpath('inq_url','.//*[@id="comments-section"]//h2/span[@class="pl"]/a/@href',TakeFirst())
        yield loader.load_item()
