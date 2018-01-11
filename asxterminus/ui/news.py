from asxterminus.config import config
from asxterminus.data.news import Document
from asxterminus.data.rss import GoogleFinance, RssItem
from asxterminus.ui.table import Table, Row
import urwid

class AnnouncementTable(Table):

    def __init__(self, portfolio):
        self.portfolio = portfolio
        data = []
        super(AnnouncementTable, self).__init__(
            headers=Document.FIELDS,
            data=data
        )

    def get_dataset(self, progress_bar=None):
        data = [
            document.to_dict()
            for document in self.portfolio.get_announcements(progress_bar)
        ]
        return data

    def refresh(self, progress_bar):
        self.update_data(
            self.get_dataset(progress_bar)
        )

class GoogleFinanceNews(Table):

    def __init__(self, portfolio):
        self.portfolio = portfolio
        data = []
        super(GoogleFinanceNews, self).__init__(
            headers=RssItem.FIELDS,
            data=data
        )

    def get_dataset(self, progress_bar=None):
        data = [
            rss.to_dict()
            for rss in self.portfolio.get_rss(progress_bar)
        ]
        return data

    def refresh(self, progress_bar):
        self.update_data(
            self.get_dataset(progress_bar)
        )