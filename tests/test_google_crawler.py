from unittest import TestCase
import requests_mock
from googleResults.google_crawler import GoogleCrawler
from tests.load_html_page import load_html


@requests_mock.Mocker()
class GoogleCrawlerTest(TestCase):

    def test_call_a_google_url_and_get_200(self, request_mock):
        request_mock.get(url='http://www.google.com/search?q=teste', text='<br>', status_code=200)
        google_crawler = GoogleCrawler()

        actual_status_code, _ = google_crawler.search('teste')

        self.assertEqual(200, actual_status_code)

    def test_if_there_is_a_problem_calling_a_google_page_return_a_status_code_different_than_200(self, request_mock):
        request_mock.get(url='http://www.google.com/search?q=teste', status_code=400)
        google_crawler = GoogleCrawler()

        actual_status_code, _ = google_crawler.search('teste')

        self.assertEqual(400, actual_status_code)

    def test_should_search_with_google_url_and_treat_search_with_more_than_one_word(self,
                                                                                    check_if_request_call_get_with):
        check_if_request_call_get_with.get('http://www.google.com/search?q=python+crawler', text='<br>')
        tosearch = "python crawler"
        google_crawler = GoogleCrawler()

        google_crawler.search(tosearch)

    def test_should_get_the_first_result_from_google_results(self, request_mock):
        tosearch = "python crawler"
        request_mock.get('http://www.google.com/search?q=python+crawler', text=load_html(tosearch))
        google_crawler = GoogleCrawler()

        _, actual_result = google_crawler.search(tosearch)

        expected_result = {
            'title': 'Scrapy | A Fast and Powerful Scraping and Web Crawling ...',
            'href': 'http://scrapy.org/'
        }
        self.assertEqual(expected_result, actual_result[0])
