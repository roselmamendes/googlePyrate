from scrapy import project, signals
from scrapy.conf import settings
from scrapy.crawler import CrawlerProcess
from scrapy.xlib.pydispatch import dispatcher
from multiprocessing.queues import Queue
from scrapy.spider import BaseSpider
from scrapy.crawler import Crawler
from google_pyrate.google_pyrate import GoogleSpider
import multiprocessing

class GoogleCrawler(multiprocessing.Process):
    def __init__(self, spider, result_queue):
        multiprocessing.Process.__init__(self)
        self.result_queue = result_queue

        self.crawler = CrawlerProcess(settings)
        if not hasattr(project, 'crawler'):
            self.crawler.install()
        self.crawler.configure()

        self.items = []
        self.spider = spider
        dispatcher.connect(self._item_passed, signals.item_passed)

    def _item_passed(self, item):
        self.items.append(item)
 
    def run(self):
        self.crawler.crawl(self.spider)
        self.crawler.start()
        self.crawler.stop()
        self.result_queue.put(self.items)
                                    
def search(self, for_search):
    results = []
    spider = GoogleSpider(for_search)
        
    results = self.build_results_from_html(r.text)
    result_queue = Queue()
    crawler = GoogleCrawler(spider, result_queue)
    crawler.start()
    
    return result_queue.get()
