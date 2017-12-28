from asxterminus.config import config
from asxterminus.data.share import Asset

class Row(object):

    TABS = config.tab_size

    def __init__(self, share):
        self.share = share
        self.assets = [
            Asset(asset[0], asset[1])
            for asset in config.assets.get(
                self.share.code, []
            )
        ]

    def render_cell(self, value):
        return '{value} \t'.format(
            value=value
        ).expandtabs(self.TABS)

    def render_return(self):
        style = 'cell'
        share_return = self.share.get_return(self.assets)
        if share_return < 0:
            style = 'loss'
        if share_return > 0:
            style = 'gain'
        return (style, str(share_return))

    def render(self):
        line = [
            ('cell', self.render_cell(cell))
            for cell in self.share.to_cell(config.columns)
        ]
        line.append(self.render_return())
        line.append('\n')
        return line


class Table(object):

    def __init__(self, portfolio):
        self.portfolio = portfolio

    def format_column(self, name):
        name = ' '.join([
            word.capitalize()
            for word in name.split('_')
            if word != 'price'
        ])
        return '{} \t'.format(name).expandtabs(Row.TABS)

    @property
    def columns(self):
        columns = [
            ('headers', self.format_column(column))
            for column in config.columns
        ]
        columns.append(('headers', 'Your Return'))
        columns.append('\n')
        return columns

    @property
    def rows(self):
        rows = [
            Row(share).render()
            for share in self.portfolio.get_share_prices()
        ]
        rows.insert(0, self.columns)
        return rows

    def render(self):
        return self.rows