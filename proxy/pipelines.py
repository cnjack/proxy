# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib2
from scrapy.exceptions import DropItem

class ProxyPipeline(object):
    def process_item(self, item, spider):
        try:
            proxy_handler = urllib2.ProxyHandler({item['scheme']: item['proxy']})
            opener = urllib2.build_opener(proxy_handler)
            r = opener.open('http://nightc.com:9010/')
            body = r.read()
        except:
            body = ""
        if body != "":
            return item
        else:
            raise DropItem("Missing price in %s" % item)
