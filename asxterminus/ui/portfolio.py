from asxterminus.config import config
from asxterminus.ui.table import PortfolioTable, Row


class QuoteRow(Row):

    def __init__(self, headers, data, tab_size, style='cell'):
        super(QuoteRow, self).__init__(
            headers=headers,
            data=data,
            tab_size=tab_size,
            style=style
        )

    def get_style(self, field):
        try:
            value = self.data[field]
            if isinstance(value, basestring) and '%' in value:
                value = value.strip('%')
            value = float(value)
        except ValueError:
            return self.style
        style = self.style
        if value < 0:
            style = 'loss'
        if value > 0:
            style = 'gain'
        return style

    def get_header_style_map(self):
        colorized_fields = [
            'change_in_percent', 'return',
        ]
        return dict([
            (field, self.get_style(field))
            for field in colorized_fields
        ])


class ShareTable(PortfolioTable):

    HEADERS = config.columns
    row_class = QuoteRow
    extra_headers = ('return', )

    def get_dataset(self, progress_bar=None):
        data = [
            share.to_dict(config.columns)
            for share in self.portfolio.get_share_prices(progress_bar)
        ]
        return data