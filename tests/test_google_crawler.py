from unittest import TestCase
from googleResults.google_crawler import GoogleCrawler


class GoogleCrawlerTest(TestCase):

    def test_should_a_search_with_more_than_one_word_with_plus_between_the_words(self):
        google_crawler = GoogleCrawler()
        tosearch = "python crawler"
        self.assertEqual('python+crawler', google_crawler.buildgoogleresults(tosearch))
