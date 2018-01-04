from unittest import TestCase
from mock import patch
from asxterminus.data.share import AsxDataProvider

class TestAsxDataProvider(TestCase):

    def setUp(self):
        self.data = {
            "annual_dividend_yield": 1.11,
            "average_daily_volume": 654798,
            "bid_price": 6.88,
            "change_in_percent": "-0.578%",
            "change_price": -0.04,
            "code": "KGN",
            "day_high_price": 6.97,
            "day_low_price": 6.83,
            "deprecated_market_cap": 643973000,
            "deprecated_number_of_shares": 93464938,
            "desc_full": "Ordinary Fully Paid",
            "eps": 0.0401,
            "last_price": 6.88,
            "last_trade_date": "2018-01-04T00:00:00+1100",
            "market_cap": 646777371,
            "number_of_shares": 93464938,
            "offer_price": 6.89,
            "open_price": 6.95,
            "pe": 172.57,
            "previous_close_price": 6.92,
            "previous_day_percentage_change": "2.065%",
            "volume": 213078,
            "year_high_date": "2017-12-27T00:00:00+1100",
            "year_high_price": 7.07,
            "year_low_date": "2017-01-04T00:00:00+1100",
            "year_low_price": 1.35
        }

    @patch('requests.get')
    def test_get(self, mock_get):
        mock_get.return_value.json.return_value = self.data
        share = AsxDataProvider.get('KGN')
        self.assertEquals(share.code, self.data['code'])
        self.assertEquals(share.last_price, self.data['last_price'])
        self.assertEquals(share.open_price, self.data['open_price'])