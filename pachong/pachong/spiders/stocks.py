# -*- coding: utf-8 -*-
import scrapy
import re

class StocksSpider(scrapy.Spider):
    name = "stocks"
    allowed_domains = ["baidu.com"]
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for href in  response.xpath('//*[@id="quotesearch"]/ul/li/a').extract():
            try:
                stock = re.findall(r"[s][hz]\d{6}", href)[0]
                url = "https://gupiao.baidu.com/stock/{}.html".format(stock)
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue

    def parse_stock(self, response):
        infoDict = {}
        stockInfo = response.xpath('//*[@class="stock-bets"]')
        stock_name = stockInfo.xpath('./h1/a[@class="bets-name"]/text()').extract()[0]
        keylist = stockInfo.xpath('.//dt/text()').extract()
        valuelist = stockInfo.xpath('.//dd/text()').extract()
        # print("------------------------------------------------")
        # print(stockInfo)
        # print(type(keylist))
        # print(type(valuelist))
        # print(stock_name)
        # print(keylist)
        # print(valuelist)
        # print(len(keylist))
        # name = re.findall(r'^\s.*\s\($', stock_name)
        # stock_name = stock_name.replace(" ", "")
        # stock_name = stock_name.replace("(", "")
        name = stock_name.strip().strip("(")   # 将名字中的 空格及不知道哪出现的左括号去掉
        # print(name)
        # print(name)
        # print(len(stock_name))
        # print(stock_name[0])
        # print(stock_name[1])
        for i in range(len(keylist)):
            key = keylist[i]
            try:
                val = valuelist[i].strip()    # 排除网页中问题，只有跌停元素的值有很多空格
            except:
                val = "--"
            infoDict[key] = val
        infoDict.update({"股票名称": name})
        yield infoDict


