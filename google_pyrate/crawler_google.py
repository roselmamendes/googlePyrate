from bs4 import UnicodeDammit
from cssselect import HTMLTranslator
import lxml.html
import requests

_HEADERS = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'DNT': '1'
}

_SEARCH_URL = 'http://www.google.com/search'

_SEARCH_PARAMS = {
            'q': '', # the search query string
            'num': '', # the number of results per page
            'numgm': None, # Number of KeyMatch results to return with the results. A value between 0 to 50 can be specified for this option.
            'start': '0', # Specifies the index number of the first entry in the result set that is to be returned. page number = (start / num) + 1
                          # The maximum number of results available for a query is 1,000, i.e., the value of the start parameter added to the value of the num parameter cannot exceed 1,000.
            'rc': '', # Request an accurate result count for up to 1M documents. If a user submits a search query without the site parameter, the entire search index is queried.
            'site': None, # Limits search results to the contents of the specified collection.
            'sort': None, # Specifies a sorting method. Results can be sorted by date.
            'client': None, # required parameter. Indicates a valid front end.
            'output': None, # required parameter. Selects the format of the search results.
            'partialfields': None, # Restricts the search results to documents with meta tags whose values contain the specified words or phrases.
            'pws': '0',      # personalization turned off
            'cd': None, # Passes down the keyword rank clicked.
            'filter': 0, # Include omitted results
            'complete': 0, #Turn auto-suggest and Google Instant on (=1) or off (=0)
            'nfpr': 1, #Turn off auto-correction of spelling
            'ncr': 1, #No country redirect: Allows you to set the Google country engine you would like to use despite your current geographic location.
            'safe': 'off', # Turns the adult content filter on or off
            'rls': None, #Source of query with version of the client and language set, other examples are can be found
            'source': None,  #Google navigational parameter specifying where you came from, here universal search
            'tbm': None, # Used when you select any of the “special” searches, like image search or video search
            'tbs': None, # Also undocumented as `tbm`, allows you to specialize the time frame of the results you want to obtain.
                         # Examples: Any time: tbs=qdr:a, Last second: tbs=qdr:s, Last minute: tbs=qdr:n, Last day: tbs=qdr:d, Time range: tbs=cdr:1,cd_min:3/2/1984,cd_max:6/5/1987
                         # But the tbs parameter is also used to specify content:
                         # Examples: Sites with images: tbs=img:1, Results by reading level, Basic level: tbs=rl:1,rls:0, Results that are translated from another language: tbs=clir:1,
                         # For full documentation, see http://stenevang.wordpress.com/2013/02/22/google-search-url-request-parameters/
            'lr': 'lang_br', # Restricts searches to pages in the specified language. If there are no results in the specified language, the search appliance displays results in all languages .
                             # lang_xx where xx is the country code such as en, de, fr, ca, ...
            'hl': 'pt_br', # Language settings passed down by your browser
            'cr': 'countryBR', # The region the results should come from
            'gr': None, # Just as gl shows you how results look in a specified country, gr limits the results to a certain region
            'gcs': None, # Limits results to a certain city, you can also use latitude and longitude
            'gpc': None, #Limits results to a certain zip code
            'gm': None, # Limits results to a certain metropolitan region
            'gl': 'de', # as if the search was conducted in a specified location. Can be unreliable.
            'ie': 'utf-8', # Sets the character encoding that is used to interpret the query string.
            'oe': 'utf-8' # Sets the character encoding that is used to encode the results.
}

def busca(a_buscar):
    _SEARCH_PARAMS.update({'q': a_buscar})
    r = requests.get(_SEARCH_URL, headers=_HEADERS,
                                 params=_SEARCH_PARAMS, timeout=3.0)

    html = r.text

    doc = UnicodeDammit(html, is_html=True)
    parser = lxml.html.HTMLParser(encoding=doc.declared_html_encoding)
    dom = lxml.html.document_fromstring(html, parser=parser)
    dom.resolve_base_href()

    li_g_results = dom.xpath(HTMLTranslator().css_to_xpath('li.g'))

    links = []
    for e in li_g_results:
        link_element = e.xpath(HTMLTranslator().css_to_xpath('h3.r > a:first-child'))
        link = link_element[0].get('href')
        title = link_element[0].text_content()

        links.append({"link_title": title, "link_url": link})

    return links
