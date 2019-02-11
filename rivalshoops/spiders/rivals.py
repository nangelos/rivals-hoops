# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RivalsSpider(CrawlSpider):
    name = 'rivals'
    allowed_domains = ['rivalshoops.com', 'n.rivals.com']
    # allowed_domains = ['www.rivalshoops.com']
    start_urls = [
    'https://n.rivals.com/prospect_rankings/rivals150/2019',
    # 'https://n.rivals.com/prospect_rankings/rivals150/2020',
    # 'https://n.rivals.com/prospect_rankings/rivals150/2021'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response)

    # def parse(self, response):
    #     pass
