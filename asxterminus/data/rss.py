import feedparser

class RssItem(object):

    FIELDS = (
        'symbol', 'title', 'link'
    )

    def __init__(self, symbol, title, link, pub_date):
        self.symbol = symbol
        self.title = title
        self.link = link
        self.pub_date = pub_date

    def to_dict(self):
        return self.__dict__


class BaseRssFeedParser(object):

    MAX_ITEMS = 10

    def __init__(self, symbol):
        self.symbol = symbol
        self.rss_url = self.BASE_RSS_URL % symbol
        self.feed = feedparser.parse(self.rss_url)

    def get_item_title(self, item):
        raise NotImplementedError()

    def get_item_link(self, item):
        raise NotImplementedError()

    def get_item_pub_date(self, item):
        raise NotImplementedError()

    @property
    def items(self):
        items = []
        for item in self.feed.entries[:self.MAX_ITEMS]:
            items.append(
                RssItem(
                    symbol=self.symbol,
                    title=self.get_item_title(item),
                    link=self.get_item_link(item),
                    pub_date=self.get_item_pub_date(item)
                )
            )
        return items



class GoogleFinance(BaseRssFeedParser):

    BASE_RSS_URL = 'https://finance.google.com/finance/company_news?q=ASX:%s&output=rss'

    def get_item_title(self, item):
        return item.title

    def get_item_link(self, item):
        return item.link

    def get_item_pub_date(self, item):
        return item.published