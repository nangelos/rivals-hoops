# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RivalsSpider(CrawlSpider):
    name = 'rivals'
    # allowed_domains = ['rivalshoops.com', 'n.rivals.com']
    # start_urls = [
    # 'https://n.rivals.com/prospect_rankings/rivals150/2019',
    # 'https://n.rivals.com/prospect_rankings/rivals150/2020',
    # 'https://n.rivals.com/prospect_rankings/rivals150/2021'
    # ]

    # rules = (
    #     Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
    #          callback="parse_item",
    #          follow=True),)


    def start_requests(self):
        urls = [
        'https://n.rivals.com/prospect_rankings/rivals150/2019'#,
        # 'https://n.rivals.com/prospect_rankings/rivals150/2020',
        # 'https://n.rivals.com/prospect_rankings/rivals150/2021'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        # filename = '%s.html' % page
        data = str(response.css('rv-prospect-ranking').getall())
        print('Data: ' + data)
        filename = '%s.txt' % page
        with open(filename, 'wb') as f:
            # f.write(response.body)
            f.write(data)
        self.log('Saved file %s' % filename)



    # def parse(self, response):
        # print('Processing..' + response)
