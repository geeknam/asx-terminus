from bs4 import BeautifulSoup
import requests


class Document(object):
    
    FIELDS = (
        'code',
        'release_date',
        'headline',
        'pages',
        'link',
    )

    def __init__(self, code, release_date, headline, pages, link):
        self.code = code
        self.release_date = release_date
        self.headline = headline
        self.pages = pages
        self.link = link

    def to_dict(self):
        return self.__dict__


class NewsScraper(object):

    DOMAIN = 'http://www.asx.com.au'
    SOURCE_URL = 'http://www.asx.com.au/asx/statistics/announcements.do'
    PARSER = 'html.parser'

    def __init__(self, code, timeframe='D', period='W'):
        self.code = code
        self.timeframe = timeframe
        self.period = period

    @property
    def content(self):
        params = {
            'by': 'asxCode',
            'asxCode': self.code,
            'timeframe': self.timeframe,
            'period': self.period
        }
        return requests.get(self.SOURCE_URL, params=params).content

    @property
    def table(self):
        soup = BeautifulSoup(self.content, self.PARSER)
        return soup.table

    def scrape(self):
        documents = []
        if self.table:
            for row in self.table.findAll('tr'):
                cols = row.findAll('td')
                if len(cols) > 0:
                    release_date = cols[0].next_element.strip()
                    headline = cols[2].next_element.strip()
                    pages = int(cols[3].next_element.strip())
                    link = '%s%s' % (self.DOMAIN, cols[4].a['href'])

                    documents.append(
                        Document(self.code, release_date, headline, pages, link)
                    )
        return documents