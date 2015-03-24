from unittest import TestCase
from unittest.mock import patch
from google_pyrate.google_pyrate import GooglePyrate


class ConsoleTest(TestCase):

    def test_should_return_welcome_message(self):
        self.assertEqual('Welcome to GooglePyrate!', GooglePyrate.welcome_message())

    def test_should_return_start_message_waiting_for_input(self):
        self.assertEqual('What Do You Look for? Type here ->', GooglePyrate.waiting_for_input_message())

    @patch('google_pyrate.google_crawler.GoogleCrawler.search')
    def test_should_get_what_user_type_and_call_google_crawler_search(self, google_crawler_search):
        GooglePyrate.show_the_results('python crawler')

        google_crawler_search.assert_called_once_with('python crawler')
