import scrapy
# import re
from pachong.items import BiliIndexItem
import json

class BiliIndex(scrapy.Spider):
    name = "anime"
    allowed_domains = []

    def start_requests(self):
        for num in range(1,141):
            yield scrapy.Request(
                "http://bangumi.bilibili.com/web_api/season/index_global?page={}&page_size=20&version=0&is_finish=0&start_year=0&tag_id=&index_type=1&index_sort=0&quarter=0".format(
                    num))                       # 可以不写callback 默认

    def parse(self, response):
        # for x in re.findall('season\_id\"\:\"([\d]{1,6})\"', response.text):
        #     href = "http://bangumi.bilibili.com/anime/" + x
        #     # print(href)
        #     yield scrapy.Request(href, callback=self.parse2)
        data = json.loads(response.text)      # 从文本中直接获取，将json格式直接转换成dict
        # print(type(response.text))
        # print(type(data))
        # print(data)
        for temp in data['result']['list']:              # 从dict中获取url
            url = temp["url"]
            yield scrapy.Request(url=url, callback=self.parse2)

    def parse2(self, response):
        item = BiliIndexItem()
        base_xpath = response.xpath('//div[@class="bangumi-info-r"]')
        info_title = base_xpath.xpath("//h1/text()").extract()[0]        # 将列表变成了字符串
        info_style_item = base_xpath.xpath(
            './/span[@class="info-style-item"]/text()').extract()      # 获取的是列表
        info_count_item_play = base_xpath.xpath(
            './/span[@class="info-count-item info-count-item-play"]/em/text()').extract()[0]
        info_count_item_fans = base_xpath.xpath(
            './/span[@class="info-count-item info-count-item-fans"]/em/text()').extract()[0]
        info_count_item_review = base_xpath.xpath(
            './/span[@class="info-count-item info-count-item-review"]/em/text()').extract()[0]
        info_update = base_xpath.xpath(
            './/div[@class="info-row info-update"]/em/span/text()').extract()
        info_cv = base_xpath.xpath(
            './/div[@class="info-row info-cv"]/em/span/text()').extract()
        info_desc_wrp = base_xpath.xpath(
            './/div[@class="info-row info-desc-wrp"]/div[@class="info-desc"]/text()').extract()

        item['info_title'] = info_title
        item['info_style_item'] = info_style_item
        item['info_count_item_play'] = info_count_item_play
        item['info_count_item_fans'] = info_count_item_fans
        item['info_count_item_review'] = info_count_item_review
        item['info_update'] = info_update
        item['info_cv'] = info_cv
        item['info_desc_wrp'] = info_desc_wrp
        yield item
