from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

import os

prods = {}

class JDSpider(BaseSpider):
    name = "jd_spider"
    start_urls = []
    for i in range(1,3):
        start_urls.append(r"http://list.jd.com/list.html?cat=9987%2C653%2C655&page="+str(i)+r"&JL=6_0_0")

    def parse(self, response):
        hxs = HtmlXPathSelector(text=response.body)
        print dir(hxs)
        xs = hxs.select('//div[@id=\"plist\"]/ul/li')
        for x in xs:
            sku = x.select('@sku').extract()[0]
            if not sku in prods.keys():
                prods[sku]={}
            print ("sku = "+ sku).encode('utf8')

            url = x.select('div[@class=\"lh-wrap\"]/div[\"p-img\"]/a/@href').extract()[0]
            prods[sku]['url'] = url
            print ("url:" + url).encode('utf8')
            
            introduction = x.select('div[@class=\"lh-wrap\"]/div[\"p-img\"]/a/img/@alt').extract()[0]
            prods[sku]['introduction'] = introduction
            print ("introduction:" + introduction).encode('utf8')

            imgurl = x.select('div[@class=\"lh-wrap\"]/div[\"p-img\"]/a/img/@data-lazyload').extract()[0]
            prods[sku]['main_imgurl'] = imgurl
