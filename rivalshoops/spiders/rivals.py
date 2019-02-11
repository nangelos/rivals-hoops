# -*- coding: utf-8 -*-
import scrapy


class RivalsSpider(scrapy.Spider):
    name = 'rivals'
    allowed_domains = ['rivalshoops.com']
    start_urls = ['http://rivalshoops.com/']

    def parse(self, response):
        pass
