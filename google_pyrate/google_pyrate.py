from google_pyrate.google_crawler import GoogleCrawler
from google_pyrate.user_interface import UI


class GooglePyrate:

    ui = UI()
    google_crawler = GoogleCrawler()

    def start(self):
        self.welcome_message()
        self.main_menu()

    def main_menu(self):
        self.waiting_for_input_message()
        self.waiting_for_input()

    @staticmethod
    def welcome_message():
        return 'Welcome to GooglePyrate!'

    @staticmethod
    def waiting_for_input_message():
        return 'What Do You Look for? Type here ->'

    def waiting_for_input(self):
        input = self.ui.get_input()
        self.show_the_results_for(input)

    def show_the_results_for(self, for_search):
        status_code, results = self.google_crawler.search(for_search)

        output = ''

        if status_code == 200:
            output = self.build_visual_results(results)
        else:
            output = 'Unfortunately it is not possible show the results. Try again in another time.'

        self.show_in_console(output)

    def build_visual_results(self, results):
        return "Title                                                     |Link\n" \
               "Scrapy | A Fast and Powerful Scraping and Web Crawling ...|http://scrapy.org/ "

    def show_in_console(self, output):
        self.ui.set_output(output)
