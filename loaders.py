from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, Compose
#MapCompose是处理列表内每个元素
class NewsLoader(ItemLoader):
    default_output_processor = Compose(Join(','), lambda s: s.strip(' \n'))