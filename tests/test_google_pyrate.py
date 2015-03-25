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
        google_pyrate = GooglePyrate()
        google_pyrate.welcome_message = Mock()
        google_pyrate.waiting_for_input_message = Mock()
        google_pyrate.waiting_for_input = Mock()

        google_pyrate.start()

        self.assertTrue(google_pyrate.welcome_message.called)
        self.assertTrue(google_pyrate.waiting_for_input_message.called)
        self.assertTrue(google_pyrate.waiting_for_input.called)

    @patch('google_pyrate.google_crawler.GoogleCrawler.search')
    def test_after_receive_what_should_research_start_building_the_results(self, google_crawler_search):
        for_search = 'python crawler'
        first_expected_result = {
            'title': 'Scrapy | A Fast and Powerful Scraping and Web Crawling ...',
            'href': 'http://scrapy.org/'
        }
        google_crawler_search.return_value = 200, first_expected_result
        google_pyrate = GooglePyrate()
        google_pyrate.build_visual_results = Mock()

        google_pyrate.show_the_results_for(for_search)

        google_crawler_search.assert_called_once_with(for_search)
        google_pyrate.build_visual_results.assert_called_once_with(first_expected_result)

        patch.stopall()

    @patch('google_pyrate.google_crawler.GoogleCrawler.search')
    def test_should_show_results_correctly(self, google_crawler_search):
        google_crawler_search.return_value = 200, {
            'title': 'Scrapy | A Fast and Powerful Scraping and Web Crawling ...',
            'href': 'http://scrapy.org/'
        }
        google_crawler = GoogleCrawler()
        google_pyrate = GooglePyrate()

        actual_visual_result = google_pyrate.build_visual_results(google_crawler.search('python crawler'))

        expected_visual_result = "Title                                                     |Link\n" \
                                 "Scrapy | A Fast and Powerful Scraping and Web Crawling ...|http://scrapy.org/ "

        self.assertEqual(expected_visual_result, actual_visual_result)

    # TODO: Check the possibility of a new search
    @patch('google_pyrate.google_crawler.GoogleCrawler.search')
    def test_if_trying_get_results_return_status_code_different_than_200_should_treat_this(self, google_crawler_search):
        for_search = 'python crawler'
        google_pyrate = GooglePyrate()
        google_pyrate.show_in_console = Mock()
        google_crawler_search.return_value = 400, []

        google_pyrate.show_the_results_for(for_search)

        google_pyrate.show_in_console.assert_called_once_with('Unfortunately it is not possible show the results.'
                                                              ' Try again in another time.')
