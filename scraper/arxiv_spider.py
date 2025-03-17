import scrapy

class ArxivSpider(scrapy.Spider):
    name = 'arxiv_spider'
    start_urls = ['https://arxiv.org/list/cs.AI/recent']

    def parse(self, response):
        for paper in response.css('div.list-title'):
            title = paper.css('div.title a::text').get()
            abstract = paper.css('div.abstract span::text').get()
            yield {
                'title': title,
                'abstract': abstract
            }

