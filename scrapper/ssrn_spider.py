import scrapy

class SSRNSpider(scrapy.Spider):
    name = 'ssrn_spider'
    start_urls = ['https://www.ssrn.com/en/']

    def parse(self, response):
        for paper in response.css('div.abstract'):
            title = paper.css('a::text').get()
            abstract = paper.css('p::text').get()
            yield {
                'title': title,
                'abstract': abstract
            }
