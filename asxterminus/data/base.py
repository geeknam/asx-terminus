import requests
from datetime import datetime, timedelta


class ApiBaseObject(object):
    
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def build_from(cls, url):
        response = requests.get(url)
        data = response.json()
        return cls(**data)

    @classmethod
    def build_from_daily(cls, url):
        response = requests.get(url)
        data = response.json()
        metadata = data['Meta Data']
        code = metadata['2. Symbol']
        time_series = data['Time Series (Daily)']
        today_utc = str(datetime.utcnow().date())
        if today_utc in time_series:
            last_day_data = time_series[today_utc]
        else:
            yesterday_utc = str(datetime.utcnow().date() - timedelta(days=1))
            last_day_data = time_series[yesterday_utc]

        current_data = dict([
            (key[3:], value)
            for key, value in last_day_data.items()
        ])
        current_data.update({
            'code': code.split('.')[0]
        })
        return cls(**current_data)