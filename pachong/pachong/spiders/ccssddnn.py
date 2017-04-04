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
        blog_url1 = str(response.url)

        item["blog_url1"] = blog_url1
        item["blog_name1"] = [n for n in blog_name1]

        yield item