from asxterminus.data.base import ApiBaseObject
from asxterminus.data.news import NewsScraper
from asxterminus.config import config


class Transaction(object):

    def __init__(self, purchase_price, volume):
        self.purchase_price = purchase_price
        self.volume = volume

    @property
    def total_price(self):
        return self.purchase_price * self.volume

    def get_return(self, current_price):
        return current_price * self.volume - self.total_price


class Share(ApiBaseObject):

    def __repr__(self):
        return '%s - %s' % (self.code, self.last_price)

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
            transaction.get_return(self.last_price)
            for transaction in self.transactions
        ])


class AsxDataProvider(object):

    BASE_URL = 'http://data.asx.com.au/data/1/share/%s/'

    @classmethod
    def get(cls, code):
        url = cls.BASE_URL % code.upper()
        return Share.build_from(url)


class Portfolio(object):

    def __init__(self, codes):
        self.codes = codes

    def get_share_prices(self):
        return [
            AsxDataProvider.get(code)
            for code in self.codes
        ]

    def get_news(self):
        documents = []
        for code in self.codes:
            documents.extend(NewsScraper(code).scrape())
        return documents