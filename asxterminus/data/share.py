from asxterminus.data.base import ApiBaseObject


class Share(ApiBaseObject):

    def __repr__(self):
        return '%s - %s' % (self.code, self.last_price)

    def to_cell(self, fields):
        return [
            getattr(self, field)
            for field in fields
        ]

    def get_return(self, assets):
        return sum([
            asset.get_return(self.last_price)
            for asset in assets
        ])


class Asset(object):

    def __init__(self, purchase_price, volume):
        self.purchase_price = purchase_price
        self.volume = volume

    @property
    def total_price(self):
        return self.purchase_price * self.volume

    def get_return(self, current_price):
        return current_price * self.volume - self.total_price



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