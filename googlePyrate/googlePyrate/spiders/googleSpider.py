import scrapy

class GoogleSpider(scrapy.Spider):
    
    name = 'googlePyrate''

    allowed_domains = ['doc.scrapy.org/']
    
    start_urls = ['http://doc.scrapy.org/en/0.24/intro/tutorial.html']
    
    def parse(self, response):
        return response.xpath('//*[@id="scrapy-tutorial"]/h1')
    