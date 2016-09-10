# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from ezreal.items import Poem

class PoemsSpider(CrawlSpider):
    name = "poems"
    allowed_domains = ["tw.18dao.net"]
    start_urls = (
        'http://tw.18dao.net/%E5%94%90%E8%A9%A9%E5%AE%8B%E8%A9%9E/%E5%94%90%E6%9C%9D%E4%BD%9C%E8%80%85%E5%88%97%E8%A1%A8',
    )

    rules = (
            Rule(LinkExtractor(allow=('/%E5%94%90%E8%A9%A9%E5%AE%8B%E8%A9%9E.*?')), callback='parse_links', follow=False),
    )

   # def parse(self, response):
    #    print(response)

    #def parse_start_url(self, response):
    #    list(self.parser_links(response))

    def parse_links(self, response):
        sel = scrapy.Selector(response)
        for link in sel.xpath('//*[@id="mw-content-text"]/ol/li/a/@href').extract():
            yield Request('http://tw.18dao.net' + link, callback=self.parse_poems)

    def parse_poems(self, response):
        sel = scrapy.Selector(response)
        item = Poem()
        item['title'] = sel.xpath('//*[@id="mw-content-text"]/p[1]').extract()[0].strip()
        item['author'] = sel.xpath('//*[@id="mw-content-text"]/p[2]').extract()[0].strip()
        item['dynasty'] = sel.xpath('//*[@id="mw-content-text"]/p[3]').extract()[0].strip()
        item['content'] = sel.xpath('//*[@id="mw-content-text"]/p[4]').extract()[0].strip()
        return item
