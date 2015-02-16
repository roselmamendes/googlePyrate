from unittest import TestCase, mock
from googleResults.google_results import GoogleResults

class TestGoogleResults(TestCase):

    def test_crawl_method_is_called(self):
        googleResults = GoogleResults()
        toSearch = "scrapy"
        googleResults.crawl = mock.Mock()
        googleResults.buildGoogleResults(toSearch)
        googleResults.crawl.assert_called_once_with('googleSpider', 'scrapy')

    def test_get_html_results(self):
        expec_result = '<div></div>'
        googleResults = GoogleResults()
        toSearch = "python mock"
        result = googleResults.buildGoogleResults(toSearch)
        self.assertEqual(expec_result, result)
