from google_pyrate.google_crawler import GoogleCrawler
from google_pyrate.user_interface import UI


class GooglePyrate:

    ui = UI()
    google_crawler = GoogleCrawler()

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
