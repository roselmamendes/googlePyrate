import requests
from bs4 import UnicodeDammit
from cssselect import HTMLTranslator
import lxml.html

URL = 'http://www.google.com/search'

PARAMETERS = {'q': '',  # the search query string
              'num': '',  # the number of results per page
              'numgm': None,  # Number of KeyMatch results to return with the results.
                              # A value between 0 to 50 can be specified for this option.
              'start': '0',  # Specifies the index number of the first entry in the result set
                             # that is to be returned self.
                             # page number = (start / num) + 1
                             # The maximum number of results available for a query is 1,000,
                             # i.e., the value of the start parameter added
                             # to the value of the num parameter cannot exceed 1,000.
              'rc': '',  # Request an accurate result count for up to 1M documents.
                         # If a user submits a search query without the site parameter,
                         # the entire search index is queried.
              'site': None,  # Limits search results to the contents of the specified collection.
              'sort': None,  # Specifies a sorting method. Results can be sorted by date.
              'client': None,  # required parameter. Indicates a valid front end.
              'output': None,  # required parameter. Selects the format of the search results.
              'partialfields': None,  # Restricts the search results to documents with meta tags
                                      # whose values contain the specified words or phrases.
              'pws': '0',      # personalization turned off
              'cd': None,  # Passes down the keyword rank clicked.
              'filter': 0,  # Include omitted results
              'complete': 0,  # Turn auto-suggest and Google Instant on (=1) or off (=0)
              'nfpr': 1,  # Turn off auto-correction of spelling
              'ncr': 1,  # No country redirect:
                         # Allows you to set the Google country engine you would like to use
                         # despite your current geographic location.
              'safe': 'off',  # Turns the adult content filter on or off
              'rls': None,  # Source of query with version of the client and language set,
                            # other examples are can be found
              'source': None,  # Google navigational parameter specifying where you came from, here universal search
              'tbm': None,  # Used when you select any of the “special” searches, like image search or video search
              'tbs': None,  # Also undocumented as `tbm`,
                            # allows you to specialize the time frame of the results you want to obtain.
                            # Examples: Any time: tbs=qdr:a, Last second: tbs=qdr:s, Last minute: tbs=qdr:n,
                            # Last day: tbs=qdr:d, Time range: tbs=cdr:1,cd_min:3/2/1984,cd_max:6/5/1987
                            # But the tbs parameter is also used to specify content:
                           # Examples: Sites with images: tbs=img:1, Results by reading level,
                           # Basic level: tbs=rl:1,rls:0, Results that are translated from another language: tbs=clir:1,
                           # For full documentation,
                         # see http://stenevang.wordpress.com/2013/02/22/google-search-url-request-parameters/
              'lr': 'lang_br',  # Restricts searches to pages in the specified language.
                                # If there are no results in the specified language,
                                # the search appliance displays results in all languages .
                               # lang_xx where xx is the country code such as en, de, fr, ca, ...
              'hl': 'pt_br',  # Language settings passed down by your browser
              'cr': 'countryBR',  # The region the results should come from
              'gr': None,  # Just as gl shows you how results look in a specified country,
                           # gr limits the results to a certain region
              'gcs': None,  # Limits results to a certain city, you can also use latitude and longitude
              'gpc': None,  # Limits results to a certain zip code
              'gm': None,  # Limits results to a certain metropolitan region
              'gl': 'de',  # as if the search was conducted in a specified location. Can be unreliable.
              'ie': 'utf-8',  # Sets the character encoding that is used to interpret the query string.
              'oe': 'utf-8'  # Sets the character encoding that is used to encode the results.
              }


class GoogleCrawler:

    def search(self, for_search):
        results = []

        r = requests.get(URL,
                         params={'q': for_search})

        if r.status_code == 200:
            results = self.build_results_from_html(r.text)

        return r.status_code, results

    def build_results_from_html(self, html):
        doc = UnicodeDammit(html, is_html=True)
        parser = lxml.html.HTMLParser(encoding=doc.declared_html_encoding)
        html_element = lxml.html.document_fromstring(html, parser=parser)

        li_g_tags = html_element.xpath(HTMLTranslator().css_to_xpath('li.g'))

        results = []
        for li_tag in li_g_tags:
            a_tag = li_tag.xpath(HTMLTranslator().css_to_xpath('h3.r > a:first-child'))
            results.append({'title': a_tag[0].text_content(),
                           'href': self.formata_url(a_tag[0].get('href'))})

        return results

    def formata_url(self, url):
        return url[url.find('http'):url.find('&sa')]
