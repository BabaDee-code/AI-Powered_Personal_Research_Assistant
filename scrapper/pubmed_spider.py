import scrapy

class PubMedSpider(scrapy.Spider):
    name = 'pubmed_spider'
    start_urls = ['https://pubmed.ncbi.nlm.nih.gov/']

    def parse(self, response):
        for paper in response.css('div.results-list'):
            title = paper.css('a.result-title::text').get()
            abstract = paper.css('div.abstract-text::text').get()
            yield {
                'title': title,
                'abstract': abstract
            }
