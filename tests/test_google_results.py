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
        expected_result = '<a href="/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=0CCcQFjAA&amp;url=https%3A%2F%2Fpypi.python.org%2Fpypi%2Fmock&amp;ei=NZzgVPvxEMXbsATpqYAY&amp;usg=AFQjCNGurnzZ47GvhKvsnHFDpGYrmDVLNg&amp;sig2=4yN6bvJBpHIMd1tXGODjMA" onmousedown="return rwt(this,\'\',\'\',\'\',\'1\',\'AFQjCNGurnzZ47GvhKvsnHFDpGYrmDVLNg\',\'4yN6bvJBpHIMd1tXGODjMA\',\'0CCcQFjAA\',\'\',\'\',event)" data-href="https://pypi.python.org/pypi/mock">mock 1.0.1 : Python Package Index</a>'
        googleResults = GoogleResults()
        toSearch = "python mock"
        result = googleResults.buildGoogleResults(toSearch)
        self.assertEqual(expected_result, result)
