__path__ = ['google_pyrate']
from google_pyrate.google_crawler import GoogleCrawler
from google_pyrate.user_interface import UI

STATUS_CODE = 200
PAGE_NOT_FOUND = 404
BAD_REQUEST = 400


class GooglePyrate:

    ui = UI()
    google_crawler = GoogleCrawler()

    def show_the_results_for(self, for_search):
        status_code = 0
        output = ''
        results = []

        if not for_search:
            output = 'Nothing to show... Are you sure that you type something?'
        else:
            status_code, results = self.google_crawler.search(for_search)
            output = self.treat_status_and_results(status_code, results)

        self.show_in_console(output)

    def treat_status_and_results(self, status_code, results):
        output = ''
        if status_code == STATUS_CODE:
            output = self.build_visual_results(results)
        elif status_code == BAD_REQUEST or status_code == PAGE_NOT_FOUND:
            output = 'Unfortunately it is not possible show the results. Try again in another time.'

        return output

    def build_visual_results(self, results):
        saida = ''
        for result in results:
            saida += '\n----------------'\
                     '\n Titulo: ' + result['title'] +\
                     '\nLink: ' + result['href']

        return saida

    def show_in_console(self, output):
        self.ui.set_output(output)
