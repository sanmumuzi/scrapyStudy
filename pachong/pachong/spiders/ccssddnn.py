import scrapy
from pachong.items import CsdnItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Mycsdn(CrawlSpider):
    name = "csdn"
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        "http://blog.csdn.net/u012150179/article/details/11749017"
    ]

    rules = [
        Rule(LinkExtractor(allow=("article/details"),), callback='parse_item', follow=True),  # 巨坑
    ]

    def parse_item(self, response):
        item = CsdnItem()
        blog_name1 = response.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()
        # 不能直接取第一个元素，很容易出现标题为空的情况
        blog_url1 = str(response.url)
        temp = ''.join([n for n in blog_name1])

        item["blog_url1"] = blog_url1
        item["blog_name1"] = temp.strip()
        # 迭代每个列表中的元素，然后进行拼接，再除去空格
        yield item