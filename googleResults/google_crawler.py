from pyquery import PyQuery
import requests


class GoogleCrawler(object):

    def buildgoogleresults(self, tosearch):
        self.forsearch = tosearch.replace(' ', '+')
        return self.forsearch

    def call(self, url):
        r = requests.get(url)
        d = PyQuery(r.text)
        if d:
            pass
        return r.status_code
