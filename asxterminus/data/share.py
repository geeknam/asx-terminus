import os
from decimal import Decimal
from asxterminus.data.base import ApiBaseObject
from asxterminus.data.news import AnnouncementsScraper
from asxterminus.data.rss import GoogleFinance
from asxterminus.config import config


class Transaction(object):

    def __init__(self, purchase_price, volume):
        self.purchase_price = purchase_price
        self.volume = volume

    @property
    def total_price(self):
        return self.purchase_price * self.volume

    def get_return(self, current_price):
        return (Decimal(current_price) * self.volume) \
            .quantize(Decimal('.01')) - Decimal(self.total_price)


class Share(ApiBaseObject):

    def __repr__(self):
        return self.code

    def to_dict(self, fields):
        data = dict([
            (field, getattr(self, field))
            for field in fields
        ])
        data.update({
            'return': self.get_return()
        })
        return data

    @property
    def transactions(self):
        return [
            Transaction(transaction[0], transaction[1])
            for transaction in config.transactions.get(self.code, [])
        ]

    def get_return(self):
        return sum([
            transaction.get_return(self.close)
            for transaction in self.transactions
        ])


# XXX: support discontinued
class AsxDataProvider(object):
    BASE_URL = 'http://data.asx.com.au/data/1/share/%s/'

    @classmethod
    def get(cls, code):
        url = cls.BASE_URL % code.upper()
        return Share.build_from(url)


class AlphavantageProvider(object):
    BASE_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&apikey=%s'

    @classmethod
    def get(cls, code):
        url = cls.BASE_URL % (
            '%s.AX' % code.upper(),
            os.getenv('ALPHAVANTAGE_API_KEY', 'Z47LCX423HZ35JA1')
        )
        return Share.build_from_daily(url)


class Portfolio(object):

    def __init__(self, codes):
        self.codes = codes

    def on_progress_update(self, progress_bar):
        progress_bar.add_progress(1)

    def get_share_prices(self, progress_bar=None):
        shares = []
        for code in self.codes:
            shares.append(AlphavantageProvider.get(code))
            if progress_bar:
                self.on_progress_update(progress_bar)
        return shares

    def get_announcements(self, progress_bar=None):
        documents = []
        for code in self.codes:
            documents.extend(AnnouncementsScraper(code).scrape())
            if progress_bar:
                self.on_progress_update(progress_bar)
        return documents

    def get_rss(self, progress_bar=None):
        rss_items = []
        for code in self.codes:
            rss_items.extend(
                GoogleFinance(code).items
            )
            if progress_bar:
                self.on_progress_update(progress_bar)
        return rss_items