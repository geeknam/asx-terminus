from asxterminus.data.share import Portfolio
from asxterminus.config import config
from asxterminus.ui.app import TerminalApp


def main():
    portfolio = Portfolio(config.codes)
    app = TerminalApp(
        config=config, portfolio=portfolio
    )
    app.run()
