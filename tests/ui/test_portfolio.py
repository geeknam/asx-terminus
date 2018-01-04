from unittest import TestCase
from mock import Mock
from asxterminus.data.share import Share
from asxterminus.ui.portfolio import QuoteRow, ShareTable


class TestQuoteRow(TestCase):

    def setUp(self):
        self.headers = ['code', 'last_price', 'change_in_percent', 'return']
        self.data = {
            'code': 'ASX',
            'last_price': 5.10,
            'change_in_percent': '-1.23%',
            'return': 2300
        }
        self.row = QuoteRow(self.headers, self.data, {})

    def test_get_header_style_map(self):
        self.assertEquals(
            self.row.get_header_style_map(),
            {'change_in_percent': 'loss', 'return': 'gain'}
        )


class TestShareTable(TestCase):

    def setUp(self):
        self.portfolio = Mock()
        self.portfolio.get_share_prices.return_value = [
            Share(
                code='ASX', last_price=4.5,
                open_price=1.00,
                day_high_price=1.00,
                day_low_price=1.00,
                change_in_percent=1.00,
                annual_dividend_yield=1.00,
                volume=100000,
            )
        ]

    def test_table(self):
        table = ShareTable(self.portfolio)
        rendered = table.render()
        self.assertEquals(
            rendered[0], [
                ('headers', 'code    '),
                ('headers', 'last_price    '),
                ('headers', 'open_price    '),
                ('headers', 'day_high_price    '),
                ('headers', 'day_low_price    '),
                ('headers', 'change_in_percent    '),
                ('headers', 'annual_dividend_yield    '),
                ('headers', 'volume    '),
                ('headers', 'return    '),
                '\n'
        ])

        self.assertEquals(
            rendered[1], [
                ('cell', 'ASX     '),
                ('cell', '4.5           '),
                ('cell', '1.0           '),
                ('cell', '1.0               '),
                ('cell', '1.0              '),
                ('gain', '1.0                  '),
                ('cell', '1.0                      '),
                ('cell', '100000    '),
                ('cell', '0         '),
                '\n'
            ]
        )