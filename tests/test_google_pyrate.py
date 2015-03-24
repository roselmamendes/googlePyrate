from unittest import TestCase
from unittest.mock import patch, Mock
from google_pyrate.google_crawler import GoogleCrawler
from google_pyrate.google_pyrate import GooglePyrate


class ConsoleTest(TestCase):

    def test_should_return_welcome_message(self):
        self.assertEqual('Welcome to GooglePyrate!', GooglePyrate.welcome_message())

    def test_should_return_start_message_waiting_for_input(self):
        self.assertEqual('What Do You Look for? Type here ->', GooglePyrate.waiting_for_input_message())

    def test_should_start_correctly(self):
        GooglePyrate.welcome_message = Mock()
        GooglePyrate.waiting_for_input_message = Mock()
        GooglePyrate.waiting_for_input = Mock()

        GooglePyrate.start()

        self.assertTrue(GooglePyrate.welcome_message.called)
        self.assertTrue(GooglePyrate.waiting_for_input_message.called)
        self.assertTrue(GooglePyrate.waiting_for_input.called)

    @patch('google_pyrate.google_crawler.GoogleCrawler.search')
    def test_after_receive_what_should_research_start_building_the_results(self, google_crawler_search):
        for_search = 'python crawler'
        first_expected_result = {
            'title': 'Scrapy | A Fast and Powerful Scraping and Web Crawling ...',
            'href': 'http://scrapy.org/'
        }
        google_crawler_search.return_value = 200, first_expected_result
        patch('google_pyrate.google_pyrate.GooglePyrate.build_visual_results').start()

        GooglePyrate.show_the_results_for(for_search)

        google_crawler_search.assert_called_once_with(for_search)
        GooglePyrate.build_visual_results.assert_called_once_with(first_expected_result)

        patch.stopall()

    @patch('google_pyrate.google_crawler.GoogleCrawler.search')
    def test_should_show_results_correctly(self, google_crawler_search):
        google_crawler_search.return_value = 200, {
            'title': 'Scrapy | A Fast and Powerful Scraping and Web Crawling ...',
            'href': 'http://scrapy.org/'
        }
        google_crawler = GoogleCrawler()

        actual_visual_result = GooglePyrate.build_visual_results(google_crawler.search('python crawler'))

        expected_visual_result = "Title                                                     |Link\n" \
                                 "Scrapy | A Fast and Powerful Scraping and Web Crawling ...|http://scrapy.org/ "

        self.assertEqual(expected_visual_result, actual_visual_result)

    # TODO: Check status code, Check the possibility of a new search
