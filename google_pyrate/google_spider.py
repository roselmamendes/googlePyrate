from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from google_pyrate.google_pyrate import ResultItem
URL = 'http://www.google.com/search'

class GoogleSpider(BaseSpider):
    name = 'google_scraper'
    allowed_domains = ['google.com']

    def __init__(self, for_search):
        self.for_search = for_search
    
    def start_requests(self):
        return Request(url=URL,meta={'q': self.for_search})

    def parse(self, response):
        hxs = Selector(response)

        li_tags = hxs.css("li.g")

        results = []
        for li_tag in li_tags:
            a_tag = li_tag.css("h3.r > a:first-child")
            
            title = a_tag[0].extract()
            href = self.formata_url(a_tag[0].select("href").extract()
            result = ResultItem(title, href)
            
            results.append(result)
                                    
        return response.status,results
