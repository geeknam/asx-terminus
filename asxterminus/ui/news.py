from asxterminus.config import config
from asxterminus.data.news import Document
from asxterminus.data.rss import GoogleFinance, RssItem
from asxterminus.ui.table import Table, Row
import urwid

class AnnouncementTable(Table):

    def __init__(self, portfolio):
        self.portfolio = portfolio
        data = self.get_dataset()
        super(AnnouncementTable, self).__init__(
            headers=Document.FIELDS,
            data=data
        )

    def get_dataset(self):
        data = [
            document.to_dict()
            for document in self.portfolio.get_announcements()
        ]
        return data

    def refresh(self):
        self.data = self.get_dataset()

class GoogleFinanceNews(Table):

    def __init__(self, portfolio):
        self.portfolio = portfolio
        data = self.get_dataset()
        super(GoogleFinanceNews, self).__init__(
            headers=RssItem.FIELDS,
            data=data
        )

    def get_dataset(self):
        data = [
            rss.to_dict()
            for rss in self.portfolio.get_rss()
        ]
        return data

    def refresh(self):
        self.data = self.get_dataset()