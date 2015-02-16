class GoogleCrawler(object):

    def buildgoogleresults(self, tosearch):
        self.forsearch = tosearch.replace(' ', '+')
        return self.forsearch
