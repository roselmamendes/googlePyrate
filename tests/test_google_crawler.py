from unittest import TestCase
from unittest.mock import Mock, patch
import requests
import requests_mock
from googleResults.google_crawler import GoogleCrawler


class GoogleCrawlerTest(TestCase):

    def test_should_a_search_with_more_than_one_word_with_plus_between_the_words(self):
        google_crawler = GoogleCrawler()
        tosearch = "python crawler"
        self.assertEqual('python+crawler', google_crawler.buildgoogleresults(tosearch))

    def test_call_a_google_url_and_get_201(self):
        google_crawler = GoogleCrawler()
        google_crawler.buildgoogleresults('teste')
        self.assertEqual('Sucess', google_crawler.search())

    @requests_mock.Mocker()
    def test_if_there_is_a_problem_calling_a_google_page_return_a_status_code_different_than_200(self, request_mock):
        request_mock.get(url='http://www.google.com/search?q=teste', status_code=400)
        google_crawler = GoogleCrawler()
        google_crawler.buildgoogleresults('teste')
        self.assertEqual('Failed', google_crawler.search())

    @patch('requests.get')
    def test_should_search_with_url(self, request_get):
        google_crawler = GoogleCrawler()
        tosearch = "python crawler"
        url = 'http://www.google.com/search?q='
        google_crawler.buildgoogleresults(tosearch)
        request_get.assert_called_once_with(url + 'python+crawler')
