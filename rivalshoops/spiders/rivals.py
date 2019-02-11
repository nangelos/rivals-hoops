# -*- coding: utf-8 -*-
import scrapy


class RivalsSpider(scrapy.Spider):
    name = 'rivals'
    allowed_domains = ['rivalshoops.com', 'https://n.rivals.com']
    start_urls = ['http://rivalshoops.com/',
    'https://n.rivals.com/prospect_rankings/rivals150/2019',
    'https://n.rivals.com/prospect_rankings/rivals150/2020',
    'https://n.rivals.com/prospect_rankings/rivals150/2021']

        rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)

    # def parse(self, response):
    #     pass
