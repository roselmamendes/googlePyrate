class GoogleResults(object):

    def crawl(self, spiderName, toSearch):
        pass

    def buildGoogleResults(self, toSearch):
        #url http://doc.scrapy.org/en/0.24/intro/tutorial.html
        #xpath //*[@id="scrapy-tutorial"]/h1
        #return '<h1>Scrapy Tutorial<a class="headerlink" href="#scrapy-tutorial" title="Permalink to this headline">¶</a></h1>'
        self.crawl('googleSpider', toSearch)
        return  '<a href="/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=0CCcQFjAA&amp;url=https%3A%2F%2Fpypi.python.org%2Fpypi%2Fmock&amp;ei=NZzgVPvxEMXbsATpqYAY&amp;usg=AFQjCNGurnzZ47GvhKvsnHFDpGYrmDVLNg&amp;sig2=4yN6bvJBpHIMd1tXGODjMA" onmousedown="return rwt(this,\'\',\'\',\'\',\'1\',\'AFQjCNGurnzZ47GvhKvsnHFDpGYrmDVLNg\',\'4yN6bvJBpHIMd1tXGODjMA\',\'0CCcQFjAA\',\'\',\'\',event)" data-href="https://pypi.python.org/pypi/mock">mock 1.0.1 : Python Package Index</a>'