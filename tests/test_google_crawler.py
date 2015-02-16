from unittest import TestCase, mock
from googleResults.google_crawler import GoogleCrawler


class GoogleCrawlerTest(TestCase):

    def test_should_receive_a_url_then_return_response(self):
        url = 'http://www.codingdojo.org'
        google_crawler = GoogleCrawler(url)

        self.assertIsNotNone('', google_crawler.getresponse())

    def test_should_a_search_with_more_than_one_word_with_plus_between_the_words(self):
        url = 'http://www.codingdojo.org'
        google_crawler = GoogleCrawler(url)
        tosearch = "python crawler"

        google_crawler.crawl = mock.Mock()

        google_crawler.buildgoogleresults(tosearch)

        google_crawler.crawl.assert_called_once_with("python+crawler")
