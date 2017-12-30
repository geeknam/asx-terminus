from asxterminus.config import config

class Row(object):

    TABS = config.tab_size

    def __init__(self, headers, data, tab_size, style='cell'):
        self.headers = headers
        self.data = data
        self.style = style
        self.tab_size = tab_size

    @property
    def cells(self):
        return [
            (field, self.data[field])
            for field in self.headers
            if field in self.data
        ]

    def get_header_style_map(self):
        return {}

    def render_cell(self, cell, style_map):
        header, value = cell
        tab_size = self.tab_size.get(header, self.TABS)
        formatted_value = '{value} \t'.format(
            value=value
        ).expandtabs(tab_size)
        style = style_map.get(header, None)
        if style:
            return (style, formatted_value)
        return (self.style, formatted_value)

    def render(self):
        style_map = self.get_header_style_map()
        row = [
            self.render_cell(cell, style_map)
            for cell in self.cells
        ]
        row.append('\n')
        return row


class Table(object):

    row_class = Row
    extra_headers = ()

    def __init__(self, headers, data):
        self.headers = headers
        self.data = data
        all_headers = self.get_headers()
        self.tab_size = self.get_tab_size()
        self.rows = [
            self.row_class(
                headers=all_headers, data=item,
                tab_size=self.tab_size
            )
            for item in data
        ]

    def get_tab_size(self):
        tab_size = {}
        for header in self.get_headers():
            all_values_in_column = [
                len(str(item[header])) for item in self.data
            ]
            all_values_in_column.append(len(header))
            tab = max(all_values_in_column)
            tab_size[header] = tab + 4
        return tab_size

    def format_column(self, name):
        return ' '.join([
            word.capitalize()
            for word in name.split('_')
            if word != 'price'
        ])

    def get_headers(self):
        headers = list(self.headers)
        if self.extra_headers:
            headers.extend(self.extra_headers)
        return headers

    def get_all_rows(self):
        rows = list(self.rows)
        headers = self.get_headers()
        header = self.row_class(
            headers=headers,
            data=dict([
                (item, item)
                for item in headers
            ]),
            tab_size=self.tab_size,
            style='headers'
        )
        rows.insert(0, header)
        return rows

    def render(self):
        return [
            row.render()
            for row in self.get_all_rows()
        ]