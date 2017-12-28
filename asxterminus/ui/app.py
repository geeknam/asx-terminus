import urwid
from .portfolio import Table

class TerminalApp(object):

    def __init__(self, config, portfolio):
        self.config = config
        self.portfolio = portfolio
        self.table = Table(portfolio=self.portfolio)
        self.main_loop = urwid.MainLoop(
            self.get_layout(),
            self.palette,
            unhandled_input=self.handle_input
        )

    def run(self):
        self.main_loop.run()

    def exit(self):
        raise urwid.ExitMainLoop()

    @property
    def palette(self):
        return [
            ('titlebar', 'dark red', ''),
            ('refresh', 'dark green,bold', ''),
            ('quit', 'dark red', ''),
            ('headers', 'dark blue,bold', ''),
            ('row', 'white', ''),
            ('cell', 'white', ''),
            ('gain', 'dark green', ''),
            ('loss', 'dark red', '')
        ]

    def handle_input(self, key):
        if key == 'R' or key == 'r':
            self.refresh(None, None)

        if key == 'Q' or key == 'q':
            self.exit()

    def refresh(self, a, b):
        self.main_loop.draw_screen()
        self.quote_box.base_widget.set_text(
            self.table.render()
        )
        self.main_loop.set_alarm_in(
            int(self.config.refresh_interval), self.refresh
        )

    def get_header(self):
        header_text = urwid.Text(self.config.title_bar)
        header = urwid.AttrMap(header_text, 'titlebar')
        return header

    def get_body(self):
        quote_text = urwid.Text(self.table.render())
        quote_filler = urwid.Filler(quote_text, valign='top', top=1, bottom=1)
        v_padding = urwid.Padding(quote_filler, left=2, right=0)
        self.quote_box = urwid.LineBox(v_padding)
        return self.quote_box

    def get_footer(self):
        menu = urwid.Text([
            'Press (', ('refresh', 'R'), ') to manually refresh. ',
            'Press (', ('quit', 'Q'), ') to quit.'
        ])
        return menu

    def get_layout(self):
        return urwid.Frame(
            header=self.get_header(),
            body=self.get_body(),
            footer=self.get_footer()
        )