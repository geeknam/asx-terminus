from os.path import expanduser, join
import yaml


DEFAULT_CONFIG = {
    'title_bar': 'ASX Terminus',
    'tab_size': 15,
    'divider_char': '-',
    'refresh_interval': 300,
    'codes': [],
    'transactions': {},
    'columns': [
        'code',
        'last_price',
        'open_price',
        'day_high_price',
        'day_low_price',
        'change_in_percent',
        'annual_dividend_yield',
        'volume'
    ]
}

class ConfigLoader(object):

    CONFIG_FILE_NAME = '.asxterminus.yaml'

    def __init__(self):
        self.__dict__.update(DEFAULT_CONFIG)

    @property
    def abs_path(self):
        return join(
            expanduser("~"),
            self.CONFIG_FILE_NAME
        )

    def load(self):
        try:
            config_content = open(self.abs_path, 'rb').read() 
            self.__dict__.update(yaml.load(config_content))
        except IOError as exc:
            print exc 
        return self


config = ConfigLoader().load()