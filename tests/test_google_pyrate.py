from unittest import TestCase
from unittest import mock
from google_pyrate.google_crawler import GoogleCrawler
from google_pyrate.google_pyrate import GooglePyrate


class ConsoleTest(TestCase):

    def test_should_treat_when_receive_a_blank_input(self):
        google_pyrate = GooglePyrate()
        google_pyrate.show_in_console = mock.Mock()

        google_pyrate.show_the_results_for('')

        google_pyrate.show_in_console.assert_called_once_with(
            'Nothing to show... Are you sure that you type something?')

    def test_should_show_results_correctly(self):
        google_pyrate = GooglePyrate()

        actual_visual_result = google_pyrate.build_visual_results([{
            'title': 'Scrapy | A Fast and Powerful Scraping and Web Crawling ...',
            'href': 'http://scrapy.org'
        }])

        expected_visual_result = '\n----------------'\
                                 '\n Titulo: Scrapy | A Fast and Powerful Scraping and Web Crawling ...'\
                                 '\nLink: http://scrapy.org'

        self.assertEqual(expected_visual_result, actual_visual_result)

    def test_if_trying_get_results_return_status_code_different_than_200_should_treat_this(self):
        google_pyrate = GooglePyrate()
        google_pyrate.show_in_console = mock.Mock()
        mock.patch.stopall()
        mock.patch('google_pyrate.google_crawler.GoogleCrawler.search', return_value=[400, []]).start()

        google_pyrate.show_the_results_for('python crawler')

        google_pyrate.show_in_console.assert_called_once_with('Unfortunately it is not possible show the results.'
                                                              ' Try again in another time.')
