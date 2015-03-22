from pyquery import PyQuery
import requests

URL = 'http://www.google.com/search?q='


class GoogleCrawler:

    def search(self, for_search):
        results = []

        r = requests.get(
            URL +
            for_search.replace(' ', '+'))

        if r.status_code == 200:
            results = self.build_results_from_html(r.text)

        return r.status_code, results

    def build_results_from_html(self, html):
        d = PyQuery(html)
        # //*[@id="rso"]/div[2]/li[1]/div/h3/a
        div_tag = d('#rso div').eq(1)

        a_tag = div_tag('li div h3 a')

        results = []

        for i in range(0, len(a_tag)):
            results.append({
                'title': a_tag[i].text,
                'href': a_tag[i].get('href')
                })

        return results
