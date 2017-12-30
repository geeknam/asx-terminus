from asxterminus.config import config
from asxterminus.data.news import Document
from asxterminus.ui.table import Table, Row
import urwid

class NewsTable(Table):

    def __init__(self, portfolio):
        self.portfolio = portfolio
        data = [
            document.to_dict()
            for document in self.portfolio.get_news()
        ]
        super(NewsTable, self).__init__(
            headers=Document.FIELDS,
            data=data
        )