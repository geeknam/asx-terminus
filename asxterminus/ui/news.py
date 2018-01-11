from asxterminus.config import config
from asxterminus.data.news import Document
from asxterminus.data.rss import GoogleFinance, RssItem
from asxterminus.ui.table import PortfolioTable, Row
import urwid

class AnnouncementTable(PortfolioTable):

    HEADERS = Document.FIELDS

    def get_dataset(self, progress_bar=None):
        data = [
            document.to_dict()
            for document in self.portfolio.get_announcements(progress_bar)
        ]
        return data

class GoogleFinanceNews(PortfolioTable):

    HEADERS = RssItem.FIELDS

    def get_dataset(self, progress_bar=None):
        data = [
            rss.to_dict()
            for rss in self.portfolio.get_rss(progress_bar)
        ]
        return data