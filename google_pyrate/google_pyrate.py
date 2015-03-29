__path__ = ['google_pyrate']
from google_pyrate.google_crawler import GoogleCrawler
from google_pyrate.user_interface import UI


class GooglePyrate:

    ui = UI()
    google_crawler = GoogleCrawler()

    def show_the_results_for(self, for_search):

        status_code = 0
        output = ''

        if not for_search:
            output = 'Nothing to show... Are you sure that you type something?'
        else:
            status_code, results = self.google_crawler.search(for_search)

        if status_code == 200:
            output = self.build_visual_results(results)
        elif status_code == 400 or status_code == 404:
            output = 'Unfortunately it is not possible show the results. Try again in another time.'

        self.show_in_console(output)

    def build_visual_results(self, results):
        saida = ''
        for result in results:
            saida += '\n----------------'\
                     '\n Titulo: ' + result['title'] +\
                     '\nLink: ' + result['href']

        return saida

    def show_in_console(self, output):
        self.ui.set_output(output)
