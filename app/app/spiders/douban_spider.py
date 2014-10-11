# -*- coding: utf-8 -*-

import scrapy

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

class DoubanSpiderSpider(scrapy.spider.Spider):
    name = "douban_spider"
    allowed_domains = ["douban.com"]
    start_urls = ['http://www.douban.com/people/dengcaiyun/']
    handle_httpstatus_list = [404,403]
    #最多抓取30个豆瓣用户的关注信息，只抓取每个用户主页上列出的8个用户。
    max_user = 30
    user_num = 0

    def parse(self, response):
        print '\n'
        print 'crawl url = ', response.url
        if response.status == 403:
            print 'meet 403, sleep 600 seconds'
            import time
            time.sleep(600)
            yield Request(response.url, callback=self.parse)
        elif response.status == 404:
            print 'meet 404, return'
        else:
            hxs = scrapy.Selector(response)
            xs = hxs.xpath('//div[@id=\"friend\"]/dl')
            for x in xs:
                print "\n"
                new_url = x.xpath('dd/a/@href').extract()[0]
                user_id = new_url.split('/')[-2]
                print 'user_id = ', user_id
                self.user_num += 1
                if self.user_num < self.max_user:
                    yield Request(new_url, callback=self.parse)
