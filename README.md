# asx-terminus


[![pypi version]( https://img.shields.io/pypi/v/asx-terminus.svg)]( https://pypi.python.org/pypi/asx-terminus)
[![Build Status](https://travis-ci.org/geeknam/asx-terminus.svg?branch=master)](https://travis-ci.org/geeknam/asx-terminus)

![Screenshot](https://raw.githubusercontent.com/geeknam/asx-terminus/master/asxterminus.png)

### Installation

Install via pip:

    $ pip install asx-terminus

Add `.asxterminus.yaml` file to your `$HOME` dir

Start in you terminal:

    $ asxterminus


### Sample Configuration file

Sample `~/.asxterminus.yaml` file

```yaml
    refresh_interval: 1200
    codes:
      - KGN
      - A2M
      - APX
    transactions:
      KGN:
        -
          - 1.48
          - 10000
        -
          - 1.34
          - 5000
      A2M:
        -
          - 2.7
          - 5000
      APX:
        -
          - 2.5
          - 10000
    columns:
      - code
      - last_price
      - open_price
      - day_high_price
      - day_low_price
```

### Available fields (columns)

- code
- desc_full
- last_price
- open_price
- day_high_price
- day_low_price
- change_price
- change_in_percent
- volume
- bid_price
- offer_price
- previous_close_price
- previous_day_percentage_change
- year_high_price
- last_trade_date
- year_high_date
- year_low_price
- year_low_date
- year_open_date
- pe
- eps
- average_daily_volume
- annual_dividend_yield
- market_cap
- number_of_shares
- deprecated_market_cap
- deprecated_number_of_shares


### TODO

- [x] Add Google Finance RSS feeds
- [x] Add progress bar when loading data
- [ ] Add Portfolio Return
- [ ] Add Return Rate (%)

### Disclaimer

This software should not be used as a financial advisor, it is for educational use only. Absolutely no warranty is implied with this product. By using this software you release the author(s) from any liability regarding the use of this software. You can lose money because this program probably has some errors in it, so use it at your own risk. And please don't take risks with money you can't afford to lose.
