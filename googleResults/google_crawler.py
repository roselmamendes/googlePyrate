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
        # //*[@id="rso"]/div[2]/li[1]/div/h3/a
        # //*[@id="rso"]/div[2]
        ol_tag = d('#rso')

        div_tag = ol_tag('div').eq(1)

        a_tag = div_tag('li div h3 a')

        results = []

        for a in range(0, len(a_tag)):
            results.append({
                '<a>': a_tag[a].text,
                'href': a_tag[a].get('href')
                })

        return results
