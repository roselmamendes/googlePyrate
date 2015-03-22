from unittest import TestCase
from unittest.mock import Mock, patch
import requests
import requests_mock
from googleResults.google_crawler import GoogleCrawler


@requests_mock.Mocker()
class GoogleCrawlerTest(TestCase):

    def test_should_a_search_with_more_than_one_word_with_plus_between_the_words(self, request_mock):
        request_mock.get('http://www.google.com/search?q=python+crawler', text='<br>')
        google_crawler = GoogleCrawler()
        tosearch = "python crawler"

        self.assertEqual('python+crawler', google_crawler.buildgoogleresults(tosearch))

    def test_call_a_google_url_and_get_200(self, request_mock):
        request_mock.get(url='http://www.google.com/search?q=teste', text='<br>', status_code=200)
        google_crawler = GoogleCrawler()

        google_crawler.buildgoogleresults('teste')

        self.assertEqual(200, google_crawler.search())

    def test_if_there_is_a_problem_calling_a_google_page_return_a_status_code_different_than_200(self, request_mock):
        request_mock.get(url='http://www.google.com/search?q=teste', status_code=400)
        google_crawler = GoogleCrawler()
        google_crawler.buildgoogleresults('teste')

        self.assertEqual(400, google_crawler.search())

    def test_should_search_with_url(self, request_mock):
        request_mock.get('http://www.google.com/search?q=python+crawler', text='<br>')
        tosearch = "python crawler"
        google_crawler = GoogleCrawler()

        google_crawler.buildgoogleresults(tosearch)
