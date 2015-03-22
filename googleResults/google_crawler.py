from pyquery import PyQuery
import requests


class GoogleCrawler(object):

    url = 'http://www.google.com/search?q='

    def search(self, tosearch):
        self.forsearch = tosearch.replace(' ', '+')
        results = []

        r = requests.get(self.url + self.forsearch)
        if r.status_code == 200:
            results = self.buildResults(r.text)

        return r.status_code, results

    def buildResults(self, html):
        d = PyQuery(html)

        return []
