from google_pyrate.google_crawler import GoogleCrawler


class GooglePyrate:

    @staticmethod
    def start():
        GooglePyrate.welcome_message()
        GooglePyrate.waiting_for_input_message()
        GooglePyrate.waiting_for_input()

    @staticmethod
    def welcome_message():
        return 'Welcome to GooglePyrate!'

    @staticmethod
    def waiting_for_input_message():
        return 'What Do You Look for? Type here ->'

    @staticmethod
    def waiting_for_input():
        GooglePyrate.show_the_results('')

    @staticmethod
    def show_the_results(for_search):
        google_crawler = GoogleCrawler()
        google_crawler.search(for_search)
