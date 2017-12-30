from asxterminus.config import config
from asxterminus.ui.table import Table, Row


class QuoteRow(Row):

    def __init__(self, headers, data, tab_size, style='cell'):
        super(QuoteRow, self).__init__(
            headers=headers,
            data=data,
            tab_size=tab_size,
            style=style
        )

    def get_header_style_map(self):
        share_return = self.data.get('return', 0)
        style = self.style
        if share_return < 0:
            style = 'loss'
        if share_return > 0:
            style = 'gain'
        return {
            'return': style
        }

class ShareTable(Table):

    row_class = QuoteRow
    extra_headers = ('return', )

    def __init__(self, portfolio):
        self.portfolio = portfolio
        data = [
            share.to_dict(config.columns)
            for share in self.portfolio.get_share_prices()
        ]
        super(ShareTable, self).__init__(
            headers=config.columns,
            data=data
        )