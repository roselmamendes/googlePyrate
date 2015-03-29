__path__ = ['google_pyrate']
from google_pyrate.crawler_google import busca

class GooglePyrate:

    def inicio(self):
        print('Bem vinda ao Google Pyrate')
        busca = input('O que você deseja procurar?')
        self.mostrar_os_resultados_para(busca)

    def mostrar_os_resultados_para(self, a_buscar):
        # status_code, resultados = self.google_crawler.search(busca)
        resultados = busca(a_buscar)

        saida = ''

        saida = self.montar_os_resultados(resultados)

        self.mostrar_no_terminal(saida)

    def montar_os_resultados(self, resultados):
        saida = ''
        for resultado in resultados:
            saida += '\n----------------'\
                     '\n Titulo: ' + resultado['titulo']+\
                     '\nLink: ' + resultado['url']

        return saida

    def mostrar_no_terminal(self, saida):
        print(saida)
