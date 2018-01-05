from asxterminus.config import config
from asxterminus.data.news import Document
from asxterminus.data.rss import GoogleFinance, RssItem
from asxterminus.ui.table import Table, Row
import urwid

class AnnouncementTable(Table):

    def __init__(self, portfolio):
        self.portfolio = portfolio
        data = [
            document.to_dict()
            for document in self.portfolio.get_announcements()
        ]
        super(AnnouncementTable, self).__init__(
            headers=Document.FIELDS,
            data=data
        )


class GoogleFinanceNews(Table):

    def __init__(self, portfolio):
        self.portfolio = portfolio
        data = [
            item.to_dict()
            for item in self.portfolio.get_rss()
        ]
        super(GoogleFinanceNews, self).__init__(
            headers=RssItem.FIELDS,
            data=data
        )