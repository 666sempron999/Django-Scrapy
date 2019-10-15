import scrapy
from example_bot.items import ExampleDotComItem

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.example.com']
    start_urls = ['http://www.example.com/']

    def parse(self, response):
            title = response.xpath('//title/text()').extract()[0]
            description = response.xpath('//body/div/p/text()').extract()[0]
            # return ExampleDotComItem(title=title, description=description)
            # ExampleDotComItem[]
            # return ExampleDotComItem(title=title, description=description)
            item = ExampleDotComItem()
            # print("!!!!!!!!!!!!!!!!!!!!!!!!1")
            # print(dir(item))
            # print("!!!!!!!!!!!!!!!!!!!!!!!!1")
            item['title'] = title
            item['description'] = description
            # print("!!!!!!!!!!!!!!!!!!!!!!!!1")
            # print(title)
            # print(description)
            # print("!!!!!!!!!!!!!!!!!!!!!!!!1")
            yield item
