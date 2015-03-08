from unittest import TestCase
from googleResults.google_crawler import GoogleCrawler


class GoogleCrawlerTest(TestCase):

    def test_should_a_search_with_more_than_one_word_with_plus_between_the_words(self):
        google_crawler = GoogleCrawler()
        tosearch = "python crawler"
        self.assertEqual('python+crawler', google_crawler.buildgoogleresults(tosearch))

    def test_call_a_google_url_and_get_201(self):
        google_crawler = GoogleCrawler()
        self.assertEqual(200, google_crawler.call('http://www.google.com/search?q=teste'))

    def test_if_there_is_a_problem_calling_a_google_page_return_a_status_code_different_than_200(self):
        google_crawler = GoogleCrawler()
        self.assertNotEqual(200, google_crawler.call('http://www.google.com/teste'))
