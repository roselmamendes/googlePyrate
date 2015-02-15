class GoogleResults(object):

    def crawl(self, spiderName):
        print('test')
        
    def buildGoogleResults(self, toSearch):
        #call spider
        #url http://doc.scrapy.org/en/0.24/intro/tutorial.html
        #xpath //*[@id="scrapy-tutorial"]/h1
        #return '<h1>Scrapy Tutorial<a class="headerlink" href="#scrapy-tutorial" title="Permalink to this headline">¶</a></h1>'
        self.crawl('googleSpider')
        return  '<h1>Scrapy Tutorial<a class="headerlink" href="#scrapy-tutorial" title="Permalink to this headline">¶</a></h1>'