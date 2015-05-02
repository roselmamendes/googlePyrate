from scrapy.item import Item

class ResultItem(Item):

    title = Field()
    href = Field()

    def __init__(self, title, href):
        self.title = title
        self.href = href
