from unittest import TestCase, mock
from googleResults.google_results import GoogleResults

class TestGoogleResults(TestCase):
    
    expected_result = '<h1>Scrapy Tutorial<a class="headerlink" href="#scrapy-tutorial" title="Permalink to this headline">¶</a></h1>'
    
    def test_get_html_results(self):
        googleResults = GoogleResults()
        toSearch = "scrapy"
        result = googleResults.buildGoogleResults(toSearch)
        self.assertEqual(self.expected_result, result)
        
    def test_crawl_method_is_called(self):
        googleResults = GoogleResults()
        toSearch = "scrapy"
        googleResults.crawl = mock.Mock()
        googleResults.buildGoogleResults(toSearch)
        googleResults.crawl.assert_called_once_with('googleSpider')
        