from google_pyrate.google_crawler import GoogleCrawler


class GooglePyrate:

    @staticmethod
    def welcome_message():
        return 'Welcome to GooglePyrate!'

    @staticmethod
    def waiting_for_input_message():
        return 'What Do You Look for? Type here ->'

    @staticmethod
    def waiting_for_input():
        pass

    @staticmethod
    def show_the_results():
        google_crawler = GoogleCrawler()
        google_crawler.search('')
