# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proxy.items import ProxyItem


class Spider(CrawlSpider):
    name = 'xicidaili'
    allowed_domains = ['www.xicidaili.com']
    start_urls = [
        'http://www.xicidaili.com/nn/1'
    ]
    rules = (
        Rule(LinkExtractor(allow=(r'http://www.xicidaili.com/nn/[0-9]',)),callback='parse'),
    )

    def parse(self, response):
        trs = response.xpath("//table[@id='ip_list']/tr[@class='odd']")
        ips = trs.xpath('//td[2]/text()').extract()
        ports = trs.xpath('//td[3]/text()').extract()
        schemes = trs.xpath('//td[6]/text()').extract()
        for key in range(0, len(ips)):
            item = ProxyItem()
            item['scheme'] = str(schemes[key]).strip().lower()
            item['host'] = str(ips[key]).strip()
            item['port'] = str(ports[key]).strip()
            item['proxy'] =  item['scheme'] + "://" + item['host'] + ":" + item['port']
            yield item
