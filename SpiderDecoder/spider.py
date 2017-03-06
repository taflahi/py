# -*- coding: utf-8 -*-
import scrapy

class PrestaSpider(scrapy.Spider):
    name = "Presta"  # Name of the Spider, required value
    start_urls = ["http://localhost:8000/taxons/novels"]  # The starting url, Scrapy will request this URL in parse

    # Entry point for the spider
    def parse(self, response):
        for href in response.css('.sylius-product-name').xpath('@href'):
            url = "http://localhost:8000" + href.extract()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_item)

        nextlink = response.css('.item.next').xpath('@href').extract()
        if(len(nextlink) > 0):
            # print("http://localhost:8000" + nextlink[0])
            yield scrapy.Request("http://localhost:8000" + nextlink[0], callback=self.parse)
        

    # Method for parsing a product page
    def parse_item(self, response):
        yield {
            'Code': response.css('.sub::text').extract()[0],
            'Author': response.css('.sylius-product-attribute-value::text').extract()[0].strip(),
            'Name': response.css('#sylius-product-name::text').extract()[0],
            'Price': response.css('#product-price::text').extract()[0].strip(),
            'Image': response.css('#main-image').xpath('@src').extract()[0],
            'Url': response.url
        }