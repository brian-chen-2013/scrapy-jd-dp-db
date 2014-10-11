# -*- coding: utf-8 -*-

import scrapy

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

class DpSpiderSpider(scrapy.spider.Spider):
    name = "dp_spider"
    allowed_domains = ["dianping.com"]

    #只抓取前3个url以做演示，如果需要抓取更多，可以用yield创建更多得Request。
    start_urls = []
    for i in range(1,3):
        start_urls.append('http://www.dianping.com/search/category/1/10/o10p'+str(i))

    #需要处理的http状态
    handle_httpstatus_list = [404,403]

    def parse(self, response):
        print '\n'
        print 'crawl url = ', response.url
        #403错误，禁止抓取，则暂停10分钟
        if response.status == 403:
            print 'meet 403, sleep 600 seconds'
            import time
            time.sleep(600)
            yield Request(response.url, callback=self.parse)
        #404，页面不存在，直接返回即可
        elif response.status == 404:
            print 'meet 404, return'
        #正常处理
        else:
            hxs = scrapy.Selector(response)
            xs = hxs.xpath('//ul[@class=\"shop-list J_shop-list\"]/li')
            for x in xs:
                shopid = x.xpath('a/@href').extract()[0].split('/')[-1]
                print 'shopid = ', shopid
                shopname = x.xpath('a/img/@title').extract()[0]
                print "shopname = ", shopname
