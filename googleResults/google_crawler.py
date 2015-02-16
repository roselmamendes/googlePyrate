from urllib.request import urlopen


class GoogleCrawler(object):

    def __init__(self, url):
        self.url = url

    def getresponse(self):
        return urlopen(self.url)

    def crawl(self, forsearch):
        pass

    def buildgoogleresults(self, tosearch):
        forsearch = tosearch.replace(' ', '+')
        self.crawl(forsearch)
