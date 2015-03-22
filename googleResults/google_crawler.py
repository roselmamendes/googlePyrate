from pyquery import PyQuery
import requests


class GoogleCrawler(object):

    url = 'http://www.google.com/search?q='

    def buildgoogleresults(self, tosearch):
        self.forsearch = tosearch.replace(' ', '+')
        self.search()
        return self.forsearch

    def search(self):
        r = requests.get(self.url + self.forsearch)

        if r.status_code == 200:
            d = PyQuery(r.text)

        return r.status_code
