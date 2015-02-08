import unittest
from google_results import GoogleResults

class TestGoogleResults(unittest.TestCase):
    
    expected_result = '<h1>Scrapy Tutorial<a class="headerlink" href="#scrapy-tutorial" title="Permalink to this headline">¶</a></h1>'
    
    def test_get_html_results(self):
        googleResults = GoogleResults()
        toSearch = "scrapy"
        result = googleResults.buildGoogleResults(toSearch)
        self.assertEqual(result, self.expected_result)
        
    def test_get_html_results_from_google(self):
        googleResults = GoogleResults()
        toSearch = "scrapy"
        result = googleResults.buildGoogleResults(toSearch)
        self.assertEqual(result, self.expected_result)
        