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
        GooglePyrate.show_the_results_for('')

    @staticmethod
    def show_the_results_for(for_search):
        google_crawler = GoogleCrawler()
        status_code, results = google_crawler.search(for_search)

        output = ''

        if status_code == 200:
            output = GooglePyrate.build_visual_results(results)
        else:
            output = 'Unfortunately it is not possible show the results. Try again in another time.'

        GooglePyrate.show_in_console(output)

    @staticmethod
    def build_visual_results(results):
        return "Title                                                     |Link\n" \
               "Scrapy | A Fast and Powerful Scraping and Web Crawling ...|http://scrapy.org/ "

    @staticmethod
    def show_in_console(output):
        pass
